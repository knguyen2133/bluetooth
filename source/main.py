#Based of off pybluez example rfcomm
import random, time

import server
import client
import scan

def tossUp(addr, res):
    if res < 5:
        server.serverBt()
    else:
        client.clientBt(addr)


def randomGenerator():
    return random.randint(0,10)

def main():
    print("Hello")
    addr = scan.selectDevice()
    while True:
        if addr != False:
            res = randomGenerator()
            tossUp(addr, res)
        else:
            continue

main()