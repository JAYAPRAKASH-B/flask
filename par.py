from flask_restful import reqparse,Resource, Api
from flask import Flask

app = Flask(__name__)
api = Api(app)
class parse(Resource):
    def get(self):
        task = {'rate': '10'}
        return task
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('foo', type=int)
        args = parser.parse_args()
        return args
        
api.add_resource(parse, '/parse')
if __name__ == '__main__':
    app.run(debug=True)
