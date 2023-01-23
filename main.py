from car import Car

if __name__ == '__main__':
    car = Car()
    try:

        car.start_engine()
        car.if_drive_destination_is_posible(150)
        car.set_gear()
        car.stop_engine()

    except ValueError as e:
        print(e)
        car.write_to_log(e)

    except OverflowError as e:
        print(e)
        car.write_to_log(e)


    except Exception as e:
        print("Some Other Errors")
        car.write_to_log(e)
