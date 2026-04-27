# Failure Load Predictor

This project predicts the failure load (kN) of UHPC concrete using Machine Learning.

## Inputs

* Mix ID
* Steel Fibre %
* Age (Days)
* Curing Method

## Output

* Predicted Failure Load (kN)

## How to Run

### 1. Clone repository

git clone <your-repo-link>

### 2. Navigate into folder

cd failure-load-predictor

### 3. Create virtual environment

python -m venv venv

### 4. Activate environment

Windows:
venv\Scripts\activate

Linux:
source venv/bin/activate

### 5. Install dependencies

pip install -r requirements.txt

### 6. Run application

streamlit run app.py
