import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import os
from sys import platform
from os.path import exists


def clear_console():
    if platform == "linux" or platform == "linux2":
        # Platform is Linux
        os.system("clear")
    elif platform == "darwin":
        # Platform is Mac OS X
        os.system("clear")
    elif platform == "win32":
        # Platform is Windows
        os.system("cls")


def system_pause_console():
    os.system("PAUSE")


# Function to get unique values
def unique_values_in_list(input_list):
    # initialize a null list
    unique_list = []
    # traverse for all elements
    for x in input_list:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)

    return unique_list


def menu_dialog():
    print("Enter a number of your choice:")
    print("1. Enter numbers to check the class")
    print("2. Print all x values - DATASET")
    print("3. Print all y values - DATASET")
    print("4. Print all model names - DATASET")
    print("5. Exit Program")


def first_menu_dialog():
    print("Enter a number of your choice:")
    print("1. Enter Custom Path for CSV file")
    print("2. Run the program with predefined CSV file.")


csv_final_path = "train_dataset.csv"
first_menu_dialog()
first_user_choice = input('Give a number of your choice: ')
while True:
    if int(first_user_choice) == 1:
        csv_path = input("Paste the file path here: ")
        if exists(csv_path):
            # File Exists
            if '.csv' in csv_path:
                # File is CSV
                csv_final_path = csv_path
                break
            else:
                # File is NOT CSV
                print("File is NOT CSV.")
        else:
            # File does NOT exists
            print("File does NOT exists.")
    elif int(first_user_choice) == 2:
        # Run program with predefined CSV
        csv_final_path = 'train_dataset.csv'
        break
    else:
        # User input in not eligible
        print("User input number is NOT eligible")

    first_menu_dialog()
    first_user_choice = input('Give a number of your choice: ')

print("Training Dataset...")

# Open Dataset CSV for Training
df = pd.read_csv("train_dataset.csv")
df.head()

inputs = df.drop('model', axis='columns')
target = df['model']

the_model = LabelEncoder()
the_x_value = LabelEncoder()
the_y_value = LabelEncoder()

# inputs['model_number'] = the_model.fit_transform(inputs['model'])
inputs['model_x_value'] = the_x_value.fit_transform(inputs['x_value'])
inputs['model_y_value'] = the_y_value.fit_transform(inputs['y_value'])

inputs_n = inputs.drop(['x_value', 'y_value'], axis='columns')

model = tree.DecisionTreeClassifier()
model.fit(inputs_n, target)
model.score(inputs_n, target)

print("Dataset Trained.")

while True:
    clear_console()
    menu_dialog()
    user_choice = input("Give a number of your choice: ")
    if int(user_choice) == 1:
        user_x_value = input("Give the x value: ")
        user_y_value = input("Give the y value: ")
        model_name_prediction = model.predict([[float(user_x_value), float(user_y_value)]])
        print("The model name, of the values x=", user_x_value, "and y=", user_y_value, "is: ", model_name_prediction[0])
    elif int(user_choice) == 2:
        x_values = []
        for i in range(0, len(inputs_n['model_x_value']), 1):
            x_values.append(inputs_n['model_x_value'][i])
        else:
            print(x_values)
    elif int(user_choice) == 3:
        y_values = []
        for i in range(0, len(inputs_n['model_y_value']), 1):
            y_values.append(inputs_n['model_y_value'][i])
        else:
            print(y_values)
    elif int(user_choice) == 4:
        model_names = []
        for i in range(0, len(df.model), 1):
            model_names.append(df.model[i])
        else:
            print(unique_values_in_list(model_names))
    elif int(user_choice) == 5:
        quit(0)
    else:
        print("Wrong choice.")

    system_pause_console()