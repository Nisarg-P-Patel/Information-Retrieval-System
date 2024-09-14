# Document Clustering using K-Means

## Aim
The goal of this project is to implement document clustering using the K-Means algorithm. The project focuses on clustering press releases from the Department of Justice between 2009 and 2018, utilizing TF-IDF vectorization and cosine similarity to analyze and group similar documents.

## Features
- **Text Preprocessing**: Implement techniques such as lowercasing, tokenization, stop word removal, and stemming to prepare the text for analysis.
- **TF-IDF Vectorization**: Generate TF-IDF vectors for the corpus, allowing for an efficient representation of the text data.
- **K-Means Clustering**: Apply the K-Means algorithm to cluster documents based on their TF-IDF representations.
- **Elbow Method**: Use the elbow method to determine the optimal number of clusters.
- **Cosine Similarity Calculation**: Compute cosine similarity to analyze the similarity between clustered documents.
- **Word Cloud Visualization**: Visualize the most common words in each cluster using word clouds.

## Packages Used
- **NLTK**: For basic text preprocessing.
- **Scikit-learn**: For generating TF-IDF matrices, K-Means clustering, and cosine similarity calculations.
- **Pandas**: For data manipulation and filtering.
- **Matplotlib**: For plotting graphs and visualizations.
- **WordCloud**: For generating word clouds.

## Installation
To run this project, you need to have Python installed along with the required libraries. You can install the necessary packages using pip:

```bash
pip install nltk scikit-learn pandas matplotlib wordcloud
