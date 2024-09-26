numbers = [2,3,5,6,7,8,12,14,15,25,65,56,78]
pares = [number for number in numbers if number%2==0]
print(pares)

sqrt = []
for number in numbers:
    sqrt.append(number**2)
print(sqrt)

cars = ("ferrari", "gol", "lambhorghini",)
for indice, car in enumerate(cars):
    print(f"{indice}: {car}")



carros = ("gol") 
print(isinstance(carros, tuple))    