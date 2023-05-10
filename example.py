import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
print("connected successfully")

# mydata=client["TR6"]
# print("database created successfully")

# mycol=mydata["Alarmss"]
# print("collection created successfully")

Datalist=client.list_database_names()
print(Datalist)
if "TR6" in Datalist:
    print("databse already exist")

    

    
else:
    mydata=client["TR6"]
    print("database created successfully")

    mycol=mydata["Alarmss"]
    print("collection created successfully")

    doc={"_id":1}
    mycol.insert_one(doc)
    
 
mydata=client["TR6"]
mycol=mydata["Alarmss"]
# collist=mydata.list_collection_names()
# if ""
query={"_id":1}
newvalue={"$set":{"Alarm 8":False}}
x=mycol.update_one(query,newvalue)
print("updated")
