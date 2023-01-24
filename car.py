import datetime as dt
import os
from dotenv import load_dotenv


class Car:
    load_dotenv()

    def __init__(self):
        self.fuel = int(os.getenv('FUEL'))
        self.fuelPerKm = float(os.getenv('FUELPERKM'))
        self.money = int(os.getenv('MONEY'))
        self.gear = int(os.getenv('GEAR'))
        self.speed = int(os.getenv('SPEED'))
        self.status_engine = os.getenv('STATUS_ENGINE')
        self.capacity = int(os.getenv('CAPACITY'))

    def start_engine(self):
        """
            :name : Dani
            :date : 22/01/20213
            :describe : the function will start the engine
            :param : self
            :return :
        """
        self.status_engine = True
        self.gear = 0

    def get_start_engine(self):
        return self.status_engine

    def get_status_engine(self):
        return self.status_engine

    def set_fuel(self, fuel):
        self.fuel = fuel

    def get_fuel(self):
        return self.fuel

    def get_money(self):
        return self.money

    def set_gear(self, gear):
        if gear > 6:
            raise OverflowError(os.getenv('OVERFLOW_ERROR1'))
        elif gear < 0:
            raise OverflowError(os.getenv('OVERFLOW_ERROR2'))
        else:
            self.gear = gear

    def get_gear(self):
        return self.gear

    def get_capacity(self):
        return self.capacity

    def get_car_speed(self):
        """
          :name : Dani
          :date : 22/01/20213
          :describe : the function will show the speed
          :param : self
          :return : speed
         """
        speed = self.gear * 30
        return speed

    def stop_engine(self):
        """
          :name : Dani
          :date : 22/01/20213
          :describe : the function will stop the engine
          :param : self
          :return : -
              """
        self.status_engine = False
        self.gear = 0
        self.speed = 0

    def get_fuel_per_km(self):
        return self.fuelPerKm

    def drive(self, km_to_drive):
        """
        :name: Dani
        :Date: 22/01/2023
        :description: this function will check if the car can start the driving
        :param km_to_drive:
        :return: -
        """
        needed_fuel = km_to_drive * self.get_fuel_per_km()
        if self.status_engine == True:
            if km_to_drive <= 0:
                raise ValueError(os.getenv('VALUE_ERROR5'))
            if needed_fuel > self.get_fuel():
                self.fill_fuel(needed_fuel)
                raise OverflowError(os.getenv('OVERFLOW_ERROR3'))
            else:
                self.set_gear(1)
                self.fuel -= km_to_drive * self.get_fuel_per_km()
                self.stop_engine()
        else:
            raise ValueError(os.getenv('VALUE_ERROR3'))

    def fill_fuel(self, km):
        """
         :name : Dani
         :date : 22/01/20213
         :describe : the function fuel the car
         :param : self
         :return : - the amount of money to pay for fuel according to the destntion
         """
        fill_fuel = self.get_capacity() - self.get_fuel()
        if ((km * self.get_fuel_per_km()) * int(os.getenv('FUEL_PRICE')) > self.get_money()):
            raise OverflowError(os.getenv('OVERFLOW_ERROR5'))
        if ((km * self.get_fuel_per_km()) > fill_fuel):
            raise OverflowError(os.getenv('OVERFLOW_ERROR6'))
        else:
            self.fuel += fill_fuel
            self.money -= (km * self.get_fuel_per_km()) * int(os.getenv('FUEL_PRICE'))

    def if_drive_destination_is_posible(self, km_to_drive):
        """
         :name : Dani
         :date : 22/01/20213
         :describe : the function will calculate the destination that the car can reach
         :param : self
         :return : destination
        """
        if self.start_engine() == True:
            raise ValueError(os.getenv('VALUE_ERROR3'))
        if km_to_drive == 0:
            raise ValueError(os.getenv('VALUE_ERROR4'))
        else:
            fuel_Per_Km_predicted = (km_to_drive // self.fuelPerKm)
            return fuel_Per_Km_predicted <= self.fuel

    def write_to_log(self, str):
        f = open(os.getenv('PATHLOG'), "a")
        f.write(f"{str} {dt.datetime.now()}\n")
        f.close()
