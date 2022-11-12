from tkinter import *
from tkinter import ttk

def registration():
    name1 = name.get()
    contact1= contact.get()
    email1 = email.get()
    gender1 = gender.get()
    city1 = city.get()
    state1 = state.get()

    if name1== '' or contact1=='' or email1 == '' or gender1 =='' or city1 =='' or state1 == '':
        message.set("Fill all the Details ")

    else:
        with open("Studinfo.txt", "a") as fp:
            if gender==1:
                fp.write(" "+name1+ " "+contact1+" "+email1+ " Male "+ city1+" "+state1 )
            else:
                fp.write(" " + name1 + " " + contact1 + " " + email1 + " Female " + city1 + " " + state1)
            message.set("Data Stored Successfully")



def registrationform():

    global registration_screen

    registration_screen = Tk()

    registration_screen.title("Registration form ")

    registration_screen.geometry("400x400")

    global message
    global name
    global contact
    global email
    global gender
    global city
    global state

    name = StringVar()
    contact = StringVar()
    email = StringVar()
    gender = IntVar()
    city = StringVar()
    state = StringVar()
    message = StringVar()

    Label(registration_screen, width="250", text="Please Enter the details below",bg='orange', fg='white').pack()

    Label(registration_screen, text="Name " ).place(x=25, y = 40)

    Entry(registration_screen, textvariable=name).place(x=85, y = 41)

    Label(registration_screen, text="contact ").place(x=25, y=80)

    Entry(registration_screen, textvariable=contact).place(x=85, y=81)

    Label(registration_screen, text="email ").place(x=25, y=120)

    Entry(registration_screen, textvariable=email).place(x=85, y=121)

    Label(registration_screen, text="Gender ").place(x=25, y=160)

    Radiobutton(registration_screen, text= 'Male', variable=gender, value=1).place(x = 85, y = 161 )
    Radiobutton(registration_screen, text= 'Female', variable=gender, value=2).place(x = 150, y = 161 )

    Label(registration_screen, text="City ").place(x=25, y=200)
    citychoosen = ttk.Combobox(registration_screen, width= 30, textvariable=city)
    citychoosen['values'] = ('Mumbai', 'Pune', "Chennai", "Kolkata", "Bengluru", "Patna", "Nagpur" )
    citychoosen.current()
    citychoosen.place(x = 85, y = 201)

    Label(registration_screen, text="State ").place(x=25, y=240)
    statechoosen = ttk.Combobox(registration_screen, width=30, textvariable=state)
    statechoosen['values'] = ('Maharastra', 'Karnataka', "Andra Pradesh", "West Bangal", "Bihar", "Meghalaya", "Uttar Pradesh")
    statechoosen.current()
    statechoosen.place(x=85, y=241)

    Label(registration_screen, text=" ", textvariable=message).place(x= 95, y = 260)

    Button(registration_screen, text="Register", width=10, height=1, bg = "orange", command=registration).place(x = 110, y =301 )

    registration_screen.mainloop()




registrationform()

