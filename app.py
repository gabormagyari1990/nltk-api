from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.summarize import summarize
import json

app = Flask(__name__)
CORS(app)

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/tokenize', methods=['POST'])
def tokenize():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        word_tokens = word_tokenize(text)
        sentence_tokens = sent_tokenize(text)
        
        return jsonify({
            "word_tokens": word_tokens,
            "sentence_tokens": sentence_tokens
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/pos-tag', methods=['POST'])
def pos_tagging():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        
        return jsonify({
            "pos_tags": [{"word": word, "tag": tag} for word, tag in pos_tags]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/ner', methods=['POST'])
def named_entity_recognition():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        named_entities = ne_chunk(pos_tags)
        
        # Convert tree to JSON-serializable format
        ne_list = []
        for chunk in named_entities:
            if hasattr(chunk, 'label'):
                entity = ' '.join(c[0] for c in chunk)
                ne_list.append({
                    "text": entity,
                    "type": chunk.label()
                })
        
        return jsonify({
            "named_entities": ne_list
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/sentiment', methods=['POST'])
def sentiment_analysis():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(text)
        
        return jsonify({
            "sentiment": sentiment_scores
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
