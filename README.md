# macFIND
macFIND allows you to retrieve and display information about MAC addresses and a great OSINT tool.

## How the script works?

- This Python script defines two classes: MacAddressInfo and MacAddressTable.
- The MacAddressInfo class takes a MAC address and an API key as input and provides methods to retrieve vendor, block, and MAC address details from the macaddress.io API.
- The class uses the requests library to make HTTP GET requests to the API and returns the JSON response as a Python dictionary.
- The MacAddressTable class takes a dictionary of data and a title as input and creates a pretty table using the prettytable library.
- The class provides a method to add data to the table and a method to print the table to the console.
- In the if __name__ == "__main__": block, the script prompts the user to input a MAC address to check, creates an instance of the MacAddressInfo class with the input MAC address and an API key, and calls the get_vendor_details(), get_block_details(), and get_mac_address_details() methods to retrieve vendor, block, and MAC address details, respectively.
- The script then creates instances of the MacAddressTable class with the retrieved data and prints the tables to the console using the print_table() method.
- If any errors occur while retrieving the data, an error message is printed to the console.

## Why use macFIND?
This OSINT tool provides a convenient way to retrieve and display MAC address information from the macaddress.io API using Python.

## Preparation

macFIND.py requires two libraries to be installed for it to work: requests and prettytable.

The requests library is used to make HTTP GET requests to the macaddress.io API, while the prettytable library is used to create a pretty table to display the retrieved MAC address information.

To install these libraries, you can use pip by running the following command in your terminal or command prompt:
```bash
pip install requests prettytable
```

### API KEY

- The script also requires an API key from macaddress.io (https://macaddress.io).
- The API key is used to authenticate your requests to the API and retrieve MAC address information.
- You can obtain an API key by registering for an account on the macaddress.io website and subscribing to one of their plans.
- Once you have your API key, you can replace the "YOURAPIKEYGOESHERE" string in the script with your own API key in order to use the script with your account.

It's important to keep your API key secure and not share it with others.

## Permissions

Ensure you give the script permissions to execute. Do the following from the terminal:
```bash
sudo chmod +x macFIND.py
```

## Usage
```bash
sudo python3 macFIND.py
Password:
░█▄▒▄█▒▄▀▄░▄▀▀▒█▀░█░█▄░█░█▀▄
░█▒▀▒█░█▀█░▀▄▄░█▀░█░█▒▀█▒█▄▀

Enter MAC address to check:
```

## Sample script
```python
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
```

## Sample output
```
sudo python3 macFIND.py                                                                                            ─╯
Password:
░█▄▒▄█▒▄▀▄░▄▀▀▒█▀░█░█▄░█░█▀▄
░█▒▀▒█░█▀█░▀▄▄░█▀░█░█▒▀█▒█▄▀

Enter MAC address to check: 00:11:22:33:44:55
Vendor Details:
+----------------+---------------------------------------------------------------------------------------+
|    Property    |                                         Value                                         |
+----------------+---------------------------------------------------------------------------------------+
|      oui       |                                         001122                                        |
|   isPrivate    |                                         False                                         |
|  companyName   |                                       Cimsys Inc                                      |
| companyAddress | #301,Sinsung-clean BLDG,140, Nongseo-Ri,Kiheung-Eup Yongin-City Kyunggi-Do 449-711 KR |
|  countryCode   |                                           KR                                          |
+----------------+---------------------------------------------------------------------------------------+
Block Details:
+---------------------+--------------+
|       Property      |    Value     |
+---------------------+--------------+
|      blockFound     |     True     |
|      borderLeft     | 001122000000 |
|     borderRight     | 001122FFFFFF |
|      blockSize      |   16777216   |
| assignmentBlockSize |     MA-L     |
|     dateCreated     |  2004-06-05  |
|     dateUpdated     |  2015-09-27  |
+---------------------+--------------+
MAC Address Details:
+--------------------+-------------------+
|      Property      |       Value       |
+--------------------+-------------------+
|     searchTerm     | 00:11:22:33:44:55 |
|      isValid       |        True       |
|   virtualMachine   |    Not detected   |
|    applications    |         []        |
|  transmissionType  |      unicast      |
| administrationType |        UAA        |
|   wiresharkNotes   |     No details    |
|      comment       |                   |
+--------------------+-------------------+
```

## Disclaimer
"The scripts in this repository are intended for authorized security testing and/or educational purposes only. Unauthorized access to computer systems or networks is illegal. These scripts are provided "AS IS," without warranty of any kind. The authors of these scripts shall not be held liable for any damages arising from the use of this code. Use of these scripts for any malicious or illegal activities is strictly prohibited. The authors of these scripts assume no liability for any misuse of these scripts by third parties. By using these scripts, you agree to these terms and conditions."

## License Information

This library is released under the [Creative Commons ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/). You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to use our code, you email us with a link to the product being created and/or sold. We want bragging rights that we helped (in a very small part) to create your 9th world wonder. We would like the opportunity to feature your work on our homepage.
