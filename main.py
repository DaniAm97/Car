from car import Car

if __name__ == '__main__':
    car = Car()
    try:

        car.start_engine()
        car.if_drive_destination_is_posible(150)
        car.set_gear()
        car.stop_engine()

    except ValueError as v:
        print(v)
        car.write_to_log(v)

    except Exception as e:
        print("Some Other Errors")
        car.write_to_log(e)
