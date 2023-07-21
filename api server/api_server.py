from flask import Flask, json, jsonify
project_db = [{"id" : 1, "name" : "pygame"}, {"id" : 2 , "name" : "webserver"}]

api = Flask(__name__)
@api.route('/project_db/<int:id>', methods = ["GET", "POST"])
def returnproject(id): 
        return jsonify(project_db[id-1])

@api.route()

if __name__ == '__main__':
    api.run(port = 80,host = '0.0.0.0')