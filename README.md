# Hybrid Smart Contract Kit
A hybrid smart contract consists of on-chain and an off-chain component. 
The on-chain component is implemented in a smart contract language such as Solidity. 
The off-chain component can be a data oracle or a computation. 
The Chainlink framework enables both off-chain data acquisition and off-chain computation in a decentralized way.  

This repository demonstrates how to set up a local hybrid smart contract development environment and provides brief, working, illustrative examples from Chainlink's documentation to help developers get started developing hybrid smart contract without the quirks.
Unless otherwise indicated, all commands are understood to be run from the project root directory.
The instructions have been tested on macOS 11.6 and Linux Mint 20.2. Windows is not supported.

## Clone Chainlink Repository
- Define an environment variable `CHAINLINK_PATH` pointing to the directory the Chainlink repository will be cloned to. Ideally, this lies outside the directory to which `hybrid-smart-contract-kit` has been cloned.
- Navigate to the parent directory of `CHAINLINK_PATH`.
- Remember to restart your terminal or resource your environment file.
- Run `git clone https://github.com/smartcontractkit/chainlink`. Here are official instructions for reference: `https://github.com/smartcontractkit/chainlink#install`.
- Change into `chainlink` directory and run `git checkout master`.
- Remember to navigate back to the `hybrid-smart-contract-kit` root directory.

## Define Local Avalanche Blockchain Storage Directory
- Create an empty directory into which avalanchego should save the blockchain.
- Store this directory in an environment variable called `AVALANCHE_DEV_DATA_PATH`.
- Remember to restart your terminal or resource your environment file.

## Define Local Ethereum Blockchain Storage Directory
- Create an empty directory into which geth should save the blockchain.
- Store this directory in an environment variable called `GETH_DEV_DATA_PATH`.
- Remember to restart your terminal or resource your environment file.

## Install Python Package in Editable Mode
- Run `pip install -e .`.

## Add Networks to Brownie

### Avalanche
- Run `brownie networks add Avalanche avax-avash host=http://127.0.0.1:9650/ext/bc/C/rpc chainid=43112 explorer=https://cchain.explorer.avax.network/`.

### Binance Smart Chain
- Run `brownie networks add Ethereum binance-smart-chain host=https://bsc-dataseed1.binance.org chainid=56`.

### Polygon Mumbai Matic Testnet
- Run `brownie networks add Ethereum mumbai host=https://rpc-mumbai.maticvigil.com/ chainid=80001 explorer=https://mumbai-explorer.matic.today`.

### Local Ethereum Blockchain Node
- Run `brownie networks add Ethereum local host=http://localhost:8545 chainid=1337`.

## Install Avalanche Client Software
- On Linux, follow the instructions at `https://github.com/ava-labs/avalanchego`
- On MacOs, download the binary from `https://github.com/ava-labs/avalanchego/releases/tag/v1.7.0` and install
- 
## Install Ethereum Client Software
- On Mac, via homebrew, run `brew install geth`.
- On Linux, follow the instructions at `https://geth.ethereum.org/docs/install-and-build/installing-geth#install-on-ubuntu-via-ppas`.

## Start Local Ethereum Node
- From the project's root directory, navigate to `geth_scripts` and run `./startGeth.sh`.

## Start Local AvalancheGo Node
- From the project's root directory, navigate to `avalanche_scripts` and run `./start_avalanche.sh`.
- To make sure that the node is running, execute `./status.sh`.

## Set Up Local Avalanche Test Account (Only Required the First Time on the Local Testnet)
- The following steps are taken from these instructions: `https://docs.avax.network/build/tutorials/platform/fund-a-local-test-network`
- Navigate to `avalanche_scripts`.
- Run `./create_account.sh` to create a user `Avalanche` with password `Ava-123;X5`.
- Run './check_x_chain_balance.sh' to check the balance on the X-Chain
- Run './check_c_chain_balance.sh' to check the balance on the C-Chain

## Set Up MetaMask
### Connect MetaMask Wallet to Polygon Mumbai Matic Testnet ###
- Network Name: "Mumbai Matic"
- New RPC URL: "https://rpc-mumbai.maticvigil.com/"
- Chain ID: "80001"
- Currency Symbol (optional): "ETH"
- Block Explorer URL (optional): "https://explorer-mumbai.maticvigil.com/"

### Connect MetaMask Wallet to Local AvalancheGo Node ###
- Network Name: "Avalanche Local"
- New RPC URL: "http://localhost:9650/ext/bc/C/rpc"
- Chain ID: "43112"
- Currency Symbol (optional): "AVAX"
- Block Explorer URL (optional): ""

### Connect MetaMask Wallet to Local GETH Node ###
- Network Name: "Localhost 8545"
- New RPC URL: "http://localhost:8545"
- Chain ID: "1337"
- Currency Symbol (optional): "ETH"
- Block Explorer URL (optional): ""

### Add Dev Account for Local GETH Node 
- In MetaMask select `Import Account` and paste the private key `0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80`.
- Name the account `Local GETH Development Account`.

### Add Dev Account for Local AvalancheGo Node 
- In MetaMask select `Import Account` and paste the private key `0x56289e99c94b6912bfc12adc093c9b51124f0dc54ac7a766b2bc5ccf558d8027`.
- Name the account `Local Avalanche Development Account`

## Transfer 10000 ETH on Local Ethereum Node From Coinbase To Development Account
- Navigate to `geth_scripts` and run `./sendEth.sh`. - Remember to navigate back to the `hybrid-smart-contract-kit` root directory.

## Transfer 10000 AVAX Each on Local Avalanche Node from Pre-Funded Account to Dev Accounts
- Run `avalanche_scripts/send_avax.sh`.

## Deploy LINK Token Contract (Only Needs to be Done on Local Networks, not Public Ones) and add to MetaMask
- On GETH, either run `./geth_scripts/deploy_link_token.sh` or `brownie run scripts/infrastructure/deploy_link_token.py --network local`.
- On AvalancheGo, either run `./avalanche_scripts/deploy_link_token.sh` or `brownie run scripts/infrastructure/deploy_link_token.py --network avax-avash`.
- Copy the address at which the LINK token has been deployed, click `Import tokens` in MetaMask below the list of all coins and tokens, and paste into the field `Token Contract Address`. Finally, click `Add Custom Token`.

## Deploy Oracle Contract (Needs to be Done on both Local and Public Networks)
- On GETH, either run `./geth_scripts/deploy_oracle.sh` or `brownie run scripts/infrastructure/deploy_oracle.py --network local`.
- On AvalancheGo, either run `./avalanche_scripts/deploy_oracle.sh` or `brownie run scripts/infrastructure/deploy_oracle.py --network avax-avash`.

## Deploy Operator Contract (Needs to be Done on both Local and Public Networks)
- On GETH, either run `./geth_scripts/deploy_operator.sh` or `brownie run scripts/infrastructure/deploy_operator.py --network local`.
- On AvalancheGo, either run `./avalanche_scripts/deploy_operator.sh` or `brownie run scripts/infrastructure/deploy_operator.py --network avax-avash`.

## Modify `/etc/hosts` on Linux
- On Linux only, associate `host.docker.internal` with `127.0.0.1` via this line in `/etc/hosts`: `127.0.0.1    localhost host.docker.internal`.

## Important: Stop a Postgres Service on the Host Machine on Port 5432 Before Running the Docker Container
- Run `systemctl stop postgresql`.

## Build Chainlink Node (This only needs to be done the first time!)
- On Mac, from the project root directory type `docker build -f chainlink/chainlink_dockerfile --tag chainlink_node .` to build a docker image for the chainlink node.
- On Linux, add `sudo` before the docker command.
- For GETH:
  - On Mac: Create container from docker image: `docker run --name chainlink_geth -p 6688:6688 -p 5432:5432 --add-host=host.docker.internal:host-gateway -it --env-file=chainlink/local.env -v $CHAINLINK_PATH:/chainlink chainlink_node`.
  - On Linux: Create container from docker image: `sudo docker run --name chainlink_geth -p 6688:6688 -p 5432:5432 --network=host -it --env-file=chainlink/local.env -v $CHAINLINK_PATH:/chainlink chainlink_node`.
- For Avalanche
  - On Mac: Create container from docker image: `docker run --name chainlink_avalanche -p 6688:6688 -p 5432:5432 --add-host=host.docker.internal:host-gateway -it --env-file=chainlink/local.env -v $CHAINLINK_PATH:/chainlink chainlink_node`.
  - On Linux: Create container from docker image: `sudo docker run --name chainlink_avalanche -p 6688:6688 -p 5432:5432 --network=host -it --env-file=chainlink/local.env -v $CHAINLINK_PATH:/chainlink chainlink_node`.
- Compile chainlink:
  - Change into `chainlink` folder.  
  - Run `yarn install`.
  - Run `make install`.
- In a different terminal, type `docker container ls - a` and store the name of the container in the environment variable `CHAINLINK_DOCKER_CONTAINER_NAME`.
- In `chainlink` folder run `./chainlink node start -p /cla/.password -a /cla/.api`.
- In a web browser navigate to `http://localhost:6688`.
- Login with username `admin@example.com` and password `password`.
- Navigate to gear icon, select `Key Management`, and copy the regular account address.
- For Geth, store the copied account address in an environment variable `CHAINLINK_NODE_ACCOUNT_ADDRESS`.
- For Avalanche, store the copied account address in an environment variable `AVALANCHE_CHAINLINK_NODE_ACCOUNT_ADDRESS`.

## To Start the Chainlink Docker Container After the First Setup
- Start a new terminal or resource your environment file.
- On Linux, remember to add `sudo` before the docker command.
- In the following, the placeholder `CHAINLINK_DOCKER_CONTAINER_NAME` refers to `chainlink_avalanche` for Avalanche and `chainlink_geth` for GETH.
- To start a stopped container, type `docker start <CHAINLINK_DOCKER_CONTAINER_NAME>`.
- To attach a terminal, type `docker attach $CHAINLINK_DOCKER_CONTAINER_NAME`.
- Navigate to `chainlink` folder via `cd chainlink`.
- In `chainlink` folder run `./chainlink node start -p /cla/.password -a /cla/.api`.

## Transfer 1000 ETH from Local Development Account to Chainlink Node Account and Set Fulfillment Permission on Oracle Contract
- On Geth, from the project's root directory, run `brownie run scripts/infrastructure/fund_chainlink_account --network local`.
- On Avalanche, from the project's root directory, run `brownie run scripts/infrastructure/fund_chainlink_account --network avax-avash`.

## Testnet Consumer
Adapted from `https://github.com/sourabhrajsingh/chainlink-remix-workshop/blob/master/ATestnetConsumer.sol`
###  Add Get > Uint256 Job on Chainlink Node
- In a browser, navigate to the Chainlink management console at `localhost:6688`.
- Select `Jobs` and click `New Job`.
- To display the oracle contract address, 
  - On Geth, run `brownie run scripts/infrastructure/print_contract_addresses.py --network local`.
  - On Avalanche, run `brownie run scripts/infrastructure/print_contract_addresses.py --network avax-avash`.
- Paste the contents of the file `chainlink/TestnetConsumerJob.toml` into the job description and replace `YOUR_ORACLE_CONTRACT_ADDRESS` with the address at which the oracle contract has been deployed.
- Click `Create Job`.

###  Deploy A Testnet Consumer Contract and Fund With LINK Tokens
- Run `brownie run scripts/oracle_example/deploy_testnet_consumer.py --network local`.

###  Initiate Request of Ether Price from Oracle (i.e. call ATestnetConsumer contract which calls the Oracle contract)
- Run `brownie run scripts/oracle_example/make_testnet_consumer_request.py --network local`.

###  Read Data Returned By Chainlink from A Testnet Consumer Contract
- Run `brownie run scripts/oracle_example/read_testnet_consumer_result.py --network local`.

## Crypto Compare External Adapter
Originally created by Thomas Hodges and published on GitHub at `https://github.com/thodges-gh/CL-EA-Python-Template`.

### Start and Test the Web Service Running the External Adapter
- To start the web service, run `python -m hsck.crypto_compare_ea.app`.
- To test the web service, run `pytest hsck`.
- To see the output from a post request, run `curl -X POST -H "content-type:application/json" "http://localhost:8082/" --data '{ "id": 0, "data": { "from": "ETH", "to": "USD" } }'`.

### Add Bridge to Crypto Compare External Adapter on Chainlink Node
- Log in to the Chainlink web management console.
- Navigate to `Bridges` and click `New Bridge`.
- Enter `CryptoCompare` under `Bridge Name`.
- Enter `http://host.docker.internal:8082` under `Bridge URL`.

### Add CryptoCompare Job on Chainlink Node
- In a browser, navigate to the Chainlink management console at `localhost:6688`.
- Select `Jobs` and click `New Job`.
- To display the oracle contract address, run `brownie run scripts/infrastructure/print_contract_addresses.py --network local`.
- Paste the contents of the file `chainlink/CryptoCompareJob.toml` into the job description and replace `YOUR_ORACLE_CONTRACT_ADDRESS` with the address at which the oracle contract has been deployed.
- Click `Create Job`.

### Initiate Request To Crypto Compare External Adapter
- Run `brownie run scripts/oracle_example/make_crypto_compare_ea_request.py --network local`.

### Read Data Returned By Chainlink Node via Crypto Compare External Adapter
- Run `brownie run scripts/oracle_example/read_crypto_compare_ea_result.py --network local`.


## Multi Word Consumer Example
See the Chainlink documentation for background information at `https://docs.chain.link/docs/multi-variable-responses/`.

###  Add Multi Word Consumer Job on Chainlink Node
- In a browser, navigate to the Chainlink management console at `localhost:6688`.
- Select `Jobs` and click `New Job`.
- To display the operator contract address, run `brownie run scripts/infrastructure/print_contract_addresses.py --network local`.
- Paste the contents of the file `chainlink/MultiWordConsumer.toml` into the job description and replace `YOUR_OPERATOR_CONTRACT_ADDRESS` with the address at which the operator contract has been deployed (not the oracle address!).
- Click `Create Job`.
 
###  Deploy Multi Word Consumer Contract and Fund With LINK Tokens
- Run `brownie run scripts/oracle_example/deploy_multi_word_consumer.py --network local`.

###  Initiate Request of Ether Price in USD, EUR, and JPY from Operator
- Run `brownie run scripts/oracle_example/make_multi_word_consumer_request.py --network local`.

###  Read Data Returned By Chainlink from Multi Word Consumer Contract
- Run `brownie run scripts/oracle_example/read_multi_word_consumer_result.py --network local`.
