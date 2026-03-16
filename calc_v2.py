import math

istoric = []

def citeste_numar(mesaj):
    while True:
        valoare = input(mesaj)
        try:
            return float(valoare)
        except ValueError:
            print("Eroare: Nu ai introdus un număr valid! Folosește punctul pentru zecimale (ex: 3.5, -2).")

while True:
    selectare_operatie = input("\nCare este urmatoarea ta operatie (+, -, /, %, radical, ^, *, !, istoric, exit)? ")
    
    if selectare_operatie not in ["+", "-", "/", "%", "^", "radical", "*", "!", "istoric", "exit"]:
        print("Ai introdus o operatie invalida. Te rog alege din lista.")
        continue
        
    if selectare_operatie == "exit":
        print("La revedere!")
        break
        
    if selectare_operatie == "istoric":
        if not istoric:
            print("Nu ai niciun calcul in istoric.")
        else:
            print("\nAcesta este istoricul calculelor:")
            for calcul in istoric:
                print(calcul)
        continue

    if selectare_operatie in ["+", "-", "*", "^"]:
        print("Care sunt termenii din operatie? ")
        a = citeste_numar("Primul termen a = ")
        b = citeste_numar("Al 2-lea termen b = ")
        
        if selectare_operatie == "+":
            rezultat = a + b
            print(f"{a} + {b} = {rezultat}")
            istoric.append(f"{a} + {b} = {rezultat}")
        elif selectare_operatie == "-":
            rezultat = a - b
            print(f"{a} - {b} = {rezultat}")
            istoric.append(f"{a} - {b} = {rezultat}")
        elif selectare_operatie == "*":
            rezultat = a * b
            print(f"{a} * {b} = {rezultat}")
            istoric.append(f"{a} * {b} = {rezultat}")
        elif selectare_operatie == "^":
            rezultat = pow(a, b)
            print(f"{a} ^ {b} = {rezultat}")
            istoric.append(f"{a} ^ {b} = {rezultat}")
            
    elif selectare_operatie in ["/", "%"]:
        print("Care sunt termenii din operatie? ")
        a = citeste_numar("Primul termen a = ")
        while True:
            b = citeste_numar("Al 2-lea termen b = ")
            if b == 0:
                print("Eroare: Împărțirea la 0 nu este permisă!")
            else:
                break
                
        if selectare_operatie == "/":
            rezultat = a / b
            print(f"{a} / {b} = {rezultat}")
            istoric.append(f"{a} / {b} = {rezultat}")
        elif selectare_operatie == "%":
            rezultat = a % b
            print(f"Restul impartirii este: {a} % {b} = {rezultat}")
            istoric.append(f"{a} % {b} = {rezultat}")

    elif selectare_operatie == "radical":
        a = citeste_numar("Numarul de sub radical este: ")
        b = citeste_numar("Ordinul radicalului este: ")
        rezultat = a ** (1/b)
        print(f"Radical de ordin {b} din {a} = {rezultat}")
        istoric.append(f"Radical de ordin {b} din {a} = {rezultat}")
        
    elif selectare_operatie == "!":
        while True:
            a_str = input("La ce numar intreg vrei sa aplicam factorial: ")
            try:
                a = int(a_str)
                if a < 0:
                    print("Factorialul se aplica doar numerelor pozitive!")
                    continue
                break
            except ValueError:
                print("Te rog sa introduci un numar INTREG valid (ex: 5).")
                
        rezultat = math.factorial(a)
        print(f"{a}! = {rezultat}")
        istoric.append(f"{a}! = {rezultat}")