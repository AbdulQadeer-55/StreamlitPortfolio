# Import necessary libraries
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

# Set up the sidebar
st.sidebar.title("My Portfolio")
st.sidebar.write("Welcome to my data science portfolio!")

# Add personal information
st.sidebar.header("About Me")
st.sidebar.write("I am a passionate data scientist with experience in machine learning and data analysis.")
# Add icons and formatting
st.sidebar.markdown("""
    <style>
    .icon-link {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    .icon-link img {
        width: 20px;
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
    <div class="icon-link">
        <img src="https://github.com/favicon.ico" alt="GitHub Icon">
        [GitHub](https://github.com/AbdulQadeer-55)
    </div>
    <div class="icon-link">
        <img src="https://twitter.com/favicon.ico" alt="Twitter Icon">
        [Twitter](https://twitter.com/your_twitter)
    </div>
    <div class="icon-link">
        <img src="https://stackoverflow.com/favicon.ico" alt="Stack Overflow Icon">
        [Stack Overflow](https://stackoverflow.com/users/19420479/abdul-qadeer)
    </div>
    <div class="icon-link">
        <img src="https://leetcode.com/favicon.ico" alt="LeetCode Icon">
        [LeetCode](https://leetcode.com/TheProgrammer_99/)
    </div>
    <div class="icon-link">
        <img src="https://medium.com/favicon.ico" alt="Medium Icon">
        [Medium](https://medium.com/@the.datascientist)
    </div>
    <div class="icon-link">
        <img src="https://www.linkedin.com/favicon.ico" alt="LinkedIn Icon">
        [LinkedIn](https://www.linkedin.com/in/abdulqadeer99)
    </div>
""", unsafe_allow_html=True)


# Load sample data (you can replace this with your own data)
@st.cache
def load_data():
    # Load a sample dataset (e.g., Iris dataset)
    iris = px.data.iris()
    return iris

data = load_data()

# Display a scatter plot
st.title("Data Science Projects")
st.write("Here are some of my data science projects:")

# Show a scatter plot
st.subheader("Iris Dataset Visualization")
species = st.selectbox("Select a species:", data["species"].unique())
filtered_data = data[data["species"] == species]
st.plotly_chart(px.scatter(filtered_data, x="sepal_width", y="sepal_length", color="species"))

# Add a timeline
st.subheader("Project Timeline")
timeline_data = pd.DataFrame({
    "Date": ["2020-01-01", "2020-03-15", "2021-06-30"],
    "Event": ["Started learning ML", "Completed Kaggle competition", "Joined Data Science team"],
})
st.timeline(timeline_data, "Date", "Event")

# Display an image
st.subheader("My Photo")
image = Image.open("your_photo.jpg")  # Replace with your own photo
st.image(image, caption="That's me!", use_column_width=True)

# Add a footer
st.sidebar.write("---")
st.sidebar.write("Created with ❤️ using Streamlit")

# Run the app
if __name__ == "__main__":
    st.set_page_config(page_title="Data Science Portfolio", page_icon="📊")
    st.write("## Explore my data science projects and learn more about me!")
