import flask
import pymongo

app = flask.Flask(__name__)

uri = 'mongodb+srv://admin:admin@cluster0.wepwf.mongodb.net/prueba?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)
mongo = client.get_database('prueba')

@app.route('/', methods=['GET'])
def nothing():
    return "Hello world"

@app.route('/songs', methods=['GET'])
def fun():
    songs = mongo.db.songs.find()
    response = flask.jsonify(songs)
    return Response(response, mimetype='application/json')