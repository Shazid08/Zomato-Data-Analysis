🍽️ Zomato Data Analysis using Python

This project performs data cleansing, preprocessing, and exploratory data analysis (EDA) on a Zomato restaurant dataset. Using Python’s data analysis and visualization libraries, the project provides insights into restaurant ratings, types, votes, online ordering trends, and cost distribution.

📦 Technologies & Libraries Used

Python 3.x

Pandas – Data manipulation and cleaning

NumPy – Numerical operations

Matplotlib – Data visualization

Seaborn – Statistical plotting

📊 Project Workflow
1. Load the Dataset

The dataset is loaded using pandas.read_csv() and previewed with .head().

2. Clean the Data

A custom function handleRate() is applied to convert rating values like "4.1/5" into numeric format (4.1).
The cleaned values are assigned back to the rate column.

3. Summary Statistics

Basic statistics (df.describe()) and dataset structure (df.info()) are displayed to understand data distribution and types.

📈 Visualizations Included
1. Restaurant Type Distribution

A countplot showing how many restaurants fall into each category.

2. Total Votes by Restaurant Type

Restaurant types are grouped by total votes and visualized using a line plot.

3. Restaurants with Maximum Votes

The restaurant(s) with the highest number of votes are identified and printed.

4. Online Order Availability

A countplot showing how many restaurants offer online ordering vs those that don’t.

5. Ratings Distribution

A histogram visualizing how ratings are spread across the dataset.

6. Cost for Two People

Countplot for approx_cost(for two people) to analyze price distribution.

7. Rate vs Online Order (Boxplot)

Shows how ratings differ between restaurants with and without online ordering.

8. Heatmap (Restaurant Type vs Online Order)

A pivot table is visualized to compare restaurant types with availability of online food ordering.

📁 Project Structure
├── dataset/
│   └── Zomato-data-.csv
├── zomato_analysis.py
├── README.md

🚀 How to Run the Project

1. Install the required libraries:
pip install pandas numpy matplotlib seaborn

2. Place the dataset in the dataset/ folder.

3. Run the script:
python zomato_analysis.py

📌 Results

This project helps in understanding:

Popular restaurant types

Rating patterns

Online ordering trends

Cost distribution

Customer engagement through votes

It provides clear visual insights into how restaurant features relate to rating and customer interest.