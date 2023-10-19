# Importing necessary libraries
import matplotlib.pyplot as plt

# Global variables


def main():
    print("Welcome to the chartmaker! Please begin by choosing one of the following options")
    print("Option 1: Manual Data Entry")
    print("Option 2: Enter Data From Text File")

    while True:
        try:
            option = int(input("Choose an option (1/2): "))
        except ValueError:
            print("Enter valid option!!")
        else:
            if option in [1, 2]:
                break
            else:
                print("Choose 1 or 2")




if __name__ == "__main__":
    main()