import datetime
import pickle
import os

from Item import Item

Items_list=[]
items_file=""
id_count=1


def register_item():
    global id_count

    title=input("Please Type Title ")
    category=input("Please Type Category ")
    price=float(input("Please Type Price "))
    stock=int(input("Please Type Stock "))

    NewItem=Item(id_count,title,category,price,stock)

    Items_list.append(NewItem)
    id_count+=1
    print("Item Created")


def display_Items():

        for itm in Items_list:
            display_Item(itm)

        
        print("Total Items: "+str(len(Items_list)))


def display_Item(itm):
    print("ID: "+str(itm.id)+" Title: "+itm.title+" Category: "+itm.category+"price: "+str(itm.price)+" stock: "+str(itm.stock))


def update_stock():

    itemID=input("Type the ID of the Item you want to Update ")

    for item in Items_list:
        if(str(item.id)==itemID):
            quantity_update=input("Type New Stock Quantity ")

            item.stock=quantity_update

            print("Stock Updated!! ")


def list_empty_stock():

    founditem=False

    for item in Items_list:
        if(item.stock==0):
            founditem=True
            display_Item(item)
    
    if(founditem==False):
        print("No Items Without Stock were found ")
    


# def register_item():
#     global id_count
def menu():
    print("Welcome to Warehouse,  Menu")
    print ("[1] - Add Item")
    print ("[2] - Update Stock")  
    print ("[3] - Display All Items")  
    print ("[4] - Display Items Without Stock") 
    print ("[x] - Exit")

menu()

opc=""
while(opc!="x"):
    menu()
    opc= input("Select an option ")
    if(opc=="x"):
        break    

    if(opc=="1"):
        register_item()
    
    if(opc=="2"):
        update_stock()


    if(opc=="3"):
        display_Items()

    if(opc=="4"):
        list_empty_stock()
    
    input("Press Enter to go back")





    



    


