

import plotly. figure_factory as ff

import pandas as pd


import csv


import plotly.graph_objects as go


import statistics


import random


#reading scores data



data = df["reading score"].tolist()


df = pd.read_csv("Students Performance.csv")

#Calculating the mean and the standard deviation


mean = sum(data) / len(data)

std_deviation = statistics.stdev(data)

median statistics.median(data)

mode = statistics.mode (data)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation second_std_deviation_start, 
second_std_deviation_end = mean- n-(2*std_deviation), mean+(2*std_deviation) third_std_deviation_start, 
third_std_deviation_end = mean- (3*std_deviation), mean+(3*std_deviation) 



fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go. Scatter (x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go. Scatter (x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STAND" 
fig.add_trace(go. Scatter (x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STAND" 
fig.add_trace(go. Scatter (x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STAND" 
fig.add_trace(go. Scatter (x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STAND" fig.show()
list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result + f 
list_of_data_within_2_std_deviation [result for result in data if result > second_std_deviation <
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and 
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_deviation))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)) 
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(data) 
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)