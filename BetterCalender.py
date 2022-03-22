from glob import glob
import tkinter as tk
from tkinter import ttk
import datetime
from math import floor

columnnumber = 0
rownumber = 0

def Day(nunbertext):
    # root window
    dayroot = tk.Tk()
    dayroot.geometry('500x200')
    dayroot.resizable(False, False)
    dayroot.title('Button Demo')

    # exit button
    exit_button = ttk.Button(
        dayroot,
        text=nunbertext,
        command=lambda: print(nunbertext)
    )

    exit_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    dayroot.mainloop()

def screenmaker(root,window_width, window_height):
       # get the screen dimension

       screen_width = root.winfo_screenwidth()
       screen_height = root.winfo_screenheight()
       # find the center point
       center_x = int(screen_width/2 - window_width / 2)
       center_y = int(screen_height/2 - window_height / 2)
       # set the position of the window to the center of the screen
       root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def Calender(nameofthemonth):
    global columnnumber
    global rownumber
    monthlist = ["itstoday","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October","Novemeber", "December"]
    # root window
    root = tk.Tk()
    screenmaker(root,985,500)

    #700 wide is poggers
    root.title('Calender')
    root.resizable(0, 0)

    # configure the grid
    root.columnconfigure(0, weight=0)


        #Title                                   #f string for the month name
    
    #Calender_label.grid(column=0, row=0, sticky=tk.EW)
    monthname = "{}"
    Calender_label = ttk.Label(root,text=monthname.format(monthlist[nameofthemonth]), font=("Comic Sans", 20),)
    Calender_label.grid(column=3, row=0,sticky=tk.NS,)
        
        

    #Makes the Days
    week = ("Sunday","Monday", "Tuesday", "Wednessday","Thursday", "Friday","Saturday")
    for i in range(7):
        Day_label = ttk.Label(root, text=week[i],)
        Day_label.grid(column=i+0, row=1, )

    #Makes the Calender



    #need a thing to put spacers
    b = 0
    columnnumber = 0
    rownumber = 0

    def dayButtonMaker(i):
        dayButton = ttk.Button(root, text="\n" + str( i ) + "\n",width=20,command = lambda: Day(i) )
        dayButton.grid(column=columnnumber, row=rownumber+2, padx= 5, pady =5)

    def spacingChecker():
        global columnnumber
        global rownumber
        if (columnnumber == 6):
            columnnumber = 0
            rownumber += 1
        else:
            columnnumber += 1

    def Bofa(ii):
        dayButtonMaker(ii)
        spacingChecker()


    todaysDate = datetime.datetime.now()

    if (nameofthemonth == 1):
        todaysYear = int(todaysDate.strftime("%y")) - 1
        numberYear = 11
    elif ((nameofthemonth == 2)):
        todaysYear = int(todaysDate.strftime("%y")) - 1
        numberYear = 12
    else:
        todaysYear = int(todaysDate.strftime("%y"))
        numberYear = nameofthemonth - 2


    print(todaysYear)
    print(numberYear)

    W = (floor(2.6 * (numberYear) - 0.2) - 34 + todaysYear + floor(todaysYear/4) ) % 7
    print(W)
    for i in range(W):
        spacerLabel = ttk.Label(root, )
        spacerLabel.grid(column = columnnumber, row = rownumber + 2)
        columnnumber += 1


    for i in range(28):
        Bofa(i+1)
    # Bofa(1)
    # Bofa(2)
    # Bofa(3)
    # Bofa(4)
    # Bofa(5)
    # Bofa(6)
    # Bofa(7)


    # Bofa(8)
    # Bofa(9)
    # Bofa(10)
    # Bofa(11)
    # Bofa(12)
    # Bofa(13)
    # Bofa(14)

    # Bofa(15)
    # Bofa(16)
    # Bofa(17)
    # Bofa(18)
    # Bofa(19)
    # Bofa(20)
    # Bofa(21)
    # Bofa(22)

    # Bofa(23)
    # Bofa(24)
    # Bofa(25)
    # Bofa(26)
    # Bofa(27)
    # Bofa(28)

    if (nameofthemonth == 2):
        pass
    elif (nameofthemonth == 1):
        Bofa(29)
        Bofa(30)
        Bofa(31)
    elif (nameofthemonth%2 == 1):
        if (nameofthemonth < 8):
            Bofa(29)
            Bofa(30)
            Bofa(31)
        else:
            Bofa(29)
            Bofa(30)
    elif (nameofthemonth %2 == 0):
        if nameofthemonth < 7:
            Bofa(29)
            Bofa(30)
        else:
            Bofa(29)
            Bofa(30)
            Bofa(31)
    
   

   #need a thing to fix end bits

    root.iconbitmap('poggers.ico')
    root.mainloop()              

Calender(9)