#read txt from tweets from a single file
lines = spark.read.text("/home/crash/text.csv").rdd.map(lambda r: r[0])

# Get Word count
counts = file.rdd.filter(lambda x :len(x) > 0).flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# write WC to Mongo
c_df = counts.toDF()
c_df.write.format("com.mongodb.spark.sql.DefaultSource").mode("overwrite").save()
