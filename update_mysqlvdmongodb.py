import mysql.connector
import pymongo
from pymongo import UpdateOne

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["covid_19"]
mycol = mydb["covid19"]

def update_mongodb():
        # benchmark something
    bulk_request = [ ]
    for doc in mycol.find().limit( 10000 ):
        bulk_request.append(UpdateOne( { '_id': doc['_id'] }, { '$set': { 'death_yn': 0 } } ) )
    result = mycol.bulk_write( bulk_request )
    return result

def test_benchmark1_update_mongodb(benchmark):
   benchmark(update_mongodb)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="covid_19"
)

def update_mysql():
    mycursor = mydb.cursor()
    mycursor.execute(" UPDATE covid19 SET death_yn = 0 LIMIT 10000")
    mydb.commit()

def test_benchmark2_update_mysql(benchmark):
  benchmark(update_mysql)


