from tkinter import*
from PIL import ImageTk
from Login_page import LOGIN
class MSMIS:
    def __init__(self,dashboard_window):
        self.dashboard_window =dashboard_window
        # =========================== title and logo =======================================
        self.dashboard_window.title("MASAI SCHOOL MANAGEMENT INFORMATON SYSYTEM")
        self.dashboard_window.iconbitmap("./img/logo.ico")
        # =========================== background Image =========================================
        self.background_image =PhotoImage(file="./img/main_background.png")
        background_image_label = Label(self.dashboard_window,image=self.background_image)
        background_image_label.grid()
        # ======================= create Menu of dashboard ==================================
        mymenu = Menu(self.dashboard_window)
        #====================== File ========================================================
        m1 = Menu(mymenu,tearoff=False)
        m1.add_command(label="save")
        m1.add_command(label="Exit",command=self.exit)
        self.dashboard_window.config(menu=mymenu)
        mymenu.add_cascade(label="File",menu=m1)
        # ============================== Empolyee ============================================
        m2 = Menu(mymenu,tearoff=False)
        m2.add_command(label="Sign In",command=self.signin)
        m2.add_command(label="Exit",command=self.exit)
        self.dashboard_window.config(menu=mymenu)
        mymenu.add_cascade(label="Empolyee",menu=m2)
        #=========================== Student ====================================================
        m3 = Menu(mymenu,tearoff=False)
        m3.add_command(label="Sign In",command=self.signin)
        m3.add_command(label="Exit",command=self.exit)
        self.dashboard_window.config(menu=mymenu)
        mymenu.add_cascade(label="Student", menu=m3)
        # ============================= Course ========================================================
        mymenu.add_command(label="Course")
        # =============================== Fee ============================================================
        mymenu.add_command(label="Fee")
        #================================ Batches =======================================================
        mymenu.add_command(label="Bachtes")

        # =============================== Reports ========================================================
        mymenu.add_command(label="Reports")
        # =================================== About =====================================================
        mymenu.add_command(label="About")
        # ==================================== Help ========================================================
        mymenu.add_command(label="Help")
        # ==================================== Admin Login =================================================
        m4 = Menu(mymenu,tearoff=False)
        m4.add_command(label="Sign In",command=self.signin)
        m4.add_command(label="Exit",command=self.exit)
        self.dashboard_window.config(menu=mymenu)
        mymenu.add_cascade(label="Admin Login ",menu=m4)
#========================================= Functionality Part=======================================================
    #========================= Login page calling ===========================================================
    def signin(self):
        self.new_win = Toplevel(self.dashboard_window)
        self.new_obj = LOGIN(self.new_win)
    
    #================================== Exit funcion ===========================================================
    def exit(self):
        self.dashboard_window.destroy()

if __name__=="__main__":
    dashboard_window = Tk()
    obj=MSMIS(dashboard_window)
    dashboard_window.mainloop()