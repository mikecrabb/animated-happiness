from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}

@app.before_request
def log_request():
    print(f"Incoming request: {request.method} {request.path}")

api.add_resource(HelloWorld, "/")


if __name__ == '__main__':
    app.run(debug=True)



