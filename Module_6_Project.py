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


def yes_or_no(message) -> str:
    choice = input(f"Would you like a {message}? [Y/N]: ").strip().lower()
    while choice not in ["Y", "y"]:
        print("Please type 'Y' for yes or 'N' for no!")
        choice = input(f"Would you like a {message}? [Y/N]: ").strip().lower()
    
    return choice


def get_name(message) -> str:
    value = input(f"Please enter a {message}: ")
    while len(value) <= 0:
        print(f"{message} can't be empty!")
        value = input(f"Please enter a {message}: ")
    
    return value


def manual_chart() -> None:
    """This function take input from user.
    It check some data validation and display the chart
    according to the user data."""
    # Getting x and y axis values
    x_values = get_data("x")
    y_values = get_data("y")
    while len(y_values) != len(x_values):
        print("x-axis and y-axis should have same number of data elements!")
        y_values = get_data("y")
    
    # Getting title
    is_titled = yes_or_no("plot title")
    if is_titled == "y" or is_titled == "Y":
        plot_title = get_name("plot title")
    
    # Getting x-axis label
    is_x_label = yes_or_no("x-axis label")
    if is_x_label == "y" or is_x_label == "Y":
        x_label = get_name("x-axis label")
    
    # Getting y-axis label
    is_y_label = yes_or_no("y-axis label")
    if is_y_label == "y" or is_y_label == "Y":
        y_label = get_name("y-axis label")

    # Getting line style
    is_line_style = yes_or_no("custom line style")
    if is_line_style == "y" or is_line_style == "Y":
        print("Available line styles are-")
        print("1. Solid Line")
        print("2. Dotted Line")
        print("3. Dashed Line")
        print("4. Dash-Dotted Line")
        while True:
            try:
                style_option = int(input("Please choose a line style (1-4): "))
            except ValueError:
                print("Enter valid option!!")
            else:
                if style_option in [1, 2, 3, 4]:
                    break
                else:
                    print("Choose value between 1 to 4")
        if style_option == 1:
            line_style = "-"
        elif style_option == 2:
            line_style = ":"
        elif style_option == 3:
            line_style = "--"
        elif style_option == 4:
            line_style = "-."
            

def file_chart():
    pass


if __name__ == "__main__":
    main()