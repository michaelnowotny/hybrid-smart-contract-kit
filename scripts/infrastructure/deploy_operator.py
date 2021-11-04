#!/usr/bin/python3
import os
from brownie import LinkToken, Operator, accounts, network, config


def main():
    dev = accounts.add(config['wallets']['dev_account_0'])

    link_token_address = LinkToken[-1].address
    print(f'Using LINK token contract at {link_token_address}')

    oracle_contract = Operator.deploy(link_token_address, dev.address, {'from': dev})
    print(f'Oracle contract deployed at {oracle_contract.address}')
