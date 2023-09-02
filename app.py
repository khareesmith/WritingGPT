from flask import Flask, render_template, request, jsonify
from Writingteam import draft_blog_post, edit_blog_post, seo_notes, photo_suggestions, final_blog_post
import os
import sys
from pathlib import Path

app = Flask(__name__)

@app.route('/draft', methods=['POST', 'GET'])
def draft():
    data = request.get_json()
    writerType = data.get('writerType', '')
    topic = data.get('topic', '')
    keywords = data.get('keywords', [])
        
    draft_output = draft_blog_post(writerType, topic, keywords)
    
    if getattr(sys, 'frozen', False):
    # The application is running as a bundled executable
        app_path = sys.executable
        p = Path(app_path).parents[1]
        
    else:
        # The application is running as a standard Python script
        app_path = os.path.dirname(os.path.abspath(__file__))
        p = Path(app_path)
        
    application_path = p.joinpath('Outputs/')
    draft_file_path = os.path.join(application_path, 'blog_post_draft.txt')
    print('Writing draft to ' + draft_file_path)
    f = open(draft_file_path, 'w')
    f.write(draft_output)
    f.flush()
        
    return jsonify({"draft" : draft_output})

@app.route('/edit', methods=['POST'])
def edit():
    data = request.get_json()
    editor_type = data.get('editor_type', '')
    draft_received = data.get('draft', '')
    editor_notes = edit_blog_post(draft_received, editor_type)
    
    if getattr(sys, 'frozen', False):
    # The application is running as a bundled executable
        app_path = sys.executable
        p = Path(app_path).parents[1]

    else:
        # The application is running as a standard Python script
        app_path = os.path.dirname(os.path.abspath(__file__))
        p = Path(app_path)
    
    application_path = p.joinpath('Outputs/')
    edit_file_path = os.path.join(application_path, 'editor_notes.txt')
    print('Writing edits to ' + edit_file_path)
    f = open(edit_file_path, 'w')
    f.write(editor_notes)
    f.flush()
    
    return jsonify({"edit" : editor_notes})

@app.route('/seo', methods=['POST'])
def seo():
    data = request.get_json()
    keywords = data.get('keywords', [])
    draft_received = data.get('draft', '')
    seoNotes = seo_notes(draft_received, keywords)
    
    if getattr(sys, 'frozen', False):
    # The application is running as a bundled executable
        app_path = sys.executable
        p = Path(app_path).parents[1]

    else:
        # The application is running as a standard Python script
        app_path = os.path.dirname(os.path.abspath(__file__))
        p = Path(app_path)
    
    application_path = p.joinpath('Outputs/')
    seo_file_path = os.path.join(application_path, 'seo_notes.txt')
    print('Writing seo notes to ' + seo_file_path)
    f = open(seo_file_path, 'w')
    f.write(seoNotes)
    f.flush()
    
    return jsonify({"seo" : seoNotes})

@app.route('/photo', methods=['POST'])
def photo():
    data = request.get_json()
    draft_received = data.get('draft', '')
    photoNotes = photo_suggestions(draft_received)
    
    if getattr(sys, 'frozen', False):
    # The application is running as a bundled executable
        app_path = sys.executable
        p = Path(app_path).parents[1]

    else:
        # The application is running as a standard Python script
        app_path = os.path.dirname(os.path.abspath(__file__))
        p = Path(app_path)
    
    application_path = p.joinpath('Outputs/')
    photo_file_path = os.path.join(application_path, 'photos.txt')
    print('Writing photo suggestions to ' + photo_file_path)
    f = open(photo_file_path, 'w')
    f.write(photoNotes)
    f.flush()
    
    return jsonify({"photo" : photoNotes})

@app.route('/final', methods=['POST'])
def prod():
    data = request.get_json()
    draft_received = data.get('draft', '')
    edit_received = data.get('edit', '')
    seo_received = data.get('seo', '')
    photo_received = data.get('photo', '')
    final_output = final_blog_post(draft_received, edit_received, seo_received, photo_received)
    
    if getattr(sys, 'frozen', False):
    # The application is running as a bundled executable
        app_path = sys.executable
        p = Path(app_path).parents[1]
    
    else:
        # The application is running as a standard Python script
        app_path = os.path.dirname(os.path.abspath(__file__))
        p = Path(app_path)
    
    application_path = p.joinpath('Outputs/')
    final_file_path = os.path.join(application_path, 'final_blog_post.txt')
    print('Writing final post/article to ' + final_file_path)
    f = open(final_file_path, 'w')
    f.write(final_output)
    f.flush()
    
    return jsonify({"final" : final_output})

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)