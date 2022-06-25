import tkinter as tk

#Creating list for Users and their PINS

user = {
    'sayani': '2001',
    'priya': '1999',
    'saheli': '2002'
}

amount = {
    'sayani': 50000,
    'priya': 65000,
    'saheli': 25000
}

LARGEFONT =("Times New Roman", 40)

class tkinterApp(tk.Tk):
     
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Bal': tk.IntVar(), 'Current_user': tk.StringVar()}

        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        self.frames = {} 

        for F in (HomePage, Login, Menu, Withdraw, Balance, Deposit):
  
            frame = F(container, self)

            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='blue')
        self.controller = controller

        self.controller.state('zoomed')

        label = tk.Label(self, text ="Welcome to ATM Simulation", font = LARGEFONT, fg='white', bg='blue')

        label.grid(row = 0, column = 4, padx = 650, pady = 30)
  
        button1 = tk.Button(self, text ="Login",
        command = lambda : controller.show_frame(Login),
        height=2, width=10)

        button1.grid(row = 1, column = 4, padx = 650, pady = 10)

class Login(tk.Frame):

    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent, bg='blue')
        self.controller = controller

        self.controller.state('zoomed')
        label = tk.Label(self, text ="Login", font = LARGEFONT, fg='white', bg='blue')
        label.grid(row = 0, column = 4, padx = 650, pady = 30)
  
        name_var = tk.StringVar()
        Login_label = tk.Label(self, text="Username", font = ('calibre',10, 'bold'), fg='white', bg='blue')
        Login_label.grid(row=3, column=4, padx=650, pady=10)

        Login_entry = tk.Entry(self, textvariable = name_var, font=('calibre',10,'normal'))
        Login_entry.grid(row=4, column=4, padx=650, pady=10, ipadx=5, ipady=5)

        passw_var = tk.StringVar()
        Password_label = tk.Label(self, text="Password", font=('calibre',10, 'bold'), fg='white', bg='blue')
        Password_label.grid(row=6, column=4, padx=650, pady=10)
        
        Password_entry = tk.Entry(self, textvariable = passw_var, show= '*', font=('calibre',10,'normal'))
        Password_entry.grid(row=7,column=4, padx=650, pady=10, ipadx=5, ipady=5)

        def submit():
            name=name_var.get()
            password=passw_var.get()

            for x,y in user.items():
                if(name == x and password == y):
                    name_var.set("")
                    passw_var.set("")
                    incorrect['text']=''
                    controller.shared_data['Current_user'].set(x)
                    for k,l in amount.items():
                        if(k == x):
                            controller.shared_data['Bal'].set(l)
                    controller.show_frame(Menu)
                else:
                    incorrect['text']='Incorrect Credential'

        sub_btn=tk.Button(self,text = 'Submit', command = submit, height=2, width=10)
        sub_btn.grid(row=8, column=4, padx=650, pady=10)

        incorrect = tk.Label(self, text='', font=('calibre', 16, 'bold'), fg='red', bg='blue')
        incorrect.grid(row=10, column=4, padx=650)

class Menu(tk.Frame):

    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent, bg='blue')
        self.controller = controller

        self.controller.state('zoomed')
        label = tk.Label(self, text ="Menu", font = LARGEFONT, fg='white', bg='blue')
        label.grid(row = 0, column = 4, padx = 650, pady = 30)

        def withdraw():
            controller.show_frame(Withdraw)

        Withdraw_btn = tk.Button(self, text='Withdraw', command=withdraw, height=2, width=10)
        Withdraw_btn.grid(row=3, column=4, padx=650, pady=10)

        def deposit():
            controller.show_frame(Deposit)

        Deposit_btn = tk.Button(self, text='Deposit', command=deposit, height=2, width=10)
        Deposit_btn.grid(row=4, column=4, padx=650, pady=10)

        def balance():
            controller.show_frame(Balance)

        Balance_btn = tk.Button(self, text='Balance', command=balance, height=2, width=10)
        Balance_btn.grid(row=5, column=4, padx=650, pady=10)

        def Exit():
            controller.show_frame(HomePage)

        Exit_btn = tk.Button(self, text='Exit', command=Exit, height=2, width=10)
        Exit_btn.grid(row=6, column=4, padx=650, pady=10)

class Withdraw(tk.Frame):

    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent, bg='blue')
        self.controller = controller

        self.controller.state('zoomed')
        label = tk.Label(self, text ="Withdraw", font = LARGEFONT, fg='white', bg='blue')
        label.grid(row = 0, column = 4, padx = 650, pady = 30)

        withdraw_lable = tk.Label(self, text='Enter amount you want to Withdraw', font=('calibri', 20, 'bold'), fg='white', bg='blue')
        withdraw_lable.grid(row=3, column=4, padx=650, pady=10)

        withdraw_amt = tk.IntVar()
        withdraw_input = tk.Entry(self, textvariable = withdraw_amt, font=('calibre',10,'normal'))
        withdraw_input.grid(row=4,column=4, padx=650, pady=10, ipadx=5, ipady=5)

        def confirm():
            cash = withdraw_amt.get()
            amt = controller.shared_data['Bal'].get()
            after_withdraw = amt-cash 
            controller.shared_data['Bal'].set(after_withdraw)
            controller.show_frame(Menu) 

        Confirm_btn = tk.Button(self, text='Confirm', command=confirm, height=2, width=10)
        Confirm_btn.grid(row=5, column=4, padx=650, pady=10)

class Balance(tk.Frame):

    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent, bg='blue')
        self.controller = controller

        self.controller.state('zoomed')
        label = tk.Label(self, text ="Withdraw", font = LARGEFONT, fg='white', bg='blue')
        label.grid(row = 0, column = 4, padx = 650, pady = 30)

        bal_label = tk.Label(self, text='Your Current balance', font=('calibre', 20, 'bold'), fg='white', bg='blue')
        bal_label.grid(row=3, column=4, padx=650, pady=10, ipadx=5, ipady=5)

        bal_msg = tk.Message(self, textvariable= controller.shared_data['Bal'],font=('calibre', 14, 'bold'), fg='white', bg='blue')
        bal_msg.grid(row=4, column=4, padx=650, pady=10, ipadx=10, ipady=5)

        def exit():
            controller.show_frame(Menu)

        Exit_btn = tk.Button(self, text='Exit', command=exit, height=2, width=10)
        Exit_btn.grid(row=5, column=4, padx=20)

class Deposit(tk.Frame):

    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent, bg='blue')
        self.controller = controller

        self.controller.state('zoomed')
        label = tk.Label(self, text ="Withdraw", font = LARGEFONT, fg='white', bg='blue')
        label.grid(row = 0, column = 4, padx = 650, pady = 30)

        deposit_label = tk.Label(self, text='Enter Amount to Deposit', font=('calibre',20,'bold'), fg='white', bg='blue')
        deposit_label.grid(row=3, column=4, padx=650, pady=10)

        deposit_amt = tk.IntVar()
        deposit_input = tk.Entry(self, textvariable=deposit_amt, font=('calibre',11,'normal'))
        deposit_input.grid(row=4,column=4, padx=650, pady=10, ipadx=5, ipady=5)

        def deposit():
            cash = deposit_amt.get()
            amt = controller.shared_data['Bal'].get()
            after_deposit = amt+cash
            controller.shared_data['Bal'].set(after_deposit)
            controller.show_frame(Menu)

        Deposit_btn = tk.Button(self, text='Deposit', command=deposit, height=2, width=10)
        Deposit_btn.grid(row=5, column=4, padx=20)


app = tkinterApp()
app.mainloop()