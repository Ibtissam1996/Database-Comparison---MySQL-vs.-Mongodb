import csv
import json
import pandas as pd
import mysql.connector
import pymongo
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["covid_19"]
mycol = mydb["covid19"]

def insert_mongodb():
      #CSV to JSON Conversion
  csvfile = open('/Users/mac/Desktop/covid_19.csv', 'r')
  reader = csv.DictReader( csvfile )
  mongo_client=MongoClient() 
  db=mongo_client.october_mug_talk
  db.segment.drop()
  header= [ "id","cdc_case_earliest_dt","cdc_report_dt","pos_spec_dt","onset_dt","current_status","sex","age_group","race_ethnicity_combined","hosp_yn","icu_yn","death_yn","medcond_yn"]

  for each in reader:
      row={}
      for field in header:
          row[field]=each[field]

      result = db.segment.insert(row)
      return result

def test_benchmark1(benchmark):
   benchmark(insert_mongodb)




mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="covid_19"
)

def insert_mysql():
    mycursor = mydb.cursor()
    mycursor.execute(" LOAD DATA LOCAL INFILE '/Users/mac/Desktop/covid_19.csv' INTO TABLE covid19 FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n'")
    mydb.commit()
 
def test_benchmark(benchmark):
  benchmark(insert_mysql)

