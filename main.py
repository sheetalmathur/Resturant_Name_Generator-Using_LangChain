import streamlit as st
from langchain_helper import generate_resturant_name_and_items
st.title ("Resturant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian", "Mexican", "Italian","Chinese"))




if cuisine:
    response = generate_resturant_name_and_items(cuisine)
    st.header(response["resturant_name"].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("Menu Items")
    for items in menu_items:
        st.write(items)