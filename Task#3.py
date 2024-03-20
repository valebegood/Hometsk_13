class Car:
    
    
    def __init__(self, brand, model, year_build: int, speed: int ):
        self.brand = brand
        self.model = model
        self.year_build = year_build
        self.speed = speed

    def accelerate(self):
        
         self.speed +=5
         return self.speed 
    
    def brake(self):
        if self.speed <= 0:
            raise ValueError('You are already stopped!')
        self.speed -=5
        return self.speed
    
    def display_speed(self):
        return self.speed

First_car = Car(brand= 'BMW', model ='X6', year_build=2015, speed = 15)

print(First_car.speed)
print(First_car.accelerate())
print(First_car.brake())
print(First_car.brake())
print(First_car.display_speed())