from tkinter import *
from tkinter import ttk
import cliente

app=Tk()

app.title('Turnos')
app.geometry('1200x800')
app.configure(bg='#202438')
app.iconbitmap('veterinaria1.ico')




etiqueta = ttk.Label(text="Veterinaria Turnos",width=100, anchor=CENTER, background="#202438", font=('Arial', 25),foreground="white")
etiqueta.pack(pady=15)

set = ttk.Treeview(app)
set.pack(pady=15)

set['columns']= ('hora', 'nombre','apellido','dni','nombre_mascota', 'tipo_mascota','telefono')
set.column("#0", width=0,  stretch=NO)
set.column("hora",anchor=CENTER, width=80)
set.column("nombre",anchor=CENTER, width=80)
set.column("apellido",anchor=CENTER, width=80)
set.column("dni",anchor=CENTER, width=80)
set.column("nombre_mascota",anchor=CENTER, width=120)
set.column("tipo_mascota",anchor=CENTER, width=120)
set.column("telefono",anchor=CENTER, width=120)

set.heading("#0",text="",anchor=CENTER)

set.heading("hora",text="Hora",anchor=CENTER)
set.heading("nombre",text="Nombre",anchor=CENTER)
set.heading("apellido",text="Apellido",anchor=CENTER)
set.heading("dni",text="DNI",anchor=CENTER)
set.heading("nombre_mascota",text="Nombre Mascota",anchor=CENTER)
set.heading("tipo_mascota",text="Tipo Mascota",anchor=CENTER)
set.heading("telefono",text="Telefono",anchor=CENTER)

data  = []
    

global count
count=0
    
for record in data:
      
    set.insert(parent='',index='end',iid = count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]))
       
    count += 1

def input_record():
    

    global count

    registro = cliente.Cliente(hora_entry.get(),nombre_entry.get(),apellido_entry.get(),dni_entry.get(),mascota_entry.get(),tipo_entry.get(),telefono_entry.get())
    
   
    set.insert(parent='',index='end',iid = count,text='',values=(registro.hora, registro.nombre, registro.apellido, registro.dni, registro.mascota, registro.tipo, registro.telefono))
    count += 1

   
    hora_entry.delete(0,END)
    nombre_entry.delete(0,END)
    apellido_entry.delete(0,END)
    dni_entry.delete(0,END)
    mascota_entry.delete(0,END)
    tipo_entry.delete(0,END)
    telefono_entry.delete(0,END)


def delete_record():
    selected_item = set.selection()[0]
    set.delete(selected_item)

etiqueta2 = ttk.Label(text="Nuevo Turno",width=30, anchor=CENTER, background="#202438", font=('Arial', 25),foreground="white", padding=10)
etiqueta2.pack()

Input_frame = Frame(app)
Input_frame.pack()

hora = Label(Input_frame,text="Hora")
hora.grid(row=0,column=0)

nombre= Label(Input_frame,text="Nombre")
nombre.grid(row=0,column=1)

apellido = Label(Input_frame,text="Apellido")
apellido.grid(row=0,column=2)

dni = Label(Input_frame,text="DNI")
dni.grid(row=0,column=3)

mascota= Label(Input_frame,text="Mascota")
mascota.grid(row=0,column=4)

tipo_mascota = Label(Input_frame,text="Tipo mascota")
tipo_mascota.grid(row=0,column=5)

telefono = Label(Input_frame,text="Telefono")
telefono.grid(row=0,column=6)

hora_entry = Entry(Input_frame)
hora_entry.grid(row=1,column=0)

nombre_entry = Entry(Input_frame)
nombre_entry.grid(row=1,column=1)

apellido_entry = Entry(Input_frame)
apellido_entry.grid(row=1,column=2)

dni_entry = Entry(Input_frame)
dni_entry.grid(row=1,column=3)

mascota_entry = Entry(Input_frame)
mascota_entry.grid(row=1,column=4)

tipo_entry = Entry(Input_frame)
tipo_entry.grid(row=1,column=5)

telefono_entry = Entry(Input_frame)
telefono_entry.grid(row=1,column=6)



Input_button = Button(app,text = "Agendar",width=30, anchor=CENTER, background="#00AC60", font=78,foreground="white",  border="1 px #00001a",command= input_record)

Input_button.pack(pady=15)

Delete_button = Button(app,text = "Borrar",width=30, anchor=CENTER, background="red", font=78,foreground="white",  border="1 px #00001a",command= delete_record)

Delete_button.pack(pady=15)


app.mainloop()