#!/usr/bin/python3
import os
from brownie import (
    ATestnetConsumer,
    LinkToken,
    Oracle,
    accounts,
    network,
    config
)

from hsck.job_id import CHAINLINK_CRYPTO_COMPARE_JOB_ID


def main():
    dev = accounts.add(config['wallets']['dev_account_0'])
    oracle_contract = Oracle[-1]
    job_id = CHAINLINK_CRYPTO_COMPARE_JOB_ID

    testnet_consumer_contract = ATestnetConsumer[-1]

    print(f'Making request to job id {job_id} from oracle contract deployed at {oracle_contract.address}')
    result = testnet_consumer_contract.requestEthereumPriceViaExternalAdapter(oracle_contract.address, job_id, {'from': dev})

    print(result)
