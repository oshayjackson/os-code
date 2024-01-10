#!/usr/bin/env python3

def host1():
    print('1.')
    hostname = "MTG"
    if hostname == "MTG":
        print(f'The hostname was found to be {hostname}')


host1()
print('--------------------------------------------------------------')


def host2():
    print('2.')
    hostname = input("What value should we set for hostname? ")
    if hostname.lower().startswith('m'):
        hostname = hostname.upper()
    print(f"The hostname was found to be {hostname}")


host2()
print('--------------------------------------------------------------')


def host3():
    print('3.')
    hostname = input("What value should we set for hostname? ")
    if hostname.lower().startswith('m'):
        hostname = hostname.lower()
    print(f"The hostname was found to be {hostname}")
    print('hostname matches expected confif')


host3()
print('--------------------------------------------------------------')
print('Script Finished')
