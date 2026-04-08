# 🏠 House Price Prediction

This is a **Streamlit** project for predicting house prices based on features like quality, living area, number of bedrooms, number of bathrooms, and year built.

## 🛠️ Tools Used
- Python 3.13
- Streamlit
- Numpy
- Pickle (for loading the trained model)

## 💡 How to Run
1. Make sure to install the requirements:
```bash
pip install streamlit numpy
Run the Streamlit app:
streamlit run UI/App.py
Enter the house details in the interface to get the predicted price.
📂 Project Structure
house_price_prediction/
│
├── model/                  # Contains house_price_model.pkl
├── UI/
│   └── App.py              # Streamlit user interface
└── README.md
⚠️ Notes
Make sure the model file house_price_model.pkl exists inside the model folder.
If the file is missing, the app will show an error message.
📈 Prediction

The app interface allows you to input:

House quality (1-10)
Living area in m²
Number of bedrooms
Number of bathrooms
Year built

Then click Predict Price to display the estimated house price.
