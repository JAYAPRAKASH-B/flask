from flask import Flask,request
from flask_restful import reqparse, Resource, Api
app = Flask(__name__)
api = Api(app)

class Do(Resource):
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', location=['headers', 'values'])
        args = parser.parse_args()
        return args
api.add_resource(Do,'/parse')

if __name__ == '__main__':
    app.run(debug=True)