from flask import Flask, request
import telegram
import os

# Get secrets from enviroment variable

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_URL = os.getenv("BOT_URL")

if not BOT_TOKEN:
    print("BOT_TOKEN do not defined")
    exit()

if not BOT_URL:
    print("BOT_URL do not defined")
    exit()

telegram_bot = telegram.Bot(token=BOT_TOKEN)

app = Flask(__name__)

@app.route('/')
def index():
    return '.'

@app.route(f'/{BOT_TOKEN}', methods=['GET', 'POST'])
def process_message():
    update = telegram.Update.de_json(request.get_json(force=True), telegram_bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id    
    telegram_bot.sendMessage(chat_id=chat_id, text="Hello World!")
    return 'ok'

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    if telegram_bot.setWebhook(f'{BOT_URL}{BOT_TOKEN}'):
        return "OK"
    else:
        return "FAILED"

if __name__ == '__main__':
    app.run(threaded=True)
