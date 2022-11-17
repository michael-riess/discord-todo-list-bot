from flask import Flask
from threading import Thread

app = Flask('')

# --------------------------------------------------------
# handlers
# --------------------------------------------------------

@app.route('/')
def home():
    return "Todo List Bot is live!"


# ========================================================
# Initialize server
# ========================================================
def run():
    app.run(host='0.0.0.0', port=8080)

# ========================================================
# Initialize server thread
# ========================================================
def keep_alive():
    thread = Thread(target=run)
    thread.start()