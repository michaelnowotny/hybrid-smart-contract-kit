#!/usr/bin/python3
import os
from brownie import (
    ATestnetConsumer,
    accounts,
    network,
    config
)


def main():
    testnet_consumer_contract = ATestnetConsumer[-1]

    current_ether_price = testnet_consumer_contract.currentPriceViaExternalAdapter()

    print(f'Current Ether price returned by Chainlink node = {current_ether_price}')
