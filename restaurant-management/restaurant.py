from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")

tops = Frame(root, bg="black", width=1600, height=500, relief=SUNKEN)
tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))
lblinfo = Label(tops, font=("arial", 30, "bold"), text="Restaurant Management System",
                fg="blue", bd=10, anchor=W)
lblinfo.grid(row=0, column=0)

lblinfo = Label(tops, font=("arial", 30, "bold"), text=localtime, fg="red", anchor=W)
lblinfo.grid(row=1, column=0)

text_input = StringVar()
operator = ""


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def clrdisplay():
    global operator
    operator = ""
    text_input.set("")


def equals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""


def ref():
    x = random.randint(12000, 50000)
    randomRef = str(x)
    rand.set(randomRef)

    _fries = float(fries.get())
    _launch_meal = float(largefries.get())
    _burger_meal = float(burger.get())
    _pizza_meal = float(filet.get())
    _cheese_burger = float(cheese_burger.get())
    _drinks = float(drinks.get())

    fries_cost = _fries * 25
    lunch_cost = _launch_meal * 40
    burger_cost = _burger_meal * 35
    pizza_cost = _pizza_meal * 50
    cheese_burger_cost = _cheese_burger * 30
    drink_cost = _drinks * 35

    meal_cost = "Rs. " + str('%.2f' % (fries_cost + lunch_cost + burger_cost + pizza_cost +
                                       cheese_burger_cost + drink_cost))

    tax_payable = (fries_cost + lunch_cost + burger_cost + pizza_cost + cheese_burger_cost + drink_cost) * 0.33

    totalcost = (fries_cost + lunch_cost + burger_cost + pizza_cost + cheese_burger_cost + drink_cost)

    ser_charge = ((fries_cost + lunch_cost + burger_cost + pizza_cost +
                   cheese_burger_cost + drink_cost) / 99)
    service = "Rs. " + str('%.2f' % service_charge)

    overallcost = "Rs. " + str(tax_payable + totalcost + ser_charge)

    paidtax = "Rs. " + str('%.2f' % tax_payable)

    service_charge.set(service)
    cost.set(meal_cost)
    tax.set(paidtax)
    subtotal.set(meal_cost)
    total.set(overallcost)


def qexit():
    root.destroy()


def reset():
    rand.set("")
    fries.set("")
    largefries.set("")
    burger.set("")
    filet.set("")
    subtotal.set("")
    total.set("")
    service_charge.set("")
    drinks.set("")
    tax.set("")
    cost.set("")
    cheese_burger.set("")


txtdisplay = Entry(f2, font=("arial", 20, "bold"), textvariable=text_input,
                   bd=5, insertwidth=7, bg="green", justify="right")
txtdisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
              text="7", bg="black", command=lambda: btnclick(7))
btn7.grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
              text="8", bg="black", command=lambda: btnclick(8))
btn8.grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
              text="9", bg="black", command=lambda: btnclick(9))
btn9.grid(row=2, column=2)

addition = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
                  text="+", bg="black", command=lambda: btnclick("+"))
addition.grid(row=2, column=3)

btn4 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
              text="4", bg="black", command=lambda: btnclick(4))
btn4.grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
              text="5", bg="black", command=lambda: btnclick(5))
btn5.grid(row=3, column=1)

btn6 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
              text="6", bg="black", command=lambda: btnclick(6))
btn6.grid(row=3, column=2)

subtraction = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
                     text="-", bg="black", command=lambda: btnclick("-"))
subtraction.grid(row=3, column=3)

btn1 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
              text="1", bg="black", command=lambda: btnclick(1))
btn1.grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
              text="2", bg="black", command=lambda: btnclick(2))
btn2.grid(row=4, column=1)

btn3 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
              text="3", bg="black", command=lambda: btnclick(3))
btn3.grid(row=4, column=2)

multiply = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
                  text="*", bg="black", command=lambda: btnclick("*"))
multiply.grid(row=4, column=3)

btn0 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
              text="0", bg="black", command=lambda: btnclick(0))
btn0.grid(row=5, column=0)

btnc = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
              text="c", bg="black", command=clrdisplay)
btnc.grid(row=5, column=1)

decimal = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
                 text=".", bg="black", command=lambda: btnclick("."))
decimal.grid(row=5, column=2)

division = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
                  text="/", bg="black", command=lambda: btnclick("/"))
division.grid(row=5, column=3)

btnequal = Button(f2, padx=16, pady=16, bd=4, fg="white", font=("arial", 20, "bold"),
                  text="=", bg="black", command=equals)
btnequal.grid(row=6, column=0, columnspan=4)

rand = StringVar()
fries = StringVar()
largefries = StringVar()
burger = StringVar()
filet = StringVar()
subtotal = StringVar()
total = StringVar()
service_charge = StringVar()
drinks = StringVar()
tax = StringVar()
cost = StringVar()
cheese_burger = StringVar()

lblreference = Label(f1, font=("Arial", 16, "bold"), text="Order No.", fg="black", bd=10, anchor=W)
lblreference.grid(row=0, column=0)

txtreference = Entry(f1, font=("Arial", 16, "bold"), textvariable=rand, bd=6, insertwidth=4, bg="red", justify="right")
txtreference.grid(row=0, column=1)

#####
lblfries = Label(f1, font=("Arial", 16, "bold"), text="Fries Meal", fg="black", bd=10, anchor=W)
lblfries.grid(row=1, column=0)

txtfries = Entry(f1, font=("Arial", 16, "bold"), textvariable=fries, bd=6, insertwidth=4, bg="red", justify="right")
txtfries.grid(row=1, column=1)

#####
lbllargefries = Label(f1, font=("Arial", 16, "bold"), text="Large Fries Meal", fg="black", bd=10, anchor=W)
lbllargefries.grid(row=2, column=0)

txtlargefries = Entry(f1, font=("Arial", 16, "bold"), textvariable=largefries, bd=6, insertwidth=4, bg="red",
                      justify="right")
txtlargefries.grid(row=2, column=1)

#####
lblburger = Label(f1, font=("Arial", 16, "bold"), text="burger", fg="black", bd=10, anchor=W)
lblburger.grid(row=3, column=0)

txtburger = Entry(f1, font=("Arial", 16, "bold"), textvariable=burger, bd=6, insertwidth=4, bg="red", justify="right")
txtburger.grid(row=3, column=1)

#####
lblfilet = Label(f1, font=("Arial", 16, "bold"), text="filet", fg="black", bd=10, anchor=W)
lblfilet.grid(row=4, column=0)

txtfilet = Entry(f1, font=("Arial", 16, "bold"), textvariable=filet, bd=6, insertwidth=4, bg="red", justify="right")
txtfilet.grid(row=4, column=1)

#####
lblcheese_burger = Label(f1, font=("Arial", 16, "bold"), text="cheese burger", fg="black", bd=10, anchor=W)
lblcheese_burger.grid(row=5, column=0)

txtcheese_burger = Entry(f1, font=("Arial", 16, "bold"), textvariable=cheese_burger, bd=6, insertwidth=4, bg="red",
                         justify="right")
txtcheese_burger.grid(row=5, column=1)

#####
lbldrinks = Label(f1, font=("Arial", 16, "bold"), text="drinks", fg="black", bd=10, anchor=W)
lbldrinks.grid(row=0, column=2)

txtdrinks = Entry(f1, font=("Arial", 16, "bold"), textvariable=drinks, bd=6, insertwidth=4, bg="red", justify="right")
txtdrinks.grid(row=0, column=3)

#####
lblcost = Label(f1, font=("Arial", 16, "bold"), text="cost", fg="black", bd=10, anchor=W)
lblcost.grid(row=1, column=2)

txtcost = Entry(f1, font=("Arial", 16, "bold"), textvariable=cost, bd=6, insertwidth=4, bg="red", justify="right")
txtcost.grid(row=1, column=3)

#####
lblservice_charge = Label(f1, font=("Arial", 16, "bold"), text="service charge", fg="black", bd=10, anchor=W)
lblservice_charge.grid(row=2, column=2)

txtservice_charge = Entry(f1, font=("Arial", 16, "bold"), textvariable=service_charge, bd=6, insertwidth=4, bg="red",
                          justify="right")
txtservice_charge.grid(row=2, column=3)

#####
lbltax = Label(f1, font=("Arial", 16, "bold"), text="tax", fg="black", bd=10, anchor=W)
lbltax.grid(row=3, column=2)

txttax = Entry(f1, font=("Arial", 16, "bold"), textvariable=tax, bd=6, insertwidth=4, bg="red", justify="right")
txttax.grid(row=3, column=3)

#####
lblsubtotal = Label(f1, font=("Arial", 16, "bold"), text="subtotal", fg="black", bd=10, anchor=W)
lblsubtotal.grid(row=4, column=2)

txtsubtotal = Entry(f1, font=("Arial", 16, "bold"), textvariable=subtotal, bd=6, insertwidth=4, bg="red",
                    justify="right")
txtsubtotal.grid(row=4, column=3)

#####
lbltotal = Label(f1, font=("Arial", 16, "bold"), text="total", fg="black", bd=10, anchor=W)
lbltotal.grid(row=4, column=2)

txttotal = Entry(f1, font=("Arial", 16, "bold"), textvariable=total, bd=6, insertwidth=4, bg="red", justify="right")
txttotal.grid(row=4, column=3)

btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="white", font=("Arial", 16, "bold"),
                  width=10, text="TOTAL", bg="black", command=ref)
btnTotal.grid(row=7, column=1)

btnreset = Button(f1, padx=16, pady=8, bd=10, fg="white", font=("Arial", 16, "bold"),
                  width=10, text="RESET", bg="black", command=reset)
btnreset.grid(row=7, column=2)

btnexit = Button(f1, padx=16, pady=8, bd=10, fg="white", font=("Arial", 16, "bold"),
                 width=10, text="EXIT", bg="black", command=qexit)
btnexit.grid(row=7, column=3)


def price():
    roo = Tk()
    roo.geometry("600x220")
    roo.title("Price List")

    x = Frame(roo, bg="white", width=600, height=220, relief=SUNKEN)
    x.pack(side=TOP)

    lblinfo = Label(x, font=("arial", 15, "bold"), text="ITEM", fg="red", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(x, font=("arial", 15, "bold"), text="____________________", fg="black", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(x, font=("arial", 15, "bold"), text="PRICE", fg="black", bd=5, anchor=W)
    lblinfo.grid(row=0, column=5)

    lblinfo = Label(x, font=("arial", 15, "bold"), text="Fries Meal", fg="steel blue", bd=5, anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(x, font=("arial", 15, "bold"), text="25", fg="steel blue", bd=5, anchor=W)
    lblinfo.grid(row=1, column=5)

    lblinfo = Label(x, font=("arial", 15, "bold"), text="Launch Meal", fg="steel blue", bd=5, anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(x, font=("arial", 15, "bold"), text="40", fg="steel blue", bd=5, anchor=W)
    lblinfo.grid(row=2, column=5)

    lblinfo = Label(x, font=("arial", 15, "bold"), text="Burger Meal", fg="steel blue", bd=5, anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(x, font=("arial", 15, "bold"), text="35", fg="steel blue", bd=5, anchor=W)
    lblinfo.grid(row=3, column=5)

    lblinfo = Label(x, font=("arial", 15, "bold"), text="Pizza Meal", fg="steel blue", bd=5, anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(x, font=("arial", 15, "bold"), text="50", fg="steel blue", bd=5, anchor=W)
    lblinfo.grid(row=4, column=5)

    lblinfo = Label(x, font=("arial", 15, "bold"), text="Cheese Burger", fg="steel blue", bd=5, anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(x, font=("arial", 15, "bold"), text="30", fg="steel blue", bd=5, anchor=W)
    lblinfo.grid(row=5, column=5)

    lblinfo = Label(x, font=("arial", 15, "bold"), text="Drinks", fg="steel blue", bd=5, anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(x, font=("arial", 15, "bold"), text="35", fg="steel blue", bd=5, anchor=W)
    lblinfo.grid(row=6, column=5)

    root.mainloop()


btnprice = Button(f1, padx=16, pady=8, bd=10, fg="white", font=("Arial", 16, "bold"),
                  width=10, text="PRICE", bg="black", command=price)
btnprice.grid(row=7, column=0)

root.mainloop()
