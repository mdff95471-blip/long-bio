from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Lala Bot is Running!'

def run():
    # Render সাধারণত পোর্ট ৮০০০ বা ১০০০০ ব্যবহার করে
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    # আপনার বটের মূল ফাইলটি (main.py) রান করার কমান্ড
    os.system("python3 main.py")
