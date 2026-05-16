from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import pandas as pd

#load model and scaler
model  = pickle.load(open("regmodel.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl",   "rb"))

app = FastAPI(
    title="Boston House Price Prediction",
    description="Predict house prices using Linear Regression",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

# Home route
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request,"index.html")

# Prediction route
@app.post("/predict", response_class=HTMLResponse)
def predict(
    request : Request,
    CRIM    : float = Form(...),
    ZN      : float = Form(...),
    INDUS   : float = Form(...),
    CHAS    : float = Form(...),
    NOX     : float = Form(...),
    RM      : float = Form(...),
    AGE     : float = Form(...),
    DIS     : float = Form(...),
    RAD     : float = Form(...),
    PTRATIO : float = Form(...),
    LSTAT   : float = Form(...)
):
    # Create DataFrame
    input_df = pd.DataFrame([[
        CRIM, ZN, INDUS, CHAS, NOX,
        RM, AGE, DIS, RAD, PTRATIO, LSTAT
    ]], columns=[
        'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX',
        'RM', 'AGE', 'DIS', 'RAD', 'PTRATIO', 'LSTAT'
    ])

    # Scale and predict
    input_scaled    = scaler.transform(input_df)
    predicted_price = model.predict(input_scaled)

    price_thousands = round(float(predicted_price[0]), 2)
    price_dollars   = round(float(predicted_price[0]) * 1000, 2)

    return templates.TemplateResponse(request, "result.html", {
    "predicted_price_in_thousands" : price_thousands,
    "predicted_price_in_dollars"   : price_dollars,
    "CRIM"                         : CRIM,
    "ZN"                           : ZN,
    "INDUS"                        : INDUS,
    "CHAS"                         : CHAS,
    "NOX"                          : NOX,
    "RM"                           : RM,
    "AGE"                          : AGE,
    "DIS"                          : DIS,
    "RAD"                          : RAD,
    "PTRATIO"                      : PTRATIO,
    "LSTAT"                        : LSTAT
})