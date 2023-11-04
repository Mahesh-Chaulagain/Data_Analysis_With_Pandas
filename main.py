import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
color = data["Primary Fur Color"]   # access the "Primary Fur Color" column
gray_squirrels_count = len(data[color == "Gray"])   # check if color column equals to Gray and count the number
red_squirrels_count = len(data[color == "Cinnamon"])    # check if color column equals to Cinnamon and count the number
black_squirrels_count = len(data[color == "Black"])     # check if color column equals to Black and count the number

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")
