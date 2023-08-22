class CurrencyFormatException(Exception):
    def __init__(self, value):
        self.value = value
        self.message = f"Currency format error: {value}. Make sure to use comma as decimal separator and period as thousands separator."
        super().__init__(self.message)

def validate_currency_format(value):
    if isinstance(value, str):
        if ',' in value and '.' in value:
            raise CurrencyFormatException(value)
    else:
        raise TypeError("Input should be a string.")

# Example usage
try:
    currency_value = "1.234,56"
    validate_currency_format(currency_value)
except CurrencyFormatException as e:
    print(e)