import pandas as pd
from csv import DictWriter, reader
from datetime import datetime
import hashlib

def show_menu():
    menu = open("data_file/Menu.txt", "r", encoding="utf-8")
    print(menu.read())
    menu.close()

def get_souce_info(saurce_input, souce_order):
    import json
    file = open('data_file/pizza_config.json', encoding="utf8")
    data = json.load(file)
    file.close()

    for key, value in data["souce"][saurce_input].items():
        souce_order[key] = value

    return souce_order["cost"], souce_order["description"]

def get_pizza_info(pizza_input, pizza_order):
    import json
    file = open('data_file/pizza_config.json', encoding="utf8")
    data = json.load(file)
    file.close()
    
    for key, value in data["pizza"][pizza_input].items():
        pizza_order[key] = value

    return pizza_order["cost"], pizza_order["description"]

def encrypt_pass(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def save(name, id, cardno, password, order, cost):
    order_time = datetime.now()
    tittle =["Name","Identification Number","Card Number","Password","Order","Cost","Time"]
    info = {
        "Name" : name,
        "Identification Number" : id,
        "Card Number" : cardno,
        "Password" : password,
        "Order" : order,
        "Cost" : cost,
        "Time" : order_time
    }
    with open('data_file/Orders_Database.csv', mode='a', encoding="utf8") as file:
        data = DictWriter(file, fieldnames=tittle, delimiter=";", lineterminator="\n")
        data.writerow(info)
        file.close()

def show_order_history():
    print("Sipariş Geçmişi")
    print("===============")
    with open('data_file/Orders_Database.csv', 'r', encoding="utf8") as csv_file:
        df = pd.DataFrame(reader(csv_file, delimiter=";"))
        print(df.to_string(index=False, header=False))