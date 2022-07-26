from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root=Tk()
root.title("Food Ordering System")
root.geometry("900x500")

burger=ImageTk.PhotoImage(Image.open("salad.png"))
burger_image=Label(root)
burger_image["image"]=burger
burger_image.place(relx=0.8, rely=0.5, anchor=CENTER)

label_heading=Label(root, text="Delightful Treat For The Soul", font=("times",30,"bold"), fg="Orange")
label_heading.place(relx=0.3, rely=0.1, anchor=CENTER)

label_select_dish=Label(root, text="Select Dish", font=("times",15))
label_select_dish.place(relx=0.06, rely=0.2, anchor=CENTER)

dish=["salad","masala chai"]
dish_dropdown=ttk.Combobox(root, state="readonly",values=dish)
dish_dropdown.place(relx=0.25, rely=0.2, anchor=CENTER)

label_select_addons=Label(root, text="Select Toppings", font=("times",15))
label_select_addons.place(relx=0.08, rely=0.5, anchor=CENTER)

toppings=[]
toppings_dropdown=ttk.Combobox(root, state="readonly",values=toppings)
toppings_dropdown.place(relx=0.25, rely=0.5, anchor=CENTER)

dish_amount=Label(root,font=("times",15,"bold"))
dish_amount.place(relx=0.2, rely=0.75, anchor=CENTER)









class parent():
    def __init__(self):
        print("This is parent class")
        
    def menu(dish):
        if dish=="salad":
            print("You can add following toppings")
            print("More paneer / Add lettuce and Brocolli")
            toppings=["paneer","lettuce and brocolli"]
            toppings_dropdown["values"]=toppings
        elif dish=="masala chai":
            print("You can add following toppings")
            print("Add ginger / Add cardamom / Add clove ")
            toppings=["ginger","cardamom","clove"]
            toppings_dropdown["values"]=toppings
        else:
            print("please enter valid dish")
            
    def final_amount(dish, add_ons):
        if dish=="salad" and add_ons=="paneer":
            print("You need to pay 250 USD")
            dish_amount["text"]="You need to pay 250 USD"
        elif dish=="salad" and add_ons=="lettuce and brocolli":
            dish_amount["text"]="You need to pay 350 USD"
            print("You need to pay 350 USD")
        elif dish=="masala chai" and add_ons=="cardamom":
            dish_amount["text"]="You need to pay 450 USD"
            print("You need to pay 450 USD")
        elif dish=="masala chai" and add_ons=="ginger":
            dish_amount["text"]="You need to pay 250 USD"
            print("You need to pay 250 USD")
        elif dish=="masala chai" and add_ons=="clove":
            dish_amount["text"]="You need to pay 550 USD"
            print("You need to pay 550 USD")
            
class child1(parent):
    
    def __init__(self,dish):
        self.new_dish=dish
    def get_menu(self):
        new_dish=dish_dropdown.get()
        parent.menu(new_dish)
        
class child2(parent):
    
    def __init__(self,dish,addons):
        self.new_dish=dish
        self.addons=addons
    def get_final_amount(self):
        new_dish=dish_dropdown.get()
        addons=toppings_dropdown.get()
        parent.final_amount(new_dish,addons)
        
child1_object=child1(dish_dropdown.get())
child1_object.get_menu()

child2_object=child2(dish_dropdown.get(), toppings_dropdown.get())
child2_object.get_final_amount()
        
btn_addons=Button(root, text="Check Toppings",command=child1_object.get_menu, bg="blue", fg="white", relief=FLAT)
btn_addons.place(relx=0.06, rely=0.3, anchor=CENTER)

btn_amount=Button(root, text="Amount",command=child2_object.get_final_amount, bg="blue", fg="white", relief=FLAT)
btn_amount.place(relx=0.04, rely=0.6, anchor=CENTER)
                  
root.mainloop()     
                  