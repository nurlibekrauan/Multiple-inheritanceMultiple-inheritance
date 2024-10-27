from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,speed,fuel_level):
        self._speed = speed
        self._fuel_level = fuel_level
    def refuel(self,amount):
        self._fuel_level += amount
    def check_fuel(self):
        if self._fuel_level==0:
            print(f"{self.__class__.__name__} has no fuel left.")
        else:
            print(f"{self.__class__.__name__} has {self._fuel_level} liters of fuel left.")
    def get_environment_type(self):
        print(F'{self.__class__.__name__}')
    
class LandVehicle(Vehicle):
    def move_on_land(self):
        self._speed +=10
        self._fuel_level-=5
        print(f"{self.__class__.__name__} is moving on land  at {self._speed} kilometers per hour.")
    def slow_down(self):
        self._speed -=5
        print(f"{self.__class__.__name__} is slowing down  at {self._speed} kilometers per hour.")

class WaterVehicle(Vehicle):
    def move_on_water(self):
        self._speed += 5
        self._fuel_level-=3
        print(f"{self.__class__.__name__} is moving on water  at {self._speed} kilometers per hour.")
    def halt_swim(self):
        self._speed = 0
        print(f"{self.__class__.__name__} is halting swim.")
class AirVehicle(Vehicle):
    def take_off(self):
        self._speed += 20
        self._fuel_level -= 15
        print(f"{self.__class__.__name__} is taake off  at {self._speed} kilometers per hour.")
    def land(self):
        self._speed =0
        print(f"{self.__class__.__name__} is landing  at {self._speed} kilometers per hour.")
class AmphibiousVehicle(LandVehicle,WaterVehicle):
    pass
class FlyingCar(LandVehicle,AirVehicle):
    pass

# Создание экземпляров различных транспортных средств
amphibious_vehicle = AmphibiousVehicle(speed=0, fuel_level=100)
flying_car = FlyingCar(speed=0, fuel_level=100)

# Передвижение амфибии по суше и воде
amphibious_vehicle.move_on_land()  # Амфибия движется по суше, скорость увеличивается
amphibious_vehicle.move_on_water()  # Амфибия движется по воде, расход топлива увеличивается

# Летающая машина взлетает и садится
flying_car.take_off()  # Летающая машина взлетает, расход топлива увеличивается
flying_car.land()  # Летающая машина садится, скорость падает до 0

# Заправка транспортных средств
amphibious_vehicle.refuel(50)  # Заправляем амфибию на 50 литров
flying_car.refuel(30)  # Заправляем летающую машину на 30 литров

# Проверка текущего уровня топлива
amphibious_vehicle.check_fuel()  # Проверяем топливо амфибии
flying_car.check_fuel()  # Проверяем топливо летающей машины
