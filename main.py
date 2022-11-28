# Program to create a graph to show the amounts of claims per month
# Author: Jonah Greening              Date: Nov 28, 2022

import matplotlib.pyplot as plt

Amt_List = []

List_Length = 12

for Amt in range(List_Length):
    Num = int(input("Enter the claims amount: "))
    Amt_List.append(Num)


x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_axis = Amt_List

plt.title("Total Amount of Claims ($)")
plt.scatter(x_axis, y_axis, color="red", marker="x", label="Claims Amount")

plt.xlabel("Time (months)")
plt.ylabel("Price (dollars)")

plt.grid(True)
plt.legend()

plt.show()
