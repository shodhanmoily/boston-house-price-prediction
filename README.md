# boston-house-price-prediction

A Machine Learning API built with FastAPI to predict Boston house prices.

---

##  Live Demo
> Deployed on Railway — [Click Here](your-railway-link-here)

---

## Model Performance
| Metric | Score |
|--------|-------|
| R² Score | 0.706 |
| MAE | 3.76 |
| RMSE | 5.35 |

---

## Tech Stack
- Python
- FastAPI
- Scikit-learn
- Docker
- Railway

---

## API Usage

**POST** `/predict`

```json
{
    "CRIM"    : 0.00632,
    "ZN"      : 18.0,
    "INDUS"   : 2.31,
    "CHAS"    : 0.0,
    "NOX"     : 0.538,
    "RM"      : 6.575,
    "AGE"     : 65.2,
    "DIS"     : 4.09,
    "RAD"     : 1.0,
    "PTRATIO" : 15.3,
    "LSTAT"   : 4.98
}
```

**Response**
```json
{
    "predicted_price_in_thousands": 31.34,
    "predicted_price_in_dollars": 31340.00
}
```

---

##  Run Locally
```bash
git clone https://github.com/shodhanmoily/boston-house-price-prediction.git
cd boston-house-price-prediction
pip install -r requirement.txt
uvicorn app:app --reload
```

---

## Run with Docker
```bash
docker build -t boston-app .
docker run -p 8000:8000 boston-app
```

---

## Author
**Shodhan Moily** — [@shodhanmoily](https://github.com/shodhanmoily)