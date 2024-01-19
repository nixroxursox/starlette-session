import time
import datetime
from urllib.parse import quote_plus
import pymongo
from pymongo.mongo_client import MongoClient as mc
from pymongo.errors import PyMongoError
from decouple import config
import multiprocessing
import motor
import uvloop
from motor.motor_asyncio import AsyncIOMotorClient as motor_async
import asyncio
# directory reach


# Configuration from environment variables or '.env' file.

ru = config("readUser")
wu = config("writeUser")
rp = config("readPass")
wp = config("writePass")


class dataBase:
    def __init__(self, method, db, col):
        self.conn: dict = {}
        self.conn['method']: str = 'method'
        self.conn['db']: str  = 'db'
        self.conn['col'] = 'col'
        self.conn['socket_path'] = '%2Ftmp%2Fmongodb-27017.sock'
        self.conn['dbUser'] = self._userType(self.conn['method'])
        if self.conn['dbUser'] == 'wu':
            self.conn['dbPass'] = config('writePass')
        else:
            self.conn['dbPass'] = config('readPass')    
        self.conn['aS']: str = 'eCom'
        self.conn['mechanism'] = 'SCRAM-SHA-256'
        self.conn[ 'dc'] = 'dict'
        self.connect: bool = True
        self.conn['uri'] = "mongodb://%s:%s@%s" % (
            quote_plus(self.conn['dbUser']),
            quote_plus(self.conn['dbPass']),
            quote_plus(self.conn['socket_path']),
        )


    def __call__(self, method):
        method: self.conn['method'] = method
        return self
            
    @staticmethod
    def db_connect():
        method = 'read'
        conn = {}
        conn['dbUser'] = 'ru'
        conn['dbPass'] = config('readPass')    
        mechanism = 'SCRAM-SHA-256'
        aS = 'eCom'
        dc = 'dict'
        conn['socket_path'] = '%2Ftmp%2Fmongodb-27017.sock'
        uri = "mongodb://%s:%s@%s" % (
            quote_plus(conn['dbUser']),
            quote_plus(conn['dbPass']),
            quote_plus(conn['socket_path'])
        )
        connect = True
        client = motor.motor_asyncio.AsyncIOMotorClient(
            uri,
            document_class=dc,
            authSource=aS,
            authMechanism=mechanism,
            connect=connect
        )
        return client['eCom']

    @staticmethod
    def db_client():
        method = 'read'
        conn = {}
        conn['dbUser'] = 'ru'
        conn['dbPass'] = config('readPass')    
        mechanism = 'SCRAM-SHA-256'
        aS = 'eCom'
        dc = 'dict'
        conn['socket_path'] = '%2Ftmp%2Fmongodb-27017.sock'
        uri = "mongodb://%s:%s@%s" % (
            quote_plus(conn['dbUser']),
            quote_plus(conn['dbPass']),
            quote_plus(conn['socket_path'])
        )
        connect = True
        client = motor.motor_asyncio.AsyncIOMotorClient(
            uri,
            document_class=dc,
            authSource=aS,
            authMechanism=mechanism,
            connect=connect
        )
        return client

    def _userType(self, method):
        if method == "write":
            dbUser = wu
            return dbUser
        else:
            dbUser = ru
            return dbUser


    async def nConfig(method):
        authSource = "eCom"
        mechanism = "SCRAM-SHA-256"
        dbObj = "eCom"
        #host = "%2Ftmp%2Fmongodb-27017.sock"
        host = "dockerswarm-mongod-1"
        port = 27017
        if method == "read":
            dbUser = ru
            dbPass = rp
        else:
            dbUser = wu
            dbPass = wp
        client = mc(
            host,
            port,
            username=dbUser,
            password=dbPass,
            authSource=authSource,
            authMechanism=mechanism,
        )
        db = client[dbObj]
        return db


    def motorConf(self, method):
        if method == "write":
            dbUser = wu
            dbPass = wp
        else:
            dbUser = ru
            dbPass = rp
        username = dbUser
        password = dbPass
        u = quote_plus(username)
        p = quote_plus(password)
        authSource = 'eCom'
        mechanism = "SCRAM-SHA-256"
        dbObj = "eCom"
        loop = asyncio.get_event_loop()
        document_class = dict
        socket_path = quote_plus("/tmp/mongodb-27017.sock")
        connect = True
        uri = "mongodb://%s:%s@%s/%s" % (u, p, socket_path, dbObj)
        client = motor.motor_asyncio.AsyncIOMotorClient(
            uri,
            document_class=document_class,
            authSource=authSource, 
            authMechanism=mechanism,
            connect=connect,
            io_loop=loop
        )
        #db = client["eCom"]
        return client


    def pyMongoConf(self, method):
        if method == "write":
            dbUser = wu
            dbPass = wp
        else:
            dbUser = ru
            dbPass = rp
        username = dbUser
        password = dbPass
        u = quote_plus(username)
        p = quote_plus(password)
        authSource = 'eCom'
        mechanism = "SCRAM-SHA-256"
        dbObj = "eCom"
        document_class = dict
        socket_path = quote_plus("/tmp/mongodb-27017.sock")
        connect = True
        uri = "mongodb://%s:%s@%s/%s" % (u, p, socket_path, dbObj)
        client = pymongo.mongo_client.MongoClient(
            uri,
            document_class=document_class,
            authSource=authSource, 
            authMechanism=mechanism,
            connect=connect
        )
        #db = client["eCom"]
        return client

    async def db_find_one(self, item):
        self.item = item
        cl = self.usConf('read')
        col = cl.eCom.userData
        return col.find_one({'reg_data.userId': item})
        

    async def connX509(self):
        client = pymongo.mongo_client.MongoClient(
            "example.com",
            authMechanism="MONGODB-X509",
            tls=True,
            tlsCertificateKeyFile="/path/to/client.pem",
            tlsCAFile="/path/to/ca.pem",
        )
        db = client["theRing"]
        return db

    async def disconnect(self):
        return db.close()
       

    # def checkPass(dbDict):
    #     if dataBase.findUser == True:s
    #         try:
    #             dbr = dataBase.conf("read")
    #             rcol = dbr["userLogins"]
    #             pw = dbDict["password"]
    #             dbp = dbDict["pinCode"]
    #             password = rcol.find({},{'_id': 0, 'userId': 1, 'password': 1, 'pin_code': 1})
    #             check = pwhash.verify(password[2], pw)
    #             checkPin = pwhash.verify(password[3], dbp)
    #             if check == True and checkPin == True:
    #                 return True
    #             else:
    #                 return False
    #         except Exception as e:
    #             return e
    #     else:
    #         return False
    #         if dbDict[fuserId] == fuserId:
    #             if pwhash.str(fpasswd, chkUser[password]) == True:
    #                 if pwhash.str(pin_code, chkUser[pin_code]) == True:
    #                     return userId
    #                 else:
    #                     return False
    #             else:
    #                 return Fals
    #         return True

    async def allUsers():
        try:
            dbr = dataBase.conf("read")
            rcol = dbr["userLogins"]
            userinfo = rcol.findMany({}, q.findMany())
            return userinfo
        except PyMongoError as e:
            print(e)

    # def addUser(chkUser, password, pin, a):
    #     try:
    #         (
    #             fuserId,
    #             fpasswd,
    #             fpinCode,
    #         ) = dbDict
    #         dbr = dataBase.conf("read")
    #         rcol = dbr["userLogins"]
    #         data = {
    #             "username": chkUser,
    #             "password": pwhash.scryptsalsa208sha256_str(password),
    #             "pin": pwhash.scryptsalsa208sha256_str(pin),
    #             "isActive": True,
    #             "isVendor": False,
    #             "broquerage": int(3),
    #             "created": datetime.datetime.now(),
    #             "vendorBond": float(500.0),
    #             "is_admin": a,
    #             "identifier": utils.random(32).hex(),
    #         }
    #         result = coll.insert_one(data)
    #         if result:
    #             return True
    #         else:
    #             return False
    #     except Exception as err:
    #         print("An exception occurred :", err)
    #         return False

    # def modUser(chkUser, appPass, newAppPass, pin, newPin):
    #     try:
    #         dbr = dataBase.conf("write")
    #         rcol = dbr["userLogins"]
    #         data = rcol.find_one_and_update({"username": chkUser})
    #         if data:
    #             update = rcol.findOne({}, notused.getUserCreds())
    #             return update.AFTER
    #     except Exception as e:
    #         print("An exception occurred :", e)
    #         return Fa

# authSource=the_database&authMechanism=SCRAM-SHA-256"


class q:
    def __init__(self, user):
        self.query = None
        self.user = None

    def findUser(self):
        return {"_id": 0, "userId": 1}

    def getUserCreds():
        return {"_id": 0, "userId": 1, "password": 1, "pinCode": 1}

    def find_one_and_update():
        return "({'username': chkUser}, { '$set': { 'appPass': newAppPass, 'pin': newPin}})"

    def insert_one():
        record = '{"userId": fuserId, "password": fpasswd, "pin_code": fpinCode, "NickName": fnickName}'
        return record

    def find_one_and_update():
        return '{"reg_data.userId": user},  { "$set": {"session_data.session_id": session_id, "data": data, "lifetime": lifetime, "ttl": ttl}}'