import os
from brownie import LinkToken, Oracle, Operator, ATestnetConsumer, accounts, network, config


def main():
    if len(LinkToken) > 0:
        print(f'LINK token contract deployed at {LinkToken[-1].address}')
    else:
        print('LINK token contract has not been deployed yet')

    if len(Oracle) > 0:
        print(f'Oracle contract deployed at {Oracle[-1].address}')
    else:
        print('Oracle contract has not been deployed yet')

    if len(Operator) > 0:
        print(f'Operator contract deployed at {Operator[-1].address}')
    else:
        print('Operator contract has not been deployed yet')

    if len(ATestnetConsumer) > 0:
        print(f'ATestnetConsumer contract deployed at {ATestnetConsumer[-1].address}')

        if len(LinkToken) > 0:
            link_balance = LinkToken[-1].balanceOf(ATestnetConsumer[-1].address)
            print(f'ATestnetConsumer contract has {link_balance} LINK tokens')
    else:
        print('ATestnetConsumer contract has not been deployed yet')
