#!/usr/bin/python3
import os
from brownie import (
    MultiWordConsumer,
    accounts,
    network,
    config
)


def main():
    dev = accounts.add(config['wallets']['dev_account_0'])
    multi_word_consumer_contract = MultiWordConsumer[-1]

    current_ether_price_in_usd = multi_word_consumer_contract.usd()
    current_ether_price_in_eur = multi_word_consumer_contract.eur()
    current_ether_price_in_jpy = multi_word_consumer_contract.jpy()

    print(f'Current Ether price in USD returned by Chainlink node = {current_ether_price_in_usd}')
    print(f'Current Ether price in EUR returned by Chainlink node = {current_ether_price_in_eur}')
    print(f'Current Ether price in JPY returned by Chainlink node = {current_ether_price_in_jpy}')
