#!/usr/bin/python3
import os
from brownie import LinkToken, accounts, network, config


def main():
    dev = accounts.add(config['wallets']['dev_account_0'])
    print(f'{network.show_active()=}')

    link_token_contract = LinkToken.deploy({'from': dev})
    print(f'LINK token contract deployed at {link_token_contract.address}')

    chain_id = network.chain.id
    print(f'{chain_id=}')

    if network.show_active() == 'avax-avash':
        ws_url = 'ws://host.docker.internal:9650/ext/bc/C/ws'  # see here: https://docs.avax.network/build/avalanchego-apis/contract-chain-c-chain-api
    else:
        ws_url = 'ws://host.docker.internal:8546'

    with open(os.path.join('chainlink', 'local.env'), "w") as f:
        f.write(f'ETH_URL={ws_url}\n')
        f.write('FEATURE_EXTERNAL_INITIATORS=TRUE\n')
        f.write('LOG_LEVEL=debug\n')
        f.write(f'ETH_CHAIN_ID={chain_id}\n')
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
