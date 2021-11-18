def checkCelsius(tempF):
    res = ((tempF-32)*5)/9
    return res


def checkFahrenheit(tempC):
    res = (tempC*(9/5)+32)
    return res


tempC = float(input("Enter a temperature of a body (in Celsius):: "))
print(checkFahrenheit(tempC))
tempF = float(input("Enter a temperature of a body (in Fahrenheit):: "))
print(checkCelsius(tempF))
