import numpy as np
import matplotlib.pyplot as plt

hours_studied = np.linspace(0 , 10 , 100)                               # Create a random value of hours that have been studied    marks_obtained = 7 * hours_studied + 5                                 
predicted_marks = 7 * hours_studied + 5                                  # Create a linear graph using the hours studied to predict marks with random slope and constant 
randomness = np.random.randn(100) * 6                                   # Create randomness in marks 
marks_randomness = predicted_marks + randomness                          # Add the randomness to marks_obtained

slope = (np.mean(hours_studied * marks_randomness) - np.mean(hours_studied) * np.mean(marks_randomness)) / (np.mean(hours_studied ** 2) - (np.mean(hours_studied) ** 2))                        # Creates a slope based on means of hours studied and marks obtained 
constant = np.mean(marks_randomness) - slope * np.mean(hours_studied)   # Creates a constant using mean 
marks_obtained = slope * hours_studied + constant                      #Predicts the marks based on the predicted slope and constant 

plt.figure(figsize = (10, 6))
plt.scatter(hours_studied, marks_randomness , label = "Original Data" , color = "red")
plt.plot(hours_studied, marks_obtained , label = "Marks Obtained" , color = "blue" )
plt.xlabel("Hours Studied") 
plt.ylabel("Marks Obtained")
plt.title("Study Hours vs Marks (Regression)")
plt.legend()
plt.show()

ss_total = np.sum((marks_randomness - np.mean(marks_randomness)) ** 2)
ss_res = np.sum((marks_randomness - predicted_marks) ** 2)
r2 = 1 - (ss_res / ss_total)

print(f"R² Score: {r2:.3f}")

hours_test = np.array([3 , 6 , 10])  # test inputs
predicted_test = slope * hours_test + constant 

for h, p in zip(hours_test, predicted_test):
    print(f"Studying {h} hours → predicted marks = {p:.2f}")