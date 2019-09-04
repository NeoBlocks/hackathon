<p align="center">
  <img src="https://neo-cdn.azureedge.net/images/neo-logo/144.png" width="144px;" alt="NEO">
</p>

<h3 align="center">NEO Smart Economy Hackathon</h3>

## Rules for the Hackathon

 - Fork the `hackathon-bootstrap` project and commit all code to this project
 - All code must be released open-source with MIT license
 - Result must be a working project (at least proof of concept)
 - Judges are Thomas Lobker, Pim Kerkhof Jonkman and Zekeriya Erkin
 - Reward for the best project is a 500 GAS prize to be used to deploy the contract to the NEO mainnet, plus domain registration and webhosting to host a project website for the first year
 - Project must utilize the NEO blockchain and any smart contract will be audited by NeoBlocks before deployment
 
 ## What are we building?
 
Create a secure messenger with the focus on privacy.

Current popular messenging services are highly centralized. The world depends on services like WhatsApp, Facebook or Google. By using a service like WhatsApp you share your contacts with Facebook who can use this data to track and profile their users. Think about the problems we need to solve to create a fully decentralized, highly secure and private way of messaging each other without compromising the usability of a service like WhatsApp. Use a decentralized smart contract to store any information that is needed for the application to work.

### Ingredients

 - "Bring Your Own Key" to let users use their own (PGP) private key
 - Use a NEO smart contract to store public keys and to allow the decentralized lookup of a public key
 - If a central server is required, then allow anyone to use a self-hosted server
 - Nobody should be required at any time to give up any personal details including an e-mail address or telephone number
 - Make a design to allow users to securely find each other if both users have each others information (like a telephone number)

## Getting started

### Connect to the NEO blockchain by setting up a NEO node

```bash
sudo docker run -it --name hackathon-node -v ~/smarteconomy/data:/app/data --restart=unless-stopped neoblocks/hackathon
```

### Fork the bootstrap project

https://github.com/NeoBlocks/hackathon-bootstrap

### Run the project

Go to http://127.0.0.1:4080/ and check if you can use the project

### Start building

**Good luck!**
