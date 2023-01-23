import datetime as dt
import os
import dotenv
from dotenv import load_dotenv


class Car:
    dotenv.load_dotenv()

    def __init__(self):
        self.feul = int(os.getenv('FEUL'))
        self.feulPerMile = int(os.getenv('FEULPERMILE'))
        self.money = int(os.getenv('MONEY'))
        self.gear = int(os.getenv('GEAR'))
        self.speed = int(os.getenv('SPEED'))
        self.status_engine = os.getenv('STATUS_ENGINE')

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

    def set_gear(self, gear):
        self.gear = gear

    def get_gear(self):
        return self.gear

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

    def fuel_to_buy(self, km):
        """
         :name : Dani
         :date : 22/01/20213
         :describe : the function fuel the car
         :param : self
         :return : - the amount of money to pay for feul ac1orrding to the destntion
         """
        if self.money == 0:
            raise ValueError(os.getenv('VALUE_ERROR1'))
        elif self.money < ((km) // self.feulPerMile) * os.getenv('FEUL_PRICE'):
            raise ValueError(os.getenv('VALUE_ERROR2'))
        else:
            x = (int(km) // self.feulPerMile) * os.getenv('FEUL_PRICE')
            return x

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
            feul_Per_mile_predicted = (km_to_drive // self.feulPerMile)
            return feul_Per_mile_predicted <= self.feul

    def write_to_log(self, str):
        f = open('C:/Users/danie/PycharmProjects/Car/CarLog.txt', "a")
        f.write(f"{str} {dt.datetime.now()}\n")
        f.close()
