import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import torch

# ✅ Use online HuggingFace model (NO local errors)
MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)


def main():
    st.title('ReviewScope - Customer Review Analysis')

    col = st.columns(3)

    # ---------------- Sidebar ----------------
    with st.sidebar:
        col2 = st.columns(2)
        lower = col2[0].selectbox('From Year', list(range(2004, 2024)))
        upper = col2[1].selectbox('To Year', list(range(lower + 1, 2025)))

    # ---------------- Load Data ----------------
    try:
        df = pd.read_csv('sample.csv')
    except:
        st.error("sample.csv")
        return

    # Fix Timestamp
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    df = df.dropna(subset=['Timestamp'])

    # Filter by year
    df = df[
        (df['Timestamp'].dt.year >= lower) &
        (df['Timestamp'].dt.year <= upper)
    ]

    # Add random categories
    categories = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5', 'Cat6']
    df['Category'] = np.random.choice(categories, size=len(df))

    # ---------------- Session ----------------
    if 'reviews' not in st.session_state:
        st.session_state.reviews = {}

    # ---------------- Input ----------------
    with col[2].form("review_form"):
        user_input = st.text_input("Enter your review")
        submit = st.form_submit_button("Analyze")

        if submit and user_input:
            encoded = tokenizer(user_input, return_tensors='pt')
            output = model(**encoded)

            scores = output.logits.detach().numpy()[0]
            scores = softmax(scores)

            labels = ['negative', 'neutral', 'positive']
            sentiment = labels[np.argmax(scores)]

            st.success(f"Predicted Sentiment: {sentiment}")
            st.session_state.reviews[user_input] = sentiment

    # ---------------- Show Reviews ----------------
    col[0].subheader("Sample Reviews")

    if 'Summary' in df.columns and 'Sentiment' in df.columns:
        for _, row in df.head(5).iterrows():
            col[0].write(f"{row['Summary']} ({row['Sentiment']})")

    # ---------------- Bar Chart ----------------
    if st.session_state.reviews:
        remarks = list(st.session_state.reviews.values())
        count_df = pd.Series(remarks).value_counts().reset_index()
        count_df.columns = ['Sentiment', 'Count']

        fig, ax = plt.subplots()
        sns.barplot(x='Sentiment', y='Count', data=count_df, ax=ax)
        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

        col[1].pyplot(fig)

    # ---------------- Pie Chart ----------------
    if 'Sentiment' in df.columns:
        fig2, ax2 = plt.subplots()
        df['Sentiment'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax2)
        ax2.set_ylabel('')
        ax2.set_title('Dataset Sentiment Distribution')

        col[1].pyplot(fig2)

    # ---------------- Stacked Bar ----------------
    if 'Id' in df.columns:
        pivot = pd.pivot_table(
            df,
            values='Id',
            index='Category',
            columns='Sentiment',
            aggfunc='count',
            fill_value=0
        )

        fig3, ax3 = plt.subplots()
        pivot.plot(kind='bar', stacked=True, ax=ax3)

        col[2].pyplot(fig3)

    # ---------------- Time Series ----------------
    if 'Id' in df.columns:
        monthly = df.groupby(df['Timestamp'].dt.to_period('M')).count()

        fig4, ax4 = plt.subplots()
        ax4.plot(monthly.index.to_timestamp(), monthly['Id'])

        ax4.set_title("Monthly Reviews")
        ax4.set_xlabel("Month")
        ax4.set_ylabel("Count")

        st.pyplot(fig4)


if __name__ == "__main__":
    main()