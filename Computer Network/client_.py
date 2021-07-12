import time
import sys
from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(1)

sayac = 1

acilandosya = open("targethosts.txt")

satir = acilandosya.readline()

while satir:

    print("#{}. Hedef: {} ".format(sayac, satir.strip()))
    
    remoteAddr = (satir.strip(), 12345)
    
    for i in range(5):
        gonderimzamani = int(time.time()*1000)
        clientSocket.sendto('PING'.encode(), remoteAddr)
        print("#{} -> UDP: {} ".format(sayac, satir.strip()))
        try:
            clientSocket.recvfrom(1024)
            recdTime = int(time.time()*1000)
            rtt = recdTime - gonderimzamani
            print("#{}. <- RTT: {} ms ".format(i+1,rtt))

        except timeout:
            print("#{}. Paket Kaybı".format(i+1))

    sayac +=1
    satir = acilandosya.readline()

