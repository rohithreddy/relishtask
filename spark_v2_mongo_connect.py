import findspark

findspark.init("/home/crash/Documents/Programs/spark-2.2.1-bin-hadoop2.7")

from pyspark.sql import SparkSession


my_spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/tweepy_y.tweepy_t") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/hashtags.tags").config('spark.jars.packages', "org.mongodb.spark:mongo-spark-connector_2.11:2.2.1")\
    .getOrCreate()

tweets_df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
clean_tweets = tweets_df.select("text", "entities.hashtags")
countsRDD = (clean_tweets.rdd.flatMap(lambda tweet: [hashtag['text'].lower() for hashtag in tweet['hashtags']]).map(lambda tag: (tag, 1)).reduceByKey(lambda a, b: a + b))
print("Printing top 100 hashtags")
print(countsRDD.takeOrdered(100,key=lambda x : -x[1] ))
hashtags_df = countsRDD.toDF()
print("Inserting TO Mongo")
hashtags_df.write.format("com.mongodb.spark.sql.DefaultSource").mode("overwrite").save()