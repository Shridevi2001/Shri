import time
from pylogix import PLC

import pymongo
from pylogix import PLC

client = client=pymongo.MongoClient("mongodb://localhost:27017/")

databaselist = client.list_database_names()

if "TR6pro1" in databaselist:
    print("databasse exist")

else:
    databasename = client["TR6pro1"]
    collection = databasename.create_collection("Status")
    document = {"_id":"12345"}
    collection.insert_one(document)

databasename = client["TR6pro1"]
x = databasename.get_collection("Status")


def read(tag):
    global comm
    comm = PLC()
    comm.IPAddress = "192.168.3.101"
    val = comm.Read(tag)
    return val

while True:
    def main():
        v = read(["current_1","current_2","tag_1"])
        x.update_one({"_id":"12345"},{"$set":{"current_1":v[0].Value,"current_2":v[1].Value,"tag_1":v[2].Value}})
        print(v[0].Value)

if __name__ == "__main__":
    main()
