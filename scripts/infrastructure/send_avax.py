#!/usr/bin/python3
import os
from brownie import accounts, network, config


def main():
    print(f'{network.is_connected()}')
    print(f'{network.show_active()=}')

    if network.show_active() != 'avax-avash':
        raise ValueError("Wrong network. Please run with option '--network avax-avash'!")


    dev = accounts.add(config['networks']['avax-avash']['ava_dev_account'])
    balance = dev.balance() / 10**18
    print(f'{balance=}')

    receiving_addresses = (
        "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
        "0x70997970c51812dc3a010c7d01b50e0d17dc79c8",
        "0x3c44cdddb6a900fa2b585dd299e03d12fa4293bc",
        "0x90f79bf6eb2c4f870365e785982e1f101e93b906",
        "0x15d34aaf54267db7d7c367839aaf71a00a2c6a65"
    )

    for receiving_address in receiving_addresses:
        dev.transfer(receiving_address, "10000 ether")
