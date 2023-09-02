from db.database import dataBase
from decouple import config
from starlette.applications import Starlette
from starlette.requests import Request as request, HTTPConnection
from starlette.responses import Response as response
import nacl
from nacl import pwhash, utils, encoding
import datetime
from starlette.types import Message, Receive, Scope, Send
import asyncio
from urllib.parse import quote_plus
import multidict
from multidict import istr


class User:
    async def __init__(self, *args, **kwargs) -> None:
        self.userId:str = kwargs.get(user)
        self.password: istr = kwargs.get(pw)
        self.pin: int = kwargs.get(pi)
        self.nname = kwargs.get(nname)
        self.st = kwargs.get(st)
        self.pgp = kwargs.get(pgp)

    @staticmethod
    async def _getDb(method):
        """ internal method to get database """
        client = dataBase.usConf(method)
        db = client.eComData
        return db

    async def createUser(self, user, pw, pi, nname, st, pgp):
        """ add a new user to the application """
        user = user
        pinCode = pwhash.scryptsalsa208sha256_str(b'pi')
        nick = nname
        statement = st
        crDate = datetime.datetime.now()
        is_active = True
        i = self._getMasterId(User, "read")
        u = int(i["uid"])
        uid = u + 1
        pgp = 'pgp'
        client = self._getDb("write")
        col = client.userRegData
        # with client.start_session(causal_consistency=True) as session:
        #     with session.start_transaction():
        # id = col.find({},{'uid'}, session=session).sort('uid',-1).limit(1)
        result = col.insert_one({'uid': uid, 'reg_Data': {'pgpKey': pgp, 'userId': user,'passWord': passWord, 'pinCode': pinCode, 'nname': nick, 'pState': statement, 'memberSince': crDate,  'isActive': is_active}})
        if result:
            content = 'User Created'
            created = True
            return created, content
        content = 'Unable tp create User'
        created = False       
        return created, content

    async def _getMasterId(self, method):
        """ find and create UID for new user object """
        client = self._getDb(method)
        col = client.userRegData
        masterId = col.find({},{'uid'}).sort('uid',-1).limit(1)
        uid = masterId[0]
        return uid

    async def v_UserId(self, userId):
        """ Login check for existing user - also for registration """
        db = self._getDb("read")
        col = db.userRegData
        found = col.find({},{'reg_data': {'userId': userId}})
        if found:
            return True
        return False

    async def v_Pass(self, userId, password):
        db = self._getDb("read")
        col = db.userRegData
        e = self.v_UserId(userId)
        if e is True:
            p = col.find_one({}, {'reg_data': {'userId': userId, 'password': password}})
            vp = pwhash.argon2id.verify(p["passWord"], b'password')
            if vp is True:
                return True
            return False
        return False
        
    async def v_PinCode(self, userId, pinCode):
        db = self._getDb("read")
        col = db.userRegData
        e = self.v_UserId
        if e is True:
            pi = col.find_one({}, {'reg_data': {'userId': userId, 'pinCode': pinCode}})
            vpi = pwhash.verify_scryptsalsa208sha256(pi["pinCode"], b'pinCode')
            if vpi is True:
                return True
            return False
        return False

    @staticmethod
    async def is_authenticated():
        """ check whether a user session exists and is authenticated """
        return True

    @staticmethod
    async def get_statement(userId):
        user = userId
        db = User._getDb("read")
        col = db.eComData.userRegData
        query = "{}, {'reg_data': {'userId': user, 'pState': 1}}"
        s = col.find_one(query)
        if s:
            s0 = s["reg_data"]
            st = s0["pState"]
            return st
        return False

    async def v_Credential_Ver(self, userId, password, pinCode):
        user = self.v_UserId(userId)
        password = self.v_Pass(userId, password)
        pinCode = self.v_PinCode(userId, pinCode)
        if user is True and password is True and pinCode is True:
            return self.is_authenticated

        

        
            
#     function getNextSequenceValue(masterId){
#    var sequenceDocument = db.counters.findAndModify({
#       query:{_id: masterId },
#       update: {$inc:{sequence_value:1}},
#       new:true
#    });
#    return sequenceDocument.sequence_value;

#    db.userRegData.insert({reg_data: {'masterId':getNextSequenceValue("masterId")
#                                      )
                          
# }
# db.find_one_and_update({})



# exports = async function(changeEvent) {
#     var docId = changeEvent.fullDocument._id;
    
#     const countercollection = context.services.get("userRegData").db(changeEvent.ns.db).collection("counters");
#     const studentcollection = context.services.get("userRegData").db(changeEvent.ns.db).collection(changeEvent.ns.coll);
    
#     var counter = await countercollection.findOneAndUpdate({_id: changeEvent.ns },{ $inc: { seq_value: 1 }}, { returnNewDocument: true, upsert : true});
#     var updateRes = await studentcollection.updateOne({_id : docId},{ $set : {masterId : counter.seq_value}});
    
#     console.log(`Updated ${JSON.stringify(changeEvent.ns)} with counter ${counter.seq_value} result : ${JSON.stringify(updateRes)}`);
#     };

# db.find().sort({"reg_data.masterId":-1}).limit(1).toArray().map(function(u){return u.reg_data.masterId}) 

# db.find({"reg_data.masterId":-1}.limit(1))