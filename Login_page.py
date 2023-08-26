from tkinter import*
from PIL import ImageTk
class LOGIN:
    def __init__(self,login_window):
        self.login_window= login_window
        #=================== size  ===========================================
        self.login_window.geometry("990x660+50+50")
        login_window.resizable(False,False)
        # ================================ title ====================================
        self.login_window.title("Login Page ")
        #================================  background_image ==================================
        self.background_image = ImageTk.PhotoImage(file="./img/Login_background.jpg")
        background_image_label = Label(self.login_window,image=self.background_image)
        background_image_label.place(x=0 ,y=0)
        #================================ heading ====================================
        heading =Label(login_window, text="USER LOGIN",font=("poppins",18,"bold"),bg="white",fg="red") 
        heading.place(x=605,y=120)
        # ====================================== username =========================================
        self.username_Entry = Entry(login_window,width=30,font=("poppins",12,"bold"),bd=0,fg="red")
        self.username_Entry.place(x=580,y=200)
        self.username_Entry.insert(0,"username")
        # <FocusIN> :- click on usrename input
        self.username_Entry.bind("<FocusIn>",self.user_enter)

        frame_1 = Frame(self.login_window,width=250, height=2,bg="red")
        frame_1.place(x=580, y=222)
        # 
        self.password_Entry = Entry(self.login_window,width=30,font=("poppins",12,"bold"),bd=0,fg="red")
        self.password_Entry.place(x=580,y=260)
        self.password_Entry.insert(0,"Password")
        # <FocusIN> :- click on usrename input
        self.password_Entry.bind("<FocusIn>",self.password_enter)

        frame_2 = Frame(self.login_window,width=250, height=2,bg="red")
        frame_2.place(x=580, y=282)
        #set eye image on password
        self.open_eye = PhotoImage(file="./img/openeye.png")
        self.eye_button = Button(self.login_window,image=self.open_eye,bd=0,bg="white",command=self.hide,activebackground="white",cursor="hand2")#,command=hide)
        self.eye_button.place(x=800,y=255)

        # create forget button 
        self.forget_button = Button(login_window,text="Forget Password?",bd=0,bg="white",command=self.forget_button,activebackground="white",cursor="hand2",font=("poppins",11,"bold"),fg="red",activeforeground="red")#,command=forget_password)
        self.forget_button.place(x=700,y=295)

        # create login button 
        self.login_button = Button(login_window,text="Login",bg="firebrick1",activebackground="white" ,cursor="hand2",font=("poppins",16,"bold"),bd=0 ,fg="white", width=19)#,command=login_user)
        self.login_button.place(x=578,y=350)

        # create OR label
        orlabel = Label(login_window,text="-------------- OR --------------",font=("poppins",16),fg="firebrick1",bg="white")
        orlabel.place(x=583,y=400)

        # add image facebook 
        self.facebook_logo = PhotoImage(file="./img/facebook.png")
        facebook_label= Label(login_window,image=self.facebook_logo,bg="white")
        facebook_label.place(x=640,y=440)

        # add image google
        self.google_logo = PhotoImage(file="./img/google.png")
        google_label= Label(self.login_window,image=self.google_logo,bg="white")
        google_label.place(x=690,y=440)
        # add image twitter
        self.twitter_logo = PhotoImage(file="./img/twitter.png")
        twitter_label= Label(self.login_window,image=self.twitter_logo,bg="white")
        twitter_label.place(x=740,y=440)
#=================================== functionality part ==========================================================
    #============================ forget button ================================================
    def forget_button(self):
        self.window = Toplevel()
        #=================== title=========================
        self.window.title("Forget Button")
        #=============== background Image ================
        self.forget_background =ImageTk.PhotoImage(file="./img/forget_background.jpg")
        forget_background_label =Label(self.window, image=self.forget_background)
        forget_background_label.grid()
        #============================== heading =====================================
        heading_label =Label(self.window,text="FORGET PASSWORD",font=("arial",18,"bold"),
                       bg ="white",fg ="red")
        heading_label.place(x=480,y=60)
        #================================== usename ======================================
        user_label=Label(self.window,text="username",font=("poppins",12,"bold"),
                         fg="red",bg="white")
        user_label.place(x=470,y=130)

        self.user_entry=Entry(self.window,width=25,bd=0,fg="red",bg="white",font=("poppins",11,"bold")) 
        self.user_entry.place(x=470,y=160)
        
        Frame(self.window,width=250,height=2,bg="red").place(x=470,y=180)
        #================================ New Password ==================================================
        user_new_password_label=Label(self.window,text="New Password",font=('poppins',12,"bold"),
                                 fg='red',bg='white')
        user_new_password_label.place(x=470,y=210)

        self.new_password_entry=Entry(self.window,width=25,bd=0,font=('poppins',11,"bold"),bg='white')
        self.new_password_entry.place(x=470,y=240)

        Frame(self.window,width=250,bg='red',height=2).place(x=470,y=260)
        #================================ Confirm New Password ============================================
        user_confirm_new_password_label=Label(self.window,text="Confirm New Password",font=("poppins",12,"bold"),
                                              fg='red', bg='white')
        user_confirm_new_password_label.place(x=470,y=290)

        self.user_confirm_new_password_entry=Entry(self.window,width=25,bd=0,font=('poppins',11,'bold'),
                                              fg="red",bg='white')
        self.user_confirm_new_password_entry.place(x=470,y=320)

        Frame(self.window,width=250,height=2,bg='red').place(x=470,y=340)
        #========================== submit button =================================
        self.submit_button=Button(self.window,text="Submit",fg='white',bg="red",bd=0,font=('poppins',16,"bold"),
                                  width=17,cursor='hand2',activebackground='red',activeforeground="white")
        self.submit_button.place(x=475,y=390)
        
        self.window.mainloop()
#=================================Functionality Part ==========================================================================
    def hide(self):
        self.open_eye.config(file="./img/closeye.png")
        self.password_Entry.config(show="*")
        self.eye_button.config(command=self.show)

    def show(self):
        self.open_eye.config(file="./img/openeye.png")
        self.password_Entry.config(show='')
        self.eye_button.config(command=self.hide)
    
    def user_enter(self,event):
        self.username_Entry.get()=="username"
        self.username_Entry.delete(0,END)

    def password_enter(self,event):
        self.password_Entry.get()=="password"
        self.password_Entry.delete(0,END)

if __name__=="__main__":
    login_window =Tk()
    obj=LOGIN(login_window)
    login_window.mainloop()