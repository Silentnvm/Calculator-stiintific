# Calculator Științific cu Interfață Grafică (GUI)

Acest proiect este un calculator științific dezvoltat în Python, dotat cu o interfață grafică modernă și intuitivă, creată cu ajutorul bibliotecii CustomTkinter. Aplicația permite efectuarea de calcule aritmetice de bază, precum și operații matematice complexe.

## Cuprins
- [Funcționalități](#funcționalități)
- [Tehnologii Utilizate](#tehnologii-utilizate)
- [Cerințe și Instalare](#cerințe-și-instalare)
- [Cum se Utilizează](#cum-se-utilizează)
- [Structura Fișierelor](#structura-fișierelor)
- [Galerie](#galerie)

## Funcționalități
Calculatorul oferă o gamă largă de operații, accesibile atât prin butoane, cât și prin scurtături de la tastatură:

- **Operații de bază**: Adunare (`+`), Scădere (`-`), Înmulțire (`*`), Împărțire (`/`).
- **Operații avansate**:
    - Ridicare la putere (`^`)
    - Calcul procentual (`%`)
    - Radical (`√`)
    - Factorial (`!`)
    - Valoare absolută / Modul (`| |`)
- **Managementul numerelor**:
    - Schimbarea semnului (`+/-`)
    - Introducerea numerelor zecimale (`.`)
- **Managementul afișajului**:
    - Ștergere caracter cu caracter (`C` / `Backspace`)
    - Ștergere totală (`CA` / `Delete`)
- **Istoric**:
    - Un istoric al calculelor poate fi vizualizat într-o fereastră separată (buton `H`).

## Tehnologii Utilizate
- **Python 3**: Limbajul de programare de bază.
- **CustomTkinter**: O bibliotecă modernă bazată pe Tkinter pentru crearea interfețelor grafice. Oferă un aspect vizual plăcut și opțiuni de personalizare avansate.
- **Tkinter**: Biblioteca standard de GUI pentru Python, folosită ca bază de CustomTkinter.
- **Modulul `math`**: Utilizat pentru funcțiile matematice precum radical.

## Cerințe și Instalare
Pentru a rula acest proiect, este necesar să ai **Python 3** instalat pe sistemul tău.

Singura dependență externă este biblioteca `customtkinter`. Aceasta poate fi instalată folosind `pip`:
```bash
pip install customtkinter
```

## Cum se Utilizează
Aplicația se pornește prin rularea fișierului `calculator_stiintific_gui.py`.

Deschide un terminal sau o linie de comandă, navighează în directorul proiectului și execută următoarea comandă:
```bash
python calculator_stiintific_gui.py
```
Acest lucru va deschide fereastra principală a calculatorului, gata pentru a fi utilizat.

## Structura Fișierelor
Proiectul este compus din următoarele fișiere principale:

- **`calculator_stiintific_gui.py`**:
  - Acesta este **fișierul principal** al aplicației.
  - Conține tot codul pentru interfața grafică, logica butoanelor și gestionarea evenimentelor (apăsarea tastelor).
  - Definește aspectul ferestrei, butoanele și funcțiile apelate de acestea.
  - Evaluează expresiile matematice introduse și afișează rezultatul.

- **`calc_v2.py`**:
  - O versiune inițială a calculatorului, care funcționează **în linia de comandă (terminal)**.
  - Oferă funcționalități similare, dar fără o interfață grafică.
  - Poate fi rulat independent pentru o experiență bazată pe text. Nu este utilizat de aplicația grafică.

