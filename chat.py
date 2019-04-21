import json
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)
@app.route('/', methods=['POST'])
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult')
    # return a fulfillment response
    return jsonify({'fulfillmentText':str(action)})
if __name__ == '__main__':
    app.run()