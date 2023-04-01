# -*- coding: utf-8 -*-
# Author : Dimitrios Zacharopoulos
# All copyrights to Obipixel Ltd
# 01 April 2023

#!/usr/bin/env python3

import requests
from prettytable import PrettyTable

class MacAddressInfo:
    def __init__(self, mac_address, api_key):
        self.mac_address = mac_address
        self.api_key = api_key
        self.endpoint = "https://api.macaddress.io/v1"

    def get_vendor_details(self):
        response = requests.get(f"{self.endpoint}?apiKey={self.api_key}&output=json&search={self.mac_address}&output=vendorDetails")
        if response.status_code == 200:
            data = response.json()
            return data["vendorDetails"]
        else:
            return None

    def get_block_details(self):
        response = requests.get(f"{self.endpoint}?apiKey={self.api_key}&output=json&search={self.mac_address}&output=blockDetails")
        if response.status_code == 200:
            data = response.json()
            return data["blockDetails"]
        else:
            return None

    def get_mac_address_details(self):
        response = requests.get(f"{self.endpoint}?apiKey={self.api_key}&output=json&search={self.mac_address}&output=macAddressDetails")
        if response.status_code == 200:
            data = response.json()
            return data["macAddressDetails"]
        else:
            return None

class MacAddressTable:
    def __init__(self, data, title):
        self.table = PrettyTable()
        self.table.field_names = ["Property", "Value"]
        self.title = title
        self.add_data(data)

    def add_data(self, data):
        for key, value in data.items():
            self.table.add_row([key, value])

    def print_table(self):
        print(self.title)
        print(self.table)

if __name__ == "__main__":
    # Set API key
    api_key = "YOURAPIKEYGOESHERE"

    # Print banner
    print("░█▄▒▄█▒▄▀▄░▄▀▀▒█▀░█░█▄░█░█▀▄")
    print("░█▒▀▒█░█▀█░▀▄▄░█▀░█░█▒▀█▒█▄▀\n")

    # Prompt user to input MAC address to check
    mac_address = input("Enter MAC address to check: ")

    # Create MacAddressInfo instance
    mac_info = MacAddressInfo(mac_address, api_key)

    # Get vendor details
    vendor_details = mac_info.get_vendor_details()
    if vendor_details:
        vendor_table = MacAddressTable(vendor_details, "Vendor Details:")
        vendor_table.print_table()
    else:
        print("Error: Unable to retrieve vendor details.")

    # Get block details
    block_details = mac_info.get_block_details()
    if block_details:
        block_table = MacAddressTable(block_details, "Block Details:")
        block_table.print_table()
    else:
        print("Error: Unable to retrieve block details.")

    # Get MAC address details
    mac_details = mac_info.get_mac_address_details()
    if mac_details:
        mac_table = MacAddressTable(mac_details, "MAC Address Details:")
        mac_table.print_table()
    else:
        print("Error: Unable to retrieve MAC address details.")
