
import random


cityName = ["Paris","London", "Mexico", "Roma", "Berlin", "Madrid"]


cityTemps = {city : random.randint(20,30) for city in cityName}

print(cityTemps)

cityAbove25 = {city: temperatur  for (city,temperatur) in cityTemps.items() if (temperatur > 25)}

print(cityAbove25)


