from pyspark.sql import SparkSession
from pyspark.sql.functions import mean, count
import sys
spark = SparkSession.builder.master("spark://spark-master:7077").appName("SimpleApp").getOrCreate()
lines = spark.read.json(sys.argv[1])
mean_data = lines.groupBy("id").agg(mean("temp"),count("*")).rdd
mean_data.saveAsTextFile("/app/output")
# lines.createOrReplaceTempView("dummy")
# spark.sql("select id, avg(temp), count(*) from dummy group by id").show()
