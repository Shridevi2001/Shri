import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydatabase=myclient["mydb"]
print("database created successfully")

mycollection=mydatabase["mycol"]
print("collection created successfully")

doc={"name":"shreee","age":23}
mydoc=mycollection.insert_one(doc)

doc=[
    {"name":"raju","age":55,"qualification":"BE"},
    {"name":"adi","age":35,"qualification":"MBA"},
    {"name":"tanu","age":55,"qualification":"MBBS"},
    {"name":"raju","age":78,"qualification":"BE"}
]
mydoc=mycollection.insert_many(doc)


# findingone=mycollection.find_one({"name":"raju"})
# print(findingone)

# findingmany=mycollection.find()
# for x in findingmany:
#     print(x)

# findingmany=mycollection.find({"age":55})
# for x in findingmany:
#     print(x)    


# query={"qualification":"BE"}

# a=mycollection.find_one(query)
# print(a)


# a=mycollection.find(query)

# for x in a:
#  print(x)

 
 
#  for x in  mycollection.find({},{"name":0}):
#    print(x)

# a=mycollection.find().sort("age")  
# for x in a:
#   print(x)

# a=mycollection.find().sort("age",-1)  
# for x in a:
#   print(x)

# query={"name":"raju"}
# a=mycollection.delete_many(query)
# c=mycollection.find()
# for x in c:
#  print(x)

# myquery={"qualification":"BE"}
# updatevalue={"$set":{"qualification":"BAMS"}}
# mycollection.update_many(myquery,updatevalue)
# for x in mycol


