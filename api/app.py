from flask import Flask, request

from contracts.request_contracts import createMessageRequest
from contracts.response_contracts import getMessagesResponse
from database import create_message, get_messages

app = Flask(__name__)

@app.route('/')
def get_site():
    return 'Hello World' #send_file('homepage.html')

@app.route('/api/message', methods = ['POST'])
def post_message():
    message = createMessageRequest(**request.get_json())
    create_message(message.message, message.createdWhen, message.createdWho)
    return {"status": "success"}, 201


@app.route('/api/messages', methods = ['GET'])
def list_messages():
    messages = get_messages()
    response = getMessagesResponse(messages=messages).model_dump_json()
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)