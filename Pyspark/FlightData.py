from pyspark import SparkConf
from  pyspark.sql import SparkSession
import findspark
import sys

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, TimestampType

findspark.init()
myconf =SparkConf()
myconf.set("spark.app.name","My First Application")
myconf.set("spark.master","local[*]")

spark= SparkSession.builder.config(conf=myconf).getOrCreate()
FlightDDL="""FlightID Integer,
            Source string,
            Destination String,
            NoOfPassenger Integer"""

FlightDF=spark.read\
    .format("csv")\
    .option("header",True)\
    .schema(FlightDDL)\
    .option("path","C:\\Users\\Dell\\OneDrive\\Pravin\\Trendy Tech\\SPARK\\Flight.csv")\
    .load()



FlightDF.printSchema()
FlightDF.createOrReplaceTempView("FlightDB")
spark.sql("""select FlightID,
          Source,
          Destination,
          Sum( NoOfPassenger) over(partition by FlightID order by FlightID asc ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING  ) as next 
                   
          from FlightDB """
          ).show()

#ordersDF.show()
spark.stop()