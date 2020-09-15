import pandas as pd
import matplotlib.pyplot as plt
import csv

data_list = open("GSPC.txt", "r")
data_list = data_list.read().splitlines()
for i in range(1, len(data_list)):
	data_list[i] = data_list[i].split("\t")
del[data_list[0]]
#print(data_list)

n = 50
wma_dict = {}
tot_list = [["Adjusted Close", "Weighted Moving Average", "Inverted Close", "Inverted WMA"]]

for i in range(n, len(data_list)-n):
	tot = 0
	for j in range(n):
		tot += (n-j)*float(data_list[i-j][5])
	wma = tot/((n*(n+1))/2)
	wma_dict[data_list[i][0]] = wma
	tot = 0
	for j in range(n):
		tot += (j)*float(data_list[-(i-j)][5])
	wma_inv = tot/((n*(n+1))/2)
	tot_list.append([data_list[i+n][5], wma, data_list[-(i+n)][5], wma_inv]) #i-n, 

with open('GSPC-WMA.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(tot_list)

print(wma_dict)

df = pd.read_csv("GSPC-WMA.csv", skipinitialspace=True, usecols=["Adjusted Close", "Weighted Moving Average"])
df.plot()
df = pd.read_csv("GSPC-WMA.csv", skipinitialspace=True, usecols=["Inverted Close", "Inverted WMA"])
df.plot()
plt.show()