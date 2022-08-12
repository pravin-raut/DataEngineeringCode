import pyspark as py
import findspark
import sys
findspark.init()
sc = py.SparkContext("local[*]","WordCount")
sc.setLogLevel("ERROR") #By defualt its warn level
input = sc.textFile("C:\\Users\\Dell\\OneDrive\\Pravin\\Trendy Tech\\SPARK\\friendsdata-201008-180523.csv")
Get_Required_Data = input.map(lambda  x:(int(x.split('::')[2]),int(x.split('::')[3])))
FindavgRDD1 =Get_Required_Data.mapValues(lambda x: (x,1))
FindavgRDD2=FindavgRDD1.reduceByKey(lambda x,y:(x[0]+y[0],x[1]+y[1]))
FindavgRDD3=FindavgRDD2.mapValues(lambda x: x[0]/x[1]).collect()
for i in FindavgRDD3:
    print(i)
