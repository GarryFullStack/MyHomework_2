class Transport:

   def __init__(self, name, max_speed, mileage):

     self.name = name

     self.max_speed = max_speed

     self.mileage = mileage

   def seating_capacity(self, capacity):

    return f"Вместимость одного автобуса Renault Logan: {capacity} пассажиров"

class Autobus(Transport):

   def seating_capacity(self, capacity = 50):

    return super ().seating_capacity (capacity = 50)

Bus = Autobus("Renault Logan", 180, 12)

print(Bus.seating_capacity())
