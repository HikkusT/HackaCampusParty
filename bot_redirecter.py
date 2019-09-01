import requests
import pyrebase
from flask import Flask, jsonify, request

app = Flask(__name__)

config = {
  "apiKey": "AIzaSyDLWP-B57TLt9tBqHkz5oi-N0gtSBtJn7w",
  "authDomain": "hackacampusparty.firebaseapp.com",
  "databaseURL": "https://hackacampusparty.firebaseio.com/",
  "storageBucket": "hackacampusparty.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route('/send_message', methods=['POST'])
def send_message():
  content = request.get_json()
  text = content.get('text')
  chat_id = get_chat_id(content.get('name'))
  send_message(text, chat_id)
  return '', 204

key = "841166799:AAG-HKf9gZKLLmaG6mp_4dgn4NNS2NIRRN8"

def send_message(message, chatid):
    url_to_send = "https://api.telegram.org/bot" + key + "/sendMessage"
    data = {'chat_id': chatid,
            'text' : message}

    r = requests.post(url = url_to_send, data = data)

def get_chat_id(name):
    return db.child(name).child("chat_id").get().val()

# def get_users_from_place(db, place):

if __name__ == '__main__':
    app.run()