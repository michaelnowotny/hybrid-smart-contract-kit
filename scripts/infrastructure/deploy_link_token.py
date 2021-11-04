#!/usr/bin/python3
import os
from brownie import LinkToken, accounts, network, config


def main():
    dev = accounts.add(config['wallets']['dev_account_0'])

    link_token_contract = LinkToken.deploy({'from': dev})
    print(f'LINK token contract deployed at {link_token_contract.address}')

    # os.makedirs("addresses", exist_ok=True)
    with open(os.path.join('chainlink', 'local.env'), "w") as f:
        f.write('ETH_URL=ws://host.docker.internal:8546\n')
        f.write('FEATURE_EXTERNAL_INITIATORS=TRUE\n')
        f.write('LOG_LEVEL=debug\n')
        f.write('ETH_CHAIN_ID=1337\n')
        f.write('MIN_OUTGOING_CONFIRMATIONS=0\n')
        f.write(f'LINK_CONTRACT_ADDRESS={link_token_contract.address}\n')
        f.write('CHAINLINK_TLS_PORT=0\n')
        f.write('SECURE_COOKIES=false\n')
        f.write('ALLOW_ORIGINS=*\n')
        f.write('DATABASE_URL=postgresql://chainlink:crum-chum-hum@localhost:5432/chainlink?sslmode=disable\n')
        f.write('DATABASE_TIMEOUT=0\n')
        f.write('FEATURE_FLUX_MONITOR=true\n')
        f.write('MINIMUM_CONTRACT_PAYMENT_LINK_JUELS=100000000000000\n')
        f.write('CHAINLINK_DEV=true\n')
        f.write('GAS_UPDATER_ENABLED=true\n')
