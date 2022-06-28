import pandas
data = pandas.read_csv("reviews.csv")

# filtering data based on conditions
print(data[data["Rating"] >= 4])

# count method
print(data[data["Rating"] >= 4].count())

# multiple conditions
print(data[(data["Rating"] > 4) & (data["Course Name"] == "The Complete Python Course: Build 10 Professional OOP Apps")]["Rating"].mean())