🥇 Olympic Medal Predictor

A machine learning project that predicts the number of Olympic medals a country's team will win, using Linear Regression based on historical data.

📌 Project Overview

This project analyzes Olympic team data and builds a predictive model using:

Number of athletes sent by a country

Previous medals won by that country

The model is trained on data before 2012 and tested on 2012 and later years.

📁 Project Structure
olympic-medal-predictor/
│
├── Medals.py          # Main script: data prep, model training, evaluation
├── teams.csv          # Dataset (Olympic team statistics)
├── model.pkl          # Saved trained model (generated after running)
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

🧠 Model Details

PropertyValueAlgorithmLinear RegressionFeaturesathletes, prev_medalsTargetmedalsTrain setYears < 2012Test setYears >= 2012EvaluationMean Absolute Error (MAE)

🚀 Getting Started
1. Clone the repository
bashgit clone https://github.com/YOUR_USERNAME/olympic-medal-predictor.git
cd olympic-medal-predictor
2. Install dependencies
bashpip install -r requirements.txt
3. Add the dataset
Place your teams.csv file in the root of the project directory.
4. Run the script
bashpython Medals.py
This will:

Train the model on pre-2012 data
Evaluate on 2012+ data
Print MAE and per-team error ratios
Save the model as model.pkl


📊 Sample Results

Predictions are clipped at 0 (no negative medals) and rounded to whole numbers
Per-team error ratios are computed to identify which teams are hardest to predict
Countries like USA and IND are spot-checked individually
