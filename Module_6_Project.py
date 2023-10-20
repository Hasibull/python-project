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
    
    if option == 1:
        manual_chart()
    elif option == 2:
        file_chart()


def get_data(axis) -> list:
    while True:
        values = input(f"Please enter the {axis}-axis values as list (i.e. 1, 2, 3)\n$: ").strip()
        values = values.split(",")
        final_data = []
        is_corrupted = False
        for value in values:
            try:
                data = float(value)
            except ValueError:
                print("Data is corrupted!!")
                final_data.clear()
                is_corrupted = True
                break
            else:
                final_data.append(data)
        
        if not is_corrupted:
            break
    
    return final_data


def manual_chart():
    x_values = get_data("x")
    y_values = get_data("y")
    while len(y_values) != len(x_values):
        print("x-axis and y-axis should have same number of data elements!")
        y_values = get_data("y")
    
    is_titled = input("Would you like a plot title? [Y/N]: ")
    plot_title = input("Please enter a plot title: ")
    is_x_label = input("Would you like an x-axis label? [Y/N]: ")
    x_label = input("Please enter x-axis label: ")
    is_y_label = input("Would you like an y-axis label? [Y/N]: ")
    y_label = input("Please enter y-axis label: ")


def file_chart():
    pass


if __name__ == "__main__":
    main()