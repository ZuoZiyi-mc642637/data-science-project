# Movie Scores Analysis: Do Critics and Audiences Agree?

## Research Question
Do Rotten Tomatoes critic scores (Tomatometer) and audience scores agree for popular films, and where do they diverge most?

## Dataset Source and Usage Permissions
The dataset `movie_scores.csv` contains Tomatometer and AudienceScore values for five films. It was provided as course material for CISC7204 (University of Macau) and is used here for educational purposes only. No personal or restricted data is included.

## Methods and Tools
- Python 3
- pandas — data loading and inspection
- numpy — numeric operations and axis positioning
- matplotlib — grouped bar chart visualization

## Key Findings
1. Critics and audiences disagree substantially for most films.
2. Critics rated *The Shape of Water* (91 vs 73), *Black Panther* (97 vs 79), and *Dunkirk* (92 vs 81) higher than audiences did.
3. *The Hobbit: An Unexpected Journey* shows the opposite pattern (64 vs 83) — audiences liked it more than critics.
4. Only *The Martian* received nearly identical scores from both groups (91 vs 91).

**Limitation:** The dataset contains only five films, so the findings cannot be generalized to the broader film industry. A larger, more diverse sample would be needed for any general claim.

## How to Run the Analysis
1. Install dependencies:
