from tkinter import*

root=Tk()
root.title("Численность популяций")
root.geometry("450x450")
lb_neogr=Label(root,text="Неограниченный рост",width=51,bg="green")
lb_neogr.place(x=45,y=20)

lb_a=Label(root,text="a",bg="yellow",width=2)
lb_a.place(x=10,y=50)

ent_a=Entry(root,bg="white",width=10)
ent_a.place(x=45,y=50)

bt1=Button(root,text="Неограниченный рост",width=18)
bt1.place(x=110,y=50)

def neogr_rost(event):
    a = float(ent_a.get())
    N = int(ent_n.get())
    ent_x1 = int(lb_Xn4_otv.get())

    for i in range(N):
        ent_x1 = ent_x1*a

    lb_Xn1_otv["text"] = str(int(ent_x1))
        
bt1.bind("<Button-1>",neogr_rost)

lb_Xn1=Label(root,text="Xn",bg="yellow",width=2)
lb_Xn1.place(x=250,y=50)

lb_Xn1_otv=Label(root,bg="cyan",width=12)
lb_Xn1_otv.place(x=280,y=50)

lb_ogr=Label(root,text="Ограниченный рост",width=51,bg="green")
lb_ogr.place(x=45,y=80)

lb_b=Label(root,text="b",bg="yellow",width=2)
lb_b.place(x=10,y=110)

ent_b=Entry(root,bg="white",width=10)
ent_b.place(x=45,y=110)

bt2=Button(root,text="Ограниченный рост",width=18)
bt2.place(x=110,y=110)

lb_Xn2=Label(root,text="Xn",bg="yellow",width=2)
lb_Xn2.place(x=250,y=110)

lb_Xn2_otv=Label(root,bg="cyan",width=12)
lb_Xn2_otv.place(x=280,y=110)

lb_ogr2=Label(root,text="Ограниченный рост с отловом",width=51,bg="green")
lb_ogr2.place(x=45,y=140)

lb_a=Label(root,text="c",bg="yellow",width=2)
lb_a.place(x=10,y=170)

ent_c=Entry(root,bg="white",width=10)
ent_c.place(x=45,y=170)

bt3=Button(root,text="огр. рост c отловом",width=18)
bt3.place(x=110,y=170)

lb_Xn3=Label(root,text="Xn",bg="yellow",width=2)
lb_Xn3.place(x=250,y=170)


lb_Xn3_otv=Label(root,bg="cyan",width=12)
lb_Xn3_otv.place(x=280,y=170)

lb_ger=Label(root,text="Жертва-хищник",width=51,bg="green")
lb_ger.place(x=45,y=200)

lb_d=Label(root,text="d",bg="yellow",width=2)
lb_d.place(x=10,y=230)

ent_d=Entry(root,bg="white",width=5)
ent_d.place(x=35,y=230)

lb_f=Label(root,text="f",bg="yellow",width=2)
lb_f.place(x=75,y=230)

ent_f=Entry(root,bg="white",width=5)
ent_f.place(x=100,y=230)

lb_q=Label(root,text="q",bg="yellow",width=2)
lb_q.place(x=140,y=230)

ent_q=Entry(root,bg="white",width=5)
ent_q.place(x=165,y=230)

bt4=Button(root,text="Жертва-хищник",width=18)
bt4.place(x=202,y=230)

lb_Xn4=Label(root,text="Жер.",bg="yellow",width=3)
lb_Xn4.place(x=80,y=260)

lb_Xn4_otv=Label(root,bg="cyan",width=8)
lb_Xn4_otv.place(x=110,y=260)

lb_Yn=Label(root,text="Хищ.",bg="yellow",width=3)
lb_Yn.place(x=200,y=260)

lb_Yn_otv=Label(root,bg="cyan",width=8)
lb_Yn_otv.place(x=230,y=260)

lb_x1=Label(root,text="Жер.",bg="yellow",width=5)
lb_x1.place(x=10,y=290)

ent_x1=Entry(root,bg="white",width=6)
ent_x1.place(x=55,y=290)

lb_y1=Label(root,text="Хищ.",bg="yellow",width=5)
lb_y1.place(x=10,y=320)

ent_y1=Entry(root,bg="white",width=6)
ent_y1.place(x=55,y=320)

lb_n=Label(root,text="циклы",bg="yellow",width=2)
lb_n.place(x=10,y=350)

ent_n=Entry(root,bg="white",width=10)
ent_n.place(x=55,y=350)

bt=Button(root,text="График",width=8)
bt.place(x=40,y=380)

canv=Canvas(root,width=260,height=130,bg="cyan")
canv.place(x=140,y=300)


root.mainloop()
