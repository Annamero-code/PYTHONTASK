def fahrenheit(celsius):
    """Temperature Conversion"""
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit
    
print("Celsius \t  fahrenheit")
   
for  celsius in range(101): 
   
    print(celsius, "\t" ,fahrenheit(celsius))
