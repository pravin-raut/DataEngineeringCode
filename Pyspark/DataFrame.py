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

OrdersSchema=StructType([
    StructField("order_id",IntegerType()),
StructField("order_date",TimestampType()),
StructField("order_customer_id",IntegerType()),
StructField("order_status",StringType()),
])

OrdersDDL="""order_id Integer,
            order_date Timestamp,
            order_customer_id String,
            order_status string"""
#.option("inferSchema",True)\
ordersDF=spark.read\
    .format("csv")\
    .option("header",True)\
    .schema(OrdersDDL)\
    .option("path","C:\\Users\\Dell\\OneDrive\\Pravin\\Trendy Tech\\SPARK\\orders-201025-223502.csv")\
    .load()


ordersDF.printSchema()
ordersDF.createOrReplaceTempView("OrdersDB")
spark.sql("select order_customer_id,count(*)  from OrdersDB where order_customer_id>10000 group by order_customer_id").show()
#ordersDF.show()
spark.stop()