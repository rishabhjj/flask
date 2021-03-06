from flask import Flask , jsonify ,request
import logging
from flask_restful import Resource,Api

application = Flask(__name__)
api = Api(application)

@application.route('/')
def hello():
    return "Welcome to the app"

@application.route('/json')
def jsonfun():
    return {"app": "Your first json response"}

@application.route('/method', methods=['GET','POST'])
def method():
    if (request.method == 'POST'):
        payload = {'requestType': 'Post type request'}
        return payload,201
    else:
        return {'about': 'using get clas'}

@application.route('/mul/<int:num>', methods=['GET'])
def last(num):
    # to access request url use: request.url
    # to use query params use: request.args.get('param') [all - request.query_string]
    param = request.args.get('param')
    if param :
        print(param)
    return {"request param is " : "num"}

class HelloWorld(Resource):
    def get(self):
        return {'about': 'using get clas'}

    def post(self):
        return {'about': 'using post class'}

class Multi(Resource):
    def get(self,num):
        return {'result' : num}

api.add_resource(HelloWorld,'/last')
api.add_resource(Multi,'/muli/<int:num>')

if __name__ == '__main__':
    application.run(debug=True)
    logging.info("App started")
