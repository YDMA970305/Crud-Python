import tkinter as tk

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
        self.entry_dni_cliente = tk.Entry(self)
        self.entry_dni_cliente.config( font=("Arial", 12,))
        self.entry_dni_cliente.grid(row=0, column=1, padx=10, pady=10,columnspan=2)
        
        self.entry_nombre_cliente = tk.Entry(self)
        self.entry_nombre_cliente.config( font=("Arial", 12,))
        self.entry_nombre_cliente.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        
        self.entry_direccion_cliente = tk.Entry(self)        
        self.entry_direccion_cliente.config( font=("Arial", 12,))
        self.entry_direccion_cliente.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
        
        self.entry_email_cliente = tk.Entry(self)
        self.entry_email_cliente.config(font=("Arial", 12,))
        self.entry_email_cliente.grid(row=3, column=1, padx=10, pady=10, columnspan=2)
        
        self.entry_matricula_cliente = tk.Entry(self)
        self.entry_matricula_cliente.config( font=("Arial", 12,))
        self.entry_matricula_cliente.grid(row=4, column=1, padx=10, pady=10,columnspan=2)
        
        self.entry_fecha_cliente = tk.Entry(self)
        self.entry_fecha_cliente.config(state='disabled', font=("Arial", 12,))
        self.entry_fecha_cliente.grid(row=5, column=1, padx=10, pady=10, columnspan=2)
        
        #Botones
        self.btn_agregar_cliente = tk.Button(self, text="Agregar Cliente")
        self.btn_agregar_cliente.config(width=20,font=("Arial", 12, "bold"),fg='#DAD5D6',bg='#158645',
                                      cursor='hand2',activebackground='#35BD6F')
        self.btn_agregar_cliente.grid(row=6, column=0, padx=10, pady=10)
        
        self.btn_guardar_cliente = tk.Button(self, text="Guardar Cliente")
        self.btn_guardar_cliente.config(width=20,font=("Arial", 12, "bold"),fg='#DAD5D6',bg='#1658A2',
                                      cursor='hand2',activebackground='#3586DF')
        self.btn_guardar_cliente.grid(row=6, column=1, padx=10, pady=10)
        
        self.btn_cancelar_cliente = tk.Button(self, text="Cancelar")
        self.btn_cancelar_cliente.config(width=20,font=("Arial", 12, "bold"),fg='#DAD5D6',bg='#BD152E',
                                      cursor='hand2',activebackground='#E15370')
        self.btn_cancelar_cliente.grid(row=6, column=2, padx=10, pady=10)
    
    
    def desabilitar_campos(self):
        self.entry_dni_cliente.config(state='disabled')
        self.entry_nombre_cliente.config(state='disabled')
        self.entry_direccion_cliente.config(state='disabled')
        self.entry_email_cliente.config(state='disabled')
        self.entry_matricula_cliente.config(state='disabled')
       
        
    def habilitar_campos(self):
        pass
        