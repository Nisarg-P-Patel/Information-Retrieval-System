# Text Classification using Naive Bayes

## Aim
The goal of this project is to implement a text classification model using the Naive Bayes approach to detect spam messages. The model is trained on a dataset of text messages labeled as either spam or non-spam, utilizing the TF-IDF vectorization technique for feature extraction.

## Features
- **Data Preprocessing**: Includes text normalization, tokenization, stopword removal, and stemming to prepare the text data for analysis.
- **TF-IDF Vectorization**: Converts text messages into numerical vectors based on term frequency-inverse document frequency (TF-IDF) scores.
- **Naive Bayes Classification**: Utilizes the Multinomial Naive Bayes algorithm for classifying messages as spam or non-spam.
- **Model Evaluation**: Evaluates the model's performance using classification metrics such as precision, recall, and F1-score.

## Packages Used
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Matplotlib** and **Seaborn**: For data visualization.
- **NLTK**: For natural language processing tasks such as tokenization and stemming.
- **Scikit-learn**: For model building, evaluation, and vectorization.

## Installation
To run this project, you need to have Python installed along with the required libraries. You can install the necessary packages using pip:

```bash
pip install pandas numpy matplotlib seaborn nltk scikit-learn
