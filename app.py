import streamlit as st
import requests


st.title("Palnadu🌶️ Restaurant")

option = st.sidebar.selectbox("select option",
                ["Home","Add item","get item","update item","Menu"])
  


if option == "Home":
    st.header("Welcome to Palnadu Resturant")
    st.write("""
            Our restaurant offers a wide variety of delicious and freshly prepared food items.
            From tasty starters and main courses to refreshing drinks and delightful desserts,
            every item is made with quality ingredients and great care.

            Browse our menu to explore different categories, check prices,
            and discover your favorite dishes.
            """)



if option == "Add item":
    food_item = st.text_input("Enter Food item")
    price = st.number_input("Enter price")
    image_url = st.text_input("Food image")
    if st.button("Add item"):
        response = requests.post(
            "http://127.0.0.1:8000/add_item",
            params={
                "food_item": food_item,
                "price": price,
                "image_url": image_url
            }
        )

        st.write(response.status_code)
        st.write(response.text)
   
if option == "get item":
    
    st.header("Get item")
    food_id = st.number_input("Enter food_id")
    if st.button("search"):
        response = requests.get("http://127.0.0.1:8000/get_item",
        params = {
            "food_id": food_id
        }
        )


        st.write(response.status_code)
        st.write(response.text)
       

if option == "update item":

    st.header("update item")
    food_id = st.number_input("Enter food_id")
    
    price = st.number_input("Enter price")
    image = st.text_input("upload image",placeholder = "upload image")
    if st.button("upload"):
        response = requests.put("http://127.0.0.1:8000/update_item",
                                
            params = {"food_id":food_id,
                    
                      "price": price,
                      "image": image})
        st.write(response.json())             

    
if option == "Menu":

    if st.button("Menu"):
        response = requests.get("http://127.0.0.1:8000/Menu")
        st.write(response.json())
       

