from tkinter import *


#splach screen geometry ,image.
ishant_root = Tk()
ishant_root.geometry("600x300")
photo = PhotoImage(file="splash_Screen.png")
ishant_label = Label(image=photo)
ishant_label.pack()

def next_page():
    ishant_root.destroy()
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
    Programmes (B.Tech in CSE, EE, ECE & IT) are NBA Accredited.""", fg="white", width=70, bg="#00004e", font=(12))
    labl_1.pack(side="top")

    f2 = Frame(base, bg="#ffffff", borderwidth=10)
    f2.pack(side="top", fill="x", pady=5)
    f3 = Frame(base, bg="#D3D3D3")
    f3.place(x=10, y=120)

    f4 = Frame(base, bg="#D3D3D3")
    f4.place(x=10, y=120)
    labl_0 = Label(f4, text="CA marks for semester 2", fg="#00004e", bg="#D3D3D3", width=22, font=("bold", 14))
    labl_0.pack(side="left")

    # subject 1 sem 2
    sub1 = Label(base, text="Math", width=4, font=("arial", 12))
    sub1.place(x=40, y=160)
    mr1 = Entry(base)
    mr1.place(x=200, y=160)
    mr2 = Entry(base)
    mr2.place(x=360, y=160)
    mr3 = Entry(base)
    mr3.place(x=520, y=160)
    mr4 = Entry(base)
    mr4.place(x=680, y=160)
    outF1 = Label(base, text="/ 25", width=4, font=("arial", 12))
    outF1.place(x=820, y=160)

    # sublect 2 sem 2
    sub2 = Label(base, text="Chemistry", width=8, font=("arial", 12))
    sub2.place(x=40, y=200)
    mr5 = Entry(base)
    mr5.place(x=200, y=200)
    mr6 = Entry(base)
    mr6.place(x=360, y=200)
    mr7 = Entry(base)
    mr7.place(x=520, y=200)
    mr8 = Entry(base)
    mr8.place(x=680, y=200)
    outF1 = Label(base, text="/ 25", width=4, font=("arial", 12))
    outF1.place(x=820, y=200)

    # subject 3 sem 2
    sub3 = Label(base, text="PPS", width=4, font=("arial", 12))
    sub3.place(x=40, y=240)
    mr9 = Entry(base)
    mr9.place(x=200, y=240)
    mr10 = Entry(base)
    mr10.place(x=360, y=240)
    mr11 = Entry(base)
    mr11.place(x=520, y=240)
    mr12 = Entry(base)
    mr12.place(x=680, y=240)
    outF1 = Label(base, text="/ 25", width=4, font=("arial", 12))
    outF1.place(x=820, y=240)

    # subject 4 sem 2
    sub31 = Label(base, text="English", width=5, font=("arial", 12))
    sub31.place(x=40, y=280)
    mr91 = Entry(base)
    mr91.place(x=200, y=280)
    mr101 = Entry(base)
    mr101.place(x=360, y=280)
    mr110 = Entry(base)
    mr110.place(x=520, y=280)
    mr120 = Entry(base)
    mr120.place(x=680, y=280)
    outF1 = Label(base, text="/ 25", width=4, font=("arial", 12))
    outF1.place(x=820, y=280)

    def display_math():
        t = int(mr1.get())
        e = int(mr2.get())
        m = int(mr3.get())
        s = int(mr4.get())
        if (t > e and t > m and t > s):
            return t
        elif (e > t and e > m and e > s):
            return e
        elif (m > t and m > s and m > e):
            return m
        else:
            return s
    def display_chemistry():
        t = int(mr5.get())
        e = int(mr6.get())
        m = int(mr7.get())
        s = int(mr8.get())
        if (t > e and t > m and t > s):
            return t
        elif (e > t and e > m and e > s):
            return e
        elif (m > t and m > s and m > e):
            return m
        else:
            return s
    def display_PPS():
        t = int(mr9.get())
        e = int(mr10.get())
        m = int(mr11.get())
        s = int(mr12.get())
        if (t > e and t > m and t > s):
            return t
        elif (e > t and e > m and e > s):
            return e
        elif (m > t and m > s and m > e):
            return m
        else:
            return s
    def display_english():
        t = int(mr91.get())
        e = int(mr101.get())
        m = int(mr110.get())
        s = int(mr120.get())
        if (t > e and t > m and t > s):
            return t
        elif (e > t and e > m and e > s):
            return e
        elif (m > t and m > s and m > e):
            return m
        else:
            return s

    f5 = Frame(base, bg="#D3D3D3")
    f5.place(x=10, y=330)
    labl_0 = Label(f5, text="PCA marks for semester 2", fg="#00004e", bg="#D3D3D3", width=22, font=("bold", 14))
    labl_0.pack(side="left")

    f8 = Frame(base, bg="#D3D3D3")
    f8.place(x=550, y=330)
    labl_08 = Label(f8, text="PCA Final marks for semester 2", fg="#00004e", bg="#D3D3D3", width=25, font=("bold", 14))
    labl_08.pack(side="right")

    # subject 1 sem 1
    sub1 = Label(base, text="Chemsitry Laboratory", width=16, font=("arial", 12))
    sub1.place(x=40, y=380)
    mr13 = Entry(base)
    mr13.place(x=200, y=380)
    mr14 = Entry(base)
    mr14.place(x=360, y=380)
    outF1 = Label(base, text="/ 40", width=4, font=("arial", 12))
    outF1.place(x=490, y=380)
    sub1 = Label(base, text="Chemsitry Laboratory", width=16, font=("arial", 12))
    sub1.place(x=550, y=380)
    mr103 = Entry(base)
    mr103.place(x=730, y=380)
    outF1 = Label(base, text="/ 60", width=4, font=("arial", 12))
    outF1.place(x=820, y=380)

    def display_workprac():
        t = int(mr13.get())
        e = int(mr14.get())
        if (t > e):
            return t
        else:
            return e

    def display_workprac_lab_final():
        q = int(mr103.get())
        return q

    # sublect 2 sem 1
    sub2 = Label(base, text="Language Laboratory", width=16, font=("arial", 12))
    sub2.place(x=40, y=420)
    mr15 = Entry(base)
    mr15.place(x=200, y=420)
    mr16 = Entry(base)
    mr16.place(x=360, y=420)
    outF1 = Label(base, text="/ 40", width=4, font=("arial", 12))
    outF1.place(x=490, y=420)
    sub2 = Label(base, text="Language Laboratory", width=16, font=("arial", 12))
    sub2.place(x=550, y=420)
    mr105 = Entry(base)
    mr105.place(x=730, y=420)
    outF1 = Label(base, text="/ 60", width=4, font=("arial", 12))
    outF1.place(x=820, y=420)

    def display_phylab():
        t = int(mr15.get())
        e = int(mr16.get())
        if (t > e):
            return t
        else:
            return e

    def display_physics_lab_final():
        wp = int(mr105.get())
        return wp

    # subject 3 sem 1
    sub3 = Label(base, text="PPS Laboratory", width=12, font=("arial", 12))
    sub3.place(x=40, y=460)
    mr17 = Entry(base)
    mr17.place(x=200, y=460)
    mr18 = Entry(base)
    mr18.place(x=360, y=460)
    outF1 = Label(base, text="/ 40", width=4, font=("arial", 12))
    outF1.place(x=490, y=460)
    sub3 = Label(base, text="PPS Laboratory", width=13, font=("arial", 12))
    sub3.place(x=550, y=460)
    mr107 = Entry(base)
    mr107.place(x=730, y=460)
    outF1 = Label(base, text="/ 60", width=4, font=("arial", 12))
    outF1.place(x=820, y=460)

    def display_BEElab():
        t = int(mr17.get())
        e = int(mr18.get())
        if (t > e):
            return t
        else:
            return e

    def display_BEE_lab_final():
        u = int(mr107.get())
        return u

        # subject 3 sem 1

    sub3 = Label(base, text="Engineering Drawing", width=16, font=("arial", 12))
    sub3.place(x=40, y=500)
    mr171 = Entry(base)
    mr171.place(x=200, y=500)
    mr181 = Entry(base)
    mr181.place(x=360, y=500)
    outF1 = Label(base, text="/ 40", width=4, font=("arial", 12))
    outF1.place(x=490, y=500)
    sub3 = Label(base, text="Engineering Drawing", width=17, font=("arial", 12))
    sub3.place(x=550, y=500)
    mr1071 = Entry(base)
    mr1071.place(x=730, y=500)
    outF1 = Label(base, text="/ 60", width=4, font=("arial", 12))
    outF1.place(x=820, y=500)

    def display_EDlab():
        t = int(mr171.get())
        e = int(mr181.get())
        if (t > e):
            return t
        else:
            return e

    def display_ED_lab_final():
        u = int(mr1071.get())
        return u

    f6 = Frame(base, bg="#D3D3D3")
    f6.place(x=10, y=540)
    labl_0 = Label(f6, text="Final Exam", fg="#00004e", bg="#D3D3D3", width=12, font=("bold", 14))
    labl_0.pack(side="left")

    # FINAL MARKS OUY OF 70 IN sem 1
    # MATH
    Fsub1 = Label(base, text="Math", width=3, font=("arial", 12))
    Fsub1.place(x=40, y=660)
    fmr1 = Entry(base)
    fmr1.place(x=200, y=660)
    outF1 = Label(base, text="/ 70", width=4, font=("arial", 12))
    outF1.place(x=300, y=660)

    def final_math():
        ft = int(fmr1.get())
        return ft

    # ATTENDANCE
    Asub1 = Label(base, text="ATTENDANCE", width=14, font=("arial", 12))
    Asub1.place(x=400, y=580)
    fmr12 = Entry(base)
    fmr12.place(x=550, y=580)
    outF12 = Label(base, text="/ 5", width=4, font=("arial", 12))
    outF12.place(x=635, y=580)

    def final_attendance():
        ft2 = int(fmr12.get())
        return ft2

    # BEE
    Fsub1 = Label(base, text="Chemistry", width=7, font=("arial", 12))
    Fsub1.place(x=40, y=580)
    fmr2 = Entry(base)
    fmr2.place(x=200, y=580)
    outF2 = Label(base, text="/ 70", width=4, font=("arial", 12))
    outF2.place(x=300, y=580)

    def final_chemistry():
        fs = int(fmr2.get())
        return fs

    # Physics
    sub2 = Label(base, text="PPS", width=3, font=("arial", 12))
    sub2.place(x=40, y=620)
    fmr3 = Entry(base)
    fmr3.place(x=200, y=620)
    outF3 = Label(base, text="/ 70", width=4, font=("arial", 12))
    outF3.place(x=300, y=620)

    def final_pps():
        fd = int(fmr3.get())
        return fd

    # english
    sub2 = Label(base, text="English", width=5, font=("arial", 12))
    sub2.place(x=40, y=700)
    fmr31 = Entry(base)
    fmr31.place(x=200, y=700)
    outF31 = Label(base, text="/ 70", width=4, font=("arial", 12))
    outF31.place(x=300, y=700)

    def final_english():
        fd = int(fmr31.get())
        return fd


    # Calculating marks out of 100
    def display_final_math_sem1():
        mathf = final_math()
        mathca = display_math()
        math_att = final_attendance()

        total = mathf + mathca + math_att
        return total

    def display_final_chemistry_sem1():
        physicf = display_chemistry()
        physicca = final_chemistry()
        physic_att = final_attendance()

        total1 = physicf + physicca + physic_att
        return total1

    def display_final_PPS_sem1():
        BEEf = display_PPS()
        BEEca = final_pps()
        BEE_att = final_attendance()

        total2 = BEEf + BEEca + BEE_att
        return total2

    def display_final_ENG_sem1():
        BEEf = display_english()
        BEEca = final_english()
        BEE_att = final_attendance()

        total3 = BEEf + BEEca + BEE_att
        return total3


    def display_final_workshoppractical_sem1():
        wfinal1 = display_workprac()
        wfinal2 = display_workprac_lab_final()

        final_workprac1 = wfinal1 + wfinal2
        return final_workprac1

    def display_final_physicslab_sem1():
        wfinal1 = display_phylab()
        wfinal2 = display_physics_lab_final()

        final_workprac2 = wfinal1 + wfinal2
        return final_workprac2

    def display_final_BEElab_sem1():
        wfinal1 = display_BEElab()
        wfinal2 = display_BEE_lab_final()

        final_workprac3 = wfinal1 + wfinal2
        return final_workprac3

    def display_final_EDlab_sem1():
        wfinal1 = display_EDlab()
        wfinal2 = display_ED_lab_final()

        final_workprac4 = wfinal1 + wfinal2
        l3 = Label(base, text=str(final_workprac4))
        l3.place(x=500, y=460)

    button46 = Button(base, text="Calculate", bg="green", command=display_final_EDlab_sem1)
    button46.place(x=540, y=460)
        # return final_workprac3

    def Calculation(marks):
        if marks >= 90 and marks <= 100:
            Grade = 'O'
            Point = 10

        elif marks >= 80 and marks <= 89:
            Grade = 'E'
            Point = 9

        elif marks >= 70 and marks <= 79:
            Grade = 'A'
            Point = 8

        elif marks >= 60 and marks <= 69:
            Grade = 'B'
            Point = 7

        elif marks >= 50 and marks <= 59:
            Grade = 'C'
            Point = 6

        elif marks >= 40 and marks <= 49:
            Grade = 'D'
            Point = 5

        elif marks <= 40:
            Grade = 'F'
            Point = 2

        else:
            Grade = 'I'
            Point = 2

        print('Grade: ', Grade)
        print('Point: ', Point)
        return Point

    def tab2():
        button1.destroy()
        next_page()
    button1 = Button(base, text='Generate',bg="green" ,font=('Times_New_Roman,25'), command=tab2)
    button1.place(x=850,y=700)
    base.mainloop()
    print("Result form is created seccussfully...")

#Splash screen timer
ishant_root.after(3000, next_page())

mainloop()