# Set up a private network for the hackathon

```
# Get the sources
git clone git@github.com:NeoBlocks/hackathon.git
cd hackathon/neo
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
docker create -it --name=neo-hackathon-1 -v ${location}/1/Chain:/app/Chain -v ${location}/1/Index:/app/Index -v ${location}/1/config.json:/app/config.json -v ${location}/1/protocol.json:/app/protocol.json -v ${location}/1/wallet.json:/app/wallet.json --network=hackathon --restart=unless-stopped --log-opt max-size=128m hackathon/neo-cli
docker create -it --name=neo-hackathon-2 -v ${location}/2/Chain:/app/Chain -v ${location}/2/Index:/app/Index -v ${location}/2/config.json:/app/config.json -v ${location}/2/protocol.json:/app/protocol.json -v ${location}/2/wallet.json:/app/wallet.json --network=hackathon --restart=unless-stopped --log-opt max-size=128m hackathon/neo-cli
docker create -it --name=neo-hackathon-3 -v ${location}/3/Chain:/app/Chain -v ${location}/3/Index:/app/Index -v ${location}/3/config.json:/app/config.json -v ${location}/3/protocol.json:/app/protocol.json -v ${location}/3/wallet.json:/app/wallet.json --network=hackathon --restart=unless-stopped --log-opt max-size=128m hackathon/neo-cli
docker create -it --name=neo-hackathon-4 -v ${location}/4/Chain:/app/Chain -v ${location}/4/Index:/app/Index -v ${location}/4/config.json:/app/config.json -v ${location}/4/protocol.json:/app/protocol.json -v ${location}/4/wallet.json:/app/wallet.json --network=hackathon --restart=unless-stopped --log-opt max-size=128m hackathon/neo-cli

# Start the nodes
for node in neo-hackathon-1 neo-hackathon-2 neo-hackathon-3 neo-hackathon-4; do docker start ${node}; done

# Create an admin neo-cli container that is not a consensus node and expose the RPC and P2P ports
docker run -it --name=neo-hackathon --network=neo -p 10332-10333:10332-10333 --restart=unless-stopped --log-opt max-size=128m -v ${location}/admin/Chain:/app/Chain -v ${location}/admin/Index:/app/Index -v ${location}/admin/node1.json:/app/node1.json -v ${location}/admin/node2.json:/app/node2.json -v ${location}/admin/node3.json:/app/node3.json -v ${location}/admin/node4.json:/app/node4.json hackathon/neo-cli
```
