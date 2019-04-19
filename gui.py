from practice import *
from tkinter import *
from tkinter import messagebox

studll=DLL()

def sel():
   print ("POP")
   #selection = "You selected the option " + str(br.get())
   
   #label.config(text = selection)


def quit_(event):
   print ("Quiting")
   import sys
   sys.exit()

lib=Tk()
lib.geometry("1280x720")
lib.focus_force()
lib.resizable(0,0)
lib.title('LIBRARY MANAGEMENT SYSTEM')


def fetch_student(event):
   reg_stud=Toplevel(lib)
   reg_stud.geometry("800x720")
   reg_stud.focus_force()
   reg_stud.resizable(0,0)
   reg_stud.title('LIBRARY MANAGEMENT SYSTEM : TEACHERs MENU / REGISTER A STUDENT')
   reg_stud.config(background="Sky Blue")
   
   lbf=LabelFrame(reg_stud,text="yup")
   lbf.pack(fill="both",expand="yes")
   
   namlabel=Label(lbf,text=" NAME ")
   namlabel.pack()
   nam=Entry(lbf,textvariable=" NAME ",bg="Sky Blue",fg="Green")
   nam.pack()
   prnlabel=Label(lbf,text=" PRN ")
   prnlabel.pack()
   prn_=Entry(lbf,textvariable=" PRN ",bg="Sky Blue",fg="Green")
   prn_.pack()
   br_label=Label(lbf,text="branch")
   br_label.pack()
   br=Entry(lbf,textvariable="Branch")
   br.pack()
   
   
   emaillabel=Label(lbf,text=" EMAIL ")
   emaillabel.pack()
   eml=Entry(lbf,textvariable=" EMAIL",bg="Sky Blue",fg="Green")
   eml.pack()
   
   def reg_student():        
      try:
         name = nam.get()
         prn = prn_.get()
   
         email=eml.get()  
         branch=br.get()
      
         studll.add(Student(name,prn,branch,email))
         messagebox.showinfo("Confirmation",str(nam.get())+" IS REGISTERED ")
      except Exception as e:
         messagebox.showinfo("Error"," error encountered "+str(e))
         
   
   CBT=Button(lbf,text=" REGISTER ",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command=reg_student,bd=1)
   CBT.pack(anchor=CENTER)
   

   reg_stud.mainloop()

def del_student(event):
   del_stud=Toplevel(lib)
   del_stud.geometry("800x720")
   del_stud.focus_force()
   del_stud.resizable(0,0)
   del_stud.title('LIBRARY MANAGEMENT SYSTEM : TEACHERs MENU / DELETE A STUDENT')
   del_stud.config(background="Sky Blue")
   frame=Frame(del_stud)
   frame.pack(anchor=CENTER)
   l1=Label(frame,text="PRN")
   l1.pack()
   prn_=Entry(frame,textvariable=" PRN",bg="Sky Blue",fg="Green")
   prn_.pack()

   def del_stu():
      studll.remove(prn_.get())
      messagebox.showinfo("Confirmation",str(prn_.get())+" IS DELETED FROM THE LIST")
   
   b1=Button(frame,text=" DELETE ",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command=del_stu,bd=1)
   b1.pack(anchor=CENTER)
   
   del_stud.mainloop()


def display_student(event):
   teacher_window = Toplevel(lib)
   teacher_window.geometry("800x720")
   teacher_window.focus_force()
   teacher_window.resizable(0,0)
   teacher_window.title('LIBRARY MANAGEMENT SYSTEM : TEACHERs MENU')
   teacher_window.config(background="Sky Blue")

   frame=Frame(teacher_window)
   frame.pack(anchor=CENTER)
   res=studll.display()
   text1=Text(frame)
   text1.pack()
   text1.insert(END,res)
   teacher_window.mainloop()


def add_book_in_lib(event):
   ab=Toplevel(lib)
   ab.geometry("800x720")
   ab.focus_force()
   ab.resizable(0,0)
   ab.title('LIBRARY MANAGEMENT SYSTEM : TEACHERs MENU / REGISTER A STUDENT')
   ab.config(background="Sky Blue")
   
   lbf=LabelFrame(ab,text="yup")
   lbf.pack(fill="both",expand="yes")
   
   namlabel=Label(lbf,text=" NAME OF THE BOOK :")
   namlabel.pack()
   namb=Entry(lbf,textvariable=" NAME ",bg="Sky Blue",fg="Green")
   namb.pack()
   author_name=Label(lbf,text=" AUTHOR NAME ")
   author_name.pack()
   an=Entry(lbf,textvariable=" AUTHOR NAME ",bg="Sky Blue",fg="Green")
   an.pack()
   quanl=Label(lbf,text=" QUANTITY")
   quanl.pack()
   quan=Entry(lbf,textvariable=" QUANTITY ")
   quan.pack()
   def add_book_m():
      try:
         name=namb.get()
         authorname=an.get()
         quantity=quan.get()
         
         books_data.add_book(name,authorname,quantity)
         messagebox.showinfo("Confirmation",str(name)+" BOOK ADDED ")
      except Exception as e:
         messagebox.showinfo("ERROR","Error encountered "+str(e))
   b1=Button(lbf,text=" ADD BOOK ",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command=add_book_m,bd=1)
   b1.pack(anchor=CENTER)
   ab.mainloop()
   


def fetch_book_holders(event):
   ab=Toplevel(lib)
   ab.geometry("800x720")
   ab.focus_force()
   ab.resizable(0,0)
   ab.title('LIBRARY MANAGEMENT SYSTEM : TEACHERs MENU / BOOK HOLDERS DETAILS')
   ab.config(background="Sky Blue")
   
   lbf=LabelFrame(ab,text="yup")
   lbf.pack(fill="both",expand="yes")
   
   namlabel=Label(lbf,text=" NAME OF THE BOOK :")
   namlabel.pack()
   namb=Entry(lbf,textvariable=" NAME ",bg="Sky Blue",fg="Green")
   namb.pack()
   
   def search_book_holder():
      res=books_holders_data(namb.get())
      frame=Frame(ab)
      frame.pack(anchor=CENTER)
      text1=Text(frame)
      text1.pack()
      text1.insert(END,res)
   


   b1=Button(lbf,text=" SEARCH ",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command=search_book_holder,bd=1)
   b1.pack(anchor=CENTER)
   ab.mainloop()
    

def teacher(event):
   teacher_window = Toplevel(lib)
   teacher_window.geometry("800x720")
   teacher_window.focus_force()
   teacher_window.resizable(0,0)
   teacher_window.title('LIBRARY MANAGEMENT SYSTEM : TEACHERs MENU')
   teacher_window.config(background="Sky Blue")

   frame=Frame(teacher_window)
   frame.pack(anchor=CENTER)
   
   rt1=Button(frame,text=" REGISTER A NEW STUDENT")
   rt1.pack( anchor = CENTER )
   rt1.bind('<Button-1>',fetch_student)
   rt2=Button(frame,text=" Delete A STUDENT")
   rt2.pack( anchor = CENTER )
   rt2.bind('<Button-1>',del_student)
   rt3=Button(frame,text=" SEE ALL THE STUDENT")
   rt3.pack( anchor = CENTER )
   rt3.bind('<Button-1>',display_student)
   rt4=Button(frame,text=" ADD BOOKS")
   rt4.pack( anchor = CENTER )
   rt4.bind('<Button-1>',add_book_in_lib)
   rt5=Button(frame,text=" SEE CURRENT BOOK HOLDERS DETAILS")
   rt5.pack( anchor = CENTER )
   rt5.bind('<Button-1>',fetch_book_holders)
   teacher_window.mainloop()


def explore_lib(event):
   res=books_data.show_books()
   teacher_window = Toplevel(lib)
   teacher_window.geometry("800x720")
   teacher_window.focus_force()
   teacher_window.resizable(0,0)
   teacher_window.title('LIBRARY MANAGEMENT SYSTEM : STUDENTs MENU : SEE YOUR STATUS')
   teacher_window.config(background="Sky Blue")

   frame=Frame(teacher_window)
   frame.pack(anchor=CENTER)
   
   text1=Text(frame)
   text1.pack()
   text1.insert(END,res)
   teacher_window.mainloop()
      


def student_win(event):
   stu_window = Toplevel(lib)
   stu_window.geometry("800x720")
   stu_window.focus_force()
   stu_window.resizable(0,0)
   stu_window.title('LIBRARY MANAGEMENT SYSTEM')
   stu_window.config(background="Sky Blue")
   frame1=Frame(stu_window)
   frame1.pack(anchor=CENTER)
   l1=Label(frame1,text=" PRN ")
   l1.pack()
   prn1=Entry(frame1,textvariable="PRN")
   prn1.pack()
   
   def can_enter():
      stu_adr=studll.search(prn1.get())
      if stu_adr is not None:
         frame=Frame(stu_window)
         frame.pack(anchor=CENTER)

         

         rt1=Button(frame,text=" EXPLORE THE LIBRARY ")
         rt1.pack( anchor = CENTER )
         rt1.bind('<Button-1>',explore_lib)
         
         def take_book(event):
            tkb=Toplevel(lib)
            tkb.geometry("800x720")
            tkb.focus_force()
            tkb.resizable(0,0)
            tkb.title('LIBRARY MANAGEMENT SYSTEM')
            tkb.config(background="Sky Blue")
            frame1=Frame(tkb)
            frame1.pack(anchor=CENTER)
            l1=Label(frame1,text=" BOOK NAME ")
            l1.pack()
            bk=Entry(frame1,textvariable="BOOK NAME")
            bk.pack()
            def issue_book():
               res=library.issue_book(stu_adr,bk.get())
               if len(res) < 3 :
                  messagebox.showinfo("Confirmation",str(bk.get())+" ISSUED")
               else:
                  messagebox.showinfo("NOT ISSUES",res)

            CBS1=Button(frame1,text=" Confirm BOOK NAME ",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command= issue_book , bd=1)
            CBS1.pack(anchor=CENTER)
            

         
         rt2=Button(frame,text=" TAKE A BOOK")
         rt2.pack( anchor = CENTER )
         rt2.bind('<Button-1>',take_book)

         def return_book(event):
            tkb=Toplevel(lib)
            tkb.geometry("800x720")
            tkb.focus_force()
            tkb.resizable(0,0)
            tkb.title('LIBRARY MANAGEMENT SYSTEM')
            tkb.config(background="Sky Blue")
            frame1=Frame(tkb)
            frame1.pack(anchor=CENTER)
            l1=Label(frame1,text=" BOOK NAME ")
            l1.pack()
            bk=Entry(frame1,textvariable="BOOK NAME")
            bk.pack()
            def return_b():
               res=library.return_book(stu_adr,bk.get())
               if len(res) < 3 :
                  messagebox.showinfo("Confirmation",str(bk.get())+" RETURNED ")
               else:
                  messagebox.showinfo("NOT ISSUES",res)

            CBS1=Button(frame1,text=" Confirm BOOK NAME ",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command= return_b , bd=1)
            CBS1.pack(anchor=CENTER)
            


         rt3=Button(frame,text=" RETURN A BOOK")
         rt3.pack( anchor = CENTER )
         rt3.bind('<Button-1>',return_book)

         def status(event):
            teacher_window = Toplevel(lib)
            teacher_window.geometry("800x720")
            teacher_window.focus_force()
            teacher_window.resizable(0,0)
            teacher_window.title('LIBRARY MANAGEMENT SYSTEM : STUDENTs MENU : SEE YOUR STATUS')
            teacher_window.config(background="Sky Blue")

            frame=Frame(teacher_window)
            frame.pack(anchor=CENTER)
            res=str(stu_adr.books_issued)
            text1=Text(frame)
            text1.pack()
            text1.insert(END,res)
            teacher_window.mainloop()
      

         rt4=Button(frame,text=" SEE YOUR STATUS")
         rt4.pack( anchor = CENTER )
         rt4.bind('<Button-1>',status)
         
         rt5=Button(frame,text=" EXIT ")
         rt5.pack( anchor = CENTER )
         rt5.bind('<Button-1>',quit_)

      else:
         messagebox.showinfo("NOT FOUND",str(prn1.get())+" NOT FOUND \n REGISTER AND COMEBACK AGAIN")
      
      
      

   CBS=Button(frame1,text=" Confirm PRN ",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command= can_enter , bd=1)
   CBS.pack(anchor=CENTER)

   """
   CBS=Button(frame,text=" Confirm Choice ",font=("Liberation Sans",9,"bold"),bg=" green ",fg=" white ",command= choice_sel_s , bd=1)
   CBS.pack(anchor=CENTER)
"""
   stu_window.mainloop()



filename = PhotoImage(file="libr.png")
background_label = Label(lib, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



teacher_button=Button(lib,text="TEACHERS Click Here ",height=20,width=50,bg="yellow")
teacher_button.pack()
teacher_button.bind('<Button-1>',teacher)



student_button=Button(lib,text=" STUDENTS Clcik Here ",height=20,width=50,bg="Sky Blue")
student_button.pack()
student_button.bind('<Button-1>',student_win)




lib.mainloop()