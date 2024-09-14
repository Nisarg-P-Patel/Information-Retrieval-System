# Dimensionality Reduction using Singular Value Decomposition (SVD)

## Aim
The goal of this project is to explore dimensionality reduction techniques using Singular Value Decomposition (SVD). This technique is applied to a dataset of press releases from the Department of Justice (2009-2018) to reduce the dimensionality of the TF-IDF representation and improve the performance of information retrieval systems.

## Features
- **Text Preprocessing**: Implement techniques such as lowercasing, tokenization, stop word removal, and stemming to prepare text data for analysis.
- **TF-IDF Vectorization**: Generate TF-IDF vectors for the corpus, allowing for a compact representation of the textual data.
- **SVD Implementation**: Apply SVD to reduce the dimensionality of the TF-IDF matrix, creating a lower-dimensional representation of the data.
- **Concept Space**: Explore the concept space created by SVD to understand relationships between documents and queries.
- **Similarity Calculation**: Calculate similarities between documents and queries in the reduced-dimensional space.

## Packages Used
- **NLTK**: For natural language processing tasks such as tokenization and stemming.
- **Scikit-learn**: For TF-IDF vectorization and dimensionality reduction using SVD.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.

## Installation
To run this project, you need to have Python installed along with the required libraries. You can install the necessary packages using pip:

```bash
pip install nltk scikit-learn pandas numpy
