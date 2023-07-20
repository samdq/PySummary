from flask import Flask, request, jsonify, render_template
from summarization.summarizer import Summarizer

app = Flask(__name__)

# Load summarizer based on the configured method
summarizer = Summarizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()

        if 'text' not in data:
            return jsonify({'error': 'Text content is missing in the request'}), 400

        text = data['text']
        length = int(data.get('length', 5))
        focus = data.get('focus', 'sentences')

        summary = summarizer.generate_summary(text, length, focus)

        return jsonify({'summary': summary})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
