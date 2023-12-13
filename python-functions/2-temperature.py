def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
convert_to_celsius = __import__('2-temperature').convert_to_celsius

print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(-459.67))
print(convert_to_celsius(32))

# def convert_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9

# temperatures = [100, -40, -459.67, 32]

# for temperature in temperatures:
#     print(convert_to_celsius(temperature))
