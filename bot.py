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

bot = telegram.Bot(token=BOT_TOKEN)

app = Flask(__name__)

@app.route('/')
def index():
    return '.'

@app.route(f'/{BOT_TOKEN}')
def process_message():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id    
    bot.sendMessage(chat_id=chat_id, text="HELLO", reply_to_message=msg_id)

    return 'ok'

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook(f'{BOT_URL}{BOT_TOKEN}')

    if s:
        return "SETUP OK"
    else:
        return "SETUP FAILED"

if __name__ == '__main__':
    app.run(threaded=True)
    app.debug = True
