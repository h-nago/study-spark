from pyspark import SparkContext
import sys
sc = SparkContext(appName="Sample",master="spark://spark-master:7077")
text_file = sc.textFile(sys.argv[1])
counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("/app/output")