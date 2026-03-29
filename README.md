# 🥇 Olympic Medal Predictor

A machine learning project that predicts the number of Olympic medals a country's team will win, using **Linear Regression** trained on historical Olympic data.

🌐 **[Live Demo → TiwariShreya05.github.io/olympic-medal-predictor](https://tiwariShreya05.github.io/olympic-medal-predictor)**

---

## 📌 Project Overview

This project analyzes Olympic team data and builds a predictive model using two key features:

- **Number of athletes** sent by a country to the Olympics
- **Previous medals** won by that country in prior Games

The model is trained on data **before 2012** and evaluated on **2012 and later** years.

---

## 🌐 Web App

The project is deployed as a fully interactive website on GitHub Pages — no installation required. Just open the link and start predicting!

**Features of the web app:**
- Sliders and number inputs for athletes and previous medals
- Instant medal prediction with a visual meter
- Estimated gold / silver / bronze breakdown
- Quick-select presets for countries like USA, China, India, France
- Works entirely in the browser — no backend needed

---

## 📁 Project Structure

```
olympic-medal-predictor/
│
├── index.html        # Deployed web app (GitHub Pages)
├── Medals.py         # Main script: data prep, model training, evaluation
├── app.py            # Streamlit app (local)
├── teams.csv         # Dataset (Olympic team statistics)
├── model.pkl         # Saved trained model (generated after running Medals.py)
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## 🧠 Model Details

| Property    | Value                        |
|-------------|------------------------------|
| Algorithm   | Linear Regression            |
| Features    | `athletes`, `prev_medals`    |
| Target      | `medals`                     |
| Train set   | Years < 2012                 |
| Test set    | Years ≥ 2012                 |
| Evaluation  | Mean Absolute Error (MAE)    |

### How the prediction works

The model learns a linear equation from historical data:

```
medals = intercept + (coef_athletes × athletes) + (coef_prev_medals × prev_medals)
```

Approximate learned coefficients:
- `intercept` ≈ -0.9
- `coef_athletes` ≈ 0.02  → each additional athlete contributes ~0.02 medals
- `coef_prev_medals` ≈ 0.72  → past performance is the strongest predictor

Predictions are **clipped at 0** (no negative medals) and **rounded** to whole numbers.

**Key insight:** Previous medals carry far more predictive weight (~0.72) than athlete count (~0.02), meaning a country's track record is the strongest signal of future performance.

---

## 🚀 Getting Started (Local)

### 1. Clone the repository

```bash
git clone https://github.com/TiwariShreya05/olympic-medal-predictor.git
cd olympic-medal-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add the dataset

Place your `teams.csv` file in the root of the project directory.

### 4. Train the model

```bash
python Medals.py
```

This will:
- Train the model on pre-2012 data
- Evaluate on 2012+ data
- Print MAE and per-team error ratios
- Save the model as `model.pkl`

### 5. Run the Streamlit app (optional)

```bash
streamlit run app.py
```

---

## 📊 Sample Results

- Predictions are clipped at 0 and rounded to whole numbers
- Per-team error ratios identify which countries are hardest to predict
- Countries like USA and IND are spot-checked individually

---

## 🛠 Tech Stack

- **Python** — data processing and model training
- **scikit-learn** — Linear Regression
- **pandas / numpy** — data manipulation
- **Streamlit** — local web app
- **HTML / CSS / JS** — deployed GitHub Pages version (no dependencies)

---

## 📬 Contact

- 💼 LinkedIn: [linkedin.com/in/shreya-tiwari-520b692b3](https://www.linkedin.com/in/shreya-tiwari-520b692b3/)
- 📧 Email: shreyatiwari0801@gmail.com
- 🐙 GitHub: [github.com/TiwariShreya05](https://github.com/TiwariShreya05)
