import logging

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
        resp = {}
        try:
            req_body = request.get_json(force=True)
            if user_collection.count_documents(req_body)==0 and re.fullmatch(regex,req_body['username']):

                user_collection.insert_one(req_body) 
            else:
                print("dfghjk")


            status = {
                "statusCode":"200",
                "statusMessage":"Success"

            }
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        resp["status"] =status
        return resp

    @endpoints.route('/signin',methods=['POST'])
    def signin():
        resp={}
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
            status = {
                "statusCode":"200"

            }
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400"
            }
        resp["status"] =status
        return resp

    return endpoints
