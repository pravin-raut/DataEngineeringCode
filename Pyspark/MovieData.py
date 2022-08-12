import pyspark as py
import findspark
import sys
findspark.init()
sc= py.SparkContext("local[*]","WordCount")
sc.setLogLevel("ERROR") #By defualt its warn level
input=sc.textFile("C:\\Users\\Dell\\OneDrive\\Pravin\\Trendy Tech\\SPARK\\moviedata-201008-180523.data")

rdd1=input.map(lambda x:(x.split('\t')[2],1))
result=rdd1.reduceByKey(lambda x,y:x+y).collect()

for a in result:
    print(a)