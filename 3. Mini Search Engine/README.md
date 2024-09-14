# Mini Search Engine

## Aim
The goal of this project is to create a mini search engine that allows users to search for related plays and characters from a dataset based on TF-IDF vectorization and cosine similarity. The project focuses on the works of Shakespeare, where each document corresponds to a line spoken by a character (Player).

## Features
- **Text Preprocessing**: Implement techniques such as lowercasing, tokenization, stop word removal, and stemming to prepare the text for analysis.
- **TF-IDF Vectorization**: Generate TF-IDF vectors for the corpus, allowing for an efficient representation of the text data.
- **Cosine Similarity Calculation**: Compute cosine similarity to find and recommend similar players based on user input.
- **Search Functionality**: Users can input a line from a play, and the program will suggest related plays and characters.

## Packages Used
- **NLTK**: For basic text preprocessing tasks.
- **Scikit-learn**: For generating TF-IDF matrices and computing cosine similarity.
- **Pandas**: For data manipulation and filtering.

## Installation
To run this project, you need to have Python installed along with the required libraries. You can install the necessary packages using pip:

```bash
pip install nltk scikit-learn pandas
