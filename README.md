<p align="center">
  <img src="https://neo-cdn.azureedge.net/images/neo-logo/144.png" width="144px;" alt="NEO">
</p>

<h3 align="center">NEO Smart Economy Workshop</h3>

# Introduction

Please find [the Slides for the workshop here](https://docs.google.com/presentation/d/1E1RUenmtULIUEH3x3DlLJJQUUoZjccKrIW1mPa7VN5M/edit?usp=sharing).

Welcome to the NEO Smart Economy hackathon on Wednesday 4 September in Amsterdam. During the hackathon, please join us on our Flock chat channel, so we can communicate with each other and share questions and information.

[![Flock](http://static.flock.co/flock/images/flocklogo.png)](https://smarteconomy.flock.com/)

You can enter your e-mail address and join.

# Preparing your environment

Make up teams and share the various tasks between the participants.

## Setup your workstation

Make sure you have Git and Docker installed. Start pulling the image and clone the workshop repository. Now you can connect to our dedicated private network and start using the NEO blockchain.

### Instructions for Linux:

```bash
# Install packages
sudo apt install git docker.io

# Create a working directory and pull the Git repository
mkdir ~/smarteconomy
cd ~/smarteconomy
git clone https://github.com/NeoBlocks/hackathon.git

# Pull the Docker image and create a local container
mkdir ~/smarteconomy/data
sudo docker run -it --name hackathon-node -v ~/smarteconomy/data:/app/data --restart=unless-stopped neoblocks/hackathon
```

### On Mac or Windows

* [Installation instructions by Atlassian on how to install Git on Mac OS X](https://www.atlassian.com/git/tutorials/install-git#mac-os-x)
* [Installation instructions by Atlassian on how to install Git on Windows](https://www.atlassian.com/git/tutorials/install-git#windows)
* [Install Docker Desktop for Mac instructions by Docker.io](https://docs.docker.com/docker-for-mac/install/)
* [Install Docker Desktop for Windows instructions by Docker.io](https://docs.docker.com/docker-for-windows/install/)

Once installed, please pull the image and run the container.

```bash
git clone https://github.com/NeoBlocks/hackathon.git
sudo docker run -it --name hackathon-node -v ~/smarteconomy/data:/app/data --restart=unless-stopped neoblocks/hackathon
```
You can always detach from the container with `Ctrl-P-Q` and then reattach with `docker attach hackathon-node`

# Interacting with your wallet

Once you have your NEO console open, you can create a wallet. With the built-in compiler you can easily compile and deploy Python smart contracts to the blockchain. Ask us to send you some GAS when you are ready to deploy the first contract.

```
# Create a new wallet
wallet create /app/data/wallet.json

# Now check your wallet
wallet

# We can now add the script hash for the Workshop Euro token:
wallet import token 0x0547ad0e6bd7bbac7781f95218454c53bc44275d
```

In the bottom of the screen you will see the progress of your node synchronization. Make sure the node is fully synced before sending any transactions. The wallet needs to be up to sync as well. Type `wallet` to check the synchornization status. If at any time you feel like something is not quite okay with your wallet or balances, you can use `wallet rebuild` to start syncing from scratch. This should take a couple of minutes. In the `wallet` overview you can also check your address and your address script hash, that should look like this:

```
Script hash b'\xadU\xc1QmV\x19;\x17\x7flq\xc7\x97\xeb\x18J\xba\x16\xe2' <class 'bytes'>
```

Share your address on Flock to receive some virtual EUR tokens.

## Spending tokens or assets

You can use your EUR balance to send some tokens to your neighbour.

```
wallet send EUR AMd14Q5C6YYGrz1cQA7GjfhgaNagrUkYzP 5 --from-addr=AH5HhymNXdQ14W4CbFjoqmkRPAcrjpSZRT
```

Now both check your wallet and notice that the tokens have moved:
```
wallet
```

# Challenges

Please make sure to check out our [neo-boa code examples and documentation](examples/README.md) first.

  When you are ready, go to [the challenge page](challenge/README.md) to read about the challenge.

**Good Luck!**
