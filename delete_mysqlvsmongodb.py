import mysql.connector
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["covid_19"]
mycol = mydb["covid19"]

def delete_mongodb():

    d = mycol.delete_many({"id":{'$lt':10000}} ) 
    result = d.deleted_count
    return result

def test_benchmark1_delete_mongodb(benchmark):
   benchmark(delete_mongodb)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="covid_19"
)

def delete_mysql():
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM covid19 LIMIT 10000")
    mydb.commit()

 
def test_benchmark2_delete_mysql(benchmark):
  benchmark(delete_mysql)


