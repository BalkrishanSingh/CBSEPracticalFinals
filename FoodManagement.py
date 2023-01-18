from datetime import datetime
import mysql.connector as connector
conn = connector.connect(
    host='localhost',
    database='food_management',
    user='root',
    password='Password@123')
if conn.is_connected():
            print('Connected to MySQL database')
cursor = conn.cursor()

def main():
    while True:
        print("""ORDER YOUR FOOD HERE
        1.CREATE YOUR ACCOUNT
        2.ORDER FOOD
        3.EXIT""")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            customer_name= input("Enter your name: ")
            customer_mobile_no = int(input("Enter your mobile number: "))
            customer_address = input("Enter your address : ")
            query = f"insert into customers values('{customer_name.lower()}', '{customer_mobile_no}', '{customer_address}');"
            cursor.execute(query)
            conn.commit()
            print("Account Created")


        if choice == 2:
            print('To Order Food Fill In The Details')
            customer_name = input('Enter your name: ')
            customer_mobile_no = input('Enter your mobile no: ')
            cursor.execute('select * from customers')
            data=cursor.fetchall()
            for row in data:
                print(row)
                if (customer_name.lower() in row) and (customer_mobile_no in row):
                    print('Welcome To Your Food Ordering System')
                    query = "SELECT * FROM food_items"
                    cursor.execute(query)
                    food_items = cursor.fetchall()
                    print()
                    print("(Food No, Food Name, Food Price)")
                    for i in food_items:  
                        print(i)
                    while True:
                        food_no = int(input("Enter the Food No: "))
                        now = datetime.now()
                        time = now.strftime("%Y-%m-%d %H:%M:%S")
                        query = f"insert into orders values({food_no}, '{customer_name}', '{customer_mobile_no}', '{time}')"
                        cursor.execute(query)
                        conn.commit()
                        more =  input("Order more food items? (Y/N) :")
                        if more.lower() == "y":
                            continue
                        elif more.lower() == "n":
                            break
                    print("Order sucessfully placed")
                    print("--------------------------------")
                else:
                    print("Please enter correct details or register a new account.")
                    print("--------------------------------")

        if choice==3:
            print("THANK YOU FOR VISITING")
            print("--------------------------------")
            break
main()