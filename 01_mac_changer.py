#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Mac address is Changing")
    parser.add_option("-m", "--mac", dest="new_mac", help="Mac address is Changing")
    (options, arguments) =  parser.parse_args()
    if not options.interface:
        parser.error("[-] Enter a spicific interface name.")
    elif not options.new_mac:
        parser.error("[-] Enter a new mac address.")
    else:
        return options


def change_mac(interface, new_mac):
    print("[+] Mac Address  change of " + interface + " to " + new_mac)

    # subprocess.call("ifconfig " + interface + " down", shell=True)
    # subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    # subprocess.call("ifconfig " + interface + " up", shell=True)

    # More secure version of above code

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_result:
        return mac_result.group(0)
    else:
        print("[-] Could not read mac address.")


# interface = options.interface
# new_mac = options.new_mac

options = get_arguments()
current_mac = get_mac(options.interface)
print("Current Mac " + current_mac )

change_mac(options.interface, options.new_mac)

current_mac = get_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] Mac address is successfully changed to " + current_mac)
else:

    print("[-] Mac address is not change")
