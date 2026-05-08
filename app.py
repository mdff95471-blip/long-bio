import os
import subprocess
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# আপনার আগে পাঠানো index.html এর ডিজাইন এখানে থাকবে
HTML_CODE = """
<!DOCTYPE html>
<html>
<head>
    <title>LALA ADMIN - FF BOT</title>
    <style>
        body { background: #0b0e14; color: #ff4757; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding-top: 50px; }
        .box { background: #161b22; width: 320px; margin: auto; padding: 30px; border-radius: 15px; border: 2px solid #ff4757; box-shadow: 0 0 20px #ff475755; }
        input { width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: 1px solid #30363d; background: #0d1117; color: white; box-sizing: border-box; }
        button { width: 100%; padding: 12px; background: #ff4757; border: none; border-radius: 8px; color: white; font-weight: bold; cursor: pointer; transition: 0.3s; }
        button:hover { background: #ff6b81; transform: scale(1.02); }
        #log { margin-top: 20px; font-size: 14px; color: #8b949e; }
    </style>
</head>
<body>
    <div class="box">
        <h2 style="margin-top: 0;">FF BOT CONTROL</h2>
        <input type="text" id="uid" placeholder="Enter Game UID">
        <input type="password" id="pass" placeholder="Enter Password">
        <button onclick="runBot()">START BOT ONLINE</button>
        <p id="log">Status: Waiting...</p>
    </div>

    <script>
        async function runBot() {
            const uid = document.getElementById('uid').value;
            const password = document.getElementById('pass').value;
            const log = document.getElementById('log');

            if(!uid || !password) return alert("Please fill all fields!");

            log.innerText = "Connecting to Server...";
            
            try {
                const response = await fetch('/execute', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ uid, password })
                });
                const data = await response.json();
                log.innerText = "Server Response: " + data.message;
            } catch (err) {
                log.innerText = "Error connecting to server!";
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/execute', methods=['POST'])
def execute():
    data = request.json
    uid = data.get('uid')
    password = data.get('password')

    # এখানে subprocess ব্যবহার করে আপনার main.py রান করা হবে
    # এটি ব্যাকগ্রাউন্ডে কমান্ড চালাবে: python main.py --uid UID --pass PASSWORD
    try:
        # আপনার main.py ফাইলটি যদি ইনপুট নিতে পারে তবে এভাবে কমান্ড পাঠানো যায়
        subprocess.Popen(['python', 'main.py', uid, password])
        return jsonify({"status": "success", "message": f"Bot started for UID: {uid}"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))