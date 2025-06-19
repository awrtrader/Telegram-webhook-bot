from flask import Flask, request
import telebot

# Telegram Bot Token
TOKEN = "7291104027:AAGzGCJ2kiqb-HUl0ZtiRl3_ADiV6eOqTHs"
bot = telebot.TeleBot(TOKEN)

# Flask app setup
app = Flask(__name__)

# Telegram Chat ID
CHAT_ID = "6828336192"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    try:
        pair = data.get('pair', 'EUR/USD')
        action = data.get('action', 'BUY')
        timeframe = data.get('timeframe', '1m')
        entry = data.get('entry', '1.07345')
        confidence = data.get('confidence', 'High')

        message = f"""📢 *New Signal Alert*
📊 Pair: `{pair}`
🕒 Timeframe: `{timeframe}`
📈 Action: *{action}*
🎯 Entry: `{entry}`
✅ Confidence: *{confidence}*"""

        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")
        return "Signal sent", 200
    except Exception as e:
        return str(e), 400

@app.route('/')
def home():
    return "👋 Webhook is running on Railway."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
