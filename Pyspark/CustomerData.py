import pyspark as py
import findspark
import sys
findspark.init()
sc= py.SparkContext("local[*]","WordCount")
sc.setLogLevel("ERROR") #By defualt its warn level
input=sc.textFile("C:\\Users\\Dell\\OneDrive\\Pravin\\Trendy Tech\\SPARK\\customerorders-201008-180523.csv")

FewCols=input.map(lambda x: (x.split(',')[0],float(x.split(',')[2])))
AddFewCols=FewCols.reduceByKey(lambda x,y:x+y)
SortAddFewCols=AddFewCols.sortBy(lambda x:x[1],False)

cols=SortAddFewCols.collect()
for row in cols:
    print(row)