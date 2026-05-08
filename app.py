from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Lala Bot is Running!'

def run():
    # Render-এর জন্য পোর্ট সেটআপ
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()

if __name__ == "__main__":
    keep_alive()
    # আপনার বটের মেইন ফাইল রান করার কমান্ড
    # নিশ্চিত করুন আপনার ফাইলের নাম main.py
    os.system("python3 main.py")
