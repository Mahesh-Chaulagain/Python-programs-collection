# MongoDB
- NoSQL database
- stores data in JSON-like documents, which makes the database very flexible and scalable

# PyMongo
- a MongoDB driver needed by python to access the MongoDB datadase
- install driver using:
    python -m pip install pymongo

- to start MongoDB:
    net start MongoDB

# Create Database
- to create a database in mongodb:
    1. start by creating a MongoClient object
    2. then specify a connection URL with the correct ip address and the name of the database you want to create
    3. MongoDB will create the database if it does not exist and make connection to it

- example: to create a database called 'mydatabase' use
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["mydatabase"]

* NOTE: In MongoDB, a database is not created until it gets content. MongoDB waits until you have created
    a collection(table) with
    at least one document(record)
before it actually creates the database(and collection)

# Check if database exists
- can check if a database exists by listing all databases in the system
- to return a list of your system's databases
    print(myclient.list_database_names())
- check a specific database by name as:   
    dblist = myclient.list_database_names()
    if 'mydatabase' in dblist: 
        print('The database exists.')

# Create Collection
- 'collection' in MongoDB is the same as the 'table' in SQL databases
- to create a collection in MongoDB, use database object and specify the name of the collection you want to create as:
    mycol = mydb["customers"]

* NOTE : In MongoDB, a collection is not created until it gets content

# Check if collection exists
- check if a collection exists in a database by listing all collections
    print(mydb.list_collection_names())

- can check a specific collection by name as:
    collist = mydb.list_collection_names()
    if "customers" in collist:
        print('The collection exists.')

# Insert document
- a 'document' in MongoDB is the same as as 'record' in SQL databases
- to insert a record into a collection we use the insert_one() method
- the first parameter of the 'insert_one()' method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert
- example:  
    mydict = { "name": "john", "address":"highway 37"}
    x = mycol.insert_one(mydict)

# Return the _id Field
- the 'insert_one() method returns a InsertOneResult object, which has a property inserted_id, that holds the id of the inserted document
- example: insert the record in the 'customers' collection and return the value of the '_id' field
    mydict = { "name": "Peter", "address": "Lowstreet 27" }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

* NOTE: if '_id' field is not specified, then MongoDB will add one for us and assign a unique id for each document

# Insert multiple documents
- to insert multiple documents into a collection in MongoDB, we use the insert_many() method
- the first parameter of the insert_many() method is a list containing dictionaries with the data you want to insert
    mylist = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
    ]

    x = mycol.insert_many(mylist)

    #print list of the _id values of the inserted documents:
    print(x.inserted_ids)

# Insert multiple documents with specified IDs
- if you do not want MongoDB to assign unique ids for your document, you can specify the '_id" field when you insert the document(s).
    mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

# MongoDB find
- like the 'SELECT' statement used to find data in table in a MYSQL database
- use the find() and find_one() methods to find a data in a collection 

- find_one() method returns the first occurance in the selection
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    x = mycol.find_one()

    print(x)

- find() method returns all occurances in the selection
- no parameters in the find() method gives us the same result as 'SELECT *' in MYSQL
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    for x in mycol.find():
    print(x)

- the first parameter of the find() method is a query object whild the second parameter is an object describing which fields to include in the result
- to return only the names and addresses no the _ids:
    for x in mycol.find({}, {"_id":0,"name":1,"address":1}):
  print(x)

* NOTE:You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). If you specify a field with the value 0, all other fields get the value 1, and vice versa

- Example: to exclude 'address' from the result:
    for x in mycol.find({}, {"address":0}):
    print(x)

## Python MongoDB Query

# Filter the result
- can filter the result by using a query object, which is the first argument of the find() method and is used to limit the search
- to find document(s) with the address "Park Lane 38" use:
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = {"address": "Park Lane 38"}

    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)

# Advanced Query
- to make advanced queries use modifiers as values in the query object
- example: to find the documents where the 'adress' field starts with the letter "S" or higher(alphabetically), use the greater than modifier:{"$gt": "S"}
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = {"address": {"$gt":"S"}}

    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)

# Filter with regular expressions
- can also use regular expressions as modifier
- regex can only be used to query strings
- to find only the documents where the "address" field starts with the letter "S"
    myquery = {"address": {"$regex":"^S"}}

# Sort the result
- use the sort() method to sort the result in ascending or descending order
- sort() method takes one parameter for 'fieldname' and one parameter for 'direction'(ascending is the default direction)
- to sort the result alphabetically by name:
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mydoc = mycol.find().sort("name")

    for x in mydoc:
        print(x)

- use the value '-1' as the second parameter to sort descending
    i.e sort("name", 1) #ascending
        sort("name", -1) #descending

- example of sort descending
    mydoc = mycol.find().sort("name", -1)

# Delete Document
- to delete one document use the delete_one() method
- the first parameter of the 'delete_one()' method is a query object defining which document to delete
- to delete the document with the address "Mountain 21" use:    
    myquery = {"address": "Mountain 21"}
    mycol.delete_one(myquery)

* NOTE: If the query finds more than one document, only the first occurance is deleted

- to delete more than one document, use the delete_many() method
- to delete all documents where the address starts with the letter 'S' use:
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = { "address": {"$regex": "^S"} }

    x = mycol.delete_many(myquery)

    print(x.deleted_count, " documents deleted.")

- to delete all documents in a collection pass an empty query object to the delete_many() method
- example: to delete all documents in the 'customers' collection use:
    x = mycol.delete_many({})

# Drop collection
- delete a collection(table) by using the 'drop()' method
    mycol.drop()

# Update collection
- update a record by using the 'update_one()' method
- the first parameter of the 'update_one()' method is a query object defining which document to update
- the second parameter is an object defining the new values of the document
- example: to change the address from "Valley 345" to "Canyon 123" use:
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = {"address": "Valley 345"}
    newvalues = {"$set": {"address": "Canyon 123"}}

    mycol.update_one(myquery, newvalues)

    for x in mycol.find():
        print(x)

* Note: If the query finds more than one record, only the first occurrence is updated

- to update all documents that meets the criteria of the query, use the 'update_many()' method
- example- to update all documents where the address starts with the letter 'S':
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    myquery = {"address": {"$regex":"^S"}}
    newvalues = {"$set": {"name": "Ram"}}

    x = mycol.update_many(myquery, newvalues)

    print(x.modified_count,"documents updated")

    for i in mycol.find():
        print(i)

# Limit
- to limit the result in MongoDB, use the limit() method
- takes one parameter, a number defining how many documents to return
- example: limit the result to only return 5 documents
