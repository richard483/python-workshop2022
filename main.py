# import numpy
# print("Hello World!")

# a = "Hello World!"

# print(a)

# #number
# b = 12 #int
# print(b.__class__)
# a = 12.34 #float
# print( (int)(a) + b)

# #operator
# a = 20
# b = 3

# print(a*b)
# print(a**b)
# print(a/b)
# print(a//b) #floor division

# #assignment
# a+=3 #a = a + 3
# a*=4 #a = a * 4
# print("Nilai A:", a)


# #comparison
# a = 4
# b = 4
# # print(a == b)
# # print(a != b)
# # print(a >= b)
# # # and: && ; or: || ; not: ! 
# # print((a==0) and (b == 3))

# #if else
# if (a == 3):
#     print("nilai a adalah 3")
# elif (a == b):
#     if(a == 10):
#         print("nilai a adalah 10 dan sama dengan b")
#     print("nilai a sama dengan b")
# else:
#     print("nilai a tidak ditemukan")



# a, b = 365, 12
# max = a if a > b else b

# print("Nilai max:", max)


#looping

#for

# for i in range (1, 15):
#     if(i == 7):
#         print("Nilai i adalah 7")
#         continue
#     print(i)

# j = 0

# while(j <10):
#     j += 1
#     print(j)

# numpy

# import numpy as np

# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr)

# import pandas as pd

# # df = pd.read_csv("Stores.csv")
# # print(df)

# fruitList = ["apple", "banana", "orange", "pineapple", "strawberry"]
fruitStock = [10, 20, 30, 40, 50]

# df = pd.DataFrame(fruitList)
# df["stock"] = fruitStock
# df.columns = ["Buah", "Stock"]
# print(df)

import matplotlib.pyplot as plt

#figure
#axes

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,4,9,16,25,36,49,64,81,100]

x1 = [1, 4, 6, 9, 12, 5]
y1 = [2, 8, 12, 18, 24, 20]

fig = plt.figure()
ax = fig.add_subplot()
ax.scatter(x, y, label="Line 1", color="#00ff00")
ax.plot(x1, y1, label="Line 2", color = "red")

ax.legend(loc = "upper left")
plt.show()




