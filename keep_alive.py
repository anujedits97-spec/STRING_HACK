import os
from threading import Thread
from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "SESSION INFO BOT is running!", 200

@app.get("/health")
def health():
    return {"status": "ok"}, 200

def _run():
    port = int(os.environ.get("PORT", 10000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False
    )

def keep_alive():
    Thread(target=_run, daemon=True).start()
