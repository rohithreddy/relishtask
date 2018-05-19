1.Install the necessary prereqs in a Virtual enviroment
```bash
$ pip install -r requirements.txt
``` 
Install MongoDB as well 
and Download Spark

2. twpy_stream_insert.py inserts tweets to MongoDB
3. I have used Jupyter Notebook to Run spark 


so when runnnign spark from a within a notebook , you have to 
run it as 

```bash 
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
./pyspark --conf "spark.mongodb.input.uri=mongodb://127.0.0.1/tweepy_y.tweepy_t?readPreference=primaryPreferred" --conf "spark.mongodb.output.uri=mongodb://127.0.0.1/hashtags.tags" --packages org.mongodb.spark:mongo-spark-connector_2.11:2.2.1
```

and run code from pyspark_prog.py to get wc from Text

4. read_wc_flask.py serves data from mongo on a flask endpoint 

