import pyspark as py
import findspark
import sys
findspark.init()

if __name__ =="__main__":
    #Common Lines
    sc= py.SparkContext("local[*]","WordCount")
    sc.setLogLevel("ERROR") #By defualt its warn level
    input=sc.textFile("C:\\Users\\Dell\\OneDrive\\Pravin\\Python\\WordCount.txt")

    word = input.flatMap(lambda x : x.split(" "))
    wordCountsOne=word.map(lambda x: (x.lower(),1))
    wordCountsGroup=wordCountsOne.reduceByKey(lambda x,y :x+y)
    wordCountsGroupSort=wordCountsGroup.sortBy(lambda x:x[1],True)
    #wordCountsOne = word.map(lambda x: (x.lower()))
    #wordCountsGroup = wordCountsOne.countByValue()
    result=wordCountsGroupSort.collect()
    for a in result:
        print(a)
    print(wordCountsGroup)
