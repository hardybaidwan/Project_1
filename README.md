# Project_1
Dataset Link: https://www.kaggle.com/harrywang/housing

Live Link: https://share.streamlit.io/hardybaidwan/project_1/main/q1.py

We are displaying the dataset according to the user. By default, all the columns are displayed.

![image](https://user-images.githubusercontent.com/67311692/133879527-b77e880a-094c-468a-a040-2ceceb82b9c4.png)

Then we show the location of the houses on the map of California.

![image](https://user-images.githubusercontent.com/67311692/133879841-c2c26577-0373-452a-86bf-279857afce46.png)

Inside our model,we drop the null values before applying our model on it
Also ignore the unwanted columns for our model

Splitting test:train in 20:80.
And apply Random Forest on the remaining dataset which gives 75% accuracy.

This makes a model.pkl file which is loaded in our python file for calculating the outputs from user inputs.

![image](https://user-images.githubusercontent.com/67311692/133880191-5d6c8ee0-31af-49dd-b115-c55af16ec1bb.png)
