from restaurant_db import conn,cursor
from fastapi import FastAPI



app = FastAPI()

@app.get("/")
def home():

    return{
        "message" :"Welcome to Palnadu Restaurant"
    }
@app.post("/add_item")
def add_item(food_item: str, price: float, image_url: str):

    print(food_item, price, image_url)

        
    query = "insert into restaurant(food_name,price,image)values(%s,%s,%s)"

    cursor.execute(query,(food_item,price,image_url))

    conn.commit()

    return{
        "message": "item added successfullly"
    }
@app.get("/Menu")
def menu():

    cursor.execute("select * from restaurant")
    data = cursor.fetchall()
    return data

@app.get("/get_item")
def get_item(food_id:int):

    query = "select * from restaurant where food_id = %s"

    cursor.execute(query,(food_id,))
    data = cursor.fetchone()

    return data

@app.put("/update_item")
def update_item(food_id:str,price:int,image:str):

    query = " update restaurant set price = %s,image = %s where food_id = %s"

    cursor.execute(query,(price,image,food_id))
    conn.commit()
    return {
        "message":"item updated successfully"
    }