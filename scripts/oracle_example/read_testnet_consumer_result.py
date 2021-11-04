#!/usr/bin/python3
import os
from brownie import (
    ATestnetConsumer,
    accounts,
    network,
    config
)


def main():
    dev = accounts.add(config['wallets']['dev_account_0'])
    testnet_consumer_contract = ATestnetConsumer[-1]

    # print(f'Making request to job id {job_id} from oracle contract deployed at {oracle_contract.address}')
    current_ether_price = testnet_consumer_contract.currentPrice()

    print(f'Current Ether price returned by Chainlink node = {current_ether_price}')
