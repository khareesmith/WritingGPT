from flask import Flask, render_template, request, jsonify
from Writingteam import draft_blog_post, edit_blog_post

import Inputs
import os

app = Flask(__name__)

@app.route('/draft', methods=['POST'])
def draft():
    data = request.get_json()
    writerType = data.get('writerType', '')
    topic = data.get('topic', '')
    keywords = data.get('keywords', [])
        
    draft_output = draft_blog_post(writerType, topic, keywords)
    f = open(os.path.realpath(os.path.join(os.path.dirname(__file__), 'Outputs', 'blog_post_draft.txt')), 'w')
    f.write(draft_output)
    f.flush()
        
    return jsonify({"draft" : draft_output})

@app.route('/edit', methods=['POST'])
def edit():
    data = request.get_json()
    editor_type = data.get('editor_type', '')
    draft_received = data.get('draft', '')
    editor_notes = edit_blog_post(draft_received, editor_type)
    f = open(os.path.realpath(os.path.join(os.path.dirname(__file__), 'Outputs', 'editor_notes.txt')), 'w')
    f.write(editor_notes)
    f.flush()
    
    return jsonify({"edit" : editor_notes})

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)