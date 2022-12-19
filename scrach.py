def tab12():
    button12.destroy()
    base = Tk()
    base.geometry('1000x850')
    base.title("Registration Form")
    base.minsize(1000, 700)
    f1 = Frame(base, bg="#00004e", borderwidth=6)
    f1.pack(side="top", fill="x")

    labl_0 = Label(f1, text="St. Thomas' College of Engineering & Technology", fg="white", bg="#00004e", width=70,
                   font=("bold", 19))
    labl_0.pack(side="top", pady=5)

    labl_1 = Label(f1, text="""4, Diamond Harbour Road, Kidderpore, Kolkata - 700023
        Programmes (B.Tech in CSE, EE, ECE & IT) are NBA Accredited.""", fg="white", width=70, bg="#00004e",
                   font=(12))
    labl_1.pack(side="top")

    f2 = Frame(base, bg="#ffffff", borderwidth=10)
    f2.pack(side="top", fill="x", pady=5)
    f3 = Frame(base, bg="#D3D3D3")
    f3.place(x=10, y=120)

button12 = Button(base, text='NEXT', font=('Times_New_Roman,25'), command=tab12)
button12.place(x=850, y=700)
base.mainloop()
print("Result form is created seccussfully...")