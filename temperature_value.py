def temperature_check(celsius,fahrenheit):

    fahrenheit = (celsius * 9 / 5) + 32
    celsius = (fahrenheit - 32) * 5 / 9

    threshold = 50

    if fahrenheit < threshold:
        return "Cold advisory"
    elif fahrenheit >= threshold:
        return "Heat alert"

    if celsius < threshold:
        return "Cold advisory"
    elif celsius >= threshold:
        return "Heat alert"



celsius = float(input("enter celsius: "))
fahrenheit = float(input("enter fahrenheit: " ))

print(temperature_check(fahrenheit, celsius))


