from flask import Flask, render_template, request, jsonify
from Writingteam import draft_blog_post
import logging

logging.basicConfig(level=logging.DEBUG)

import Inputs
import os

app = Flask(__name__)

@app.route('/draft', methods=['POST'])
def draft():
    
    if request.method == 'POST':
        data = request.get_json()
        writerType = data.get('writerType', '')
        topic = data.get('topic', '')
        keywords = data.get('keywords', [])
        
        draft_output = draft_blog_post(writerType, topic, keywords)
        return jsonify({"draft" : draft_output})

    return render_template('draft.html')

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)