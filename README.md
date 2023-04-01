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

- The script also requires an API key from macaddress.io (https://macaddress.io/login).
- The API key is used to authenticate your requests to the API and retrieve MAC address information.
- You can obtain an API key by registering for an account on the macaddress.io website and subscribing to one of their plans.
- Once you have your API key, you can replace the "YOURAPIKEYGOESHERE" string in the script with your own API key in order to use the script with your account.

It's important to keep your API key secure and not share it with others.



