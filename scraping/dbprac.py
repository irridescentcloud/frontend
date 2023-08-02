from pymongo import MongoClient


client = MongoClient('mongodb://sparta:test@ac-gbmvobs-shard-00-00.wzl4jv6.mongodb.net:27017,ac-gbmvobs-shard-00-01.wzl4jv6.mongodb.net:27017,ac-gbmvobs-shard-00-02.wzl4jv6.mongodb.net:27017/?ssl=true&replicaSet=atlas-lk9ter-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.dbsparta


db.users.delete_one({'name':'영수'})