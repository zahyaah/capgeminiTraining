from Car import Car 
from Bike import Bike 

carObject = Car("Audi")
bikeObject = Bike("Kawasaki")

maxSpeedCar = carObject.max_speed()
maxSpeedBike = bikeObject.max_speed()

print(carObject.brand)
print(maxSpeedCar)

print()

print(bikeObject.brand)
print(maxSpeedBike)
