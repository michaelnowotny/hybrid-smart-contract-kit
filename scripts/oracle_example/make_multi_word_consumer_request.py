#!/usr/bin/python3
import os
from brownie import (
    MultiWordConsumer,
    Operator,
    accounts,
    network,
    config
)

from hsck.job_id import CHAINLINK_MULTI_WORD_JOB_ID


def main():
    dev = accounts.add(config['wallets']['dev_account_0'])
    operator_contract = Operator[-1]
    job_id = bytes(CHAINLINK_MULTI_WORD_JOB_ID, 'utf-8')

    print(f'{job_id=}')

    multi_word_consumer_contract = MultiWordConsumer[-1]

    payment = 1 * 10**18
    print(f'Making request to job id {job_id} at operator contract deployed at '
          f'{operator_contract.address} from a multi word consumer contract deployed at '
          f'{multi_word_consumer_contract.address}')
    result = multi_word_consumer_contract.requestMultipleParameters(job_id, payment, {'from': dev})

    print(result)
