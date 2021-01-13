from flask import Flask, request, jsonify, Response, send_from_directory, send_file
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename
import pymongo, os
from google.oauth2 import id_token
from google.auth.transport import requests

UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/grafitisdb"
app.config['UPLOAD_FOLDER']  = UPLOAD_FOLDER
#mongo = PyMongo(app)

url_mongo_atlas = "mongodb+srv://admin:admin@cluster0.wepwf.mongodb.net/prueba?retryWrites=true&w=majority"
client = pymongo.MongoClient(url_mongo_atlas)
mongo = client.get_database('grafitis')



@app.route('/songs', methods=['GET'])
def get_usuarios():
    songs = mongo.db.songs.find()
    response = json_util.dumps(songs)
    return Response(response, mimetype='application/json')

