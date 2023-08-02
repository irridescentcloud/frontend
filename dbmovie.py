from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient('mongodb://sparta:test@ac-gbmvobs-shard-00-00.wzl4jv6.mongodb.net:27017,ac-gbmvobs-shard-00-01.wzl4jv6.mongodb.net:27017,ac-gbmvobs-shard-00-02.wzl4jv6.mongodb.net:27017/?ssl=true&replicaSet=atlas-lk9ter-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.dbsparta

db.movies2.update_one({'title':'부당거래'},{'$set':{'age':'18세 이상 관람가'}})





