import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

def fantasy_design():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #8a63b4;
            color: white;
        }
        .stButton>button {
            color: #FFFFFF;
            background-color: #8a63b4;
            border-color: #8a63b4;
            border-radius: 8px;
        }
       h1, h2, h3, h4 {
            color: black
       }
        </style>
        """,
        unsafe_allow_html=True
    )

st.title("Book Calculator")
fantasy_design()

toothless_image = Image.open("toothless.jpg")
st.sidebar.image(toothless_image, caption="What u looking at? Go finish your book🖤", use_column_width=True)

st.header("My Books")
st.write("This app imports a CSV file from Goodreads and displays various statistics about your books.")

uploaded_file = st.file_uploader("Upload Goodreads CSV File", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.header("Current Calculator")
    if 'Title' in df.columns:  # Check if the column exists
        selected_book = st.selectbox("Select a book:", df['Title'])
        total_pages = st.number_input("Enter total pages of the book:", min_value=1)
        read_pages = st.number_input("Enter pages you have read:", min_value=0, max_value=total_pages)
        if total_pages > 0:
            percent_read = (read_pages / total_pages) * 100
            st.write("You have already read {:.2f}% .".format(percent_read, selected_book))
            if percent_read > 75:
                st.write("Great job! You're almost done with this book!❤️❤️❤️")
            elif percent_read > 50:
                st.write("You're halfway there! Keep it up!❤️❤️")
            elif percent_read > 25:
                st.write("You've already read a quarter of the book. Keep going!❤️")
            else:
                st.write("Keep going! Every page gets you closer to your goal.❤️")

    st.header("Book count")
    st.write("Read Books:", len(df[df['Read Count'] > 0]))
    st.write("Unread Books:", len(df[df['Read Count'] == 0]))
    st.write("Total Books:", len(df))

    if 'Date Read' in df.columns:  # Check if the column exists
        df['Year'] = pd.to_datetime(df['Date Read']).dt.year
        df = df[df['Year'].notnull()]  # Drop NaN values from the Year column

        st.header("Books Read Over the Years")
        fig, ax = plt.subplots()
        sns.countplot(x='Year', data=df, palette='plasma', ax=ax)
        ax.set_xlabel('Year')
        ax.set_ylabel('Book Count')
        st.pyplot(fig)

    else:
        st.write("The column 'Date Read' does not exist in the DataFrame.")
