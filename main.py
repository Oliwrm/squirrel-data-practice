# #with open("./weather_data.csv") as weather_data:
#  #   data=weather_data.readlines()
#   #  print(data)
#
# # import csv
# # with open("./weather_data.csv") as weather_data:
# #     data=csv.reader(weather_data)
# #     temps=[]
# #     for row in data:
# #         if row[1]!="temp":
# #             temps.append(int(row[1]))
# #     print(temps)
#
# import pandas
# #total=0
# data= pandas.read_csv("weather_data.csv")
# # temp_list=data["temp"].to_list()
# # for temp in temp_list:
# #     total+=temp
# # print(total/len(temp_list))
# # print(data["temp"].mean())
# # print(data["temp"].max())
# # print(data[data.temp==data.temp.max()])
# monday=data[data.day=="Monday"]
# print(monday.temp)


import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
greys_count= len(data[data["Primary Fur Color"] == "Gray"])
reds_count= len(data[data["Primary Fur Color"] == "Cinnamon"])
blacks_count= len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Colour": ["Grey","Cinnamon","Black"],
    "Count": [greys_count,reds_count,blacks_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


