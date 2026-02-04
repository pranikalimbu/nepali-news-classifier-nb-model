import streamlit as st
import joblib

st.title("Nepali News Category Classifier")


model = joblib.load("nepali_news_nb_model.joblib")


input_text = st.text_area(
    label="Enter News Article Text",
    height=200,
    max_chars=1000
)

if st.button("Predict Category"):
    if input_text.strip():
        
            prediction = model.predict([input_text])[0]
            st.success(f"The predicted category is: {prediction}")
        
    else:
        st.warning("Please enter some text first!")
