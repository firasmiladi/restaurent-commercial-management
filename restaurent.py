from tkinter import *
import random
import time
import datetime
from tkinter import messagebox, ttk
# ========================================================================================================
#                               Restaurent management
#========================================================================================================
root=Tk()
root.geometry("1550x850+0+0")
root.title("Restaurant Management System")
root.configure(background='white')
# ========================================================================================================
#                                PRINCIPAL FRAMES
#========================================================================================================
Tops = Frame(root, width=1550, height=80, bd=12, relief="raise")
Tops.pack(side = TOP)
lblTitle = Label(Tops, font=("arial", 50, 'bold'),background="white", text="             Restaurant Management System          ")
lblTitle.grid(row=0, column=0)
# ========================================================================================================
#                                DATE TIME
#========================================================================================================
localtime=time.asctime(time.localtime(time.time()))
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
# ========================================================================================================
#                                SECONDARY FRAMES
#========================================================================================================
BottomMainFrame = Frame(root, width=1550, height=770, bd=12, relief="raise")
BottomMainFrame.pack(side=BOTTOM)

f1 = Frame(BottomMainFrame, width=500, height=770, bd=12, relief=SUNKEN)
f1.pack(side=LEFT)

f1top = Frame(f1, width=500, height=570, bd=12, relief="raise")
f1top.pack(side=TOP)
f1bottom = Frame(f1, width=500, height=200, bd=12, relief="raise")
f1bottom.pack(side=BOTTOM)


f2 = Frame(BottomMainFrame, width=400, height=770, bd=12, relief=SUNKEN)
f2.pack(side=LEFT)
f2Top = Frame(f2, width=400, height=350, bd=4, relief="raise")
f2Top.pack(side=TOP)
f2Bottom = Frame(f2, width=400, height=450,bd=4, relief="raise")
f2Bottom.pack(side=BOTTOM)

f3 = Frame(BottomMainFrame, width=400, height=770, bd=12, relief=SUNKEN)
f3.pack(side=RIGHT)

f3top = Frame(f3, width=400, height=770, bd=12, relief="raise")
f3top.pack(side=TOP)
f3bottom = Frame(f3, width=400, height=100, bd=12, relief="raise")
f3bottom.pack(side=BOTTOM)

# ========================================================================================================
#                                VARIABLES
#========================================================================================================
Receipt_Ref = StringVar()
DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%y"))

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var100 = IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var100.set(0)
# ========================================================================================================
#                                BOTTOM FRAME : FRAME 1 VARIABLES
#========================================================================================================
varFrite = StringVar()
varSaladee = StringVar()
varHamburger = StringVar()
varLibanais = StringVar()
varMakloub = StringVar()
varSandwichFromage = StringVar()
varSandwichEscalope = StringVar()
varSandwichThon = StringVar()

varFrite.set(0)
varSaladee.set(0)
varHamburger.set(0)
varLibanais.set(0)
varMakloub.set(0)
varSandwichFromage.set(0)
varSandwichEscalope.set(0)
varSandwichThon.set(0)
# ========================================================================================================
#                               BOTTOM FRAME : FRAME 2 TOP FRAME VARIABLES
#========================================================================================================
varChocoBrownie = StringVar()
varGlace = StringVar()
vartiramiso = StringVar()
varTarte = StringVar()
varCroissant = StringVar()

varChocoBrownie.set(0)
varGlace.set(0)
vartiramiso.set(0)
varTarte.set(0)
varCroissant.set(0)

#====================================BOTTOM FRAME : FRAME 2 BOTTOM FRAME VARIABLES==================================================
varTotal = StringVar()
varTVA = StringVar()
varServiceCharge = StringVar()
varPay = StringVar()
varPM = StringVar()
varTotal.set(0)
varTVA.set(0)
varServiceCharge.set(0)
varPay.set(0)

#====================================BOTTOM FRAME : FRAME 3 VARIABLES==================================================
varTea = StringVar()
varCola = StringVar()
varCoffee = StringVar()
varOrange = StringVar()
varWater= StringVar()
varChocolateShake = StringVar()
varFruitCocktail = StringVar()
varVanillaShake = StringVar()
varOreoKrusher = StringVar()

varTea.set(0)
varCoffee.set(0)
varCola.set(0)
varOrange.set(0)
varWater.set(0)
varChocolateShake.set(0)
varFruitCocktail.set(0)
varVanillaShake.set(0)
varOreoKrusher.set(0)


#================================================================================
#                       BUTTON FUNCTIONS
# ================================================================================

#========================EXIT FUNCTION======================================
def iExit():
    qExit = messagebox.askyesno("Restraunt Management","Do you want to quit ?")
    if qExit :
        root.destroy()
        return 
    
#========================RESET FUNCTION======================================

def Reset():
    varFrite.set(0)
    varSaladee.set(0)
    varHamburger.set(0)
    varLibanais.set(0)
    varMakloub.set(0)
    varSandwichFromage.set(0)
    varSandwichEscalope.set(0)
    varSandwichThon.set(0)
    varChocoBrownie.set(0)
    varGlace.set(0)
    vartiramiso.set(0)
    varTarte.set(0)
    varCroissant.set(0)
    varTotal.set(0)
    varTVA.set(0)
    varServiceCharge.set(0)
    varPay.set(0)
    varTea.set(0)
    varCoffee.set(0)
    varCola.set(0)
    varOrange.set(0)
    varWater.set(0)
    varChocolateShake.set(0)
    varFruitCocktail.set(0)
    varVanillaShake.set(0)
    varOreoKrusher.set(0)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)

    txtFrite.configure(state=DISABLED)
    txtSaladee.configure(state=DISABLED)
    txtHamburger.configure(state=DISABLED)
    txtLibanais.configure(state=DISABLED)
    txtMakloub.configure(state=DISABLED)
    txtSandwichFromage.configure(state=DISABLED)
    txtSandwichEscalope.configure(state=DISABLED)
    txSandwichThon.configure(state=DISABLED)
    txtChocoBrownie.configure(state=DISABLED)
    txtGlace.configure(state=DISABLED)
    txtTiramisu.configure(state=DISABLED)
    txtTarte.configure(state=DISABLED)
    txtCroissant.configure(state=DISABLED)
    txtTotal.configure(state=DISABLED)
    txtTVA.configure(state=DISABLED)
    txtServiceCharge.configure(state=DISABLED)
    txtpay.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)
    txtCoffee.configure(state=DISABLED)
    txtCola.configure(state=DISABLED)
    txtOrange.configure(state=DISABLED)
    txtWater.configure(state=DISABLED)
    txtChocolateShake.configure(state=DISABLED)
    txtOreoKrusher.configure(state=DISABLED)
    txtVanillaShake.configure(state=DISABLED)
    txtOreoKrusher.configure(state=DISABLED)




# ===============================================================
#                       RECEIPT FUMCTION
# ================================================================

def Receipt():
    roor = Tk()
    roor.geometry("600x700+0+0")

    f1 = Frame(roor, width = 1600, height = 700, bd = 12, relief = "raise")
    f1.pack()
    lblReceipt = Label(f1, font=('arial', 12, 'bold'), text="Receipt", bd=2, anchor='w')
    lblReceipt.grid(row=0, column=0, sticky=W)
    txtReceipt = Text(f1, width=64, height=35, bg="white", bd=8, font=('arial', 11, 'bold'))
    txtReceipt.grid(row=1, column=0)
    txtReceipt.delete("1.0", END)
    x = random.randint(1000, 500890)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ Receipt_Ref.get() + '\t\t\t' + DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t\t\t' + "No. of Items \n\n")
    txtReceipt.insert(END, 'Frite:\t\t\t\t\t' + varFrite.get() + "\n")
    txtReceipt.insert(END, 'Saladee: \t\t\t\t\t' + varSaladee.get() + "\n")
    txtReceipt.insert(END, 'HamBurger: \t\t\t\t\t' + varHamburger.get() + "\n")
    txtReceipt.insert(END, 'Libanais: \t\t\t\t\t' + varLibanais.get() + "\n")
    txtReceipt.insert(END, 'Makloub: \t\t\t\t\t' + varMakloub.get() + "\n")
    txtReceipt.insert(END, 'Sandwich Fromage: \t\t\t\t\t' + varSandwichFromage.get() + "\n")
    txtReceipt.insert(END, 'Sandwich Escalope: \t\t\t\t\t' + varSandwichEscalope.get() + "\n")
    txtReceipt.insert(END, 'Sandwich Thon: \t\t\t\t\t' + varSandwichThon.get() + "\n")
    txtReceipt.insert(END, 'Choco Brownie: \t\t\t\t\t' + varChocoBrownie.get() + "\n")
    txtReceipt.insert(END, 'Glace: \t\t\t\t\t' + varGlace.get() + "\n")
    txtReceipt.insert(END, 'tiramisu: \t\t\t\t\t' + vartiramiso.get() + "\n")
    txtReceipt.insert(END, 'Tarte: \t\t\t\t\t' + varTarte.get() + "\n")
    txtReceipt.insert(END, 'Croissant: \t\t\t\t\t' + varCroissant.get() + "\n")
    txtReceipt.insert(END, 'The: \t\t\t\t\t' + varTea.get() + "\n")
    txtReceipt.insert(END, 'Caffe: \t\t\t\t\t' + varCoffee.get() + "\n")
    txtReceipt.insert(END, 'Cola: \t\t\t\t\t' + varCola.get() + "\n")
    txtReceipt.insert(END, 'Jus Orange: \t\t\t\t\t' + varOrange.get() + "\n")
    txtReceipt.insert(END, 'H2O: \t\t\t\t\t' + varWater.get() + "\n")
    txtReceipt.insert(END, 'Chocolate Shake: \t\t\t\t\t' + varChocolateShake.get() + "\n")
    txtReceipt.insert(END, 'Cocktail Fruit: \t\t\t\t\t' + varFruitCocktail.get() + "\n")
    txtReceipt.insert(END, 'Vanilla Shake: \t\t\t\t\t' + varVanillaShake.get() + "\n")
    txtReceipt.insert(END, 'Oreo Krusher: \t\t\t\t\t' + varOreoKrusher.get() + "\n")
    txtReceipt.insert(END, '\nHT: \t\t' + varTotal.get() + "\n TVA:\t\t" + varTVA.get() +"\nService Charge:\t\t" + varServiceCharge.get() + "\nTotal Payble amount:\t\t" + varPay.get())
    roor.mainloop()


#================================================PRICE LIST=======================================
def price_list():
    roo = Tk()
    roo.geometry("600x700+0+0")
    roo.title("Price List")

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Frite", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Saladee", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Hamburger", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="12", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Libanais", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="3", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Makloub", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="6", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Sandwich Fromage", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="7", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Sandwich Escalope", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="7", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Sandwich Thon", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="7", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chocolate Brownie", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="13", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Glace", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="5", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tiramisu", fg="steel blue", anchor=W)
    lblinfo.grid(row=11, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="9", fg="steel blue", anchor=W)
    lblinfo.grid(row=11, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tarte", fg="steel blue", anchor=W)
    lblinfo.grid(row=12, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="5", fg="steel blue", anchor=W)
    lblinfo.grid(row=12, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Croissant", fg="steel blue", anchor=W)
    lblinfo.grid(row=13, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="3", fg="steel blue", anchor=W)
    lblinfo.grid(row=13, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="The", fg="steel blue", anchor=W)
    lblinfo.grid(row=14, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2", fg="steel blue", anchor=W)
    lblinfo.grid(row=14, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cafe", fg="steel blue", anchor=W)
    lblinfo.grid(row=15, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2", fg="steel blue", anchor=W)
    lblinfo.grid(row=15, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cola", fg="steel blue", anchor=W)
    lblinfo.grid(row=16, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2", fg="steel blue", anchor=W)
    lblinfo.grid(row=16, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Jus d'Orange", fg="steel blue", anchor=W)
    lblinfo.grid(row=17, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2", fg="steel blue", anchor=W)
    lblinfo.grid(row=17, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="H2O", fg="steel blue", anchor=W)
    lblinfo.grid(row=18, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2", fg="steel blue", anchor=W)
    lblinfo.grid(row=18, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chocolate Shake", fg="steel blue", anchor=W)
    lblinfo.grid(row=19, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="5", fg="steel blue", anchor=W)
    lblinfo.grid(row=19, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Oreo Krusher", fg="steel blue", anchor=W)
    lblinfo.grid(row=20, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=20, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Vanilla Shake", fg="steel blue", anchor=W)
    lblinfo.grid(row=21, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="5", fg="steel blue", anchor=W)
    lblinfo.grid(row=21, column=3)
    roo.mainloop()

# ===============================TOTAL FUNCTION===============================================
def TotalCost():
    m1 = float(varFrite.get())
    m2 = float(varSaladee.get())
    m3 = float(varHamburger.get())
    m4 = float(varLibanais.get())
    m5 = float(varMakloub.get())
    m6 = float(varSandwichFromage.get())
    m7 = float(varSandwichEscalope.get())
    m8 = float(varSandwichThon.get())
    m9 = float(varChocoBrownie.get())
    m10 = float(varGlace.get())
    m11 = float(vartiramiso.get())
    m12 = float(varTarte.get())
    m13 = float(varCroissant.get())
    m14 = float(varTea.get())
    m15 = float(varCola.get())
    m16 = float(varCoffee.get())
    m17 = float(varOrange.get())
    m18 = float(varWater.get())
    m19 = float(varChocolateShake.get())
    m20 = float(varVanillaShake.get())
    m21 = float(varOreoKrusher.get())

    iTotal = (m1*1 + m2*10 + m3*12 + m4*3 + m5*6 + m6*7 + m7*7 + m8*7 + m9*13 + m10*5 + m11*9 + m12*5 + m13*3 + m14*2 + m15*2 + m16*2 +
                 m17*2 + m18*2 + m19*5 + m20*5 + m21*10)

    striTotal = '$',str(iTotal)
    varTotal.set(striTotal)

    TVA = (12/100)*iTotal
    strTVA = '$',str(TVA)
    varTVA.set(strTVA)


    service_charge = 0.1*iTotal
    strService_charge = "$",str(service_charge)
    varServiceCharge.set(strService_charge)

    strPay = '$', str('%.2f'%(iTotal+TVA+service_charge))
    varPay.set(strPay)

#================================================================================
#                       CHECKBOX FUNCTION
# ================================================================================
def a():
    if var1.get() == 1:
        txtFrite.configure(state=NORMAL)
        varFrite.set("")
    elif var1.get() == 0:
        txtFrite.configure(state=DISABLED)
        varFrite.set("0")

def b():
    if var2.get() == 1:
        txtSaladee.configure(state=NORMAL)
        varSaladee.set("")
    elif var2.get() == 0:
        txtSaladee.configure(state=DISABLED)
        varSaladee.set("0")

def c():
    if var3.get() == 1:
        txtHamburger.configure(state=NORMAL)
        varHamburger.set("")
    elif var3.get() == 0:
        txtHamburger.configure(state=DISABLED)
        varHamburger.set("0")

def d():
    if var4.get() == 1:
        txtLibanais.configure(state=NORMAL)
        varLibanais.set("")
    elif var4.get() == 0:
        txtLibanais.configure(state=DISABLED)
        varLibanais.set("0")

def e():
    if var5.get() == 1:
        txtMakloub.configure(state=NORMAL)
        varMakloub.set("")
    elif var5.get() == 0:
        txtMakloub.configure(state=DISABLED)
        varMakloub.set("0")


def f():
    if var6.get() == 1:
        txtSandwichFromage.configure(state=NORMAL)
        varSandwichFromage.set("")
    elif var6.get() == 0:
        txtSandwichFromage.configure(state=DISABLED)
        varSandwichFromage.set("0")

def g():
    if var7.get() == 1:
        txtSandwichEscalope.configure(state=NORMAL)
        varSandwichEscalope.set("")
    elif var7.get() == 0:
        txtSandwichEscalope.configure(state=DISABLED)
        varSandwichEscalope.set("0")

def h():
    if var8.get() == 1:
        txSandwichThon.configure(state=NORMAL)
        varSandwichThon.set("")
    elif var8.get() == 0:
        txSandwichThon.configure(state=DISABLED)
        varSandwichThon.set("0")

def i():
    if var9.get() == 1:
        txtChocoBrownie.configure(state=NORMAL)
        varChocoBrownie.set("")
    elif var9.get() == 0:
        txtChocoBrownie.configure(state=DISABLED)
        varChocoBrownie.set("0")

def j():
    if var10.get() == 1:
        txtGlace.configure(state=NORMAL)
        varGlace.set("")
    elif var10.get() == 0:
        txtGlace.configure(state=DISABLED)
        varGlace.set("0")

def k():
    if var11.get() == 1:
        txtTiramisu.configure(state=NORMAL)
        vartiramiso.set("")
    elif var11.get() == 0:
        txtTiramisu.configure(state=DISABLED)
        vartiramiso.set("0")
        
def l():
    if var12.get() == 1:
        txtTarte.configure(state=NORMAL)
        varTarte.set("")
    elif var12.get() == 0:
        txtTarte.configure(state=DISABLED)
        varTarte.set("0")
        
def m():
    if var13.get() == 1:
        txtCroissant.configure(state=NORMAL)
        varCroissant.set("")
    elif var13.get() == 0:
        txtCroissant.configure(state=DISABLED)
        varCroissant.set("0")
        
def n():
    if var14.get() == 1:
        txtTea.configure(state=NORMAL)
        varTea.set("")
    elif var14.get() == 0:
        txtTea.configure(state=DISABLED)
        varTea.set("0")
        
def o():
    if var15.get() == 1:
        txtCola.configure(state=NORMAL)
        varCola.set("")
    elif var15.get() == 0:
        txtCola.configure(state=DISABLED)
        varCola.set("0")
        
def p():
    if var16.get() == 1:
        txtCoffee.configure(state=NORMAL)
        varCoffee.set("")
    elif var16.get() == 0:
        txtCoffee.configure(state=DISABLED)
        varCoffee.set("0")
        
def q():
    if var17.get() == 1:
        txtOrange.configure(state=NORMAL)
        varOrange.set("")
    elif var17.get() == 0:
        txtOrange.configure(state=DISABLED)
        varOrange.set("0")
        
def r():
    if var18.get() == 1:
        txtWater.configure(state=NORMAL)
        varWater.set("")
    elif var18.get() == 0:
        txtWater.configure(state=DISABLED)
        varWater.set("0")
        
def s():
    if var19.get() == 1:
        txtChocolateShake.configure(state=NORMAL)
        varChocolateShake.set("")
    elif var19.get() == 0:
        txtChocolateShake.configure(state=DISABLED)
        varChocolateShake.set("0")
        
def t():
    if var20.get() == 1:
        txtVanillaShake.configure(state=NORMAL)
        varVanillaShake.set("")
    elif var20.get() == 0:
        txtVanillaShake.configure(state=DISABLED)
        varVanillaShake.set("0")
        
def u():
    if var21.get() == 1:
        txtOreoKrusher.configure(state=NORMAL)
        varOreoKrusher.set("")
    elif var21.get() == 0:
        txtOreoKrusher.configure(state=DISABLED)
        varOreoKrusher.set("0")

#================================================================================
#                       FRAME 1
# ================================================================================

lblMeal = Label(f1top,font=("arial",25,'bold'), text="Fast Meal")
lblMeal.grid(row=0, column=0)

Frite = Checkbutton(f1top, text="Frite", variable=var1, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=a)
Frite.grid(row=1, column=0, sticky = W)
txtFrite = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varFrite, width=4, justify="right",state=DISABLED)
txtFrite.grid(row=1, column=1)

Salade = Checkbutton(f1top, text="Salade", variable=var2, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=b)
Salade.grid(row=2, column=0, sticky = W)
txtSaladee = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varSaladee, width=4, justify="right",state=DISABLED)
txtSaladee.grid(row=2, column=1)

Hamburger = Checkbutton(f1top, text="Hamburger", variable=var3, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=c)
Hamburger.grid(row=3, column=0, sticky = W)
txtHamburger = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varHamburger, width=4, justify="right",state=DISABLED)
txtHamburger.grid(row=3, column=1)

Libanais = Checkbutton(f1top, text="Libanais", variable=var4, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=d)
Libanais.grid(row=4, column=0, sticky = W)
txtLibanais = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varLibanais, width=4, justify="right",state=DISABLED)
txtLibanais.grid(row=4, column=1)

Makloub = Checkbutton(f1top, text="Makloub", variable=var5, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=e)
Makloub.grid(row=5, column=0, sticky = W)
txtMakloub = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varMakloub, width=4, justify="right",state=DISABLED)
txtMakloub.grid(row=5, column=1)

lblSpace = Label(f1top,text="\n")
lblSpace.grid(row=6, column=0)
lblSandwich = Label(f1top,font=("arial",25,'bold'), text="Sandwiches")
lblSandwich.grid(row=7, column=0)

SandwichFromage = Checkbutton(f1top, text="Sandwich Fromage", variable=var6, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=f)
SandwichFromage.grid(row=8, column=0, sticky = W)
txtSandwichFromage = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varSandwichFromage, width=4, justify="right",state=DISABLED)
txtSandwichFromage.grid(row=8, column=1)

SandwichEscalope = Checkbutton(f1top, text="Sandwich Escalope", variable=var7, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=g)
SandwichEscalope.grid(row=9, column=0, sticky = W)
txtSandwichEscalope = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varSandwichEscalope, width=4, justify="right",state=DISABLED)
txtSandwichEscalope.grid(row=9, column=1)

SandwichThon = Checkbutton(f1top, text="Sandwich Thon", variable=var8, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=h)
SandwichThon.grid(row=10, column=0, sticky = W)
txSandwichThon = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varSandwichThon, width=4, justify="right",state=DISABLED)
txSandwichThon.grid(row=10, column=1)

#lblSpace = Label(f1top,text="\n\n\n\n\n\n\n")
#lblSpace.grid(row=11, column=0)
btnReceipt=Button(f1bottom,padx=20,pady=2,bd=14,fg="black",font=('arial',16,'bold'),width=16,text="GENERATE RECEIPT", command = Receipt)
btnReceipt.grid(row=0,column=0)
#================================================================================
#                       FRAME 2 Top
# ================================================================================



lblMeal = Label(f2Top,font=("arial",25,'bold'), text="Desserts")
lblMeal.grid(row=0, column=0)

ChocoBrownie = Checkbutton(f2Top, text="Chocolate Brownie", variable=var9, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=i)
ChocoBrownie.grid(row=1, column=0, sticky = W)
txtChocoBrownie = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varChocoBrownie, width=4, justify="right",state=DISABLED)
txtChocoBrownie.grid(row=1, column=1)

Glace = Checkbutton(f2Top, text="Glace", variable=var10, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=j)
Glace.grid(row=2, column=0, sticky = W)
txtGlace = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varGlace, width=4, justify="right",state=DISABLED)
txtGlace.grid(row=2, column=1)

Tiramisu = Checkbutton(f2Top, text="Tiramisu", variable=var11, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=k)
Tiramisu.grid(row=3, column=0, sticky = W)
txtTiramisu = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = vartiramiso, width=4, justify="right",state=DISABLED)
txtTiramisu.grid(row=3, column=1)

Tarte = Checkbutton(f2Top, text="Tarte", variable=var12, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=l)
Tarte.grid(row=4, column=0, sticky = W)
txtTarte = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varTarte, width=4, justify="right",state=DISABLED)
txtTarte.grid(row=4, column=1)

Croissant = Checkbutton(f2Top, text="Croissant", variable=var13, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=m)
Croissant.grid(row=5, column=0, sticky = W)
txtCroissant = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varCroissant, width=4, justify="right",state=DISABLED)
txtCroissant.grid(row=5, column=1)


#================================================================================
#                       FRAME 2 BOTTOM
# ================================================================================



lblPaymentMethod = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Payment Method", bd=10, width=16, anchor='w')
lblPaymentMethod.grid(row=0,column=0)

cmbPaymentMethod = ttk.Combobox(f2Bottom, textvariable=varPM, state="readonly", font=("arial", 10, 'bold'), width=20)
cmbPaymentMethod['value']=('Cash','Paytm','Master Card','Visa Card','Debit Card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=0, column=1)

lblTotal = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Total", bd=10, width=16, anchor='e')
lblTotal.grid(row=2,column=1)
txtTotal = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varTotal, width=10, justify="right",state=DISABLED)
txtTotal.grid(row=2, column=2)


lblTVA = Label(f2Bottom, font=("arial", 18, 'bold'), text = "TVA @12%", bd=10, width=16, anchor='e')
lblTVA.grid(row=4,column=1)
txtTVA = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varTVA, width=10, justify="right",state=DISABLED)
txtTVA.grid(row=4, column=2)

lblServiceCharge = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Service Charge @10%", bd=10, width=16, anchor='e')
lblServiceCharge.grid(row=5,column=1)
txtServiceCharge = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varServiceCharge, width=10, justify="right",state=DISABLED)
txtServiceCharge.grid(row=5, column=2)


#======================================================================================================================
#                                     BUTTONS
#======================================================================================================================
btnprice=Button(f2Bottom,padx=20,pady=1, bd=14 ,fg="black",font=('arial' ,16,'bold'),width=5, text="PRICE LIST", command = price_list)
btnprice.grid(row=2, column=0)

btnTotal = Button(f2Bottom, padx=20, pady=1, bd=14, fg="black", font=("arial", 16, 'bold'), width=5,
                  text="TOTAL", command = TotalCost).grid(row=3, column=0)

btnReset=Button(f2Bottom,padx=20,pady=1,bd=14,fg="black",font=('arial',16,'bold'),width=5,text="RESET", command=Reset)
btnReset.grid(row=4,column=0)

btnExit=Button(f2Bottom,padx=20,pady=1,bd=14,fg="black",font=('arial',16,'bold'),width=5,text="EXIT", command = iExit)
btnExit.grid(row=5,column=0)



#================================================================================
#                       FRAME 3
# ================================================================================

lblDrinks = Label(f3top,font=("arial",25,'bold'), text="Drinks")
lblDrinks.grid(row=0, column=0)

Tea = Checkbutton(f3top, text="The", variable=var14, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=n)
Tea.grid(row=1, column=0, sticky = W)
txtTea = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varTea, width=4, justify="right",state=DISABLED)
txtTea.grid(row=1, column=1)

Cola = Checkbutton(f3top, text="Cola", variable=var15, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=o)
Cola.grid(row=2, column=0, sticky = W)
txtCola = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varCola, width=4, justify="right",state=DISABLED)
txtCola.grid(row=2, column=1)

Coffee = Checkbutton(f3top, text="Cafee", variable=var16, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=p)
Coffee.grid(row=3, column=0, sticky = W)
txtCoffee = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varCoffee, width=4, justify="right",state=DISABLED)
txtCoffee.grid(row=3, column=1)

Orange = Checkbutton(f3top, text="Orange Juice", variable=var17, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=q)
Orange.grid(row=4, column=0, sticky = W)
txtOrange = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varOrange, width=4, justify="right",state=DISABLED)
txtOrange.grid(row=4, column=1)

Water = Checkbutton(f3top, text="Mineral Water", variable=var18, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=r)
Water.grid(row=5, column=0, sticky = W)
txtWater = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varWater, width=4, justify="right",state=DISABLED)
txtWater.grid(row=5, column=1)

lblSpace = Label(f3top,text="\n\n")
lblSpace.grid(row=6, column=0)

lblShakes = Label(f3top,font=("arial",25,'bold'), text="Shakes & Krushers")
lblShakes.grid(row=7, column=0)

ChocolateShake = Checkbutton(f3top, text="Chocolate Shake", variable=var19, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=s)
ChocolateShake.grid(row=8, column=0, sticky = W)
txtChocolateShake = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varChocolateShake, width=4, justify="right",state=DISABLED)
txtChocolateShake.grid(row=8, column=1)

VanillaShake = Checkbutton(f3top, text="Vanilla Shake", variable=var20, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=t)
VanillaShake.grid(row=9, column=0, sticky = W)
txtVanillaShake = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varVanillaShake, width=4, justify="right",state=DISABLED)
txtVanillaShake.grid(row=9, column=1)

OreoKrusher = Checkbutton(f3top, text="Oreo Krusher", variable=var21, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=u)
OreoKrusher.grid(row=10, column=0, sticky = W)
txtOreoKrusher = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varOreoKrusher, width=4, justify="right",state=DISABLED)
txtOreoKrusher.grid(row=10, column=1)

#lblSpace = Label(f3top,text="\n\n\n\n\n")
#lblSpace.grid(row=11, column=0)

lblpay = Label(f3bottom, font=("arial", 18, 'bold'), text = "Total Payable Amount", fg="red", bd=10, width=16, anchor='e')
lblpay.grid(row=0, column=0)
txtpay = Entry(f3bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varPay, width=10, justify="right",state=DISABLED)
txtpay.grid(row=0, column=1)

root.mainloop()
