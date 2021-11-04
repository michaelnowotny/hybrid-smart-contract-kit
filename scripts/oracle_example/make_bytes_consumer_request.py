#!/usr/bin/python3
import os
from brownie import (
    BytesConsumer,
    LinkToken,
    Operator,
    accounts,
    network,
    config
)

from hsck.job_id import CHAINLINK_BYTES_JOB_ID


def main():
    dev = accounts.add(config['wallets']['dev_account_0'])
    operator_contract = Operator[-1]
    job_id = bytes(CHAINLINK_BYTES_JOB_ID, 'utf-8')

    bytes_consumer_contract = BytesConsumer[-1]

    payment = 1 * 10**18
    print(f'Making request to job id {job_id} at operator contract deployed at '
          f'{operator_contract.address} from a bytes consumer contract deployed at '
          f'{bytes_consumer_contract.address}')

    result = bytes_consumer_contract.requestBytes(job_id, payment, {'from': dev})

    print(result)
