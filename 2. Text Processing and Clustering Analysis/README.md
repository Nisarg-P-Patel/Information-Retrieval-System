# Text Processing and Clustering Analysis

## Objective
This project performs text processing and clustering analysis on a set of documents. The main objectives include:
- Tokenizing and preprocessing textual data (removing stop words, stemming).
- Creating a word-document matrix to analyze word frequencies.
- Visualizing word frequencies using histograms and word clouds.
- Performing clustering on the documents using cosine similarity and generating dendrograms.
- Calculating TF-IDF values for documents and queries for information retrieval.

## Features
- **Text Preprocessing**: Tokenization, stop words removal, and stemming.
- **Word Frequency Analysis**: Count and visualize frequencies of words across documents.
- **Word Cloud Visualization**: Generate a word cloud to visualize the most common words.
- **Clustering**: Use hierarchical clustering to group similar documents and visualize the results with a dendrogram.
- **TF-IDF Calculation**: Compute the TF-IDF representation of documents and queries for search functionality.
- **Cosine Similarity**: Compare the similarity of a user query against the set of documents.

## Requirements
- Python 3.x
- NLTK library
- Pandas
- Matplotlib
- WordCloud
- NumPy
- SciPy
- Scikit-learn

You can install the required libraries using pip:
```bash
pip install nltk pandas matplotlib wordcloud numpy scipy scikit-learn
