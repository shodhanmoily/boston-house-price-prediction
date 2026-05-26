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
```text
boston-house-price-prediction/
│
├── app.py
├── regmodel.pkl
├── scaler.pkl
├── requirement.txt
├── Dockerfile
├── .gitignore
├── README.md
│
└── templates/
    ├── index.html
    └── result.html
```
## Feature Description & Suggested Input Range

| Feature | Meaning | Suggested Range |
|---|---|---|
| CRIM | Crime rate by town | 0.0 - 100.0 |
| ZN | Residential land zoned percentage | 0 - 100 |
| INDUS | Non-retail business area proportion | 0 - 30 |
| CHAS | Charles River dummy variable (1 = near river, 0 = not near) | 0 or 1 |
| NOX | Nitric oxide pollution concentration | 0.3 - 1.0 |
| RM | Average number of rooms per house | 3 - 9 |
| AGE | Percentage of old houses built before 1940 | 0 - 100 |
| DIS | Distance to employment centers | 1 - 15 |
| RAD | Accessibility to highways | 1 - 25 |
| PTRATIO | Student-teacher ratio | 10 - 25 |
| LSTAT | Percentage of lower-status population | 1 - 40 |





## Author

**Shodhan Moily**
- GitHub: [@shodhanmoily](https://github.com/shodhanmoily)


## License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.