import langchain
import streamlit as st
import pandas as pd

def main():
    # Set the title and description of the app
    st.title("LearningStreamlit-Abdul Qadeer")
    st.subheader("Welcome to my app!")
    
    table = pd.DataFrame({"age": [20, 30, 40], "height": [180, 170, 160]})
    st.table(table)
    
    # Create a sidebar
    st.sidebar.header("Sidebar Header")
    st.sidebar.text("This is a sidebar")
    
    st.dataframe(table)
    st.write("This is a dataframe")
    st.balloons()
    st.area_chart(table)
    st.code("print('Hello, World!')")
    st.latex("f(x) = x^2")
    st.markdown("This is a markdown")
    st.write("This is a write")
    st.pyplot()
    st.text("This is a text")
    st.title("This is a title")
    st.video("https://www.youtube.com/watch?v=9Q6_TgNZ9VQ")
    st.audio("https://www.youtube.com/watch?v=9Q6_TgNZ9VQ")
    st.image("https://www.python.org/static/img/python-logo.png")
    st.caption("This is a caption")
    st.subheader("This is a subheader")
    st.write("This is a write")
    st.write("This is a write")
    
    
    
if __name__ == "__main__":
    main()