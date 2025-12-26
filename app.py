# app.py
from flask import Flask, request, jsonify
import html2text
import os

app = Flask(__name__)

@app.route('/html2text', methods=['POST'])
def convert_html():
    try:
        data = request.get_json()
        html_content = data.get('html', '')
        
        # Configure html2text options
        h = html2text.HTML2Text()
        h.ignore_links = data.get('ignore_links', False)
        h.body_width = data.get('body_width', 0)
        
        # Convert HTML to text
        text_output = h.handle(html_content)
        
        return jsonify({'text': text_output, 'success': True})
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='::', port=port)