#!/usr/bin/python3
import os
from brownie import (
    BytesConsumer,
    accounts,
    network,
    config
)


def main():
    dev = accounts.add(config['wallets']['dev_account_0'])
    bytes_consumer_contract = BytesConsumer[-1]

    print(f'Bytes returned by Chainlink node = {bytes_consumer_contract.data()}')
    print(f'Number of bytes returned by Chainlink node = {bytes_consumer_contract.numberOfBytes()}')
    print(f'Number of times fulfillment function called = {bytes_consumer_contract.numberOfTimesFulfillmentCalled()}')
