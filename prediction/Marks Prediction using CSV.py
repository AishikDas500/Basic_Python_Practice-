from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
import pandas as pd 

file_path = str(input("Enter the file path of the CSV: ")).strip().strip('"') # Takes the file path as input and removes any extra spaces or quotes
try:
    csv = pd.read_csv(file_path)
except Exception as e:
    print("Error while reading file" , e)
    exit()
while True: 
    # Train the model if required columns are present
    if "Hours" in csv.columns and "Scores" in csv.columns:
        x = csv[['Hours']]  # Features (independent variable)
        y = csv["Scores"]  # Target variable (dependent variable)
        model = LinearRegression()
        model.fit(x, y)       # Training model on the data
        predictions = model.predict(x)     # Predicting based on the trained data

    user_choice = int(input("""Enter what do you want to do with the provided data:
                            1| Print General Overview of the CSV
                            2| Plot the Original Data 
                            3| Perform Linear Regression on the Data
                            4| Perform Linear Regression and compare the graph between Original Data and Best-fit Line
                            5| Using Linear Regression check predicted scores for different hours value
                            6| Exit"
                            """))
    if user_choice == 1:
        print(csv.head())                   #Prints first 5 rows
        print(csv.tail())                  #Prints last 5 rows
        print(csv.shape)                    #No. of columns and rows
        print(csv.columns)                  #Columns in the CSV and its object type
        print(csv.describe())               #Describes the CSV with mean count etc.
        print(csv.dtypes)                   #Provides what type of object the columns have 
    elif user_choice == 2:
        if "Hours" in csv.columns and "Scores" in csv.columns:
            plt.scatter(csv['Hours'], csv['Scores'])
            plt.xlabel("Hours Studied")
            plt.ylabel("Scores")
            plt.title("Hours vs Scores")
            plt.show()
        else: 
            print("Required columns not found in the CSV file")
            quit()
    elif user_choice == 3:
        print("Slope: ", model.coef_[0])
        print("Intercept: ", model.intercept_)

    elif user_choice == 4:
        if "Hours" in csv.columns and "Scores" in csv.columns:
            plt.scatter(csv["Hours"], csv["Scores"], color = "orange", label = "Original Data")
            plt.plot(csv["Hours"], predictions , color = "red", label = "Best-fit Line")

            plt.title("Regression vs Original Data")
            plt.xlabel("Hours")
            plt.ylabel("Scores")
            plt.legend()
            plt.show()
        else:
            print("Required columns not found in the CSV file")

    elif user_choice == 5:
        if "Hours" in csv.columns and "Scores" in csv.columns:
            hours = float(input("Enter the hour parameter to check the respective Score: "))
            predicted_score = model.predict([[hours]])
            print(f"For {hours} hours the predicted score is {predicted_score[0]}")
        else:
            print("Required columns not found in the CSV file")

    elif user_choice == 6:
        break
    else:
        break