
Content

1- intro 
2- Big Data Fundamentals with PySpark
3- Cleaning Data with PySpark
4- Feature Engineering with PySpark
5- Machine Learning with PySpark
6- Building Recommendation Engines with PySpark


# ----------------------------------------------------------------------------------------
Apache Spark: PySpark
# ----------------------------------------------------------------------------------------
1- Introduction to PySpark
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
2- Big Data Fundamentals with PySpark
# ----------------------------------------------------------------------------------------

Big Data fundementals: Volume, Variety, Velocity
Apache Spark: distributed, fast cluster computing system: batch, real time processing
(better than Hadoop which is fault tolerant framework for batch processing)
RDD: resilient distributed dataset: paralelized


# -----
RDD SparkContext(), parallelize(), textFile(), collect(), rdd.getNumPartitions()
map(), flatMap(), filter(), reduceByKey(), sortByKey(), countByKey(),
# -----


# create sparkcontext, rdd parallelize, textFile
from pyspark import SparkContext
sc = SparkContext("local", "Spark_Example_App")

RDD = sc.parallelize(["Spark", "is", "a", "framework", "for", "Big Data processing"])
print(RDD.collect())
['Spark', 'is', 'a', 'framework', 'for', 'Big Data processing']

fileRDD = sc.textFile('/usr/local/share/datasets/README.md', minPartitions = 5)
print("The file types ", type(RDD), type(fileRDD), fileRDD_part.getNumPartitions())
#<class 'pyspark.rdd.RDD'>, <class 'pyspark.rdd.RDD'>, 5

# map, filter
numbRDD = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
cubedRDD = numbRDD.map(lambda x: x**3)
for i in cubedRDD.collect():
	print(i)
1
8
27
...
fileRDD_filter = fileRDD.filter(lambda line: 'Spark' in line.split())
print('total lines: ' fileRDD_filter.count())
5
for i in fileRDD_filter.take(3):
  print(i)
line 1 Spark 
line 2 Spark
line 3 Spark

# reduceByKey
Rdd = sc.parallelize([(1,2), (3,4), (3,6), (4,5)])
Rdd_Reduced = Rdd.reduceByKey(lambda x, y: x + y)
print(Rdd_Reduced.collect())
[(1, 2), (3, 10), (4, 5)]
for num in Rdd_Reduced.collect(): 
  print("Key {} has {} Counts".format(num[0], num[1]))
Key 1 has 2 Counts
Key 3 has 10 Counts
Key 4 has 5 Counts

# sortByKey
Rdd_Reduced_Sort = Rdd_Reduced.sortByKey(ascending=False)
for num in Rdd_Reduced_Sort.collect():
  print("Key {} has {} Counts".format(num[0], num[1]))
Key 4 has 5 Counts
Key 3 has 10 Counts
Key 1 has 2 Counts

# countByKey
Rdd = sc.parallelize([(1,2), (3,4), (3,6), (4,5)])
total = Rdd.countByKey()
#defaultdict(int, {1: 1, 3: 2, 4: 1})
for k, v in total.items(): 
  print("key", k, "has", v, "counts")
key 1 has 1 counts
key 3 has 2 counts
key 4 has 1 counts


example:
# Create a baseRDD from the file path
baseRDD = sc.textFile(file_path)
['The Project Gutenberg EBook of The Complete Works of William Shakespeare, by',
 'William Shakespeare',
 '', ...]
splitRDD = baseRDD.flatMap(lambda x: x.split())
['The', 'Project', 'Gutenberg', ...]

stop_words = ['i', 'me', 'my', 'myself', ...]
splitRDD_no_stop = splitRDD.filter(lambda x: x.lower() not in stop_words)
splitRDD_no_stop_words = splitRDD_no_stop.map(lambda w: (w, 1))
resultRDD = splitRDD_no_stop_words.reduceByKey(lambda x, y: x + y)
print(resultRDD.collect())
[('Project', 85), ('Gutenberg', 26), ('EBook', 2), ... ]

# swap the keys and values 
resultRDD_swap = resultRDD.map(lambda x: (x[1], x[0]))
resultRDD_swap_sort = resultRDD_swap.sortByKey(ascending=False)
for word in resultRDD_swap_sort.take(10):
	print("{},{}". format(word[1], word[0]))
thou,4247
thy,3630
shall,3018
...


# -----
dataframe spark.createDataFrame(), spark.read.csv(), spark.sql(),
createOrReplaceTempView(), show(), select(), filter(), printSchema(), 
dropDuplicates(), describe().show(), 
# -----

# rdd parallelize, create dataframe, create session
sample_list = [('Mona', 20), ('Jennifer', 34), ('John', 20), ('Jim', 26)]
rdd = sc.parallelize(sample_list)
spark = SparkSession.builder.appName("Python Spark SQL basic example") \
							.config("spark.some.config.option", "some-value") \
    						.getOrCreate()
names_df = spark.createDataFrame(rdd, schema=['Name', 'Age'])
names_df.show()
+--------+---+
|    Name|Age|
+--------+---+
|    Mona| 20|
|Jennifer| 34|
|    John| 20|

# read, schema
people_df = spark.read.csv(file_path, header=True, inferSchema=True)
people_df.printSchema()
people_df.columns
people_df.show()
+---+---------+--------------+------+-------------+
|_c0|person_id|          name|   sex|date of birth|
+---+---------+--------------+------+-------------+
|  0|      100|Penelope Lewis|female|   1990-8-31|
|  1|      101| David Anthony|  male|   1971-10-14|
|  2|      102|     Ida Shipp|female|   1962-05-24|

# select, drop duplicate, filter
people_df_sub = people_df.select('name', 'sex', 'date of birth')

people_df_sub = people_df_sub.dropDuplicates()

people_df_female = people_df.filter(people_df.sex == "female")

#sql
people_df.createOrReplaceTempView("people")
people_male_df = spark.sql('SELECT * FROM people WHERE sex=="male"')
people_male_df.show(3)
+---+---------+-------------------+----+-------------+
|_c0|person_id|               name| sex|date of birth|
+---+---------+-------------------+----+-------------+
|  1|      101|      David Anthony|male|   1971-10-14|
|  5|      105|      David Simmons|male|   1999-12-30|
|  6|      106|      Edward Hudson|male|   1983-05-9|

# describe
fifa_df_germany_age.describe().show()
+-------+-----------------+
|summary|              Age|
+-------+-----------------+
|  count|             1140|
|   mean|24.20263157894737|
| stddev|4.197096712293756|
|    min|               16|
|    max|               36|

# toPandas, plot
df_pandas = names_df.toPandas()
df_pandas.plot(kind='barh', x='Name', y='Age', colormap='winter_r')
plt.show()
fifa_df_germany_age_pandas = fifa_df_germany_age.toPandas()
fifa_df_germany_age_pandas.plot(kind='density')
plt.show()



# ----------------------------------------------------------------------------------------
3- Cleaning Data with PySpark
# ----------------------------------------------------------------------------------------


# -----
dataframe spark.read.format().options().load(), spark.read.parquet(), write.parquet()
StructType([]), withColumn(), drop(), union(), distinct(), filter().select(), where(),
join(), broadcast(), orderBy(), desc(), cache(), unpersist(), withColumnRenamed(),
functions F.lower(), F.col().contains(), F.size(), F.split(), F.udf(), F.rand(),
F.monotonically_increasing_id(), rdd.getNumPartitions(), rdd.max(), isin()
# -----

lazy processing: 
Transformations and actions: withColumn, F.method() etc.

import pyspark.sql.functions as F
from pyspark.sql.types import *

# schema, read, drop, withColumn, F.lower, udf
people_schema = StructType([
  StructField('name', StringType(), False),
  StructField('age', IntegerType(), False),
  StructField('city', StringType(), False)
])
aa_dfw_df = spark.read.format('csv').options(Header=True).load('AA_DFW_2018.csv.gz')
aa_dfw_df = aa_dfw_df.withColumn('airport', F.lower(aa_dfw_df['Destination Airport']))
aa_dfw_df = aa_dfw_df.drop(aa_dfw_df['Destination Airport'])
aa_dfw_df.show()

print(joined_df.select('dog_list').show(10, truncate=False))
DogType = StructType([
	StructField("breed", StringType(), False),
    StructField("start_x", IntegerType(), False),
    StructField("start_y", IntegerType(), False),
    StructField("end_x", IntegerType(), False),
    StructField("end_y", IntegerType(), False)])
def dogParse(doglist):
  dogs = []
  for dog in doglist:
    (breed, start_x, start_y, end_x, end_y) = dog.split(',')
    dogs.append((breed, int(start_x), int(start_y), int(end_x), int(end_y)))
  return dogs
udfDogParse = F.udf(dogParse, ArrayType(DogType))
joined_df = joined_df.withColumn('dogs', udfDogParse('dog_list')).drop('dog_list')
joined_df.select(F.size('dogs')).show(3)
+----------+
|size(dogs)|
+----------+
|         1|
|         1|

# uniuon, parquet, sql
df3 = df1.union(df2)
df3.write.parquet('AA_DFW_ALL.parquet', mode='overwrite')
flights_df = spark.read.parquet('AA_DFW_ALL.parquet')
flights_df.createOrReplaceTempView('flights')
avg_duration = spark.sql('SELECT avg(flight_duration) from flights').collect()[0]
print('The average flight time is: %d' % avg_duration)
The average flight time is: 151

# filter, distinct, select, withColumn, where
voter_df = voter_df.filter(~ F.col('VOTER_NAME').contains('_'))
voter_df = voter_df.select('VOTER_NAME').distinct().show(40, truncate=False)
voter_df = voter_df.filter('ID > 3000').select("Name", "State")
#voter_df = voter_df.withColumn('splits', F.split(voter_df.VOTER_NAME, '\s+'))
voter_df = voter_df.withColumn('first_name', voter_df.splits.getItem(0))
voter_df = voter_df.withColumn('last_name', voter_df.splits.getItem(F.size('splits') - 1))
voter_df = voter_df.drop('splits')
voter_df = voter_df.where('ID > 3000').show()

# isin
li=["OH","CA","DE"]
df.filter(df.state.isin(li)).show()
+--------------------+------------------+-----+------+
|                name|         languages|state|gender|
+--------------------+------------------+-----+------+
|    [James, , Smith]|[Java, Scala, C++]|   OH|     M|
| [Julia, , Williams]|      [CSharp, VB]|   OH|     F|

# udf user function
def getmiddle(names):
  return ' '.join(names)
udfmiddle = F.udf(getmiddle, StringType())
voter_df = voter_df.withColumn('first_and_middle_name', udfmiddle(voter_df.splits))

def retriever(cols, colcount):
  return cols[4:colcount]
udfRetriever = F.udf(retriever, ArrayType(StringType()))
split_df = split_df.withColumn('dog_list', 
	udfRetriever(split_df.split_cols, split_df.colcount))

#when condition with withColumn
voter_df = voter_df.withColumn('random_val',
                               when(voter_df.TITLE == 'Councilmember', F.rand())
                               .when(voter_df.TITLE == 'Mayor', 2)
                               .otherwise(0))
voter_df.show()
+----------+-------------+-------------------+-------------------+
|      DATE|        TITLE|         VOTER_NAME|         random_val|
+----------+-------------+-------------------+-------------------+
|02/8/2017|Councilmember|  Jennifer S. Gates| 0.7698189422227172|
|02/8/2017|Councilmember| Philip T. Kingston| 0.3436982512986465|

voter_df.filter(voter_df.random_val == 0).show()
+----------+--------------------+-----------------+----------+
|      DATE|               TITLE|       VOTER_NAME|random_val|
+----------+--------------------+-----------------+----------+
|04/25/2018|Deputy Mayor Pro Tem|     Adam Medrano|       0.0|
|04/25/2018|       Mayor Pro Tem|Dwaine R. Caraway|       0.0|

# monotonically_increasing_id
voter_df = voter_df.withColumn('ROW_ID', F.monotonically_increasing_id())
voter_df.orderBy(voter_df.ROW_ID.desc()).show(2)
+--------------------+------+
|          VOTER NAME|ROW_ID|
+--------------------+------+
|        Lee Kleinman|    35|
|  the  final  201...|    34|

previous_max_ID = voter_df_march.select('ROW_ID').rdd.max()[0]
voter_df_april = voter_df_april.withColumn('ROW_ID', 
	F.monotonically_increasing_id() + previous_max_ID)
voter_df_march.select('ROW_ID').show()
+------+
|ROW_ID|
+------+
|     0|
|     1|
...
voter_df_april.select('ROW_ID').show()
+------+
|ROW_ID|
+------+
|    35|
|    36|
...

# caching
start_time = time.time()
departures_df = departures_df.distinct().cache()
print("Counting %d rows took %f seconds" % (departures_df.count(), time.time() - start_time))
start_time = time.time()
print("Counting %d rows again took %f seconds" % (departures_df.count(), time.time() - start_time))
Counting 139358 rows took 5.327054 seconds
Counting 139358 rows again took 0.973428 seconds
print("Is departures_df cached?: %s" % departures_df.is_cached)
departures_df.unpersist()

# split files before reading
Which of the following is the best option to improve performance?
#Split the 2 files into 50 files of 400K rows each, split files more
full_df = spark.read.csv('departures_full.txt.gz')
split_df = spark.read.csv('departures_*.txt.gz')
start_time_a = time.time()
print(full_df.count() % (time.time() - start_time_a))
start_time_b = time.time()
print(full_df.count() % (time.time() - start_time_b))
Total rows in full DataFrame:	139359
Time to run: 0.786977
Total rows in split DataFrame:	278718
Time to run: 0.514275

# cluster types: single node, standalone, 
# managed (yarn, mesos, kubernetes), driver and worker jobs
app_name = spark.conf.get('spark.app.name')
driver_tcp_port = spark.conf.get('spark.driver.port')
num_partitions = spark.conf.get('spark.sql.shuffle.partitions')
print(app_name, driver_tcp_port, num_partitions)
Name: pyspark-shell
Driver TCP port: 46047
Number of partitions: 200
spark.conf.set('spark.sql.shuffle.partitions', 500)

# improve performance; broadcast for join
normal_df = flights_df.join(airports_df,
	flights_df["Destination Airport"] == airports_df["IATA"] )
normal_df.explain()  # show query plan
from pyspark.sql.functions import broadcast
broadcast_df = flights_df.join(broadcast(airports_df),
	flights_df["Destination Airport"] == airports_df["IATA"] )
broadcast_df.explain()

start_time = time.time()
normal_count = normal_df.count()
normal_duration = time.time() - start_time
start_time = time.time()
broadcast_count = broadcast_df.count()
broadcast_duration = time.time() - start_time
print("Normal count:\t\t%d\tduration: %f" % (normal_count, normal_duration))
print("Broadcast count:\t%d\tduration: %f" % (broadcast_count, broadcast_duration))
Normal count:		119910	duration: 2.048253
Broadcast count:	119910	duration: 0.746952

# quik pipeline: read file, transformation, output file
departures_df = spark.read.csv('2015-departures.csv.gz', header=True)
departures_df = departures_df.filter(departures_df['Actual elapsed time (Minutes)'] > 0)
departures_df = departures_df.withColumn('id', F.monotonically_increasing_id())
departures_df.write.json('output.json', mode='overwrite')

# rename column
valid_folders_df = valid_folders_df.withColumnRenamed('_c0', 'folder')
# remove comment, invalid rows
no_comments_df = spark.read.csv('annotations.csv.gz', sep='|', comment='#')
split_cols = F.split(annotations_df['_c0'], '\t')
# Remove any rows containing fewer than 5 fields
annotations_df_filtered = annotations_df.drop(~ (F.size(split_cols) > 5))
#create new columns
split_df = annotations_df.withColumn('folder', split_cols.getItem(0))
split_df = split_df.withColumn('filename', split_cols.getItem(1))
split_df = split_df.withColumn('width', split_cols.getItem(2))
split_df = split_df.withColumn('height', split_cols.getItem(3))
split_df = split_df.withColumn('split_cols', split_cols)
+--------------------+--------+--------+---------------+-----+------+--------------------+
|                 _c0|colcount|  folder|       filename|width|height|          split_cols|
+--------------------+--------+--------+---------------+-----+------+--------------------+
#|02110627\tn021106...|       5|02110627|n02110627_12938|  200|   300|[02110627, n02110...|
#|02093754\tn020937...|       5|02093754| n02093754_1148|  500|   378|[02093754, n02093...|


# ----------------------------------------------------------------------------------------
4- Feature Engineering with PySpark
# ----------------------------------------------------------------------------------------

# Exploratory Data Analysis

# describe column
df = spark.read.parquet('Real_Estate.parq')
df.columns
['NO', 'MLSID', 'STREETNUMBERNUMERIC', 'STREETADDRESS', ...]
Y_df = df.select(['SALESCLOSEPRICE'])
Y_df.describe().show()
+-------+------------------+
|summary|   SALESCLOSEPRICE|
+-------+------------------+
|  count|              5000|
|   mean|       262804.4668|
| stddev|140559.82591998563|
|    min|             48000|
|    max|           1700000|

# check loaded data
def check_load(df, num_records, num_columns):
  message = 'Validation Failed'
  if num_records == df.count():
    if num_columns == len(df.columns):
      message = 'Validation Passed'
  return message
print(check_load(df, 5000, 74))
Validation Passed

# check dtypes of columns
df.dtypes
[('No.', 'bigint'),
 ('MLSID', 'string'),
 ('StreetNumberNumeric', 'bigint'),
 ...]
for attribute_tuple in df.dtypes:
  col_name = attribute_tuple[0]
  if col_name in validation_dict:
    col_type = attribute_tuple[1]
    if col_type != validation_dict[col_name]:
      print(col_name + ' has not expected dtype.')

# corr columns
columns = ['FOUNDATIONSIZE', 'DAYSONMARKET', 'FIREPLACES', ...]
corr_max = 0
corr_max_col = columns[0]
for col in columns:
    corr_val = df.corr(col, 'SALESCLOSEPRICE')
    if corr_val > corr_max:
        corr_max = corr_val
        corr_max_col = col
print(corr_max_col)
LIVINGAREA

# sample data, distplot, lmshow
sample_df = df.select(['LISTPRICE']).sample(False, 0.5, 42) # Sample 50% of data, replacement false
pandas_df = sample_df.toPandas()
sns.distplot(pandas_df)
plt.show()
from pyspark.sql.functions import skewness
print(df.agg({'LISTPRICE': 'skewness'}).collect()) # df is both dataframe and Rdd
# [Row(skewness(LISTPRICE)=2.790448093916559)]
sample_df = df.select(['SALESCLOSEPRICE', 'LIVINGAREA']).sample(False, 0.5, 42)
pandas_df = sample_df.toPandas()
sns.lmplot(x='LIVINGAREA', y='SALESCLOSEPRICE', data=pandas_df)
plt.show()

# drop columns
df.show(2)
+-------------------+----------+--------------------+---------------+------+
|STREETNUMBERNUMERIC|FIREPLACES|   LOTSIZEDIMENSIONS|       LISTTYPE| ACRES|
+-------------------+----------+--------------------+---------------+------+
|              11511|         0|             279X200|Exclusive Right|  1.28|
|              11200|         0|             100x140|Exclusive Right|  0.32|
cols_to_drop = ['STREETNUMBERNUMERIC', 'LOTSIZEDIMENSIONS']
df = df.drop(*cols_to_drop)

# filter, where
df.select(['ASSUMABLEMORTGAGE']).distinct().show()
+------------------+
| ASSUMABLEMORTGAGE|
+------------------+
|Information Coming|
|              null|
|     Not Assumable|
yes_values = ['Yes w/ Qualifying', 'Yes w/No Qualifying']
text_filter = ~df['ASSUMABLEMORTGAGE'].isin(yes_values) | df['ASSUMABLEMORTGAGE'].isNull()
df = df.where(text_filter)
print(df.count())    #4976

# agg, mean, stddev
from pyspark.sql.functions import mean, stddev
df.agg({'log_SalesClosePrice': 'mean'}).show()
+------------------------+
|avg(log_SalesClosePrice)|
+------------------------+
|      12.369716258093085|
mean_val = df.agg({'log_SalesClosePrice': 'mean'}).collect()[0][0]
stddev_val = df.agg({'log_SalesClosePrice': 'stddev'}).collect()[0][0]
low_bound = mean_val - (3 * stddev_val)
hi_bound = mean_val + (3 * stddev_val)
df = df.where((df['log_SalesClosePrice'] < hi_bound) & 
              (df['log_SalesClosePrice'] > low_bound))

# scaling data
def min_max_scaler(df, cols_to_scale):
  for col in cols_to_scale:
    max_days = df.agg({col: 'max'}).collect()[0][0]
    min_days = df.agg({col: 'min'}).collect()[0][0]
    new_column_name = 'scaled_' + col
    df = df.withColumn(new_column_name, 
            (df[col] - min_days) / (max_days - min_days))
  return df
df = min_max_scaler(df, ['FOUNDATIONSIZE', 'DAYSONMARKET', 'FIREPLACES'])
df[['DAYSONMARKET', 'scaled_DAYSONMARKET']].show()
+------------+--------------------+
|DAYSONMARKET| scaled_DAYSONMARKET|
+------------+--------------------+
|          10|0.044444444444444446|
|           4|0.017777777777777778|

from pyspark.sql.functions import log
print(df.agg({'YEARBUILT': 'skewness'}).collect()[0][0])   # -0.2455425013492729
max_year = df.agg({'YEARBUILT': 'max'}).collect()[0][0]    # 2018
df = df.withColumn('Reflect_YearBuilt', (max_year + 1) - df['YEARBUILT'])
df = df.withColumn('adj_yearbuilt', 1 / log(df['Reflect_YearBuilt']))
df.select('YEARBUILT', 'Reflect_YearBuilt', 'adj_yearbuilt').show(2)
+---------+-----------------+-------------------+
|YEARBUILT|Reflect_YearBuilt|      adj_yearbuilt|
+---------+-----------------+-------------------+
|     1950|               69|0.23617733727628992|
|     1971|               48|0.25831776680732876|

# fill missing data
columns = ['APPLIANCES', 'BACKONMARKETDATE', 'ROOMFAMILYCHAR', 
           'BASEMENT', 'DININGROOMDESCRIPTION']
sample_df = df.select(*columns).sample(False, 0.1, 42)
sample_df = sample_df.toPandas()
tf_df = sample_df.isnull()
     APPLIANCES  BACKONMARKETDATE  ROOMFAMILYCHAR  BASEMENT  DININGROOMDESCRIPTION
0         False              True           False     False                  False
1         False              True           False     False                  False
sns.heatmap(data=tf_df)
plt.xticks(rotation=30, fontsize=10)
plt.yticks(rotation=0, fontsize=10)
plt.show()
answer = 'BACKONMARKETDATE'   # most missing data

# imputing missing data with col mean
missing = df.where(df['PDOM'].isNull()).count()     # 9
col_mean = df.agg({'PDOM': 'mean'}).collect()[0][0] # 20.792025646163093
df = df.fillna(col_mean, subset=['PDOM'])
df.where(df['PDOM'].isNull()).count()               # 0

def column_dropper(df, threshold):
  total_records = df.count()
  for col in df.columns:
    missing = df.where(df[col].isNull()).count()
    missing_percent = missing / total_records
    if missing_percent > threshold:
      df = df.drop(col)
  return df
df = column_dropper(df, 0.6)

# join dataframes
# careful, check longitude and latitude type and round decimals before join
walk_df = walk_df.withColumn('longitude', walk_df['longitude'].cast('double'))
walk_df = walk_df.withColumn('latitude', walk_df['latitude'].cast('double'))
df = df.withColumn('longitude', round('longitude', 5))
df = df.withColumn('latitude', round('latitude', 5))
condition = [walk_df['latitude'] == df['latitude'], walk_df['longitude'] == df['longitude']]
join_df = walk_df.join(df, on=condition, how='left')
print(join_df.where(~join_df['walkscore'].isNull()).count())     # 4849, null=0

df.createOrReplaceTempView('df')
walk_df.createOrReplaceTempView('walk_df')
join_sql =  """SELECT * FROM df LEFT JOIN walk_df 
         ON df.longitude = walk_df.longitude AND df.latitude = walk_df.latitude"""
joined_df = spark.sql(join_sql)
type(joined_df)   # pyspark.sql.dataframe.DataFrame



# Feature Engineering

# create columns and correlations
acres_to_sqfeet = 43560
df = df.withColumn('LOT_SIZE_SQFT', df['ACRES'] * acres_to_sqfeet)
df = df.withColumn('YARD_SIZE', df['LOT_SIZE_SQFT'] - df['FOUNDATIONSIZE'])

print("Corr of ACRES vs SALESCLOSEPRICE: " + str(df.corr('SALESCLOSEPRICE', 'YARD_SIZE')))
print("Corr of FOUNDATIONSIZE vs SALESCLOSEPRICE: " + str(df.corr('SALESCLOSEPRICE', 'FOUNDATIONSIZE')))
print("Corr of YARD_SIZE vs SALESCLOSEPRICE: " + str(df.corr('SALESCLOSEPRICE', 'LOT_SIZE_SQFT')))
Corr of ACRES vs SALESCLOSEPRICE: 0.20714585430854268
Corr of FOUNDATIONSIZE vs SALESCLOSEPRICE: 0.6152231695664402
Corr of YARD_SIZE vs SALESCLOSEPRICE: 0.22060612588935338

df = df.withColumn('ASSESSED_TO_LIST', (df['ASSESSEDVALUATION'] / df['LISTPRICE']))
df[['ASSESSEDVALUATION', 'LISTPRICE', 'ASSESSED_TO_LIST']].show(2)
+-----------------+---------+----------------+
|ASSESSEDVALUATION|LISTPRICE|ASSESSED_TO_LIST|
+-----------------+---------+----------------+
|              0.0|   139900|             0.0|
|              0.0|   210000|             0.0|
df = df.withColumn('TAX_TO_LIST', (df['TAXES'] / df['LISTPRICE']))
df[['TAX_TO_LIST', 'TAXES', 'LISTPRICE']].show(2)
+--------------------+-----+---------+
|         TAX_TO_LIST|TAXES|LISTPRICE|
+--------------------+-----+---------+
|0.013280914939242315| 1858|   139900|
| 0.00780952380952381| 1640|   210000|
df = df.withColumn('BED_TO_BATHS', (df['BEDROOMS'] / df['BATHSTOTAL']))
df[['BED_TO_BATHS', 'BEDROOMS', 'BATHSTOTAL']].show(2)
+------------------+--------+----------+
|      BED_TO_BATHS|BEDROOMS|BATHSTOTAL|
+------------------+--------+----------+
|               1.5|       3|         2|
|1.3333333333333333|       4|         3|

df = df.withColumn('Total_SQFT', df['SQFTBELOWGROUND'] + df['SQFTABOVEGROUND'])
df = df.withColumn('BATHS_PER_1000SQFT', df['BATHSTOTAL'] / (df['Total_SQFT'] / 1000))
df[['BATHS_PER_1000SQFT']].describe().show()
+-------+-------------------+
|summary| BATHS_PER_1000SQFT|
+-------+-------------------+
|  count|               5000|
|   mean| 1.4302617483739894|
| stddev|  14.12890410245937|
|    min|0.39123630672926446|
|    max|             1000.0|

pandas_df = df.sample(False, 0.5, 0).toPandas()
sns.jointplot(x='Total_SQFT', y='SALESCLOSEPRICE', data=pandas_df, kind="reg", stat_func=r2)
plt.show()
sns.jointplot(x='BATHS_PER_1000SQFT', y='SALESCLOSEPRICE', data=pandas_df, kind="reg", stat_func=r2)
plt.show()


# date
from pyspark.sql.functions import to_date, dayofweek
df = df.withColumn('LISTDATE', to_date('LISTDATE'))
df = df.withColumn('List_Day_of_Week', dayofweek('LISTDATE'))
sample_df = df.sample(False, 0.5, 42).toPandas()
sns.countplot(x="List_Day_of_Week", data=sample_df)
plt.show()

from pyspark.sql.functions import year
df = df.withColumn('list_year', year('LISTDATE'))
df = df.withColumn('report_year', (df['list_year'] - 1))
condition = [df['CITY'] == price_df['City'], df['report_year'] == price_df['Year']]
df = df.join(price_df, on=condition, how='left')
df[['MedianHomeValue']].show()
+---------------+
|MedianHomeValue|
+---------------+
|         401000|
|         401000|

from pyspark.sql.functions import lag, datediff, to_date
from pyspark.sql.window import Window
mort_df = mort_df.withColumn('DATE', to_date('DATE'))
# window() allows you to return a value for each record based off some calculation against a group of record
w = Window().orderBy(mort_df['DATE'])
mort_df = mort_df.withColumn('DATE-1', lag('DATE', count=1).over(w))
mort_df = mort_df.withColumn('Days_Between_Report', datediff('DATE', 'DATE-1'))
mort_df.select('Days_Between_Report').distinct().show()
+-------------------+
|Days_Between_Report|
+-------------------+
|               null|
|                  7|
|                  6|
|                  8|


# when
from pyspark.sql.functions import when
has_attached_garage = df['GARAGEDESCRIPTION'].like('%Attached Garage%')
has_detached_garage = df['GARAGEDESCRIPTION'].like('%Detached Garage%')
df = df.withColumn('has_attached_garage', (when(has_attached_garage, 1)
                                          .when(has_detached_garage, 0)
                                          .otherwise(None)))
df[['GARAGEDESCRIPTION', 'has_attached_garage']].show(truncate=100)
+------------------------------------------------------------------+-------------------+
|                                                 GARAGEDESCRIPTION|has_attached_garage|
+------------------------------------------------------------------+-------------------+
|                                                   Attached Garage|                  1|
|           Attached Garage, Driveway - Asphalt, Garage Door Opener|                  1|


# explode
from pyspark.sql.functions import split, explode
df = df.withColumn('garage_list', split(df['GARAGEDESCRIPTION'], ', '))
+--------------------+
|         garage_list|
+--------------------+
|   [Attached Garage]|
|[Attached Garage,..]|
|   [Attached Garage]|
ex_df = df.withColumn('ex_garage_list', explode(df['garage_list']))
ex_df[['ex_garage_list']].distinct().show(100, truncate=50)
+----------------------------+
|              ex_garage_list|
+----------------------------+
|             Attached Garage|
|      On-Street Parking Only|


# pivoting
from pyspark.sql.functions import coalesce, first
piv_df = ex_df.groupBy('NO').pivot('ex_garage_list').agg(coalesce(first('constant_val')))
joined_df = df.join(piv_df, on='NO', how='left')
zfill_cols = piv_df.columns
zfilled_df = joined_df.fillna(0, subset=zfill_cols)
---+---------------+-------+---
...|Attached Garage|Carport|...
---+---------------+-------+---
...|              1|      0|...
...|              1|      0|...


# Binarizer
from pyspark.ml.feature import Binarizer
binarizer = Binarizer(threshold=5.0, inputCol='List_Day_of_Week', outputCol='Listed_On_Weekend')
df = binarizer.transform(df)
df[['List_Day_of_Week', 'Listed_On_Weekend']].show()
+----------------+-----------------+
|List_Day_of_Week|Listed_On_Weekend|
+----------------+-----------------+
|             6.0|              1.0|
|             1.0|              0.0|

# Bucketizer
from pyspark.ml.feature import Bucketizer
splits = [0, 1, 2, 3, 4, 5, float('Inf')]
buck = Bucketizer(splits=splits, inputCol='BEDROOMS', outputCol='bedrooms')
df_bucket = buck.transform(df)
df_bucket[['BEDROOMS', 'bedrooms']].show()
+--------+--------+
|BEDROOMS|bedrooms|
+--------+--------+
|     3.0|     3.0|
|     4.0|     4.0|


# One Hot Encoding
from pyspark.ml.feature import OneHotEncoder, StringIndexer
string_indexer = StringIndexer(inputCol='SCHOOLDISTRICTNUMBER', outputCol='School_Index')
indexed_df = string_indexer.fit(df).transform(df)
encoder = OneHotEncoder(inputCol='School_Index', outputCol='School_Vec')
encoded_df = encoder.transform(indexed_df)
encoded_df[['SCHOOLDISTRICTNUMBER', 'School_Index', 'School_Vec']].show(truncate=100)
+-----------------------------+------------+-------------+
|         SCHOOLDISTRICTNUMBER|School_Index|   School_Vec|
+-----------------------------+------------+-------------+
|             834 - Stillwater|         3.0|(7,[3],[1.0])|
|622 - North St Paul-Maplewood|         1.0|(7,[1],[1.0])|



# Building a Model

'''
predict quantity: regression
                  generalized linear reg, linear reg, decision tree reg, GBT reg, randomforest reg
predict category: labeled data= classification
                  unlabeled data= clustering
predict similarity: user based= collaborative filtering (recommendation)
                    basket based= association rules


'''

# train test split

def train_test_split_date(df, split_col, test_days=45):
  max_date = df.agg({split_col: 'max'}).collect()[0][0]
  min_date = df.agg({split_col: 'min'}).collect()[0][0]
  split_date = max_date - timedelta(days=test_days)
  return split_date

split_date = train_test_split_date(df, 'OFFMKTDATE')
train_df = df.where(df['OFFMKTDATE'] < split_date) 
test_df = df.where(df['OFFMKTDATE'] >= split_date).where(df['LISTDATE'] <= split_date) 

from pyspark.sql.functions import datediff, to_date, lit

split_date = to_date(lit('2017-12-10'))
test_df = df.where(df['OFFMKTDATE'] >= split_date).where(df['LISTDATE'] <= split_date)

test_df = test_df.withColumn('DAYSONMARKET_Original', test_df['DAYSONMARKET'])
test_df = test_df.withColumn('DAYSONMARKET', datediff(split_date, 'LISTDATE'))
test_df[['LISTDATE', 'OFFMKTDATE', 'DAYSONMARKET_Original', 'DAYSONMARKET']].show()
+-------------------+-------------------+---------------------+------------+
|           LISTDATE|         OFFMKTDATE|DAYSONMARKET_Original|DAYSONMARKET|
+-------------------+-------------------+---------------------+------------+
#|2017-10-06 00:00:00|2018-01-24 00:00:00|                  110|          65|
#|2017-09-18 00:00:00|2017-12-12 00:00:00|                   82|          83|


# Which of the following preprocessing techniques are needed for Random Forest Regression?
# - Perform value replacement for missing values
# - encode categorical text features to numeric.

# Dropping Columns with Low Observations
obs_threshold = 30
cols_to_remove = list()
for col in binary_cols[0:10]:
  obs_count = df.agg({col:'sum'}).collect()[0][0]
  if obs_count <= obs_threshold:
    cols_to_remove.append(col)
new_df = df.drop(*cols_to_remove)

print('Rows: ' + str(df.count()) + ' Columns: ' + str(len(df.columns)))
print('Rows: ' + str(new_df.count()) + ' Columns: ' + str(len(new_df.columns)))
Rows: 5000 Columns: 253
Rows: 5000 Columns: 250

# Naively Handling Missing and Categorical Values
# Replace missing values
df = df.fillna(-1, subset=['WALKSCORE', 'BIKESCORE'])
indexers = [StringIndexer(inputCol=col, outputCol=col+"_IDX")\
            .setHandleInvalid("keep") for col in categorical_cols]
indexer_pipeline = Pipeline(stages=indexers)
df_indexed = indexer_pipeline.fit(df).transform(df)
df_indexed = df_indexed.drop(*categorical_cols)
print(df_indexed.dtypes)
[('CITY', 'string'), ('LISTTYPE', 'string'), ('SCHOOLDISTRICTNUMBER', 'string'), ...]


# train
from pyspark.ml.regression import GBTRegressor
gbt = GBTRegressor(featuresCol='features',
                           labelCol='SALESCLOSEPRICE',
                           predictionCol="Prediction_Price",
                           seed=42
                           )
model = gbt.fit(train_df)

# evaluate
from pyspark.ml.evaluation import RegressionEvaluator
evaluator = RegressionEvaluator(labelCol="SALESCLOSEPRICE", 
                                predictionCol="Prediction_Price")
models = {'Gradient Boosted Trees': gbt_predictions, 'Random Forest Regression': rfr_predictions}
for key, preds in models.items():
  rmse = evaluator.evaluate(preds, {evaluator.metricName: "rmse"})
  r2 = evaluator.evaluate(preds, {evaluator.metricName: "r2"})
  print(key + ' RMSE: ' + str(rmse))
  print(key + ' R^2: ' + str(r2))

# save and load

fi_df = pd.DataFrame(importances, columns=['importance'])
fi_df['feature'] = pd.Series(feature_cols)
fi_df.sort_values(by=['importance'], ascending=False, inplace=True)
fi_df.head(10)

from pyspark.ml.regression import RandomForestRegressionModel
model.save('rfr_no_listprice')
loaded_model = RandomForestRegressionModel.load('rfr_no_listprice')



# ----------------------------------------------------------------------------------------
5- Machine Learning with PySpark
# ----------------------------------------------------------------------------------------
#MLLIB pyspark.mllib is the builtin library for RDD-based API for machine learning

# read input data
from pyspark.sql import SparkSession
spark = SparkSession.builder \
                    .master('local[*]') \
                    .appName('test') \
                    .getOrCreate()
#spark.stop()
flights = spark.read.csv('flights.csv', sep=',', header=True,
                         inferSchema=True, nullValue='NA')
flights.count()
flights.dtypes
flights.show(2)
+---+---+---+-------+------+---+----+------+--------+-----+
|mon|dom|dow|carrier|flight|org|mile|depart|duration|delay|
+---+---+---+-------+------+---+----+------+--------+-----+
| 11| 20|  6|     US|    19|JFK|2153|  9.48|     351| null|
|  0| 22|  2|     UA|  1107|ORD| 316| 16.33|      82|   30|

from pyspark.sql.types import StructType, StructField, IntegerType, StringType
schema = StructType([
    StructField("id", IntegerType()),
    StructField("text", StringType()),
    StructField("label", IntegerType())
])
sms = spark.read.csv("sms.csv", sep=';', header=False, schema=schema)
sms.printSchema()
root
 |-- id: integer (nullable = true)
 |-- text: string (nullable = true)
 |-- label: integer (nullable = true)


# data preperation
flights_drop_column = flights.drop('flight')
flights_drop_column.filter('delay IS NULL').count()
flights_valid_delay1 = flights_drop_column.filter('delay IS NOT NULL')
47022
flights_valid_delay2 = flights_drop_column.dropna()
47022

from pyspark.sql.functions import round
flights_km = flights.withColumn('km', round(flights.mile * 1.60934, 0))
                    .drop('mile')
flights_km = flights_km.withColumn('label', (flights_km.delay >= 15)
                       .cast('integer'))
flights_km.show(2)
+---+---+---+-------+---+------+--------+-----+------+-----+
|mon|dom|dow|carrier|org|depart|duration|delay|    km|label|
+---+---+---+-------+---+------+--------+-----+------+-----+
|  0| 22|  2|     UA|ORD| 16.33|      82|   30| 509.0|    1|
|  2| 20|  4|     UA|SFO|  6.17|      82|   -8| 542.0|    0|

# -----
categorical columns; StringIndexer(), fit(), transform(),
VectorAssembler(), transform(), 
train test split; randomSplit(), count(),
# -----
from pyspark.ml.feature import StringIndexer

# string indexer
indexer = StringIndexer(inputCol='carrier', outputCol='carrier_idx')
indexer_model = indexer.fit(flights)
flights_indexed = indexer_model.transform(flights)

flights_indexed = StringIndexer(inputCol='org', outputCol='org_idx')
                               .fit(flights_indexed)
                               .transform(flights_indexed)
flights_indexed.show(2)
+---+---+---+-------+---+------+--------+-----+------+-----+-----------+-------+
|mon|dom|dow|carrier|org|depart|duration|delay|    km|label|carrier_idx|org_idx|
+---+---+---+-------+---+------+--------+-----+------+-----+-----------+-------+
|  0| 22|  2|     UA|ORD| 16.33|      82|   30| 509.0|    1|        0.0|    0.0|
|  2| 20|  4|     UA|SFO|  6.17|      82|   -8| 542.0|    0|        0.0|    1.0|


# vector assembler
from pyspark.ml.feature import VectorAssembler
assembler = VectorAssembler(inputCols=['mon', 'dom', 'dow', 'carrier_idx', 
                           'org_idx', 'km', 'depart', 'duration'], 
                           outputCol='features')
flights_assembled = assembler.transform(flights)
flights_assembled.select('features', 'delay')
                 .show(2, truncate=False)
+-----------------------------------------+-----+
|features                                 |delay|
+-----------------------------------------+-----+
|[0.0,22.0,2.0,0.0,0.0,509.0,16.33,82.0]  |30   |
|[2.0,20.0,4.0,0.0,1.0,542.0,6.17,82.0]   |-8   |


# train test split
flights_train, flights_test = flights.randomSplit([0.8, 0.2], seed=43)
training_ratio = flights_train.count() / flights.count()
print(training_ratio)   # 0.8035334184759472


# -----
classification; DecisionTreeClassifier(), LogisticRegression(), 
fit(), transform(), 
MulticlassClassificationEvaluator(), BinaryClassificationEvaluator(), 
# -----
# flights.columns: ['mon', 'dom', 'dow', 'carrier', 'org', 'depart', 'duration',
# 'delay', 'km', 'label', 'carrier_idx', 'org_idx', 'features']

# decision tree
from pyspark.ml.classification import DecisionTreeClassifier
tree = DecisionTreeClassifier()
tree_model = tree.fit(flights_train)
prediction = tree_model.transform(flights_test)
prediction.select('label', 'prediction', 'probability')
          .show(2, False)
+-----+----------+----------------------------------------+
|label|prediction|probability                             |
+-----+----------+----------------------------------------+
|1    |1.0       |[0.33779477374123645,0.6622052262587635]|
|1    |1.0       |[0.33779477374123645,0.6622052262587635]|


# confusion matrix
prediction.groupBy('label', 'prediction').count().show()
+-----+----------+-----+
|label|prediction|count|
+-----+----------+-----+
|    1|       0.0|  196|
|    0|       0.0|  310|
|    1|       1.0|  255|
|    0|       1.0|  162|
TN = prediction.filter('prediction = 0 AND label = 0').count()
TP = prediction.filter('prediction = 1 AND label = 1').count()
FN = prediction.filter('prediction = 0 AND label = 1').count()
FP = prediction.filter('prediction = 1 AND label = 0').count()
accuracy = (TP + TN) / (TP + FP + TN + FN)
print(accuracy)
0.6121343445287107

# logistic regresion
from pyspark.ml.classification import LogisticRegression
logistic = LogisticRegression().fit(flights_train)
prediction = logistic.transform(flights_test)
prediction.groupBy("label", "prediction").count().show()

# evaluate
from pyspark.ml.evaluation import MulticlassClassificationEvaluator, BinaryClassificationEvaluator
precision = TP / (TP + FP)
recall = TP / (TP + FN)
print('precision = {:.2f}\nrecall = {:.2f}'.format(precision, recall))
precision = 0.59, recall = 0.60

multi_evaluator = MulticlassClassificationEvaluator()
weighted_precision = multi_evaluator.evaluate(prediction, 
  {multi_evaluator.metricName: "weightedPrecision"})
0.5926069839466499

binary_evaluator = BinaryClassificationEvaluator()
auc = binary_evaluator.evaluate(prediction, 
  {multi_evaluator.metricName: "areaUnderROC"})
0.6308282856740386


# -----
text into tables, regexp_replace(), Tokenizer().transform(), 
StopWordsRemover().transform(), HashingTF().transform(), IDF().fit().transform(),
# -----

from pyspark.sql.functions import regexp_replace
from pyspark.ml.feature import Tokenizer

wrangled = sms.withColumn('text', regexp_replace(sms.text, '[_():;,.!?\\-]', ' '))
wrangled = wrangled.withColumn('text', regexp_replace(wrangled.text, '[0-9]', ' '))
wrangled = wrangled.withColumn('text', regexp_replace(wrangled.text, ' +', ' '))

wrangled = Tokenizer(inputCol='text', outputCol='words').transform(wrangled)
wrangled.show(4, truncate=False)
+---+----------------------------------+-----+------------------------------------------+
|id |text                              |label|words                                     |
+---+----------------------------------+-----+------------------------------------------+
|1  |Sorry I ll call later in meeting  |0    |[sorry, i, ll, call, later, in, meeting]  |
|2  |Dont worry I guess he is busy     |0    |[dont, worry, i, guess, he, is, busy]     |

from pyspark.ml.feature import StopWordsRemover, HashingTF, IDF
wrangled = StopWordsRemover(inputCol='words', outputCol='terms').transform(sms)
wrangled = HashingTF(inputCol='terms', outputCol='hash', numFeatures=1024)
                    .transform(wrangled)
tf_idf = IDF(inputCol='hash', outputCol='features')
                    .fit(wrangled).transform(wrangled)
tf_idf.show(2, truncate=False)
+---+--------------------+-----+--------------------+--------------------+--------------------+
| id|               words|label|               terms|                hash|            features|
+---+--------------------+-----+--------------------+--------------------+--------------------+
#|  1|[sorry, i,ll, cal...|    0|[sorry, call, lat...|(1024,[138,384,57...|(1024,[138,384,57...|
#|  2|[dont, worry, i, ...|    0|[dont, worry, gue...|(1024,[215,233,27...|(1024,[215,233,27...|

sms_train, sms_test = tf_idf.randomSplit([0.8, 0.2], seed=13)
logistic = LogisticRegression(regParam=0.2).fit(sms_train)
prediction = logistic.transform(sms_test)
prediction.groupBy("label", "prediction").count().show()
+-----+----------+-----+
|label|prediction|count|
+-----+----------+-----+
|    1|       0.0|   41|
|    0|       0.0|  948|
|    1|       1.0|  105|
|    0|       1.0|    2|


# classification example
from pyspark.mllib.classification import LogisticRegressionWithLBFGS

spam_rdd = sc.textFile(file_path_spam)
non_spam_rdd = sc.textFile(file_path_non_spam)
spam_words = spam_rdd.flatMap(lambda email: email.split(' '))
non_spam_words = non_spam_rdd.flatMap(lambda email: email.split(' '))

tf = HashingTF(numFeatures=200)
spam_features = tf.transform(spam_words)
non_spam_features = tf.transform(non_spam_words)

spam_samples = spam_features.map(lambda features:LabeledPoint(1, features))
non_spam_samples = non_spam_features.map(lambda features:LabeledPoint(0, features))
samples = spam_samples.join(non_spam_samples)
train_samples, test_samples = samples.randomSplit([0.8, 0.2])

model = LogisticRegressionWithLBFGS.train(train_samples)
predictions = model.predict(test_samples.map(lambda x: x.features))
labels_and_preds = test_samples.map(lambda x: x.label).zip(predictions)
accuracy = labels_and_preds.filter(lambda x: x[0] == x[1]).count() / float(test_samples.count())
print("Model accuracy : {:.2f}".format(accuracy))
Model accuracy : 0.76


# -----
regression; LinearRegression(), fit(), transform(), 
OneHotEncoder().fit().transform(), Bucketizer().transform(), 
RegressionEvaluator(), 
# -----

# one hot encoding
from pyspark.ml.feature import OneHotEncoder
onehot = OneHotEncoder(inputCols=['org_idx'], outputCols=['org_dummy'])
onehot = onehot.fit(flights)
flights_onehot = onehot.transform(flights)
flights_onehot.select('org', 'org_idx', 'org_dummy').distinct().sort('org_idx').show()
+---+-------+-------------+
|org|org_idx|    org_dummy|
+---+-------+-------------+
|ORD|    0.0|(7,[0],[1.0])|
|SFO|    1.0|(7,[1],[1.0])|


# regression
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
regression = LinearRegression(labelCol='duration').fit(flights_train)
predictions = regression.transform(flights_test)
predictions.select('duration', 'prediction').show(2, False)
+--------+------------------+
|duration|prediction        |
+--------+------------------+
|105     |118.60747064619201|
|115     |70.00972888630639 |
RegressionEvaluator(labelCol='duration').evaluate(predictions)
17.567113541049192

regression.intercept
regression.coefficients
regression.coefficients[0]


'''
0 — km, 1 — ORD, 2 — SFO, 3 — JFK, 4 — LGA, 5 — SJC, 6 — SMF, 7 — TUS, 8 — 00:00 to 03:00,
9 — 03:00 to 06:00,10 — 06:00 to 09:00,11 — 09:00 to 12:00,12 — 12:00 to 15:00,
13 — 15:00 to 18:00,14 — 18:00 to 21:00
'''
# bucketing and on hot encoder
from pyspark.ml.feature import Bucketizer, OneHotEncoder
buckets = Bucketizer(splits=[0, 3, 6, 9, 12, 15, 18, 21, 24], 
  inputCol='depart', outputCol='depart_bucket')
bucketed = buckets.transform(flights)

onehot = OneHotEncoder(inputCols=['depart_bucket'], outputCols=['depart_dummy'])
flights_onehot = onehot.fit(bucketed).transform(bucketed)
flights_onehot.select('depart', 'depart_bucket', 'depart_dummy').show(2)
+------+-------------+-------------+
|depart|depart_bucket| depart_dummy|
+------+-------------+-------------+
|  9.48|          3.0|(7,[3],[1.0])|
| 16.33|          5.0|(7,[5],[1.0])|

# regression
from pyspark.ml.evaluation import RegressionEvaluator
rmse = RegressionEvaluator(labelCol='duration').evaluate(predictions)
10.68279557023109
regression.intercept
10.470157159054379
# Average minutes on ground at OGG for flights departing between 03:00 and 06:00
avg_night_ogg = regression.intercept + regression.coefficients[8]
-2.7425333357930377
# Average minutes on ground at JFK for flights departing between 03:00 and 06:00
avg_night_jfk = regression.intercept + regression.coefficients[3] + regression.coefficients[8]
48.90395499832854


# regularization
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# ridge: λ > 0, α = 0. lasso: λ > 0, α = 1.
# Fit Lasso model (λ = 1, α = 1) to training data
regression = LinearRegression(labelCol='duration', regParam=1, elasticNetParam=1).fit(flights_train)
rmse = RegressionEvaluator(labelCol='duration').evaluate(regression.transform(flights_test))
11.847247620737766
coeffs = regression.coefficients
[0.07344906677784574,1.4137375580081961,-2.6351822824590694, ...]
zero_coeff = sum([beta for beta in regression.coefficients])
print("Number of coefficients equal to 0:", zero_coeff)
Number of coefficients equal to 0: 15.05084828147903


Pipeline().fit().transform(), 
# pipeline
flights.show()
+---+---+---+-------+------+---+------+--------+-----+------+
|mon|dom|dow|carrier|flight|org|depart|duration|delay|km    |
+---+---+---+-------+------+---+------+--------+-----+------+
|11 |20 |6  |US     |19    |JFK|9.48  |351     |null |3465.0|
|0  |22 |2  |UA     |1107  |ORD|16.33 |82      |30   |509.0 |

indexer = StringIndexer(inputCol='org', outputCol='org_idx')
onehot = OneHotEncoder(inputCols=['org_idx', 'dow'],
                       outputCols=['org_dummy', 'dow_dummy'])
assembler = VectorAssembler(inputCols=['km', 'org_dummy', 'dow_dummy'], 
                            outputCol='features')
regression = LinearRegression(labelCol='duration')

from pyspark.ml import Pipeline
pipeline = Pipeline(stages=[indexer, onehot, assembler, regression])
pipeline = pipeline.fit(flights_train)
predictions = pipeline.transform(flights_test)
+---+---+---+-------+------+---+------+--------+-----+------+-------+
|mon|dom|dow|carrier|flight|org|depart|duration|delay|    km|org_idx|
+---+---+---+-------+------+---+------+--------+-----+------+-------+
|  0|  1|  2|     AA|     3|JFK|  12.0|     370|   11|3983.0|    2.0|
|  0|  1|  2|     AA|   254|OGG| 15.33|     310|  173|4001.0|    7.0|
-------------+-------------+--------------------+------------------+
    org_dummy|    dow_dummy|            features|        prediction|
-------------+-------------+--------------------+------------------+
(7,[2],[1.0])|(6,[2],[1.0])|(14,[0,3,10],[398.])|364.38375267209113|
    (7,[],[])|(6,[2],[1.0])|(14,[0,10],[4001..])| 313.2461800798374|


# example
+---+---------------------------------+-----+
|id |text                             |label|
+---+---------------------------------+-----+
|1  |Sorry I ll call later in meeting |0    |
|2  |Dont worry I guess he is busy    |0    |
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF
tokenizer = Tokenizer(inputCol='text', outputCol='words')
remover = StopWordsRemover(inputCol='words', outputCol='terms')
hasher = HashingTF(inputCol='terms', outputCol="hash")
idf = IDF(inputCol="hash", outputCol="features")
logistic = LogisticRegression()
pipeline = Pipeline(stages=[tokenizer, remover, hasher, idf, logistic])


CrossValidator().fit()
# cross validation: better way to evaluate model performance
flights.show()
+------+--------+--------+
|km    |features|duration|
+------+--------+--------+
|2317.0|[2317.0]|232     |
|2943.0|[2943.0]|250     |

params = ParamGridBuilder().build()
regression = LinearRegression(labelCol="duration")
evaluator = RegressionEvaluator(labelCol="duration")

from pyspark.ml.tuning import CrossValidator
cv = CrossValidator(estimator=regression, estimatorParamMaps=params, 
                    evaluator=evaluator, numFolds=5)
cv = cv.fit(flights_train)

# example
indexer = StringIndexer(inputCol='org', outputCol='org_idx')
onehot = OneHotEncoder(inputCols=['org_idx'], outputCols=['org_dummy'])
assembler = VectorAssembler(inputCols=['km', 'org_dummy'], outputCol='features')
pipeline = Pipeline(stages=[indexer, onehot, assembler, regression])
cv = CrossValidator(estimator=pipeline, estimatorParamMaps=params, evaluator=evaluator)


ParamGridBuilder().addGrid().build()
# grid search
params = ParamGridBuilder()
params = params.addGrid(regression.regParam, [0.01, 0.1, 1.0, 10.0])
               .addGrid(regression.elasticNetParam, [0.0, 0.5, 1.0])
params = params.build()
print('Number of models to be tested: ', len(params)) # 12
cv = CrossValidator(estimator=pipeline, estimatorParamMaps=params, 
                    evaluator=evaluator, numFolds=5)
best_model = cv.bestModel
predictions = best_model.transform(flights_test)
evaluator.evaluate(predictions)
12.44394990230698

best_model.stages
[StringIndexerModel: uid...]
# Get the parameters for the LinearRegression object in the best model
best_model.stages[3].extractParamMap()

# example
params = ParamGridBuilder()
params = params.addGrid(hasher.numFeatures, [1024, 4096, 16384]) \
               .addGrid(hasher.binary, [True, False])
params = params.addGrid(logistic.regParam, [0.01, 0.1, 1.0, 10.0]) \
               .addGrid(logistic.elasticNetParam, [0.0, 0.5, 1.0])
params = params.build()


DecisionTreeClassifier(), GBTClassifier(), RandomForestClassifier(),
BinaryClassificationEvaluator(), 
# ensemble
flights.show()
+---+------+--------+-----------------+-----+
|mon|depart|duration|features         |label|
+---+------+--------+-----------------+-----+
|0  |16.33 |82      |[0.0,16.33,82.0] |1    |
|2  |6.17  |82      |[2.0,6.17,82.0]  |0    |

from pyspark.ml.classification import DecisionTreeClassifier, GBTClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
tree = DecisionTreeClassifier().fit(flights_train)
gbt = GBTClassifier().fit(flights_train)
# Compare AUC on testing data
evaluator = BinaryClassificationEvaluator()
print(evaluator.evaluate(tree.transform(flights_test)))
print(evaluator.evaluate(gbt.transform(flights_test)))
0.627540858561942
0.6841776126811533
# Find the number of trees and the relative importance of features
print(gbt.trees)
#[DecisionTreeRegressionModel: uid=dtr_249715c0c0ae, depth=5 ...]
print(gbt.featureImportances)
(3,[0,1,2],[0.3147273781412654,0.3202519980471864,0.36502062381154826])

# Create a random forest classifier
forest = RandomForestClassifier()
params = ParamGridBuilder()
         .addGrid(forest.featureSubsetStrategy, ['all', 'onethird', 'sqrt', 'log2'])
         .addGrid(forest.maxDepth, [2, 5, 10])
         .build()
evaluator = BinaryClassificationEvaluator()
cv = CrossValidator(estimator=forest, estimatorParamMaps=params, 
                    evaluator=evaluator, numFolds=5)
evaluator.evaluate(cv.transform(flights_test))
0.7026685175668

print(cv.bestModel)
#RandomForestClassificationModel: uid ...
print(cv.avgMetrics)
[0.61550451929848, 0.661275302749083, 0.6832959983649716, ,,,]
# What's the optimal parameter value for maxDepth?
print(cv.bestModel.explainParam('maxDepth'))
# What's the optimal parameter value for featureSubsetStrategy?
print(cv.bestModel.explainParam('featureSubsetStrategy'))


KMeans().train()
# Clustering, KMeans

from pyspark.mllib.clustering import KMeans

clusterRDD = sc.textFile(file_path)
rdd_split = clusterRDD.map(lambda x: x.split("\t"))
rdd_split_int = rdd_split.map(lambda x: [int(x[0]), int(x[1])])
[[664159, 550946],
 [665845, 557965],
 [597173, 575538] ...]

for clst in range(13, 17):
    model = KMeans.train(rdd_split_int, clst, seed=1)
    WSSSE = rdd_split_int.map(lambda point: error(point)).reduce(lambda x, y: x + y)
    print("The cluster {} has Within Set Sum of Squared Error {}".format(clst, WSSSE))
model = KMeans.train(rdd_split_int, k=16, seed=1) # best k = 16
cluster_centers = model.clusterCenters
[array([801616.78164557, 321123.34177215]),
 array([167856.14071856, 347812.71556886]),
 array([670929.06818182, 862765.73295455]) ...]

rdd_split_int_df_pandas = spark.createDataFrame(rdd_split_int, schema=["col1", "col2"]).toPandas()
cluster_centers_pandas = pd.DataFrame(cluster_centers, columns=["col1", "col2"])
plt.scatter(rdd_split_int_df_pandas["col1"], rdd_split_int_df_pandas["col2"])
plt.scatter(cluster_centers_pandas["col1"], cluster_centers_pandas["col2"], color="red", marker="x")
plt.show()


# ----------------------------------------------------------------------------------------
6- Building Recommendation Engines with PySpark
# ----------------------------------------------------------------------------------------

TJ_ratings.show()
+---------+--------------------+------+
|user_name|          movie_name|rating|
+---------+--------------------+------+
|   Taylor|            Twilight|   4.9|
|   Taylor|  A Walk to Remember|   4.5|
# Generate recommendations for users
get_ALS_recs(["Taylor","Jane"]) 
    userId  pred_rating                 title          genres
0   Taylor         3.89   Seven Pounds (2008)           Drama
1   Taylor         3.61      Cure, The (1995)           Drama
2   Taylor         3.55  Kiss Me, Guido (1997)         Comedy
...
6     Jane         4.96           Fear (1996)        Thriller
7     Jane         4.85  Lord of the Rings: T  Adventure|Fant
...

'''
recommendations are content-based and collaborative-based engines
explicit vs implicit
apply factorization matrix from 1 matrice to 2 matrices
latent features: Features contained in data, but aren't directly observable.

matrix mult
nmmmm
n
n

nxm     matmult   mxd = nxd -> np.dot(a,b)
num of latent features: k or rank to determine m from nxd to nxm and mxd
'''

to_long(), distinct().coalesce(1), monotonically_increasing_id(),
withColumn().persist(),
#data preperation
from pyspark.sql.functions import monotonically_increasing_id

R.show()
+----------------+-----+----+----------+--------+
|            User|Shrek|Coco|Swing Kids|Sneakers|
+----------------+-----+----+----------+--------+
|    James Alking|    3|   4|         4|       3|
|Elvira Marroquin|    4|   5|      null|       2|

# ratings.melt(ids=['A'], values=['B', 'C'],
# variableColumnName="variable", valueColumnName="value")
ratings = to_long(R)
ratings.show()
+----------------+----------+------+
|            User|     Movie|Rating|
+----------------+----------+------+
|    James Alking|     Shrek|     3|
|    James Alking|      Coco|     4|

users = ratings.select("User").distinct().coalesce(1)
users = users.withColumn("userId", monotonically_increasing_id()).persist()
users.show()
+----------------+------+
|            User|userId|
+----------------+------+
|Elvira Marroquin|     0|
|      Jack Bauer|     1|

movies.show()
+----------+-------+
|     Movie|movieId|
+----------+-------+
|  Sneakers|      0|
|      Coco|      1|

movie_ratings = ratings.join(users, "User", "left").join(movies, "Movie", "left")
movie_ratings.show()
+----------+----------------+------+------+-------+
|     Movie|            User|Rating|userId|movieId|
+----------+----------------+------+------+-------+
|     Shrek|    James Alking|     3|     2|      3|
|      Coco|    James Alking|     4|     2|      1|


randomSplit(), ALS().fit().transform(), RegressionEvaluator().evaluate()
# ALS model
(training_data, test_data) = ratings.randomSplit([0.8, 0.2], seed=42)

from pyspark.ml.recommendation import ALS
als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating", 
          rank=10, maxIter=15, regParam=0.1, coldStartStrategy="drop", 
          nonnegative=True, implicitPrefs=False)
model = als.fit(training_data)
test_predictions = model.transform(test_data)
test_predictions.show()
+------+-------+------+----------+
|userId|movieId|rating|prediction|
+------+-------+------+----------+
|     0|      1|   5.0|  2.421466|
|     0|      3|   4.0|  2.518772|
from pyspark.ml.evaluation import RegressionEvaluator
evaluator = RegressionEvaluator(metricName="rmse", 
            labelCol="ratings.columns", predictionCol="prediction")
RMSE = evaluator.evaluate(test_predictions)
0.16853197489754093


# movielens dataset
ratings.show()
+------+-------+------+----------+
|userId|movieId|rating| timestamp|
+------+-------+------+----------+
|     1|     31|   2.5|1260759144|
|     1|   1029|   3.0|1260759179|

numerator = ratings.select("rating").count()                # 100004
num_users = ratings.select("userId").distinct().count()     # 671
num_movies = ratings.select("movieId").distinct().count()   # 9066
denominator = num_users * num_movies
sparsity = (1.0 - (numerator *1.0)/denominator)*100
print("The ratings dataframe is ", "%.2f" % sparsity + "% empty.")
The ratings dataframe is 98.36% empty

from pyspark.sql.functions import col
ratings.filter(col("userId") < 100).show()
ratings.groupBy("userId").count().show()   # ratings count
+------+-----+
|userId|count|
+------+-----+
|   296|   20|
|   467|   64|
|   125|  210|
ratings.groupBy("movieId").count().select(min("count")).show()
ratings.groupBy("movieId").count().select(avg("count")).show()
ratings.groupBy("userId").count().select(min("count")).show()
ratings.groupBy("userId").count().select(avg("count")).show()
+------------------+
|        avg(count)|
+------------------+
|149.03725782414307|

ratings.printSchema()
ratings = ratings.select(ratings.userId.cast("integer"), 
          ratings.movieId.cast("integer"), ratings.rating.cast("double"))
ratings.printSchema()
root
 |-- userId: integer (nullable = true)
 |-- movieId: integer (nullable = true)
 |-- rating: double (nullable = true)

# ALS, evaluate, grid, crossval
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
(train, test) = ratings.randomSplit([0.8, 0.2], seed = 1234)
als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating", 
          nonnegative = True, implicitPrefs = False)
param_grid = ParamGridBuilder() \
            .addGrid(als.rank, [10, 50, 100, 150]) \
            .addGrid(als.maxIter, [5, 50, 100, 200]) \
            .addGrid(als.regParam, [.01, .05, .1, .15]) \
            .build()
evaluator = RegressionEvaluator(metricName="rmse", 
            labelCol="rating", predictionCol="prediction") 
cv = CrossValidator(estimator=als, estimatorParamMaps=param_grid, 
                    evaluator=evaluator, numFolds=5)
cv = cv.fit(train)
test_predictions = cv.bestModel.transform(test)
RMSE = evaluator.evaluate(test_predictions)
0.6332304339145925

cv.bestModel.getRank()        # 50
cv.bestModel.getMaxIter()     # 100
cv.bestModel.getRegParam()    # 0.1
test_predictions.show()
+------+-------+------+------------------+
|userId|movieId|rating|        prediction|
+------+-------+------+------------------+
|   380|    463|   3.0| 4.093334993256898|
|   460|    471|   5.0| 4.789751482535894


# Million Songs dataset
# what if you do not have customer rating? look at implicitly
msd.show()
+------+------+---------+
|userId|songId|num_plays|
+------+------+---------+
|   148|   148|        0|
|   243|   496|        0|

user_count = msd.select("userId").distinct().count()    # 321
song_count = msd.select("songId").distinct().count()    # 729
msd.filter(col("num_plays") > 0).groupBy("songId").count()
   .select(avg("count")).show()
+------------------+
|        avg(count)|
+------------------+
|35.251063829787235|
msd.filter(col("num_plays") > 0).groupBy("userId").count()
   .select(avg("count")).show()
+-----------------+
|       avg(count)|
+-----------------+
|77.42056074766356|

Z.show()
+------+---------+-------------+
|userId|productId|num_purchases|
+------+---------+-------------+
|  2112|      777|            1|
|     7|       44|           23|
users = Z.select("userId").distinct()
products = Z.select("productId").distinct()
cj = users.crossJoin(products)
+------+---------+
|userId|productId|
+------+---------+
|    22|       44|
|    22|      777|
Z_expanded = cj.join(Z, ["userId", "productId"], "left").fillna(0)
Z_expanded.show()
+------+---------+-------------+
|userId|productId|num_purchases|
+------+---------+-------------+
|    22|       44|            0|
|    22|      777|            0|
|    22|     1811|           96|

# ALS implicit model
ranks = [10, 20, 30, 40]
maxIters = [10, 20, 30, 40]
regParams = [.05, .1, .15]
alphas = [20, 40, 60, 80]
for r in ranks:
    for mi in maxIters:
        for rp in regParams:
            for a in alphas:
                model_list.append(
                  ALS(userCol= "userId", itemCol= "songId", ratingCol= "num_plays", 
                    rank = r, maxIter = mi, regParam = rp, alpha = a, c
                    oldStartStrategy="drop", nonnegative = True, implicitPrefs = True)
                )
len(model_list) # 192
# ROEM did not implemented here, ROEM is used instead of RMSE for better prediction
(training, test) = msd.randomSplit([0.8, 0.2])
train1, train2, train3, train4, train5 = training.randomSplit([0.2, 0.2, 0.2, 0.2, 0.2], seed = 1)
fold1 = train2.union(train3).union(train4).union(train5)
fold2 = train3.union(train4).union(train5).union(train1)
fold3 = train4.union(train5).union(train1).union(train2)
fold4 = train5.union(train1).union(train2).union(train3)
fold5 = train1.union(train2).union(train3).union(train4)
foldlist = [(fold1, train1), (fold2, train2), (fold3, train3), (fold4, train4), (fold5, train5)]
ROEMS = []
for model in model_list:
    for ft_pair in foldlist:
        fitted_model = model.fit(ft_pair[0])
        predictions = fitted_model.transform(ft_pair[1])
        r = ROEM(predictions)
        print ("ROEM: ", r)
    v_fitted_model = model.fit(training)
    v_predictions = v_fitted_model.transform(test)
    v_ROEM = ROEM(v_predictions)
    ROEMS.append(v_ROEM)
    print ("Validation ROEM: ", v_ROEM)
import numpy
i = numpy.argmin(ROEMS)             # 38
print("Smallest ROEM: ", ROEMS[i])  # 0.01980198019801982
best_model = model_list[38]
print ("Rank: ", best_model.getRank())
print ("MaxIter: ", best_model.getMaxIter())
print ("RegParam: ", best_model.getRegParam())
print ("Alpha: ", best_model.getAlpha())
Rank:  10
MaxIter:  40
RegParam:  0.05
Alpha:  60.0


# binary rating

from pyspark.sql.functions import col
binary_test_predictions.show()
+------+-------+------+-----------+
|userId|movieId|viewed| prediction|
+------+-------+------+-----------+
|    91|    148|     0|        0.0|
|   601|    148|     0|        0.0|
|   545|    148|     0|0.060729448|
ROEM(binary_test_predictions)
ROEM: 0.07436376290899886
# Look at user 42's test predictions
binary_test_predictions.filter(col("userId") == 42).show()
+------+-------+------+-----------+
|userId|movieId|viewed| prediction|
+------+-------+------+-----------+
|    42|    858|     0|  0.9915983|
|    42|   3703|     0|  0.5134803|

original_ratings.filter(col("userId") == 26).show()
+------+-------+------+--------------------+--------------------+
|userId|movieId|rating|               title|              genres|
+------+-------+------+--------------------+--------------------+
|    26|      1|     5|      ToyStory(1995)|Adventure|Animati...|
|    26|   2542|     5|LockStock&TwoSmok...|Comedy|Crime|Thri...|
binary_recs.filter(col("userId") == 26).show()
+------+-------+----------+--------------------+--------------------+
|userId|movieId|prediction|               title|              genres|
+------+-------+----------+--------------------+--------------------+
|    26|  30707| 1.1401137|Million Dollar Ba...|               Drama|
|    26|    293| 1.1154407|Léon: The Profess...|Action|Crime|Dram...|


# example on RDD rather than dataframe
from pyspark.mllib.recommendation import ALS

data = sc.textFile(file_path)
ratings = data.map(lambda l: l.split(','))
ratings.collect()
[['1', '31', '2.5', '1260759144'],
 ['1', '1029', '3.0', '1260759179'],
 ['1', '1061', '3.0', '1260759182'] ...]

ratings_final = ratings.map(lambda line: Rating(int(line[0]), int(line[1]), float(line[2])))
[Rating(user=1, product=31, rating=2.5),
 Rating(user=1, product=1029, rating=3.0),
 Rating(user=1, product=1061, rating=3.0) ...]

training_data, test_data = ratings_final.randomSplit([0.8, 0.2])
model = ALS.train(training_data, rank=10, iterations=10)
testdata_no_rating = test_data.map(lambda p: (p[0], p[1]))
predictions = model.predictAll(testdata_no_rating)
predictions.take(2)
[Rating(user=624, product=69069, rating=1.453145849276426),
 Rating(user=390, product=667, rating=2.3272204469965674)]

rates = ratings_final.map(lambda r: ((r[0], r[1]), r[2]))
preds = predictions.map(lambda r: ((r[0], r[1]), r[2]))
rates_and_preds = rates.join(preds)
[((1, 31), (2.5, 1.9392769510659549)),
 ((1, 1293), (2.0, 0.812552128115867)),
 ((1, 2455), (2.5, 0.36069686984833416)) ...]

MSE = rates_and_preds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
print("Mean Squared Error of the model for the test data = {:.2f}".format(MSE))
Mean Squared Error of the model for the test data = 1.33
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------