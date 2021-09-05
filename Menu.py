from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from decimal import *


class Invoice:
    invoicelst = []
    def __init__(self):
        self.invoice = []
        self.subtotal = []
        
    #def ClearInv(self):
       
    
    def Drinks(self,drink):
        self.drink = drink
        drinkslst = [['Soda Water', Decimal('2.00')],
                     ['Mineral Water',Decimal('2.50')],
                     ['Fresh Juice', Decimal('3.50')],
                     ['Scotch', Decimal('5.00')],
                     ['Whiskey',Decimal('5.00')],
                     ['Beer',Decimal('5.00')]
                                        ]
        if drink == 'Soda Water':
            self.invoice.insert(0,drinkslst[0])
            #self.subtotal.append(Decimal('drinkslst[0][1]'))
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

    def Entrees(self,entree):
        self.entree = entree
        entreelst = [['Garlic Bread', Decimal('3.50')],
                     ['Spinach Salad', Decimal('3.00')],
                     ['Caesar Salad', Decimal('3.50')],
                     ['Mixed Green Salad', Decimal('3.50')],
                                       ]
        if entree == 'Garlic Bread':
            self.invoice.insert(0,entreelst[0])
        if entree == 'Spinach Salad':
            self.invoice.insert(0,entreelst[1])
        if entree == 'Caesar Salad':
            self.invoice.insert(0,entreelst[2])
        if entree == 'Mixed Green Salad':
            self.invoice.insert(0,entreelst[3])

    def Deserts(self,desert):
        self.desert = desert
        desertlst = [['Cheesecake', Decimal('5.00')],
                     ['Red Velvet Cake', Decimal('3.00')],
                     ['Icecream', Decimal('3.00')],
                                       ]
        if desert == 'Cheesecake':
            self.invoice.insert(0,desertlst[0])
        if desert == 'Red Velvet Cake':
            self.invoice.insert(0,desertlst[1])
        if desert == 'Icecream':
            self.invoice.insert(0,desertlst[2])

    def Sides(self,side):
        self.side = side
        sideslst = [['Mac & Cheese', Decimal('9.00')],
                     ['Lasagna',Decimal('12.00')],
                     ['French Fries', Decimal('4.50')],
                     ['Mashed Potatoes', Decimal('4.50')],
                     ['Pasta Salad',Decimal('4.50')],
                     ['Pork Chops',Decimal('10.00')],
                     ['Grilled Chicken',Decimal('10.00')],
                     ['Grilled Salmon',Decimal('10.00')]
                                        ]
        if side == 'Mac & Cheese':
            self.invoice.insert(0,sideslst[0])
        if side == 'Lasagna':
            self.invoice.insert(0,sideslst[1])
        if side == 'French Fries':
            self.invoice.insert(0,sideslst[2])
        if side == 'Mashed Potatoes':
            self.invoice.insert(0,sideslst[3])
        if side == 'Pasta Salad':
            self.invoice.insert(0,sideslst[4])
        if side == 'Pork Chops':
            self.invoice.insert(0,sideslst[5])
        if side == 'Grilled Chicken':
            self.invoice.insert(0,sideslst[6])
        if side == 'Grilled Salmon':
            self.invoice.insert(0,sideslst[7])
    
    def Totalinv(self):
        self.invoice = self.invoice[:]
        for i in self.invoice:
            self.subtotal.append(i[1])
            #for price in i:
               # if type(price) == float:
                    #self.invoice.insert(0,'total',price)
        print(self.subtotal)
        
        #for newprice in self.total:
        #    newprice += newprice
        #taxPrice = newprice * 1.15
        #tipCost = newprice * 0.07
        #totalPrice = taxPrice + tipCost

    def listMessageBox(self):
        window=Tk()
        listbox=Listbox(window)
        listbox.pack(fill=BOTH,expand=1)
        [listbox.insert(END,row) for row in self.invoice]
        window.mainloop()

        


b1Cust = Invoice()
b2Cust = Invoice()
#b1Cust.drinks('Soda Water')
#b1Cust.drinks('Mineral Water')
#b1Cust.drinks('Fresh Juice')
#b1Cust.drinks('Scotch')
#b1Cust.drinks('Whiskey')
#b1Cust.drinks('Beer')



def menuOptions(num):
    menuWindow = Tk()
    menuWindow.title('Bar Stool 1 Customer Invoice')
    menuWindow.configure(background='black')
    Label(menuWindow, text=('Menu Selection For Customer at Bar Stool',num),bg='blue',fg='white').grid(row=0,column=1,sticky='ew',padx=8,pady=8)
    Label(menuWindow, text='ENTREES',bg='blue',fg='white',width=25).grid(row=1,column=0,padx=8,pady=8)
    Label(menuWindow, text='SIDES',bg='blue',fg='white',width=25).grid(row=1,column=1,padx=8,pady=8)
    Label(menuWindow, text='DESERTS',bg='blue',fg='white',width=25).grid(row=1,column=2,padx=8,pady=8)
    Label(menuWindow, text='DRINKS',bg='blue',fg='white',width=25).grid(row=1,column=3,padx=8,pady=8)

    entree_btn1 = Button(menuWindow, text='Garlic Bread $3.50',width=25,command=lambda: b1Cust.Entrees('Garlic Bread'))
    entree_btn2 = Button(menuWindow, text='Spinach Salad $3.00',width=25,command=lambda: b1Cust.Entrees('Spinach Salad'))
    entree_btn3 = Button(menuWindow, text='Caesar Salad $3.50',width=25,command=lambda: b1Cust.Entrees('Caesar Salad'))
    entree_btn4 = Button(menuWindow, text='Mixed Green Salad $3.50',width=25,command=lambda: b1Cust.Entrees('Mixed Green Salad'))
    entree_btn1.grid(row=2,column=0, padx=8, pady=8)
    entree_btn2.grid(row=3,column=0, padx=8, pady=8)
    entree_btn3.grid(row=4,column=0, padx=8, pady=8)
    entree_btn4.grid(row=5,column=0, padx=8, pady=8)

    desert_btn1 = Button(menuWindow, text='Cheesecake $5.00',width=25,command=lambda: b1Cust.Deserts('Cheesecake'))
    desert_btn2 = Button(menuWindow, text='Red Velvet Cake $3.00',width=25,command=lambda: b1Cust.Deserts('Red Velvet Cake'))
    desert_btn3 = Button(menuWindow, text='Icecream $3.00',width=25,command=lambda: b1Cust.Deserts('Icecream'))
    desert_btn1.grid(row=2,column=2, padx=8, pady=8)
    desert_btn2.grid(row=3,column=2, padx=8, pady=8)
    desert_btn3.grid(row=4,column=2, padx=8, pady=8)

    sides_btn1 = Button(menuWindow, text='Mac & Cheese $9.00',width=25,command= lambda:b1Cust.Sides('Mac & Cheese'))
    sides_btn2 = Button(menuWindow, text='Lasagna $12.00',width=25,command= lambda:b1Cust.Sides('Lasagna'))
    sides_btn3 = Button(menuWindow, text='French Fries $4.50',width=25,command= lambda:b1Cust.Sides('French Fries'))
    sides_btn4 = Button(menuWindow, text='Mashed Potatoes $4.50',width=25,command= lambda:b1Cust.Sides('Mashed Potatoes'))
    sides_btn5 = Button(menuWindow, text='Pasta Salad $4.50',width=25,command= lambda:b1Cust.Sides('Pasta Salad'))
    sides_btn6 = Button(menuWindow, text='Pork Chops $10.00',width=25,command= lambda:b1Cust.Sides('Pork Chops'))
    sides_btn7 = Button(menuWindow, text='Grilled Chicken $10.00',width=25,command= lambda:b1Cust.Sides('Grilled Chicken'))
    sides_btn8 = Button(menuWindow, text='Grilled Salmon $10.00',width=25,command= lambda:b1Cust.Sides('Grilled Salmon'))
    sides_btn1.grid(row=2,column=1, padx=8, pady=8)
    sides_btn2.grid(row=3,column=1, padx=8, pady=8)
    sides_btn3.grid(row=4,column=1, padx=8, pady=8)
    sides_btn4.grid(row=5,column=1, padx=8, pady=8)
    sides_btn5.grid(row=6,column=1, padx=8, pady=8)
    sides_btn6.grid(row=7,column=1, padx=8, pady=8)
    sides_btn7.grid(row=7,column=1, padx=8, pady=8)
    sides_btn8.grid(row=9,column=1, padx=8, pady=8)

    drinks_btn1 = Button(menuWindow, text='Soda Water $2.00',width=25,command= lambda:b1Cust.Drinks('Soda Water'))
    drinks_btn2 = Button(menuWindow, text='Mineral Water $2.50',width=25,command=lambda: b1Cust.Drinks('Mineral Water'))
    drinks_btn3 = Button(menuWindow, text='Fresh Juice $3.50',width=25,command=lambda: b1Cust.Drinks('Fresh Juice'))
    drinks_btn4 = Button(menuWindow, text='Scotch $5.00',width=25,command=lambda: b1Cust.Drinks('Scotch'))
    drinks_btn5 = Button(menuWindow, text='Whiskey $5.00',width=25,command=lambda:b1Cust.Drinks('Whiskey'))
    drinks_btn6 = Button(menuWindow, text='Beer $5.00',width=25,command=lambda:b1Cust.Drinks('Beer'))
    drinks_btn1.grid(row=2,column=3, padx=8, pady=8)
    drinks_btn2.grid(row=3,column=3, padx=8, pady=8)
    drinks_btn3.grid(row=4,column=3, padx=8, pady=8)
    drinks_btn4.grid(row=5,column=3, padx=8, pady=8)
    drinks_btn5.grid(row=6,column=3, padx=8, pady=8)
    drinks_btn6.grid(row=7,column=3, padx=8, pady=8)


    cust_inv_btn = Button(menuWindow, text='INVOICE',width=25,command=b1Cust.listMessageBox)
    total_btn = Button(menuWindow, text='TOTAL',width=25,command=lambda: b1Cust.Totalinv)
    #clear_inv_btn = Button(menuWindow, text='RESET',width=25,command=lambda:b1Cust.ClearInv)
    cust_inv_btn.grid(row=14,column=1, padx=8, pady=8)
    total_btn.grid(row=14,column=2, padx=8, pady=8)
    #clear_inv_btn.grid(row=14,column=3, padx=8, pady=8)
 

  
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
