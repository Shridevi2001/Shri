import pymongo
from pylogix import PLC

client = client=pymongo.MongoClient("mongodb://localhost:27017/")

databaselist = client.list_database_names()

if "TR6pro" in databaselist:
    print("databasse exist")

else:
    databasename = client["TR6pro"]
    collection = databasename.create_collection("Status")
    document = {"_id":"12345"}
    collection.insert_one(document)

databasename = client["TR6pro"]
x = databasename.get_collection("Status")

taglist = ["CurrentScreen","Zone1ASpeed","Zone2ASpeed","Zone2BSpeed","CurrentScreen","Zone1ASpeed","Zone2ASpeed","Zone2BSpeed"]

# while True:
with PLC() as comm:
        comm.IPAddress = '192.168.1.9'
        ret = comm.Read(taglist)
        print(ret.Value)
        # for i in ret:
        #     x.update_one({"_id":"12345"},{"$set":{""}}) 