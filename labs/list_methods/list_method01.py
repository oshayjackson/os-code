#!/usr/bin/env python3
def proto1():
    proto = ["ssh", "http", "https"]
    print(proto)
    print(proto[1])
    proto.extend(
        "dns"
    )  # extend takes the value and iterates over the indexed value while adding it to     the list its extending
    print(proto)


proto1()

print("----------------------------------")
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]


def proto2():
    print(proto)
    proto.append("dns")
    protoa.append("dns")
    print(proto)
    proto2 = [22, 80, 443, 53]
    proto.extend(proto2)
    print(proto)
    protoa.append(proto2)
    print(protoa)


proto2()
