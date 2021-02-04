import mysql.connector
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["covid_19"]
mycol = mydb["covid19"]

def select_mongodb():
        # benchmark something
    result = mycol.find().limit(10000)
    return result

def test_benchmark1_select_mongodb(benchmark):
   benchmark(select_mongodb)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="covid_19"
)

def select_mysql():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM covid19 LIMIT 10000")
    result = mycursor.fetchall()
    return result
 
def test_benchmark2_select_mysql(benchmark):
  benchmark(select_mysql)


