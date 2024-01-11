#!/usr/bin/env python3
import uuid


def a():

    dnsfile = open("dnsservers.txt", "r")

    dnslist = dnsfile.readlines()

    for svr in dnslist:

        print(svr, end="")

    dnsfile.close()


a()


def b():

    with open("dnsservers.txt", "r") as dnsfile:

        dnslist = dnsfile.readlines()

        for svr in dnslist:

            print(svr, end="")


b()


def c():
    with open("dnsservers.txt", "r") as dnsfile:

        for svr in dnsfile:

            print(svr, end="")


c()


def d():
    # open file in read mode
    with open("dnsservers.txt", "r") as dnsfile:   # 'r' is read mode

        for svr in dnsfile:
            svr = svr.rstrip('\n')  # remove newline char if exists

            if svr.endswith('org'):
                with open("org-domain.txt", "a") as srvfile:  # 'a' is append mode
                    srvfile.write(svr + "\n")

            elif svr.endswith('com'):
                with open("com-domain.txt", "a") as srvfile:  # 'a' is append mode
                    srvfile.write(svr + "\n")


d()


def loop3():
    howmany = int(input("How many UUIDs should be generated? "))
    print("Generating UUIDs...")

# range is required because an int cannot be looped
    for rando in range(howmany):
        print(uuid.uuid4())   # each time through the loop produce a UUID


loop3()
