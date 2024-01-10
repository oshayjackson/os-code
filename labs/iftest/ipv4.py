#!/usr/bin/env python3


def check_ip():

    ipchk = input("Apply an IP address: ")

    if ipchk != "192.168.70.1":
        print(f"Warning: Setting the IP address of the Gateway to {
              ipchk} is not recommended.")
        print("You did not provide a correct input.")

    elif ipchk == "192.168.70.1":
        print(f"Looks like the IP address was set: {ipchk}")


check_ip()
