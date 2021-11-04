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

    chainlink_node_account_address = os.getenv('CHAINLINK_NODE_ACCOUNT_ADDRESS')
    if chainlink_node_account_address is None:
        raise ValueError('Environmnet variable CHAINLINK_NODE_ACCOUNT_ADDRESS not set.')

    operator_contract.setAuthorizedSenders([chainlink_node_account_address], {'from': dev})
