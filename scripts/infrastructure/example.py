import os
from brownie import LinkToken, accounts, network, config


def main():
    dev = accounts.add(config['wallets']['dev_account_0'])

    link_token_contract = LinkToken[-1]
    print(f'Using LINK token deployed at {link_token_contract.address}')

    chainlink_node_account_address = os.getenv('CHAINLINK_NODE_ACCOUNT_ADDRESS')
    if chainlink_node_account_address is None:
        raise ValueError('Environmnet variable CHAINLINK_NODE_ACCOUNT_ADDRESS not set.')

    print(f'Transferring LINK to Chainlink node account at {chainlink_node_account_address}')
    link_token_contract.transfer(chainlink_node_account_address, 1 * 10**18, {'from': dev})
