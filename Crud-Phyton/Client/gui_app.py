import tkinter as tk
from tkinter import ttk

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu,width=600,height=600)
    
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
    
    menu_inicio.add_command(label="Crear Cliente")
    menu_inicio.add_command(label="Eliminar Cliente")
    menu_inicio.add_command(label="Editar Cliente")
    menu_inicio.add_command(label="Ver Cliente")
    menu_inicio.add_command(label="Listar Clientes")
    menu_inicio.add_command(label="Salir", command=root.destroy)

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root,width=600,height=600)
        self.root = root
        self.pack()
        #self.config(bg="green")
        
        
        
        self.campos_cliente()
        self.after(1, self.desabilitar_campos)
        self.tabla_clientes()
        
        
    def campos_cliente(self):
        #campos de cliente label
        self.dni_cliente = tk.Label(self, text="DNI Cliente")
        self.dni_cliente.config(font=("Arial", 10, "bold"))
        self.dni_cliente.grid(row=0, column=0,padx=10, pady=10)
        
        self.nombre_cliente = tk.Label(self, text="Nombre Cliente")
        self.nombre_cliente.config(font=("Arial", 10, "bold"))
        self.nombre_cliente.grid(row=1, column=0,padx=10, pady=10)
        
        self.direccion_cliente = tk.Label(self, text="Direccion Cliente")
        self.direccion_cliente.config(font=("Arial", 10, "bold"))
        self.direccion_cliente.grid(row=2, column=0,padx=10, pady=10)
        
        self.email_cliente = tk.Label(self, text="Email Cliente")
        self.email_cliente.config(font=("Arial", 10, "bold"))
        self.email_cliente.grid(row=3, column=0,padx=10, pady=10)
        
        self.vehiculo_usado_matricula = tk.Label(self, text="Vehiculo Usado Matricula")
        self.vehiculo_usado_matricula.config(font=("Arial", 10, "bold"))
        self.vehiculo_usado_matricula.grid(row=4, column=0,padx=10, pady=10)
        
        self.fecha = tk.Label(self, text="Fecha")
        self.fecha.config(font=("Arial", 10, "bold"))        
        self.fecha.grid(row=5, column=0, padx=10, pady=10)
        
       #Entradas de cliente
        self.dni=tk.StringVar()
        self.entry_dni_cliente = tk.Entry(self, textvariable=self.dni)
        self.entry_dni_cliente.config( font=("Arial", 12,))
        self.entry_dni_cliente.grid(row=0, column=1, padx=10, pady=10,columnspan=2)
        
        self.nombre=tk.StringVar()
        self.entry_nombre_cliente = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre_cliente.config( font=("Arial", 12,))
        self.entry_nombre_cliente.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        
        self.direccion=tk.StringVar()
        self.entry_direccion_cliente = tk.Entry(self,textvariable=self.direccion)
        self.entry_direccion_cliente.config( font=("Arial", 12,))
        self.entry_direccion_cliente.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
        
        self.email=tk.StringVar()
        self.entry_email_cliente = tk.Entry(self, textvariable=self.email)
        self.entry_email_cliente.config(font=("Arial", 12,))
        self.entry_email_cliente.grid(row=3, column=1, padx=10, pady=10, columnspan=2)
        
        self.matricula=tk.StringVar()
        self.entry_matricula_cliente = tk.Entry(self, textvariable=self.matricula)
        self.entry_matricula_cliente.config( font=("Arial", 12,))
        self.entry_matricula_cliente.grid(row=4, column=1, padx=10, pady=10,columnspan=2)
        
        self.fecha=tk.StringVar()
        self.entry_fecha_cliente = tk.Entry(self, textvariable=self.fecha)
        self.entry_fecha_cliente.config(state='disabled', font=("Arial", 12,))
        self.entry_fecha_cliente.grid(row=5, column=1, padx=10, pady=10, columnspan=2)
        
        #Botones
        self.btn_agregar_cliente = tk.Button(self, text="Agregar Cliente", command=self.habilitar_campos)
        self.btn_agregar_cliente.config(width=20,font=("Arial", 12, "bold"),fg='#DAD5D6',bg='#158645',
                                      cursor='hand2',activebackground='#35BD6F')
        self.btn_agregar_cliente.grid(row=6, column=0, padx=10, pady=10)
        
        self.btn_guardar_cliente = tk.Button(self, text="Guardar Cliente",command=self.guardar_cliente)
        self.btn_guardar_cliente.config(width=20,font=("Arial", 12, "bold"),fg='#DAD5D6',bg='#1658A2',
                                      cursor='hand2',activebackground='#3586DF')
        self.btn_guardar_cliente.grid(row=6, column=1, padx=10, pady=10)
        
        self.btn_cancelar_cliente = tk.Button(self, text="Cancelar", command=self.desabilitar_campos)
        self.btn_cancelar_cliente.config(width=20,font=("Arial", 12, "bold"),fg='#DAD5D6',bg='#BD152E',
                                      cursor='hand2',activebackground='#E15370')
        self.btn_cancelar_cliente.grid(row=6, column=2, padx=10, pady=10)
    
    
    def desabilitar_campos(self):
        self.dni.set("")
        self.nombre.set("")
        self.direccion.set("")
        self.email.set("")
        self.matricula.set("")
        self.fecha.set("")  
        self.entry_dni_cliente.config(state='disabled')
        self.entry_nombre_cliente.config(state='disabled')
        self.entry_direccion_cliente.config(state='disabled')
        self.entry_email_cliente.config(state='disabled')
        self.entry_matricula_cliente.config(state='disabled')
        self.btn_guardar_cliente.config(state='disabled')
        self.btn_cancelar_cliente.config(state='disabled');
       
        
    def habilitar_campos(self):
        self.entry_dni_cliente.config(state='normal')
        self.entry_nombre_cliente.config(state='normal')
        self.entry_direccion_cliente.config(state='normal')
        self.entry_email_cliente.config(state='normal')
        self.entry_matricula_cliente.config(state='normal')
        self.btn_guardar_cliente.config(state='normal')
        self.btn_cancelar_cliente.config(state='normal');
       
    def guardar_cliente(self):
        self.desabilitar_campos()
        
    def tabla_clientes(self):
        self.tabla_clientes = ttk.Treeview(self, 
        columns=("DNI", "Nombre", "Direccion", "Email", "Matricula", "Fecha"))
        self.tabla_clientes.grid(row=8, column=0, columnspan=6)
        
        self.tabla_clientes.heading("#0", text="DNI")
        self.tabla_clientes.heading("#1", text="Nombre")
        self.tabla_clientes.heading("#2", text="Direccion")
        self.tabla_clientes.heading("#3", text="Email")
        self.tabla_clientes.heading("#4", text="Matricula")
        self.tabla_clientes.heading("#5", text="Fecha")
        
        self.tabla_clientes.insert("", 0, text="123456789", values=("123456789", "Melisa mamasita hermosa", "Calle 1", "juanperez@gmail.com", "123456789", "2022-01-01"))
        self.tabla_clientes.insert("", 1, text="123456789", values=("123456789", "Juan Perez", "Calle 1", "juanperez@gmail.com", "123456789", "2022-01-01"))
        
        #botones editar y eliminar
        self.btn_editar_cliente = tk.Button(self, text="Editar Cliente")
        self.btn_editar_cliente.config(width=20,font=("Arial", 12, "bold"),fg='#DAD5D6',bg='#158645',
                                      cursor='hand2',activebackground='#35BD6F')
        self.btn_editar_cliente.grid(row=9, column=0, padx=10, pady=10)
        
        
        self.btn_eliminar_cliente = tk.Button(self, text="Eliminar Cliente")
        self.btn_eliminar_cliente.config(width=20,font=("Arial", 12, "bold"),fg='#DAD5D6',bg='#BD152E',
                                      cursor='hand2',activebackground='#E15370')
        self.btn_eliminar_cliente.grid(row=9, column=2, padx=10, pady=10)    