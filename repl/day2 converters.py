def convert_to_fahrenheit():
    celcius = float(input("Enter temperature in celcius: "))
    fahrenheit = celcius * 9 / 5 + 32
    print("In fahrenheit:", fahrenheit)

def convert_to_celcius():
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celcius = (fahrenheit - 32) * 5 / 9
    print("In celcius:", celcius)


unit = input("Convert from celcius, fahrenheit? ")

if unit == "celcius":
    convert_to_fahrenheit()
else:
    convert_to_celcius()
