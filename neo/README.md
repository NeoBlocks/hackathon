# Set up a private network for the hackathon

```
# Get the sources
git clone git@github.com:NeoBlocks/hackathon.git
cd hackathon/neo
git submodule init
git submodule update --remote

# Build the Docker container
docker build -t hackathon/neo-cli:2.10.3 .
docker tag hackathon/neo-cli:2.10.3 hackathon/neo-cli:latest

# Choose a local directory for persistent data
location=/usr/local/etc/neo/hackathon

# Copy the local configuration files to a persistent location
mkdir -p ${location}
mkdir -p local/1/Index local/1/Chain local/2/Index local/2/Chain local/3/Index local/3/Chain local/4/Index local/4/Chain local/admin/Index local/admin/Chain
cp -r local/[1234] ${location}/
cp -r local/admin ${location}/

# Create a Docker network bridge
docker network create -d bridge hackathon

# Create 4 NEO consensus nodes for our private network
docker create -it --name=neo-hackathon-node-1 -p 31332-31333:31332-31333 -v ${location}/1/Chain:/app/Chain -v ${location}/1/Index:/app/Index -v ${location}/1/config.json:/app/config.json -v ${location}/1/protocol.json:/app/protocol.json -v ${location}/1/wallet.json:/app/wallet.json --network=hackathon --restart=unless-stopped --log-opt max-size=128m hackathon/neo-cli
docker create -it --name=neo-hackathon-node-2 -p 32332-32333:32332-32333 -v ${location}/2/Chain:/app/Chain -v ${location}/2/Index:/app/Index -v ${location}/2/config.json:/app/config.json -v ${location}/2/protocol.json:/app/protocol.json -v ${location}/2/wallet.json:/app/wallet.json --network=hackathon --restart=unless-stopped --log-opt max-size=128m hackathon/neo-cli
docker create -it --name=neo-hackathon-node-3 -p 33332-33333:33332-33333 -v ${location}/3/Chain:/app/Chain -v ${location}/3/Index:/app/Index -v ${location}/3/config.json:/app/config.json -v ${location}/3/protocol.json:/app/protocol.json -v ${location}/3/wallet.json:/app/wallet.json --network=hackathon --restart=unless-stopped --log-opt max-size=128m hackathon/neo-cli
docker create -it --name=neo-hackathon-node-4 -p 34332-34333:34332-34333 -v ${location}/4/Chain:/app/Chain -v ${location}/4/Index:/app/Index -v ${location}/4/config.json:/app/config.json -v ${location}/4/protocol.json:/app/protocol.json -v ${location}/4/wallet.json:/app/wallet.json --network=hackathon --restart=unless-stopped --log-opt max-size=128m hackathon/neo-cli

# Start the nodes
for node in neo-hackathon-node-1 neo-hackathon-node-2 neo-hackathon-node-3 neo-hackathon-node-4; do docker start ${node}; done

# Create an admin neo-cli container that is not a consensus node and expose the RPC and P2P ports
docker run -it --name=neo-cli-hackathon --network=hackathon -p 30332-30333:30332-30333 --restart=unless-stopped --log-opt max-size=128m -v ${location}/admin/Chain:/app/Chain -v ${location}/admin/Index:/app/Index -v ${location}/admin/node1.json:/app/node1.json -v ${location}/admin/node2.json:/app/node2.json -v ${location}/admin/node3.json:/app/node3.json -v ${location}/admin/node4.json:/app/node4.json hackathon/neo-cli

# Now attach to the container and send all NEO to a new wallet
docker attach neo-cli-hackathon

# Show the network state and create a new wallet
show state
create wallet admin.json

# Open the first node wallet
open wallet node1.json

# Import the multi-signature contract where the initial NEO is deployed
import multisigaddress 3 0250f9e1d661ad03b97a8580c64a8e32bd350b411472176361d841adfe3be77bbf 03010d52cdec237e6c07fb07ed0d677eee198d540ff24778c05b1133eacb4d3d7b 02149e84cbd0d0f8a5ac456f3db9cdcda9c25767eba218f7beefa49ea7416b6f8d 020da19d8f693b1eb74f86f0f21ab7246928516a923f3bb5bc85e5ceec4da0b099

# Check your balance and send all NEO to your new wallet in admin.json
list asset
send NEO <address> all

# This will create a partially signed transaction. Open two more node wallets to sign the transaction and relay the signed transaction
open wallet node2.json
import multisigaddress 3 0250f9e1d661ad03b97a8580c64a8e32bd350b411472176361d841adfe3be77bbf 03010d52cdec237e6c07fb07ed0d677eee198d540ff24778c05b1133eacb4d3d7b 02149e84cbd0d0f8a5ac456f3db9cdcda9c25767eba218f7beefa49ea7416b6f8d 020da19d8f693b1eb74f86f0f21ab7246928516a923f3bb5bc85e5ceec4da0b099
sign {}
open wallet node3.json
import multisigaddress 3 0250f9e1d661ad03b97a8580c64a8e32bd350b411472176361d841adfe3be77bbf 03010d52cdec237e6c07fb07ed0d677eee198d540ff24778c05b1133eacb4d3d7b 02149e84cbd0d0f8a5ac456f3db9cdcda9c25767eba218f7beefa49ea7416b6f8d 020da19d8f693b1eb74f86f0f21ab7246928516a923f3bb5bc85e5ceec4da0b099
sign {}
relay {}

# Now we claim any GAS from the multi-signature address and send it to the same address
claim gas all <address>

# Open the first wallet again and check the balances
open wallet admin.json
rebuild index
list asset
show utxo
```
