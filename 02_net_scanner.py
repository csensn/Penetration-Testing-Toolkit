#!/usr/bin/env python

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target", dest="target", help="Target IP")
    options = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    #arp_request_broadcast.show() #its show details...
    #answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)
    #We are interest in only answeres list, so other way to select...

    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    #print(answered_list.summary())
    client_list = []

    for element in answered_list:
        client_dic = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dic)
        return client_list

def print_result(result_list):
    print("IP\t\t\tMAC Address\n---------------------------------------------")
    client_list = []
    for client in client_list:
        print(client["ip"] + "\t\t" + client["mac"])

# scan("192.168.43.1/25")

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)