import csv
import pandas
import math

# with open("dia25/weather_data.csv") as file:
#     reader=csv.reader(file)
#     temperatures=[]
#     for row in reader:
#         # print (row)
#         if row[1]!='temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


data=pandas.read_csv("dia25/weather_data.csv")

#Así imprimo la columna de condition
print(data["condition"])

#Así saco el promedio de las temperaturas
tlist=data["temp"].mean()
print(tlist)

#Así saco el la temperatura mayor
print(data["temp"].max())

#Así saco la informacion del día monday
print(data[data.day=="Monday"])


#Así saco la fila del día con la mayor temperatura
print("\n")
monday=data[data.temp==data.temp.max()]

#Así convierto la temperatura del día más caliente a fahrenheit
tfahrenheit=(int(monday.temp)*9/5)+32
print(f"tfahrenheit: {tfahrenheit}")

#Así creo un dataframe y lo convierto a un csv
data_dict={
    "students": ["Amy","James", "Angela"], 
    "scores": [76,56,65]
}

info=pandas.DataFrame(data_dict)
info.to_csv("dia25/CSV.csv")