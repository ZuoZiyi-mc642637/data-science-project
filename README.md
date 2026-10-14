# Movie Scores Analysis: Do Critics and Audiences Agree?

A small data science project that compares Rotten Tomatoes critic scores (Tomatometer) and audience scores (AudienceScore) for five popular films, and visualizes where the two groups disagree.

---

## 1. Research Question

Do Rotten Tomatoes critic scores and audience scores agree for popular films, and where do they diverge most?

The goal of this analysis is to check whether critics and general audiences tend to rate the same films similarly, and to identify which films show the largest critic–audience gap.

---

## 2. Dataset Source and Usage Permissions

The dataset `movie_scores.csv` contains five films with two scores each:

- `MovieTitle` — the name of the film
- `Tomatometer` — the percentage of approved Tomatometer critics who gave a positive review
- `AudienceScore` — the percentage of users who gave a score of 3.5 or higher out of 5

The dataset was provided as course material for **CISC7204 (Data Visualization)** at the **University of Macau** and is used here strictly for **educational purposes**. No personal, confidential, or restricted data is included. The dataset is small and publicly derived; no special permission is required for this academic use.

---

## 3. Methods and Tools

- **Python 3**
- **pandas** — loading and inspecting the CSV
- **numpy** — array operations and bar positioning
- **matplotlib** — grouped bar chart visualization
- **Jupyter Notebook** — interactive analysis environment

The analysis is intentionally simple: load the data, inspect it, reshape it for plotting, and produce a single grouped bar chart that makes the critic–audience gap visible at a glance.

---

## 4. Key Findings

1. **Critics and audiences disagree substantially for most films.** Only one of the five films received nearly identical scores from both groups.

2. **Critics rated three films higher than audiences did:**
   - *The Shape of Water*: 91 (critics) vs 73 (audience) — a 18-point gap
   - *Black Panther*: 97 vs 79 — a 18-point gap
   - *Dunkirk*: 92 vs 81 — a 11-point gap

3. **One film shows the opposite pattern:**
   - *The Hobbit: An Unexpected Journey*: 64 (critics) vs 83 (audience) — a 19-point gap in the other direction

4. **One film shows near agreement:**
   - *The Martian*: 91 vs 91 — identical scores

### Limitation

The dataset contains **only five films**, which is far too small to support any general claim about critics and audiences in the film industry. The findings describe these five films only. A larger and more diverse sample — across genres, years, and countries — would be needed before drawing broader conclusions.

---

## 5. How to Run the Analysis

### Requirements

Install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
