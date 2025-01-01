# pip install currencyconverter
from currency_converter import CurrencyConverter

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyConverter()
    result = c.convert(amount, from_currency, to_currency)

    return result

amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from: ").upper()
to_currency = input("Enter the currency to convert to: ").upper()

# performing the conversion
converted_amount = convert_currency(amount, from_currency, to_currency)

# displaying the result
print(f"{amount} {from_currency} is equal to {converted_amount: .2f} {to_currency}")

