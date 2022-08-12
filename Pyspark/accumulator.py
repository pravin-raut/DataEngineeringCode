import pyspark as py
import findspark
import sys


def blankline(line):
    if len(line)==0:
        myacc.add(1)
findspark.init()
sc = py.SparkContext("local[*]","WordCount")
sc.setLogLevel("ERROR") #By defualt its warn level

input = sc.textFile("C:\\Users\\Dell\\OneDrive\\Pravin\\Trendy Tech\\SPARK\\SampleBklanklines.txt")
myacc=sc.accumulator(0)

input.foreach(blankline)
print(myacc)