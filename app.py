from flask import Flask, request, jsonify, render_template
import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

app = Flask(__name__)

# Load tokenizer and model
print('loading tokenizer')
tokenizer = PegasusTokenizer.from_pretrained('./pegasus-samsum/checkpoint-920')
print('loading model')
model = PegasusForConditionalGeneration.from_pretrained('./pegasus-samsum/checkpoint-920')
print('model state dictionary')
model.load_state_dict(torch.load('model_state_dict.pth', map_location=torch.device('cpu')))
print('loaded successfully')
model.eval()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    tokens = tokenizer(text, truncation=True, padding='longest', return_tensors="pt")
    summary_ids = model.generate(tokens['input_ids'], max_length=150, num_beams=5, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
