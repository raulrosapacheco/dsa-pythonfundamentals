import datetime
# Install pymongo package to connect to MongoDB database
# Importar a função MongoClient do pacote pymongo
from pymongo import MongoClient

# Connecting to MongoDB
# ('localhost', 27017): significa que o Mongo está nessa máquina na porta 27017
# guardamos a informação sobre a conexão no objeto connect
connect = MongoClient('localhost', 27017)
print(type(connect))

# A single instance of MongoDB can support multiple databases.
# Let's create the registration_db database
# A partir da conexão com registration_db, colocamos isso em db
db = connect.registration_db
print(type(db))  # é um banco de dados do pymongo

# A collection is a group of documents stored in MongoDB
# Um banco NoSQL possui varias coleções que são similares as tabelas em SQL
collection = db.registration_db
print(type(collection))

"""
An important note about collections (and databases) in MongoDB is that they are created later - 
none of the above commands actually performed any operation on the MongoDB server. 
Collections and databases are created when the first document is inserted.

Data in MongoDB is represented (and stored) using JSON (Java Script Object Notation) documents. 
With PyMongo we use dictionaries to represent documents.
"""
doc1 = {"code": "ID-9987725", "prod_name": "refrigerator", "brands": ["brastemp", "consul", "elecrolux"],
        "data_registration": datetime.datetime.utcnow()}
# Criando uma coleção docs
collection = db.docs
# Inserindo doc1
doc_id = collection.isert_one(doc1)

# QUando um documento é inserido uma chave especial, "_id", é adicionada automaticamente se o documento ainda n possuir
# id
print(doc_id.inserted_id)
print(doc_id)



