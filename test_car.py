import pytest
from car import Car
from infra import write_to_log


@pytest.fixture
def car():
    return Car()


def test_start_engine(car):
    """
     :name : Dani
     :date : 22/01/2023
     :describe : the function will check if the engine starts
     :param : -
     :return : -
     :test: Pass
    """
    try:
        car.start_engine()
        assert car.get_gear() == 0
        assert car.status_engine == True
        car.write_to_log(f'Passed(test_start_engine):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_start_engine): {ae}')


def test_start_engine_should_fail(car):
    """
    :name : Dani
    :date : 22/01/2023
    :describe : the function will check if the engine starts
    :param : -
    :return : -
    :test: fail
    """
    try:
        car.start_engine()
        assert car.get_gear() == 0
        assert car.status_engine == False
        car.write_to_log(f'Passed(test_start_engine):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_start_engine): {ae}')


def test_set_gear(car):
    """
    :name : Dani
    :date : 22/01/2023
    :describe : the function will set the gear
    :param : int 0,1,2,3,4,5,6
    :return : -
    :test: Pass
    """
    try:
        car.set_gear(2)
        assert car.get_gear() == 2
        car.write_to_log(f'Passed(test_set_gear):')
    except AssertionError as ae:
        car.write_to_log(f"Failed (test_set_gear):  {ae}")


def test_set_gear_should_Fail(car):
    """
      :name : Dani
      :date : 22/01/2023
      :describe : the function will set the gear
      :param : int 0,1,2,3,4,5,6
      :return : -
      :test: fail
      """
    try:
        car.set_gear(2)
        assert car.get_gear() == 3
        car.write_to_log(f'Passed(test_set_gear):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_set_gear): {ae}')


def test_get_gear(car):
    """
      :name : Dani
      :date : 22/01/2023
      :describe : the function will get the gear
      :param :
      :return : - int- 0,1,2,3,4,5,6
      :test: PASS
      """
    try:
        assert car.get_gear() == 0
        car.write_to_log(f'Passed(test_get_gear):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_get_gear): {ae}')


def test_get_gear_shoud_fail(car):
    """
      :name : Dani
      :date : 22/01/2023
      :describe : the function will get the gear
      :param :
      :return : - int- 0,1,2,3,4,5,6
      :test: fail
      """
    try:
        assert car.get_gear() == 1
        car.write_to_log(f'Passed(test_get_gear):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_get_gear): {ae}')


def test_get_speed_car(car):
    """
      :name : Dani
      :date : 22/01/2023
      :describe : the function will return the speed
      :param :
      :return :  int 60
      :test: PASS
      """
    try:
        car.set_gear(2)
        assert car.get_car_speed() == 60
        car.write_to_log(f'Passed(test_get_speed_car):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_get_speed_car): {ae}')


def test_get_speed_car_should_fail(car):
    """
     :name : Dani
     :date : 22/01/2023
     :describe : the function will return the speed
     :param :
     :return :  int 60
     :test: fail
     """
    try:
        car.set_gear(2)
        assert car.get_car_speed() == 70
        car.write_to_log(f'Passed(test_get_speed_car):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_get_speed_car): {ae}')


@pytest.mark.one
def test_stop_engine(car):
    """
     :name : Dani
     :date : 22/01/2023
     :describe : the function will stop the engine
     :param :
     :return :
     :test: pass
     """
    try:
        car.stop_engine()
        assert car.get_gear() == 0
        assert car.status_engine == False
        car.write_to_log(f'Passed(test_stop_engine):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_stop_engine): {ae}')


@pytest.mark.skip
def test_fuel_to_buy(car):
    """
     :name : Dani
     :date : 22/01/2023
     :describe : the function will return the speed
     :param :
     :return :
     :test: skip
     """
    try:
        assert car.fuel_to_buy(50) == 35
        car.write_to_log(f'Passed(test_fuel_to_buy):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_fuel_to_buy): {ae}')


def test_if_drive_destination_is_possible(car):
    """
     :name : Dani
     :date : 22/01/2023
     :describe : the function will calculate if there is enough fuel for the new destination
     :param :
     :return :  Bool True
     :test: pass
     """
    try:
        assert car.if_drive_destination_is_posible(100) == True
        car.write_to_log(f'Passed(test_fuel_to_buy):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_fuel_to_buy): {ae}')


def test_if_drive_destination_is_possible_should_fail(car):
    """
     :name : Dani
     :date : 22/01/2023
     :describe : the function will calculate if there is enough fuel for the new destination
     :param :
     :return :  bool False
     :test: fail
     """
    try:
        assert car.if_drive_destination_is_posible(1050) == True
        car.write_to_log(f'Passed(test_if_drive_destination_is_posible_should_fail):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_if_drive_destination_is_possible_should_fail): {ae}')


def test_drive_gear(car):
    """
     :name : Dani
     :date : 22/01/2023
     :describe : the function will check if the gear is 0 thats means that the engine is stopped.
     :param :
     :return :  true
     :test: pass
    """
    try:
        car.start_engine()
        car.set_gear(3)
        car.drive(20)
        assert car.get_gear() == 0
        car.write_to_log(f'Passed(test_drive):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_drive): {ae}')


def test_drive_not_enoug_money_should_fail(car):
    """
    :name : Dani
    :date : 22/01/2023
    :describe : the function will check if there is enough money to fuel the car by the km were given
    :param :
    :return :  -
    :test: fail
    """
    with pytest.raises(Exception) as e:
        car.start_engine()
        car.drive(1050)  # 1000*0.05*10 = 500 <,1050 = 525 not enough cash
    car.write_to_log(e)


def test_drive_fuel_should_fail(car):
    """
   :name : Dani
   :date : 22/01/2023
   :describe : the function will check over refuel
   :param :
   :return :  -
   :test: fail
   """
    with pytest.raises(Exception) as e:
        car.start_engine()
        car.drive(650)  # 600 * 0.05 = 30 capacity = 50 current fuel = 30 <650 Over refuel
    car.write_to_log(e)


def test_fill_fuel(car):
    """
     :name : Dani
     :date : 22/01/2023
     :describe : the function calculate the total money that left (money = 500 ,300*0.05*10 = 150 , 500-150 = 350 !)
     :param : int km
     :return :  -
     :test: pass
     """

    try:
        car.start_engine()
        car.fill_fuel(300)
        assert car.get_money() == 350
        car.write_to_log(f'Passed(test_drive):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_drive): {ae}')


def test_fill_fuel_should_fail(car):
    """
     :name : Dani
     :date : 22/01/2023
     :describe : the function calculate the total money that left inserting wrong value
     :param : int km
     :return :  -
     :test: fail
     """
    try:
        car.start_engine()
        car.fill_fuel(300)
        assert car.get_money() == 355
        car.write_to_log(f'Passed(test_drive):')
    except AssertionError as ae:
        car.write_to_log(f'Failed (test_drive): {ae}')
