from tkinter import *

# splach screen geometry ,image.
ishant_root = Tk()
ishant_root.geometry("1000x900")

lb156 = Label(ishant_root, text="Subjects Offered       \t    Letter Grade     \t      Points    \t     Credits     \t    Credit Points", width=90, font=("bold", 13))
lb156.place(x=90, y=380)
lb106 = Label(ishant_root,text=f"physics  \t                            \t 4                           5                             5                                35 ", width=90, font=("bold", 13))
lb106.place(x=90, y=420)
mainloop()