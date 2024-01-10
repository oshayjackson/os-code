#!/usr/bin/env python3

hostname = "MTG"
if hostname == "MTG":
    print(f'The hostname was found to be {hostname}')


def host2():
    hostname = input("What value should we set for hostname? ")
    if hostname.startswith('m'):
        hostname = hostname.upper()
    return print(f"The hostname was found to be {hostname}")


host2()


def host3():
    hostname = input("What value should we set for hostname? ")
    if hostname.startswith('m'):
        hostname = hostname.lower()
    return print(f"The hostname was found to be {hostname}")


host3()
