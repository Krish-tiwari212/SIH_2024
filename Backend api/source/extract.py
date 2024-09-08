import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
import re
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Function to scrape data
def scrape_data():
    url = 'https://doj.gov.in'  # Replace with the URL you want to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the data you need
    # Example: Extracting all paragraphs
    data = []
    for p in soup.find_all('p'):
        data.append(p.get_text())

    return data

# Function to store data in the database
def store_data(data):
    conn = sqlite3.connect('scraped_data.db')
    c = conn.cursor()

    # Create table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS scraped_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Insert data into the table
    for item in data:
        c.execute('INSERT INTO scraped_data (content) VALUES (?)', (item,))

    conn.commit()
    conn.close()

# Function to clean text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = re.sub(r'\[.*?\]', '', text)  # Remove text in brackets
    return text.strip()

# Function to chunk text
def chunk_text(text, chunk_size=30):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield ' '.join(words[i:i + chunk_size])

# Main function
def main():
    data = scrape_data()
    store_data(data)

    # Combine all data into a single text
    combined_text = ' '.join(data)

    # Clean the extracted text
    cleaned_text = clean_text(combined_text)

    # Chunk the cleaned text
    chunked_text = list(chunk_text(cleaned_text))

    # Load pre-trained sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Convert chunks to embeddings
    embeddings = model.encode(chunked_text)

    # Save the embeddings to a .npy file
    with open('embeddings.npy', 'wb') as f:
        np.save(f, embeddings)

    # Save the chunked text
    with open('chunked_text.npy', 'wb') as f:
        np.save(f, chunked_text)

    # Create a FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Save the FAISS index
    faiss.write_index(index, 'faiss_index.index')

    print("Data scraped, stored, and embeddings saved successfully.")

if __name__ == '__main__':
    main()
