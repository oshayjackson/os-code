#!/usr/bin/env python3

# create a list of strings
def firstlab():
    vendors = ["cisco", "juniper", "big_ip",
               "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings
    approved_vendors = ["cisco", "juniper", "big_ip"]
# loop across the list called vendors
    for x in vendors:
        # newline, print current vendor, and end without newline
        print("\nThe vendor is " + x, end="")
        if x not in approved_vendors:   # if x does not appear within the list approved_vendors
            print(" - NOT AN APPROVED VENDOR!", end="")
    print("\nOur loop has ended.")  # print when loop has finished


firstlab()
