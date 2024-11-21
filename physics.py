from operator import truediv


def calculate_distance():
    speed=float(input("speed"))
    time=float(input("time"))
    distance=speed/time
    print("distance is" ,distance)


def calculate_velocity():
    displacement=float(input("displacement"))
    time=float(input("time"))
    velocity=displacement/time
    print("velocity is" ,velocity)


def calculate_density():
    mass=float(input("mass"))
    volume=float(input("volume"))
    density=mass/volume
    print("density is",density)


def calculate_power():
    work=float(input("work"))
    time=float(input("time"))
    power=work/time
    print("power is",power)


def calculate_momentum():
    mass=float(input("mass"))
    velocity=float(input("velocity"))
    momentum=mass*velocity
    print("momentum is",momentum)


def main():
    while True:
        print("physics formula calculator")
        print("1. distance")
        print("2. velocity")
        print("3. density")
        print("4. power")
        print("5. momentum")

        choice = int(input("enter your choice(1/2/3/4/5):"))

        if choice == 1:
            calculate_distance()
        elif choice == 2:
             calculate_velocity()
        elif choice == 3:
             calculate_density()
        elif choice == 4:
            calculate_power()
        elif choice == 5:
            calculate_momentum()
        elif choice == 6:
            break
        else:
            print("invalid choice. please try again")

if __name__ == "__main__":
    main()


