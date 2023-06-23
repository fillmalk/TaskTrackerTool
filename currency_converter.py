# currency_converter.py

import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key

    def convert_currency(self, amount, from_currency, to_currency):
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            print("An error occurred:", data["error"])
            return

        conversion_rate = data["rates"][to_currency]
        converted_amount = amount * conversion_rate

        print(f"{amount} {from_currency} = {converted_amount} {to_currency}")

# Usage example
api_key = "YOUR_API_KEY"
converter = CurrencyConverter(api_key)

amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from: ")
to_currency = input("Enter the currency to convert to: ")

converter.convert_currency(amount, from_currency, to_currency)
