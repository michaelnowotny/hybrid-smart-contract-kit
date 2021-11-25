#!/usr/bin/python3
import os
from brownie import (
    MultiWordConsumer,
    LinkToken,
    Operator,
    accounts,
    network,
    config
)


def main():
    dev = accounts.add(config['wallets']['dev_account_0'])
    operator_contract = Operator[-1]
    link_token_contract = LinkToken[-1]

    multi_word_consumer_contract = MultiWordConsumer.deploy(
        link_token_contract.address,
        operator_contract.address,
        {'from': dev}
    )

    multi_word_consumer_contract = MultiWordConsumer[-1]
    print(f'Transferring LINK to MultiWordConsumer contract at {multi_word_consumer_contract.address}')
    link_token_contract.transfer(multi_word_consumer_contract.address, 1 * 10 ** 24, {'from': dev})

    if network.show_active() == 'avax-avash':
        chainlink_node_account_address_env_name = 'AVALANCHE_CHAINLINK_NODE_ACCOUNT_ADDRESS'
    else:
        chainlink_node_account_address_env_name = 'CHAINLINK_NODE_ACCOUNT_ADDRESS'

    chainlink_node_account_address = os.getenv(chainlink_node_account_address_env_name)
    if chainlink_node_account_address is None:
        raise ValueError(f'Environment variable {chainlink_node_account_address_env_name} not set.')

    operator_contract.setAuthorizedSenders([chainlink_node_account_address], {'from': dev})
