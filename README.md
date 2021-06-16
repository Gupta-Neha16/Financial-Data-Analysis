# Financial-Data-Analysis

The purpose of this coding project is to take a financial data set and analyze it. This dataset has been taken from Kaggle. There are 10,000 rows in the data set.


The goal is to understand relationship between a person's income, loan balance, status as a student(Yes/No) and if they have defaulted on their loan balance(Yes/No).

The columns in the data set are - 'default', 'student', 'balance' and 'income'

Top 4 rows from the dataset -

<img width="258" alt="Screen Shot 2021-06-11 at 8 46 03 PM" src="https://user-images.githubusercontent.com/29782408/121761547-0b94d180-caf6-11eb-8592-aaf8aa6e6266.png">

Description of the data set -

<img width="238" alt="Screen Shot 2021-06-11 at 8 46 47 PM" src="https://user-images.githubusercontent.com/29782408/121761565-25ceaf80-caf6-11eb-87b4-fc535eb868c7.png">

Using boxplot, we can visualize the “minimum”, first quartile (Q1), median, third quartile (Q3), and “maximum” for balance and income. 
There are outliers present in the balance data which would have to be cleaned out. 


<img width="940" alt="Screen Shot 2021-06-11 at 8 50 54 PM" src="https://user-images.githubusercontent.com/29782408/121761650-b907e500-caf6-11eb-861f-6aac865eac69.png">




The bar chart below shows the total count of students and the total count of people who have defaulted on their loans.

<img width="1002" alt="Screen Shot 2021-06-11 at 9 02 43 PM" src="https://user-images.githubusercontent.com/29782408/121761910-5fa0b580-caf8-11eb-9cef-ca2d02d42eeb.png">

The boxplot below highlights the range of loan balance left for people who have defaulted Vs people who have not defaulted on their payments. It also shows a the range of income of the people who have defaulted vs the income of the people who have not defaulted. The people who have defaulted have a similar salary range to people who have not dafaulted on their loan balance.

We are also able to see the outliers in the balance boxplot.

<img width="922" alt="Screen Shot 2021-06-11 at 9 05 22 PM" src="https://user-images.githubusercontent.com/29782408/121761962-bdcd9880-caf8-11eb-95be-040e8fec5993.png">

Being a student is not a big factor to determine if you would default.


![Screen Shot 2021-06-16 at 4 10 12 PM](https://user-images.githubusercontent.com/29782408/122294150-62672600-cebd-11eb-8721-0f04aeb0c4cc.png)


In this program, the outliers for the balance column have been removed and have been set to the upper limit value.

<img width="417" alt="Screen Shot 2021-06-11 at 9 10 30 PM" src="https://user-images.githubusercontent.com/29782408/121762107-7562aa80-caf9-11eb-81bc-309f6a1c7e06.png">



