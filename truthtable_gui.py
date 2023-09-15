from tkinter import*;


root=Tk()

label2=Label(root,text="only for Ece guys ",font=("algerian",20))
label2.pack()
root.geometry("500x500")
root.title("Logical expression Truth table generator")
root.iconbitmap("favicon.ico")
text=Label(text="Enter logical expression")
text.pack()
input=Entry(borderwidth=7)
input.pack()

def tt():
    ex=input.get()
    ex=ex.replace("and",'&')
    ex=ex.replace("or",'|')
    ex=ex.replace("not",'~')
    ex1=Label(text=f"Expression is:{ex}",font=15)
    ex1.pack()
    
    
    text1=Label(text="Truth Table:",font=15)
    text1.pack()
    text2=Label(text="P Q R Y",font=12)
    text2.pack()
    
    X=[]
    for p in range(0,2):
        for q in range(0,2):
            for r in range(0,2):
                expr = ex.replace("P", str(p)).replace("Q", str(q)).replace("R", str(r))
                x=abs(eval(expr))
                X.append(x)
                label_tex=f"{str(p)} {str(q)} {str(r)} {str(x)}"
                label=Label(root,text=label_tex,fg="red",font=("algerian",20))
                label.pack()
                
    
my_button=Button(text="Generate truth table",command=tt,bg="blue",font=20,borderwidth=5)
my_button.pack()
root.mainloop()




