from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import json
import requests
import sqlite3
from bs4 import BeautifulSoup
import re
from groq import Groq

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Load the embeddings and chunked text
with open('../embeddings.npy', 'rb') as f:
    embeddings = np.load(f)

with open('../chunked_text.npy', 'rb') as f:
    chunked_text = np.load(f, allow_pickle=True)

# Load the FAISS index
index = faiss.read_index('../faiss_index.index')

# Load pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to retrieve relevant chunks using FAISS
def retrieve_chunks(query, top_n=5):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_n)
    return [chunked_text[i] for i in indices[0]]

# Function to generate response using Groq API
def generate_response(query):
    # Retrieve relevant chunks
    relevant_chunks = retrieve_chunks(query)
    relevant_document = ' '.join(relevant_chunks)

    # Generate prompt
    prompt = f"""
    Remember you are a robot chatbot, do not add any extra information than what is given in the document.
    This is the recommended activity: {relevant_document}
    The user input is: {query}
    Compile a recommendation to the user based on the recommended activity and the user input.
    """
    key='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'
    client = Groq(api_key=key)
    completion = client.chat.completions.create(
        model="llama3-groq-70b-8192-tool-use-preview",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=0.65,
        stream=True,
        stop=None,
    )

    full_response = []
    for chunk in completion:
        if chunk.choices[0].delta.content:
            full_response.append(chunk.choices[0].delta.content)

    return ''.join(full_response)

@app.route('/api/generate', methods=['POST'])
def api_generate():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({'error': 'Query is required'}), 400

    response = generate_response(query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000)
