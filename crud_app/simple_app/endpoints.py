


from flask_pymongo import pymongo
from flask import jsonify, request
from matplotlib.style import use
import pandas as pd
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


con_string = "mongodb+srv://kiran:kiran@cluster0.9bnuchr.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_string)

db = client.get_database('example')

user_collection = pymongo.collection.Collection(db, 'collectionsexample') #(<database_name>,"<collection_name>")
print("MongoDB connected Successfully")


def project_api_routes(endpoints):
    @endpoints.route('/register-user', methods=['POST'])
    def register_user():
        msg=''
        
        
        
        
        try:
            req_body = request.get_json(force=True)
            var=req_body['username']
            if (not user_collection.find_one({"username":var})) and re.fullmatch(regex,req_body['username']):
                
                  
                user_collection.insert_one(req_body) 
                msg='SignUp Successful'
            else:
                msg='User Already Exists'
      
        except Exception as e:
            print(e)
            msg='Sign Up Unsuccessful'
        return {'resp': msg}

    @endpoints.route('/signin',methods=['POST'])
    def signin():
        msg=''
        try:
            data=request.get_json(force=True)
            print(data)
            var=data['username'] 
            var2=data['password']
            out=user_collection.find_one({"username":var,"password":var2})
            u1=out.get('username')
            p1=out.get('password')
            print("**",u1," ",p1)
            print(data,"hibaaaaaa")
            msg='Login Successful'
        except Exception as e:
            print(e)
            msg='Unsuccessful'
        return {'resp': msg}

    return endpoints
