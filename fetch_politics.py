import pandas as pd

data = pd.read_csv("/home/aditig/Downloads/wire_2018.csv")
saved_column = data.title

#print(len(saved_column))
#print (type(saved_column[1]))

fp = open('politics.txt', 'w')
for i in range(len(saved_column)):
   fp.write(saved_column[i] + "\n")
fp.close()
