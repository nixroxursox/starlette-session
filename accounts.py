from db.database import dataBase
from decouple import config
from starlette.applications import Starlette
from starlette.requests import Request as request, HTTPConnection
from starlette.responses import Response as response
import nacl
from nacl import pwhash, utils, encoding
from nacl.encoding import binascii, HexEncoder
import datetime
from starlette.types import Message, Receive, Scope, Send
import asyncio
from urllib.parse import quote_plus
import pprint
import uuid
from typing import List, Optional
 


class UserData:
    def __init__(self, *args, **kwargs) -> None:
        self.method = 'read'
        # self.userId:str = kwargs.get(user)
        # self.password: str = kwargs.get(pw)
        # self.pin: int = kwargs.get(pi)
        # self.nname = kwargs.get(nname)
        # self.st = kwargs.get(st)
        # self.pgp = kwargs.get(pgp)
        self.col = self._get_pyDb(self.method).eCom.userData
        self.session_id: Optional[int] = None


    def __call__(self, user):
        self.userId = user
        return self.py_userid(self.userId)

    @staticmethod
    async def _get_motorDb(method):
        """ internal method to get database """
        cl = dataBase.motorConf('cl', method)
        db = cl['eCom']
        return db


    @staticmethod
    def _get_pyDb(method):
        """ internal method to get database """
        cl = dataBase.pyMongoConf('cl', method)
        db = cl['eCom']
        return db


    def _getMasterId(self, method):
        """ find and create UID for new user object """
        db = UserData._get_pyDb(method)
        col =  db['userData']
        masterId = col.find({},{'uid'}).sort('uid',-1).limit(1)
        uid = masterId[0]
        return uid


    @staticmethod
    def py_createUser(user, pw, pi: int, nname, st, pgp):
        """ add a new user to the application """
        user = user
        pi1 = bytes(pi, 'UTF-8')
        pinCode = pwhash.scryptsalsa208sha256_str(pi1)
        pw1 = bytes(pw, 'UTF-8')
        pWord = pwhash.argon2id.str(pw1)
        nick = nname
        statement = st
        crDate = datetime.datetime.now()
        is_active = True
        i = UserData._getMasterId("i","read")
        u = int(i["uid"])
        uid = u + 1
        pgp = pgp
        client = dataBase.pyMongoConf('client','write')
        col =  client['eCom']['userData']
        result = col.insert_one({'uid': uid, 'reg_data': {'userId': user,'password': pWord, 'pinCode': pinCode, 'nname': nick, 'pState': statement, 'pgpKey': pgp, 'memberSince': crDate,  'isActive': is_active}})
        if result:
            created = True
            return created
        created = False
        return created


    @staticmethod
    async def v_UserId(user):
        client = dataBase.motorConf('client','read')
        col = client['eCom']['userData']
        q = await col.find_one({'reg_data.userId': user})


    @staticmethod
    def py_userid(user):
        client = dataBase.pyMongoConf('client','read')
        col = client['eCom']['userData']
        q = col.find_one({'reg_data.userId': user}, {'reg_data': {'userId': 1}})
        if q:
            return True
        return False


    async def v_Pass(self, userId, pWord):
        client = dataBase.pyMongoConf('client','read')
        lp = cl.get_io_loop()
        uv = lp.run_until_complete((self.find_one_v_UserId(userId)))
        if uv is True:
            pw = cl.find_one({'reg_data.userId': userId}, {'reg_data': {'userId': 1, 'password': 1, 'pinCode': 1}})
            vp = pwhash.argon2id.verify(b'p["password"]', b'pWord')
            if vp is True:
                return True
            return False
        return False


    @staticmethod
    def py_v_Pass(user, pw) -> bool:
        client = dataBase.pyMongoConf('client','read')
        col = client['eCom']['userData']
        q = col.find_one({'reg_data.userId' : user}, {'_id': 0, 'reg_data.userId': 1, 'reg_data.password': 1})
        if q:
            p = q['reg_data']
            pw1 = pw.encode('UTF-8')
            vp = pwhash.argon2id.verify(p['password'], pw1)
            if vp is True:
                return True
        return False


    @staticmethod
    async def v_PinCode(userId, pinCode):
        db = UserData._get_pyDb("read")
        col =  db['userData']
        e = UserData.v_UserId
        if e is True:
            pi = await col.find_one({}, {'reg_data': {'userId': userId, 'pinCode': pinCode}})
            loop = pi.get_io_loop()
            loop.run_until_complete(pi)
            pi.result()
            vpi = pwhash.verify_scryptsalsa208sha256(pi["pinCode"], b'pinCode')
            if vpi is True:
                return True, userId
            return False
        return False


    @staticmethod
    def py_v_Pin(user, pin) -> bool:
        client = dataBase.pyMongoConf('client','read')
        col = client['eCom']['userData']
        q = col.find_one({'reg_data.userId' : user}, {'_id': 0, 'reg_data.userId': 1, 'reg_data.pinCode': 1})
        if q:
            p = q['reg_data']
            pi1 = bytes(pin, 'UTF-8')
            vpi = pwhash.verify_scryptsalsa208sha256(p['pinCode'], pi1)
            if vpi is True:
                return True
        return False
# col.find_one({}, {'reg_data': {'userId': user, 'password': 1}})

    @staticmethod
    async def is_authenticated():
        """ check whether a user session exists and is authenticated """
        return True

    @staticmethod
    async def get_statement(userId):
        user = userId
        db = await UserData._get_pyDb("read")
        col =  db.eCom.userData
        query = "{}, {'reg_data': {'userId': user, 'pState': 1}}"
        s = await col.find_one(query)
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
            return True
        return False



    def py_get_session_m_id(self, user):
        user = user
        client = dataBase.pyMongoConf('client','read')
        col = client['eCom']['userData']
        q = col.find_one({'reg_data.userId' : user}, {'_id': 0, 'session_data.session_id': 1, 'session_data.metadata.lifetime' : 1})
        if q:
            sk = q['session_data']
            return sk['session_id']
        

    @staticmethod
    def gen_session_m_id(user, client_ip):
        raw = nacl.utils.random(32)
        seed = nacl.utils.randombytes_deterministic(32, raw, encoder=encoding.HexEncoder)
        ip_addr = client_ip.replace('.','-')
        sess_encoded = user + "-" + ip_addr + str(binascii.b2a_base64(seed), 'UTF-8')
        return sess_encoded


    # @staticmethod
    # async def session_manager(user, session_id: Optional[bin] = None):
    #     if session_id is None:
    #         session_id = UserData.gen_session_m_id(user)
    #     client = dataBase.pyMongoConf('client','write')
    #     with client.start_session(causal_consistency=True) as session:
    #         col = client['eCom']['userData']
    #         user_id = col.find_one({},{'reg_data.userId': user, '_id': 0}, session=session)
    #         record = {
    #             'session_data.session_id': session_id,
    #             'session_data.max_age':  max_age,
                
    #         }
    #         result = col.insert_one(record, session=session)
    #         session.commit()
    #         if result['acknowledged']:
    #             return True
    #     return False
                
        
    
#     function getNextSequenceValue(masterId){
#    var sequenceDocument = db.counters.findAndModify({
#       query:{_id: masterId },
#       update: {$inc:{sequence_value:1}},
#       new:true
#    });
#    return sequenceDocument.sequence_value;

#    db.userData.insert({reg_data: {'masterId':getNextSequenceValue("masterId")
#                                      )

# }
# db.find_one_and_update({})


class motorLoop:
    def __init__(self, query):
        self.query = query


    @staticmethod
    async def readQuery(query):
        client = dataBase.usConf('cl','read')
        lp = client.get_io_loop()
        return lp.run_until_complete(query)

    @staticmethod
    async def writeQuery(query):
        lp = client.get_io_loop()
        a = lp.run_until_complete(query)
        return a

#     var docId = changeEvent.fullDocument._id;

#     const countercollection = context.services.get("userData").db(changeEvent.ns.db).collection("counters");
#     const studentcollection = context.services.get("userData").db(changeEvent.ns.db).collection(changeEvent.ns.coll);

#     var counter = countercollection.findOneAndUpdate({_id: changeEvent.ns },{ $inc: { seq_value: 1 }}, { returnNewDocument: true, upsert : true});
#     var updateRes = studentcollection.updateOne({_id : docId},{ $set : {masterId : counter.seq_value}});

#     console.log(`Updated ${JSON.stringify(changeEvent.ns)} with counter ${counter.seq_value} result : ${JSON.stringify(updateRes)}`);
#     };

# db.find().sort({"reg_data.masterId":-1}).limit(1).toArray().map(function(u){return u.reg_data.masterId})

# db.find({"reg_data.masterId":-1}.limit(1))
