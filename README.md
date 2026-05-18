# Boston House Price Prediction

A Machine Learning web application built with FastAPI to predict Boston house prices based on property features like crime rate, number of rooms, pollution level, and more.

---

## Live Demo

Deployed on Railway — [Click Here](https://boston-house-price-prediction-production.up.railway.app)

---

## Project Overview

This project uses the Boston Housing Dataset to train a Linear Regression model that predicts the median value of owner-occupied homes. The model is served through a FastAPI web application with a responsive UI and containerized using Docker.

---

## Model Performance

| Metric | Score |
|--------|-------|
| R² Score | 0.706 |
| Adjusted R² | 0.683 | 
| MSE | 28.672 |
| MAE | 3.76 |
| RMSE | 5.35 |
| Train/Test Split | 70/30 |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Programming language |
| FastAPI | Web framework |
| Scikit-learn | Machine learning model |
| Pandas | Data manipulation |
| StandardScaler | Feature scaling |
| Jinja2 | HTML templating |
| Docker | Containerization |
| Railway | Cloud deployment |
| GitHub | Version control |

---

## Project Structure
boston-house-price-prediction/
│
├── app.py
├── regmodel.pkl
├── scaler.pkl
├── requirement.txt
├── Dockerfile
├── .gitignore
├── README.md
└── templates/
├── index.html
└── result.html


## Author

**Shodhan Moily**
- GitHub: [@shodhanmoily](https://github.com/shodhanmoily)


## License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.