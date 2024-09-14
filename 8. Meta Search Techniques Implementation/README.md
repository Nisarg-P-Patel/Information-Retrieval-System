# Meta Search Techniques Implementation

## Aim
The aim of this project is to implement various meta search techniques to determine the final ranking of web pages based on rankings provided by different evaluators. The implemented techniques include:
1. Borda Count
2. Condorcet Method
3. Reciprocal Ranking

## Features
- **Borda Count**: A voting method in which voters rank options, and points are assigned based on the position in the ranking.
- **Condorcet Method**: A ranking method that compares each option against every other option to determine a winner.
- **Reciprocal Ranking**: A technique that assigns scores inversely proportional to the rank of each option.

## Packages Used
- **NumPy**: For numerical operations.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For potential future visualizations (if needed).

## Installation
To run this project, you need to have Python installed along with the required libraries. You can install the necessary packages using pip:

```bash
pip install numpy pandas matplotlib
