import unittest
from car import Car


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.x = Car()

    def test_start_engine(self):
        try:
            self.x.start_engine()
            self.assertEqual(self.x.start_engine(), True)
            self.x.write_to_log(f'Passed(test_start_engine)')
        except AssertionError as ae:
            self.x.write_to_log(f'Failed (test_start_engine): {ae}')

    def test_set_gear(self):
        self.x.set_gear(2)
        try:

            self.assertEqual(self.x.get_gear(), 2)
            self.x.write_to_log(f'Passed(test_set_gear):')
        except AssertionError as ae:
            self.x.write_to_log(f'Failed (test_set_gear): {ae}')

    def test_get_gear(self):
        try:
            self.assertEqual(self.x.gear, 0)
            self.x.write_to_log(f'Passed(test_get_gear): ')
        except AssertionError as ae:
            self.x.write_to_log(f'Failed (test_get_gear): {ae}')

    def test_get_speed_car(self):
        try:
            self.x.set_gear(2)
            self.assertEqual(self.x.get_car_speed(), 60)
            # self.assertEqual(self.x.get_car_speed(),0)
            self.x.write_to_log(f'Passed(test_get_speed_car):')
        except AssertionError as ae:
            self.x.write_to_log(f'Failed (test_get_speed_car): {ae}')

    def test_stop_engine(self):
        try:
            self.x.stop_engine()
            self.assertEqual(self.x.get_status_engine(), False)
            self.x.write_to_log(f"Passed(test_stop_engine): ")
        except AssertionError as ae:
            self.x.write_to_log(f'Failed (test_stop_engine): {ae}')

    def test_fuel_to_buy(self):
        try:
            self.assertEqual(self.x.fuel_to_buy(100), 35)
            self.x.write_to_log(f"Passed(test_fuel_to_buy): ")
        except AssertionError as ae:
            self.x.write_to_log(f'Failed (test_fuel_to_buy): {ae}')

    def test_if_drive_destination_is_posible(self):
        try:
            self.x.if_drive_destination_is_posible(100)
            self.assertEqual(self.x.if_drive_destination_is_posible(100), True)
            self.x.write_to_log(
                f"Passed(test_if_drive_destination_is_posible):")
        except AssertionError as ae:
            self.x.write_to_log(f'Failed (test_fuel_to_buy) : {ae}')


if __name__ == '__main__':
    unittest.main()
