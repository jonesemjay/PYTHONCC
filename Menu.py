from tkinter import *
from tkinter import ttk


class Invoice:
    invoicelst = []
    def __init__(self):
        self.invoice = []
    
    def drinks(self,drink):
        self.drink = drink
        drinkslst = [['Soda Water', 2.00],
                     ['Mineral Water',2.50],
                     ['Fresh Juice', 3.50],
                     ['Scotch', 5.00],
                     ['Whiskey',5.00],
                     ['Beer',5.00]
                                        ]
        if drink == 'Soda Water':
            self.invoice.insert(0,drinkslst[0])
        if drink == 'Mineral Water':
            self.invoice.insert(0,drinkslst[1])
        if drink == 'Fresh Juice':
            self.invoice.insert(0,drinkslst[2])
        if drink == 'Scotch':
            self.invoice.insert(0,drinkslst[3])
        if drink == 'Whiskey':
            self.invoice.insert(0,drinkslst[4])
        if drink == 'Beer':
            self.invoice.insert(0,drinkslst[5])

    def desert(self,desert):
        self.desert = desert
        desertlst = [['Cheesecake', 5.00],
                     ['Red Velvet Cake', 3.00],
                     ['Icecream', 3.00],
                                       ]
        if desert == 'Cheesecake':
            self.invoice.insert(0,desertlst[0])
        if desert == 'Red Velvet Cake':
            self.invoice.insert(0,desertlst[1])
        if desert == 'Icecream':
            self.invoice.insert(0,desertlst[2])

    
    def Total(self):
        total = self.invoice[:]
        for i in total:
            print(i)
            for price in i:
                if type(price) == float:
                    total.insert(0,price)
        #print(self.total)
        
        #for newprice in self.total:
        #    newprice += newprice
        #taxPrice = newprice * 1.15
        #tipCost = newprice * 0.07
        #totalPrice = taxPrice + tipCost
        


b1Cust = Invoice()
#b1Cust.drinks('Soda Water')
#b1Cust.drinks('Mineral Water')
#b1Cust.drinks('Fresh Juice')
#b1Cust.drinks('Scotch')
#b1Cust.drinks('Whiskey')
#b1Cust.drinks('Beer')




def drinksTab(btn,num):
    if btn == 16:
        if num == 1:
            customer_tab_1.update({'Soda Water': float(2.00)})                  
        elif num == 2:
            customer_tab_2.update({'Soda Water': 2.00})
        elif num == 3:
            customer_tab_3.update({'Soda Water': 2.00})
        elif num == 4:
            customer_tab_4.update({'Soda Water': 2.00})
        elif num == 5:
            customer_tab_5.update({'Soda Water': 2.00})
        elif num == 6:
            customer_tab_6.update({'Soda Water': 2.00})
        elif num == 7:
            customer_tab_7.update({'Soda Water': 2.00})
        elif num == 8:
            customer_tab_9.update({'Soda Water': 2.00})
    if btn == 17:
        if num == 1:
            customer_tab_1.update({'Mineral Water': float(2.50)})                  
        elif num == 2:
            customer_tab_2.update({'Soda Water': 2.00})
        elif num == 3:
            customer_tab_3.update({'Soda Water': 2.00})
        elif num == 4:
            customer_tab_4.update({'Soda Water': 2.00})
        elif num == 5:
            customer_tab_5.update({'Soda Water': 2.00})
        elif num == 6:
            customer_tab_6.update({'Soda Water': 2.00})
        elif num == 7:
            customer_tab_7.update({'Soda Water': 2.00})
        elif num == 8:
            customer_tab_9.update({'Soda Water': 2.00})


def menuOptions(num):
    menuWindow = Tk()
    menuWindow.title('Bar Stool 1 Customer Invoice')
    menuWindow.configure(background='black')
    Label(menuWindow, text=('Menu Selection For Customer at Bar Stool',num),bg='blue',fg='white').grid(row=0,column=1,sticky='ew',padx=8,pady=8)
    Label(menuWindow, text='ENTREES',bg='blue',fg='white',width=25).grid(row=1,column=0,padx=8,pady=8)
    Label(menuWindow, text='SIDES',bg='blue',fg='white',width=25).grid(row=1,column=1,padx=8,pady=8)
    Label(menuWindow, text='DESERTS',bg='blue',fg='white',width=25).grid(row=1,column=2,padx=8,pady=8)
    Label(menuWindow, text='DRINKS',bg='blue',fg='white',width=25).grid(row=1,column=3,padx=8,pady=8)

    entree_btn1 = Button(menuWindow, text='Garlic Bread $3.50',width=25).grid(row=2,column=0, padx=8, pady=8)
    entree_btn2 = Button(menuWindow, text='Spinach Salad $3.00',width=25).grid(row=3,column=0, padx=8, pady=8)
    entree_btn3 = Button(menuWindow, text='Caesar Salad $3.50',width=25).grid(row=4,column=0, padx=8, pady=8)
    entree_btn4 = Button(menuWindow, text='Mixed Green Salad $3.50',width=25).grid(row=5,column=0, padx=8, pady=8)

    desert_btn1 = Button(menuWindow, text='Cheesecake $5.00',width=25,command=lambda:b1Cust.desert('Cheesecake')).grid(row=2,column=2, padx=8, pady=8)
    desert_btn2 = Button(menuWindow, text='Red Velvet Cake $3.00',width=25,command=lambda:b1Cust.desert('Red Velvet Cake')).grid(row=3,column=2, padx=8, pady=8)
    desert_btn3 = Button(menuWindow, text='Icecream $3.00',width=25).grid(row=4,column=2, padx=8, pady=8)

    sides_btn1 = Button(menuWindow, text='Mac & Cheese $9.99',width=25).grid(row=2,column=1, padx=8, pady=8)
    sides_btn2 = Button(menuWindow, text='Lasagna $12.99',width=25).grid(row=3,column=1, padx=8, pady=8)
    sides_btn3 = Button(menuWindow, text='French Fries $4.50',width=25).grid(row=4,column=1, padx=8, pady=8)
    sides_btn4 = Button(menuWindow, text='Mashed Potatoes $4.50',width=25).grid(row=5,column=1, padx=8, pady=8)
    sides_btn5 = Button(menuWindow, text='Pasta Salad $4.50',width=25).grid(row=6,column=1, padx=8, pady=8)
    sides_btn6 = Button(menuWindow, text='Pork Chops $10.00',width=25).grid(row=7,column=1, padx=8, pady=8)
    sides_btn7 = Button(menuWindow, text='Grilled Chicken $10.00',width=25).grid(row=7,column=1, padx=8, pady=8)
    sides_btn8 = Button(menuWindow, text='Grilled Salmon $10.00',width=25).grid(row=9,column=1, padx=8, pady=8)

    drinks_btn1 = Button(menuWindow, text='Soda Water $2.00',width=25,command= b1Cust.drinks('Soda Water')).grid(row=2,column=3, padx=8, pady=8)
    drinks_btn2 = Button(menuWindow, text='Mineral Water $2.50',width=25,command=lambda: b1Cust.drinks('Mineral Water')).grid(row=3,column=3, padx=8, pady=8)
    drinks_btn3 = Button(menuWindow, text='Fresh Juice $3.50',width=25,command=lambda: b1Cust.drinks('Fresh Juice')).grid(row=4,column=3, padx=8, pady=8)
    drinks_btn4 = Button(menuWindow, text='Scotch $5.00',width=25,command=lambda: b1Cust.drinks('Scotch')).grid(row=5,column=3, padx=8, pady=8)
    drinks_btn5 = Button(menuWindow, text='Whiskey $5.00',width=25,command=lambda:b1Cust.drinks('Whiskey')).grid(row=6,column=3, padx=8, pady=8)
    drinks_btn6 = Button(menuWindow, text='Beer $5.00',width=25,command=lambda:b1Cust.drinks('Beer')).grid(row=7,column=3, padx=8, pady=8)
    cust_inv_btn1 = Button(menuWindow, text='INVOICE',width=25,command=lambda: print(b1Cust.invoice)).grid(row=12,column=1, padx=8, pady=8)
    total_btn1 = Button(menuWindow, text='TOTAL',width=25,command=lambda:print(b1Cust.Total)).grid(row=12,column=2, padx=8, pady=8)

    customer_tab_1 = []
       
def customer_invoice_1():
    
    for amount in customer_tab_1.values():
        amount += amount
        
    customer_tab_1.update({'Total is': round(amount,2)})
    for item, price in customer_tab_1.items():
        print(item,'--- $',round(price,2))
    customer_tab_1.clear()

  
def mainWindow():
    mainWindow = Tk()
    mainWindow.title('MJ\'s Bar n Grill')
    mainWindow.configure(background='black')

    Label(mainWindow,text='Choose the customer\'s seat number',bg='sky blue',fg='black').grid(row=0, column=0, padx=8, pady=8, sticky='ew')

    b1 = Button(mainWindow, text='Bar Stool 1', width=8,command=lambda: menuOptions(1))
    b2 = Button(mainWindow, text='Bar Stool 2', width=8,command=lambda: menuOptions(2))
    b3 = Button(mainWindow, text='Bar Stool 3', width=8)
    b4 = Button(mainWindow, text='Bar Stool 4', width=8)
    t1 = Button(mainWindow, text='Table 1', width=8)
    t2 = Button(mainWindow, text='Table 2', width=8)
    t3 = Button(mainWindow, text='Table 3', width=8)
    t4 = Button(mainWindow, text='Table 4', width=8)
    t5 = Button(mainWindow, text='Table 5', width=8)

    b1.grid(row=1,column=0,sticky=W)
    b2.grid(row=2,column=0,sticky=W)
    b3.grid(row=3,column=0,sticky=W)
    b4.grid(row=4,column=0,sticky=W)
    t1.grid(row=1,column=1, sticky=W)
    t2.grid(row=2,column=1)
    t3.grid(row=3,column=1)
    t4.grid(row=4,column=1)
    t5.grid(row=5,column=1)









    mainWindow.mainloop()
mainWindow()
