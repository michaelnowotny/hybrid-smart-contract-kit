#!/usr/bin/python3
import os
from brownie import LinkToken, Oracle, accounts, network, config


def main():
    dev = accounts.add(config['wallets']['dev_account_0'])

    if network.show_active() == 'avax-avash':
        chainlink_node_account_address_env_name = 'AVALANCHE_CHAINLINK_NODE_ACCOUNT_ADDRESS'
    else:
        chainlink_node_account_address_env_name = 'GETH_CHAINLINK_NODE_ACCOUNT_ADDRESS'

    chainlink_node_account_address = os.getenv(chainlink_node_account_address_env_name)
    if chainlink_node_account_address is None:
        raise ValueError(f'Environment variable {chainlink_node_account_address_env_name} not set.')

    print(f'Funding Chainlink node account at {chainlink_node_account_address}')

    dev.transfer(chainlink_node_account_address, "1000 ether")

    # Set fulfillment permission
    oracle_contract = Oracle[-1]
    oracle_contract.setFulfillmentPermission(chainlink_node_account_address, True, {'from': dev})
