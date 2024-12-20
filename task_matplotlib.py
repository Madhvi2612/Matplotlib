# -*- coding: utf-8 -*-
"""Task Matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jMKNkwVcw6A_1VfUxFWRUXBn50u8UZPi

Exercise 1: Basic Line Plot
- **Task**: Create a line plot using the following data:
  ```python
  x = [1, 2, 3, 4, 5]
  y = [2, 4, 6, 8, 10]
  ```
  - Label the x-axis as **"X-Axis"** and the y-axis as **"Y-Axis"**.
  - Add a title: **"Simple Line Plot"**.
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Simple Line Plot')

plt.show()

"""Exercise 2: Bar Chart of Scores
- **Task**: Create a bar chart showing the scores of students:
  - **Categories**: `['Student A', 'Student B', 'Student C']`
  - **Values**: `[85, 90, 78]`
  - Label the x-axis as **"Students"** and the y-axis as **"Scores"**.
  - Add a title: **"Students' Scores"**.
"""

import matplotlib.pyplot as plt

Students = ['Student A', 'Student B', 'Student C']
Scores = [85, 90, 78]

plt.bar(Students, Scores)

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title("Students' Scores")

plt.show()

"""Exercise 3: Scatter Plot of Heights vs Weights
- **Task**: Create a scatter plot using the following data:
  ```python
  heights = [150, 160, 170, 180, 190]
  weights = [50, 60, 65, 80, 85]
  ```
  - Label the x-axis as **"Heights"** and the y-axis as **"Weights"**.
  - Add a title: **"Heights vs Weights"**.
"""

import matplotlib.pyplot as plt

categories = [150, 160, 170, 180, 190]
values = [550, 60, 65, 80, 85]

plt.scatter(categories, values)

plt.xlabel('Heights')
plt.ylabel('Weights')
plt.title("Heights vs Weights")

plt.show()

"""Exercise 4: Line Plot of Temperature Over Time
- **Task**: Create a line plot showing the change in temperature over time:
  ```python
  time = [1, 2, 3, 4, 5]
  temperature = [30, 32, 35, 33, 31]
  ```
  - Label the x-axis as **"Time"** and the y-axis as **"Temperature"**.
  - Add a title: **"Temperature Over Time"**.
"""

import matplotlib.pyplot as plt

time = [1, 2, 3, 4, 5]
temperature = [30, 32, 35, 33, 31]

plt.plot(time, temperature)

plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Temperature Over Time')

plt.show()

"""Exercise 5: Bar Chart for Favorite Colors
- **Task**: Create a bar chart showing how many people like each color:
  - **Categories**: `['Red', 'Blue', 'Green', 'Yellow']`
  - **Values**: `[10, 20, 15, 5]`
  - Label the x-axis as **"Colors"** and the y-axis as **"Number of People"**.
  - Add a title: **"Favorite Colors"**.
"""

import matplotlib.pyplot as plt

categories = ['Red', 'Blue', 'Green', 'Yellow']
values = [10, 20, 15, 5]

plt.bar(categories, values)

plt.xlabel('Colors')
plt.ylabel('Number of Colors')
plt.title('Favorite Colors')
plt.show()

"""Exercise 6: Scatter Plot of Age vs Height
- **Task**: Create a scatter plot using the following data:
  ```python
  age = [10, 12, 14, 16, 18]
  height = [140, 145, 150, 160, 170]
  ```
  - Label the x-axis as **"Age"** and the y-axis as **"Height"**.
  - Add a title: **"Age vs Height"**.
"""

import matplotlib.pyplot as plt

categories = [10, 12, 14, 16, 18]
values = [140, 145, 150, 160, 170 ]

plt.scatter(categories, values)

plt.xlabel('Age')
plt.ylabel('Height')
plt.title('Age vs Height')

plt.show()

"""Exercise 7: Customizing Line Plot
- **Task**: Create a line plot using the following data:
  ```python
  x = [1, 2, 3, 4]
  y = [1, 4, 9, 16]
  ```
  - Change the line color to **red** and the line style to **dashed (`'--'`)**.
  - Add labels for both axes and a title.
"""

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1, 4, 9, 16]
plt.plot(x, y, color='r', linestyle='--')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple line plot')

plt.show()

""" Exercise 8: Bar Chart of Monthly Sales
- **Task**: Create a bar chart to show monthly sales:
  - **Categories**: `['January', 'February', 'March']`
  - **Values**: `[300, 400, 350]`
  - Label the x-axis as **"Months"** and the y-axis as **"Sales"**.
  - Add a title: **"Monthly Sales"**.
"""

import matplotlib.pyplot as plt

categories = ['January', 'February', 'March']
values = [300, 400, 350]

plt.bar(categories, values)

plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales')

plt.show()

"""Exercise 9: Scatter Plot for Test Scores
- **Task**: Create a scatter plot showing scores in two different subjects:
  ```python
  subject1_scores = [80, 85, 88, 90]
  subject2_scores = [70, 78, 85, 87]
  ```
  - Label the x-axis as **"Subject 1 Scores"** and the y-axis as **"Subject 2 Scores"**.
  - Add a title: **"Test Scores Comparison"**
"""

import matplotlib.pyplot as plt

subject1_scores= [80, 85, 88, 90]
subject2_scores = [70, 78, 85, 87]

plt.scatter(subject1_scores, subject2_scores)

plt.xlabel('Subject 1 Scores')
plt.ylabel('Subject 2 Scores')
plt.title('Test Scores Comparison')

plt.show()

"""Exercise 10: Simple Line Plot with Labels
- **Task**: Create a line plot using the following data:
  ```python
  x = [0, 1, 2, 3, 4]
  y = [0, 1, 4, 9, 16]
"""

import matplotlib.pyplot as plt

x = [0,1,2,3,4]
y = [0,1,4,9,16]

plt.plot(x, y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple line plot')

plt.show()