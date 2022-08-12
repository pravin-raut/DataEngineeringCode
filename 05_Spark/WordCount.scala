val RDD1=sc.textFile("file2.txt") //Loaded into Array

val RDD2=RDD1.flatMap(x=>x.split(" ")) //Takes each line as input 

val RDD3=RDD2.map(x=>(x,1)) //Takes one row as input and gives one row as output

val RDD4=RDD3.reduceByKey((x,y)=>x+y) //It aggregates the values based on key

RDD4.collect() /Action is called

sys.props.update("spark.ui.proxyBase", "") //If CSS is broken for Spark
