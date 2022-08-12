import pyspark as py
import findspark
import sys
findspark.init()
sc = py.SparkContext("local[*]","WordCount")
sc.setLogLevel("ERROR") #By defualt its warn level

input = sc.textFile("C:\\Users\\Dell\\OneDrive\\Pravin\\Trendy Tech\\SPARK\\bigdatacampaigndata-201014-183159.csv")

def getRequiredFields1(inputData):
    fields=inputData.split(",")
    First=fields[10]
    Second = fields[0]
    return (First,Second)

Biringwords=['in','data']
#RequedInput=input.map(lambda x:(x.split(",")[10],x.split(",")[0]))
nameset=sc.broadcast(Biringwords)
output=input.map(getRequiredFields1)
output1=output.map(lambda x:(x[1].lower(),x[0]))
output2=output1.reduceByKey(lambda x,y:x+y)

output3=output2.sortBy(lambda x: x[1],False)
output4=output3.map(lambda x:(x[0],1))
output5=output4.flatMap(lambda x:(x[0].split(" ")))
NewOutput=output5.filter(lambda x: x not in nameset.value)

OutputCol=NewOutput.collect()

for i in OutputCol:
    print(i)