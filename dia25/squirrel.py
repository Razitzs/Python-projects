from this import d
from matplotlib.pyplot import gray
import pandas
data=pandas.read_csv("dia25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


gray=len(data[data["Primary Fur Color"]=="Gray"])
black=len(data[data["Primary Fur Color"]=="Black"])
cinnamon=len(data[data["Primary Fur Color"]=="Cinnamon"])

data_dict={
    "primaryFurColor": ["gray", "black", "cinnamon"],
    "count": [gray, black,cinnamon]

}


f=pandas.DataFrame(data_dict)
f.to_csv("dia25/SquirrelFurData.csv")