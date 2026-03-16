import customtkinter as ctk
import math

istoric = []

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.geometry("300x600")
app.title("Calculator GUI")


ecran = ctk.CTkEntry(app, font=("Arial", 35), justify="right", height=50)
ecran.pack(pady=20, padx=10, fill="x")


def adauga_ecran(caracter):
    ecran.insert("end", caracter)

def clear_all():
    ecran.delete(0, "end")
    
def clear():
    if len(ecran.get()) > 0:
        ecran.delete(len(ecran.get()) - 1, "end")
        
def calculeaza():
    expresie = ecran.get()
    expresie_calcul = expresie.replace("^", "**")
    try:
        rezultat = eval(expresie_calcul)
        ecran.delete(0, "end")
        ecran.insert("end", str(rezultat))
        istoric.append(f"{expresie} = {rezultat}")
    except ZeroDivisionError:
        ecran.delete(0, "end")
        ecran.insert("end", "Nu poti imparti la 0")
    except Exception:
        ecran.delete(0, "end")
        ecran.insert("end", "Eroare de sintaxa")      

def schimba_semn():
    curent = ecran.get()
    if curent:
        if curent[0] == "-":
            ecran.delete(0, "end")
            ecran.insert(0, curent[1:])
        else:
            ecran.delete(0, "end")
            ecran.insert(0, "-" + curent)

def modul():
    curent = ecran.get()
    if curent:
        if curent[0] == "-":
            rezultat = curent[1:]
            ecran.delete(0, "end")
            ecran.insert(0, rezultat)
            istoric.append(f"|{curent}| = {rezultat}")  

def factorial():
    copie = ecran.get()
    rezultat = 1
    if "." in copie or copie =="":
        ecran.delete(0, "end")
        ecran.insert(0, "Eroare de sintaxa")
        return
    numar = int(copie)
    if numar < 0:
        ecran.delete(0, "end")
        ecran.insert(0, "Eroare de sintaxa")
    else:
        for i in range(1, numar+1):
            rezultat = rezultat * i
        ecran.delete(0, "end")
        ecran.insert("end", str(rezultat))
        istoric.append(f"{numar}! = {rezultat}")
        
def radical():
    numar = ecran.get()
    if "-" in numar or numar == "":
        ecran.delete(0, "end")
        ecran.insert(0, "Eroare de sintaxa")
        return
    nr = float(numar)
    rezultat = math.sqrt(nr)
    ecran.delete(0, "end")
    ecran.insert(0, str(rezultat))
    istoric.append(f"√({numar}) = {rezultat}")


def arata_istoric():
    fereastra_istoric = ctk.CTkToplevel(app)
    fereastra_istoric.geometry("250x400")
    fereastra_istoric.title("Istoric")
    fereastra_istoric.attributes("-topmost", True)
    titlu = ctk.CTkLabel(fereastra_istoric, text="Istoricul tau:", font=("Arial", 20, "bold"))
    titlu.pack(pady=10)
    
    if len(istoric) == 0:
        mesaj = ctk.CTkLabel(fereastra_istoric, text="Niciun calcul inca.", font=("Arial", 16))
        mesaj.pack(pady=20)
    else:
        for calcul in istoric:
            eticheta_calcul = ctk.CTkLabel(fereastra_istoric, text=calcul, font=("Arial", 16))
            eticheta_calcul.pack(pady=2)
    

frame_butoane = ctk.CTkFrame(app, fg_color="transparent")
frame_butoane.pack()

btn_modul = ctk.CTkButton(frame_butoane, text = "| |", width=60, height=60, font=("Arial",20),fg_color="#2b2b2b", command=lambda:modul())
btn_modul.grid(row=0, column=0, padx=5, pady=5)

btn_istoric = ctk.CTkButton(frame_butoane, text = "H", width=60, height=60, font=("Arial",20),fg_color="#2b2b2b", command=lambda:arata_istoric())
btn_istoric.grid(row=0, column=1, padx=5, pady=5)

btn_clear = ctk.CTkButton(frame_butoane, text = "C", width=60, height=60, font=("Arial",20),fg_color="#2b2b2b", command=lambda:clear())
btn_clear.grid(row=0, column=2, padx=5, pady=5)

btn_clearall = ctk.CTkButton(frame_butoane, text = "CA", width=60, height=60, font=("Arial",20),fg_color="#2b2b2b", command=lambda:clear_all())
btn_clearall.grid(row=0, column=3, padx=5, pady=5)

btn_rest = ctk.CTkButton(frame_butoane, text = "%", width=60, height=60, font=("Arial",20),fg_color="#2b2b2b", command= lambda: adauga_ecran("%"))
btn_rest.grid(row=1, column=0, padx=5, pady=5)

btn_pow = ctk.CTkButton(frame_butoane, text = "^", width=60, height=60, font=("Arial",20),fg_color="#2b2b2b", command=lambda: adauga_ecran("^"))
btn_pow.grid(row=1, column=1, padx=5, pady=5)

btn_radical = ctk.CTkButton(frame_butoane, text = "√", width=60, height=60, font=("Arial",20),fg_color="#2b2b2b", command=lambda: radical())
btn_radical.grid(row=1, column=2, padx=5, pady=5)

btn_fact = ctk.CTkButton(frame_butoane, text = "!", width=60, height=60, font=("Arial",20),fg_color="#2b2b2b", command=lambda: factorial())
btn_fact.grid(row=1, column=3, padx=5, pady=5)

btn_7 = ctk.CTkButton(frame_butoane, text = "7", width=60, height=60, font=("Arial",20),fg_color="#636363",command=lambda: adauga_ecran("7"))
btn_7.grid(row=2, column=0, padx=5, pady=5)

btn_8 = ctk.CTkButton(frame_butoane, text = "8", width=60, height=60, font=("Arial",20),fg_color="#636363",command=lambda: adauga_ecran("8"))
btn_8.grid(row=2, column=1, padx=5, pady=5)

btn_9 = ctk.CTkButton(frame_butoane, text = "9", width=60, height=60, font=("Arial",20),fg_color="#636363",command=lambda: adauga_ecran("9"))
btn_9.grid(row=2, column=2, padx=5, pady=5)

btn_frac = ctk.CTkButton(frame_butoane, text = "/", width=60, height=60, font=("Arial",20),fg_color="#2b2b2b", command=lambda: adauga_ecran("/"))
btn_frac.grid(row=2, column=3, padx=5, pady=5)

btn_4 = ctk.CTkButton(frame_butoane, text = "4", width=60, height=60, font=("Arial",20),fg_color="#636363",command=lambda: adauga_ecran("4"))
btn_4.grid(row=3, column=0, padx=5, pady=5)

btn_5 = ctk.CTkButton(frame_butoane, text = "5", width=60, height=60, font=("Arial",20),fg_color="#636363",command=lambda: adauga_ecran("5"))
btn_5.grid(row=3, column=1, padx=5, pady=5)

btn_6 = ctk.CTkButton(frame_butoane, text = "6", width=60, height=60, font=("Arial",20),fg_color="#636363",command=lambda: adauga_ecran("6"))
btn_6.grid(row=3, column=2, padx=5, pady=5)

btn_inmultire = ctk.CTkButton(frame_butoane, text = "*", width=60, height=60, font=("Arial",20),fg_color="#2b2b2b", command=lambda: adauga_ecran("*"))
btn_inmultire.grid(row=3, column=3, padx=5, pady=5)

btn_1 = ctk.CTkButton(frame_butoane, text = "1", width=60, height=60, font=("Arial",20),fg_color="#636363",command=lambda: adauga_ecran("1"))
btn_1.grid(row=4, column=0, padx=5, pady=5)

btn_2 = ctk.CTkButton(frame_butoane, text = "2", width=60, height=60, font=("Arial",20),fg_color="#636363",command=lambda: adauga_ecran("2"))
btn_2.grid(row=4, column=1, padx=5, pady=5)

btn_3 = ctk.CTkButton(frame_butoane, text = "3", width=60, height=60, font=("Arial",20),fg_color="#636363",command=lambda: adauga_ecran("3"))
btn_3.grid(row=4, column=2, padx=5, pady=5)

btn_scadere = ctk.CTkButton(frame_butoane, text = "-", width=60, height=60, font=("Arial",20),fg_color="#2b2b2b", command=lambda: adauga_ecran("-"))
btn_scadere.grid(row=4, column=3, padx=5, pady=5)

btn_semn = ctk.CTkButton(frame_butoane, text = "+/-", width=60, height=60, font=("Arial",20),fg_color="#636363", command=lambda: schimba_semn())
btn_semn.grid(row=5, column=0, padx=5, pady=5)

btn_0 = ctk.CTkButton(frame_butoane, text = "0", width=60, height=60, font=("Arial",20),fg_color="#636363", command=lambda: adauga_ecran("0"))
btn_0.grid(row=5, column=1, padx=5, pady=5)

btn_zec = ctk.CTkButton(frame_butoane, text = ".", width=60, height=60, font=("Arial",20),fg_color="#636363", command=lambda: adauga_ecran("."))
btn_zec.grid(row=5, column=2, padx=5, pady=5)

btn_adunare = ctk.CTkButton(frame_butoane, text = "+", width=60, height=60, font=("Arial",20),fg_color="#2b2b2b", command=lambda: adauga_ecran("+"))
btn_adunare.grid(row=5, column=3, padx=5, pady=5)

btn_egal = ctk.CTkButton(frame_butoane, text="=", height=60, font=("Arial", 20), fg_color="#1f6aa5", command=lambda:calculeaza()) # Folosim un albastru pentru a ieși în evidență
btn_egal.grid(row=6, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

app.bind("0", lambda event: adauga_ecran("0"))
app.bind("1", lambda event: adauga_ecran("1"))
app.bind("2", lambda event: adauga_ecran("2"))
app.bind('3', lambda event: adauga_ecran('3'))
app.bind('4', lambda event: adauga_ecran('4'))
app.bind('5', lambda event: adauga_ecran('5'))
app.bind('6', lambda event: adauga_ecran('6'))
app.bind('7', lambda event: adauga_ecran('7'))
app.bind('8', lambda event: adauga_ecran('8'))
app.bind('9', lambda event: adauga_ecran('9'))
app.bind('+', lambda event: adauga_ecran('+'))
app.bind('-', lambda event: adauga_ecran('-'))
app.bind('*', lambda event: adauga_ecran('*'))
app.bind('/', lambda event: adauga_ecran('/'))
app.bind('%', lambda event: adauga_ecran('%'))
app.bind('.', lambda event: adauga_ecran('.'))
app.bind('^', lambda event: adauga_ecran('^'))
app.bind('=', lambda event: calculeaza())
app.bind('!', lambda event: factorial())
app.bind('<Return>', lambda event: calculeaza())
app.bind('<BackSpace>', lambda event: clear())
app.bind('<Delete>', lambda event: clear_all())
app.bind('<Escape>', lambda event: clear_all())
app.bind('h', lambda event: arata_istoric())
app.bind('r', lambda event: radical())
app.bind('m', lambda event: modul())
app.bind('s', lambda event: schimba_semn())


app.mainloop()