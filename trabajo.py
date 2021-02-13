from tkinter import *
import csv

 
# Manipular datos de campos de registro
def send_data():

  veiculo_info = str(veiculo.get())
  rastra_info = str(rastra.get())
  username_info = username.get()
  geocerca_info = geocerca.get()
  fechaentrada_info =  str(fechaentrada.get())
  fechasalida_info = str(fechasalida.get())
  diftiempo_info = str(diftiempo.get())
  print( veiculo_info,"\t", rastra_info,"\t", username_info,"\t", geocerca_info,"\t", fechaentrada_info,"\t", fechasalida_info, "\t", diftiempo_info)
 
#  Abrir y escribir datos en un archivo
  archivo = open("archivo csv", "a")
  archivo.write(veiculo_info)
  archivo.write("\t")
  archivo.write(rastra_info)
  archivo.write("\t")
  archivo.write(username_info)
  archivo.write("\t")
  archivo.write(geocerca_info)
  archivo.write("\t")
  archivo.write(fechaentrada_info)
  archivo.write("\t")
  archivo.write(fechasalida_info)
  archivo.write("\t")
  archivo.write(diftiempo_info)
  archivo.write("\t")
  archivo.close()
  print(" New user registered. Username: {} | fechaentrada: {}   ".format(username_info, fechaentrada_info))
 
#  Eliminar datos del evento anterior
  veiculo_entry.delete(0, END)
  rastra_entry.delete(0, END)
  username_entry.delete(0, END)
  geocerca_entry.delete(0, END)
  fechaentrada_entry.delete(0, END)
  fechasalida_entry.delete(0, END)
  diftiempo_entry.delete(0, END)

# Crear nueva instancia - Clase Tk () 
mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title(" TRABAJO")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = "Python Form | PROYECTO", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()

# Definir campos de etiqueta 
veiculo_label = Label(text = "veiculo", bg = "#FFEEDD")
veiculo_label.place(x = 22, y = 70)
rastra_label = Label(text = "rastra", bg = "#FFEEDD")
rastra_label.place(x = 22, y = 130)
username_label = Label(text = "Username", bg = "#FFEEDD")
username_label.place(x = 22, y = 190)
geocerca_label = Label(text = "geocerca", bg = "#FFEEDD")
geocerca_label.place(x = 22, y = 250)
fechaentrada_label = Label(text = "Fechaentrada", bg = "#FFEEDD")
fechaentrada_label.place(x = 22, y = 320)
fechasalida_label = Label(text = "fechasalida", bg = "#FFEEDD")
fechasalida_label.place(x = 22, y = 380)
diftiempo_label = Label(text = "diftiempo", bg = "#FFEEDD")
diftiempo_label.place(x = 22, y = 450)
 
 
# Obtener y almacenar datos de los usuarios
veiculo = StringVar()
rastra = StringVar()
username = StringVar()
geocerca  = StringVar()
fechaentrada = StringVar()
fechasalida = StringVar()
diftiempo = StringVar()
 
 
veiculo_entry = Entry(textvariable = veiculo, width = "40")
rastra_entry = Entry(textvariable = rastra, width = "40")
username_entry = Entry(textvariable = username, width = "40")
geocerca_entry = Entry(textvariable = geocerca, width = "40",)
fechaentrada_entry = Entry(textvariable = fechaentrada, width = "40")
fechasalida_entry = Entry(textvariable = fechasalida, width = "40")
diftiempo_entry = Entry(textvariable = diftiempo, width = "40")

veiculo_entry.place(x = 22, y = 100)
rastra_entry.place(x = 22, y = 160)
username_entry.place(x = 22, y = 220)
geocerca_entry.place(x = 22, y = 280)
fechaentrada_entry.place(x = 22, y = 350)
fechasalida_entry.place(x = 22, y = 420)
diftiempo_entry.place(x = 22, y = 480)
 
# -- FILL LIST--
	
 

# Submit Button
submit_btn = Button(mywindow,text = "Submit Info", width = "30", height = "2", command = send_data, bg = "#00CD63")
submit_btn.place(x = 22, y = 510)


mywindow.mainloop()
      

