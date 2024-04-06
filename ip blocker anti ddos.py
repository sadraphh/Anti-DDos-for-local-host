from flask import Flask, request, jsonify
from collections import defaultdict
import time

app = Flask(__name__)
ip_counter = defaultdict(int)

@app.before_request
def limit_ip_requests():
    ip = request.remote_addr
    current_time = time.time()

    
    ip_counter[ip] += 1

   
    if ip_counter[ip] > 100: 
        return jsonify({'message': 'You have sent too many requests. Please try again later.'}), 429

    
    for key in list(ip_counter.keys()):
        if current_time - key > 60:
            del ip_counter[key]

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)