# file_obj= open("psychology.txt")
# file_data= file_obj.readline()
# print(file_data)
# print(file_obj.readlines())
# file_obj.close ()


#/////csv files ////
import csv 
with open ('year2017.csv')as file_obj :
  content=csv.reader(file_obj)
  for row in content:
    print(row)
print(type(content))



