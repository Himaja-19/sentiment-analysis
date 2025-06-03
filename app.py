import streamlit as st
from textblob import TextBlob

st.title("🧠 Sentiment Analysis App")

st.write("Enter a sentence or review and this app will predict the sentiment.")

# User input
text = st.text_area("Enter your text here:")

if st.button("Analyze Sentiment"):
    if text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            st.success("✅ Sentiment: Positive")
        elif sentiment < 0:
            st.error("❌ Sentiment: Negative")
        else:
            st.info("😐 Sentiment: Neutral")

        # Optional: show sentiment score
        st.caption(f"Polarity Score: {sentiment:.2f}")
