#!/usr/bin/python3
import os
from brownie import (
    ATestnetConsumer,
    LinkToken,
    accounts,
    network,
    config
)


def main():
    dev = accounts.add(config['wallets']['dev_account_0'])
    link_token_contract = LinkToken[-1]

    testnet_consumer_contract = ATestnetConsumer.deploy(link_token_contract.address, {'from': dev})

    testnet_consumer_contract = ATestnetConsumer[-1]
    print(f'Transferring LINK to ATestnetConsumer contract at {testnet_consumer_contract.address}')
    # link_token_contract.transfer(testnet_consumer_contract.address, 1 * 10**18, {'from': dev})
    link_token_contract.transfer(testnet_consumer_contract.address, 1 * 10 ** 24, {'from': dev})
