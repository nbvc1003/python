import pymongo

con = pymongo.MongoClient('127.0.0.1',27017)
print(con)

con.close()