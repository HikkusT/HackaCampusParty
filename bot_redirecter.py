import requests

key = "841166799:AAG-HKf9gZKLLmaG6mp_4dgn4NNS2NIRRN8"

def send_message(message, chatid):
    url_to_send = "https://api.telegram.org/bot" + key + "/sendMessage"
    data = {'chat_id': chatid,
            'text' : message}

    r = requests.post(url = url_to_send, data = data)

def main():
    send_message("Eu gosto de batata", 890335959)

if __name__ == '__main__':
    main()