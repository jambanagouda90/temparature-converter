# Temperature Converter
def validate_celsius(celsius):
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero")
    return celsius

def celsius_to_fahrenheit(celsius):
    celsius = validate_celsius(celsius)
    return round((celsius * 9 / 5) + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    celsius = validate_celsius(celsius)
    return round(celsius, 2)

def convert(value, choice):
    if choice == 1:
        return celsius_to_fahrenheit(value), "°F"
    elif choice == 2:
        return fahrenheit_to_celsius(value), "°C"
    else:
        raise ValueError("Invalid choice")

# Main program
if __name__ == "__main__":
    print("===== TEMPERATURE CONVERTER =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Enter your choice (1/2): "))
    value = float(input("Enter the temperature: "))
    result, unit = convert(value, choice)
    print("\n----- CONVERSION RESULT -----")
    print("Input Temperature:", value)
    print("Converted Temperature:", result, unit)
