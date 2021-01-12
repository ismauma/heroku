import flask
import pymongo

app = flask.Flask(__name__)

uri = 'mongodb+srv://admin:admin@cluster0.wepwf.mongodb.net/prueba?retryWrites=true&w=majority'

@app.route('/', methods=['GET'])
def nothing():
    return "Hello world"

@app.route('/songs', methods=['GET'])
def fun():
    client = pymongo.MongoClient(uri)

    db = client.get_default_database()
    songs = db.songs
    return flask.jsonify(songs)