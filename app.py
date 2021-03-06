from tkinter import *
from database import *
from tkinter import messagebox
from tkinter import ttk



class App:

	def __init__(self, master):
		self.frame = master
		self.DrawEntry()
		self.DrawButtons()
		self.DrawLabel()
		self.DrawList()
		

	def DrawLabel(self):
		self.lbl_veiculo = Label(self.frame, foreground="white",font=(8), background="#314252",text="veiculo").place(x=60, y=110)
		self.lbl_rastra = Label(self.frame, foreground="white",font=(8), background="#314252", text="rastra").place(x=60, y=160)
		self.lbl_nombre = Label(self.frame, foreground="white",font=(8), background="#314252", text="nombre").place(x=60, y=210)


	def DrawEntry(self):
		self.veiculo = StringVar()
		self.rastra = StringVar()
		self.nombre = StringVar()
		self.txt_name = Entry(self.frame,font=('Arial', 12),relief="flat", background="#E7E7E7" ,textvariable=self.veiculo).place(x=140, y=110, height=25, width=150)
		self.txt_age = Entry(self.frame,font=('Arial', 12),relief="flat", background="#E7E7E7" ,textvariable=self.rastra).place(x=140, y=160, height=25, width=150)
		self.txt_age = Entry(self.frame,font=('Arial', 12),relief="flat", background="#E7E7E7" ,textvariable=self.nombre).place(x=140, y=210, height=25, width=150)

	def DrawButtons(self):
		self.btn_confirm = Button(self.frame,foreground="white", text="Guardar",borderwidth=2,relief="flat", cursor="hand1",overrelief="raise",background="#0051C8", command=lambda:self.confirmProcess()).place(x=750, y=340, width=90)
		self.btn_cancel = Button(self.frame, text="Cancelar",foreground="white",borderwidth=2,relief="flat", cursor="hand1",overrelief="raise",background="#E81123", command= lambda:self.canceProcess()).place(x=850, y=340, width=90)


	def loadImage(self):
		self.lbl_image = Label(self.frame, text="imagen", background="#314252", foreground="white").place(x=430, y=25)
		canvas = Canvas(self.frame)
		canvas.place(x=350, y=50, width=200, height=160)


	def DrawList(self):
		self.list_elemts = ttk.Treeview(self.frame, columns=(1, 2, 3), show="headings", height="8")

		# --- ESTILO ---	
		style = ttk.Style()
		style.theme_use("clam")
		style.configure("Treeview.Heading", background="#0051C8",relief="flat",foreground="white")
		style.map("Treeview", background=[('selected', 'yellow')], foreground=[('selected', 'black')])

		#--- EVENTO---
		self.list_elemts.bind("<Double 1>", self.getRow)
		#---- FIN ---

		self.list_elemts.heading(1, text="veiculo")
		self.list_elemts.heading(2, text="rastra")
		self.list_elemts.heading(3, text="nombre")
		self.list_elemts.column(1, anchor=CENTER)
		self.list_elemts.column(2, anchor=CENTER)
		self.list_elemts.column(3, anchor=CENTER)

	
        #LLENAR LISTA

		d = Data()
		self.rows = d.returnAllElements()
		for i in self.rows:
			self.list_elemts.insert('', 'end', values=i)
		# ----- FIN -----

		self.list_elemts.place(x=340, y=90)


	def getRow(self, event):
		rowName = self.list_elemts.identify_row(event.y)
		item = self.list_elemts.item(self.list_elemts.focus())
		n = item['values'][0]
		e = item['values'][1]
		c = item['values'][2]
		pop = Toplevel(self.frame)
		pop.geometry("400x200")
		lbl_n = Label(pop, text=n).place(x=40, y = 40)
		lbl_e = Label(pop, text=e).place(x=40, y = 80)
		lbl_c = Label(pop, text=c).place(x=40, y = 120)
		btn_change = Button(pop, text="Cambiar", relief="flat", background="#00CE54", foreground="white").place(x=270, y=160, width=90)



	def ClearList(self):
		self.list_elemts.delete(*self.list_elemts.get_children())

	def canceProcess(self):
		self.ClearEntry()


	def ClearEntry(self):
		self.veiculo.set("")
		self.rastra.set("")
		self.Nombre.set("")


	def confirmProcess(self):
		d = Data()
		arr = [self.name.get(), self.age.get(), self.carrer.get()]
		d.InsertItems(arr)
		messagebox.showinfo(title="Alerta", message="Se inserto correctamente!")
		self.ClearList()
		self.DrawList()
		self.ClearEntry()



root = Tk()
root.title("Reyes")
root.config(background="#314252")
root.geometry("1000x400")
aplication = App(root)
root.mainloop()