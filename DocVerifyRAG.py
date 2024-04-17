import streamlit as st

# Set the page config to wide mode
st.set_page_config(layout="wide")

# Create columns for the layout
col1, col2 = st.columns(2)

with col1:
    st.header("Upload Documents")
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)
    st.text_input("Sample media")
    st.text_area("Classification instructions")
    st.text_input("Ask me anything")
    if st.button("Assign"):
        # Process the assignment
        pass
    st.text_input("OpenAI Key")
    if st.button("Submit"):
        # Process the submission
        pass
    
with col2:
    st.header("Upload Documents")
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)
    st.text_input("Sample media")
    st.text_area("Classification instructions")
    st.text_input("Ask me anything")
    if st.button("Assign"):
        # Process the assignment
        pass
    st.text_input("OpenAI Key")
    if st.button("Submit"):
        # Process the submission
        pass



