#!/usr/bin/python3
import os
from brownie import accounts, network, config


def main():
    # if not network.is_connected():
    #     network.connect('local')

    print(f'{network.is_connected()}')
    print(f'{network.show_active()=}')

    # dev = accounts.add(config['wallets']['dev_account_0'])
    # chainlink_node_account_address = os.getenv('CHAINLINK_NODE_ACCOUNT_ADDRESS')
    # if chainlink_node_account_address is None:
    #     raise ValueError('Environmnet variable CHAINLINK_NODE_ACCOUNT_ADDRESS not set.')
    #
    # print(f'Funding Chainlink node account at {chainlink_node_account_address}')
    #
    # dev.transfer(chainlink_node_account_address, "1000 ether")
    #
    # # Set fulfillment permission
    # oracle_contract = Oracle[-1]
    # oracle_contract.setFulfillmentPermission(chainlink_node_account_address, True, {'from': dev})
