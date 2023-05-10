from ctypes import pointer
import pymongo
import pprint

myclient=pymongo.MongoClient("mongodb://localhost:27017")
print("connected")

datalist=myclient.list_database_names()
print(datalist)

database=myclient["new"]
collist=database.list_collection_names()
print(collist)

def insert_document():
 database=myclient["new"]
 mycol=database["example"]
 docs={"name":"tomato","type":"vegetable"}
 inserted_id=mycol.insert_one(docs).inserted_id
 print(inserted_id)

insert_document()


production=myclient["production"]
customer=production["customer"]

def insert_documents():
 firstname=["sss","aaa","bbbbb"]
 lastname=["d","t","u"]
 age=[24,56,78]

 docs=[]

 for firstname,lastname,age in zip(firstname,lastname,age):
  doc={"firstname":firstname,"lastname":lastname,"age":age}
  docs.append(doc)
 customer.insert_many(docs)
insert_documents()   


# def find_document():
#  finding=customer.find()
#  for x in finding:
#   print(x)

# find_document()

# def findone_doc():
#  findone=customer.find_one({"firstname":"sss"})
#  print("--------------------------------------------------------------------------------------------------------")
#  print(findone)

# findone_doc() 

# def count_doc():
 
#  count=customer.count_documents(filter={})
#  print("number of docs=",count)

# count_doc()

# def getcustomerbyid(customer_id):
#  from bson.objectid import ObjectId

#  _id=ObjectId(customer_id)
#  customer_one=customer.find_one({"_id":_id})
#  print(customer_one)


# getcustomerbyid("645735cce2b0ee998c569a23")

# def get_age_range(min_age,max_age):
#     query={"$and" : [
#               {"age": {"$gte":min_age}},
#               {"age": {"$gte":max_age}}
#             ]}
#     print("----------------------------------------------------------------------")
#     c=customer.find(query).sort("age")
#     for x in c:
#      print(x)
# get_age_range(20,60)


# def columns():
#  columns={"_id":0,"firstname":1,"lastname":1}
#  u=customer.find({},columns)
#  for c in u:
#   print(c)
# columns()

# def update_customerby_id(customer_id):
#  from bson.objectid import ObjectId
#  _id=ObjectId(customer_id)

# #  updates={
# #     "$set":{"new_field":True},
# #     # "$inc":{"age",1},
# #     "$rename":{"firstname":"first","lastname":"last","age":"a"}
# #  }
# #  customer.update_one({"_id":_id},updates)

#  customer.update_one({"_id":_id},{"$unset":{"new_field":""}})

def replaceaaa(customer_id):
  from bson.objectid import ObjectId
  _id=ObjectId(customer_id) 

  doc={"firstname":"fname","lastname":"lname","age":909}
     
  
  customer.replace_one({"_id":_id},doc)
replaceaaa("64575387c417276aad65fa8e") 

def deleteone(customer_id):
  from bson.objectid import ObjectId
  _id=ObjectId(customer_id) 
  customer.delete_one({"_id":_id})
deleteone("64575387c417276aad65fa8e")
