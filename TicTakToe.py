spielfeld= [" ",
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"]

Aktueller_Spieler ="X"
spiel_aktiv = True




def spielfeld_output():
    print(spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3])
    print(spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6])
    print(spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9])





def spieler_input(Aktueller_Spieler):
    spielzug = input(f"Bitte Feld eingeben Spieler: {Aktueller_Spieler}")


    try:
        spielzug = int(spielzug)
    except ValueError:
        print("Bitte Geben sie eine Zahl ein")
    else:

        if spielzug <1 or spielzug >9:
            print("Bitte gib eine Zahl zwischen 1 und 9 ein")
            spieler_input(Aktueller_Spieler)
        elif spielfeld[spielzug] == "X" or spielfeld[spielzug] == "O":
            print("Spielfelf ist schon vergeben")
            spieler_input(Aktueller_Spieler)
        elif spielzug >= 1 or spielzug <= 9 and spielfeld[spielzug] != "X" or spielfeld[spielzug] != "O":
            spielfeld[spielzug] = Aktueller_Spieler


def spieler_wechsel(Aktueller_Spieler):


    if Aktueller_Spieler == "X":
       Aktueller_Spieler = "O"

    elif Aktueller_Spieler == "O":
        Aktueller_Spieler = "X"

    return Aktueller_Spieler





def gewonnen_check(spiel_aktiv):

    if spielfeld[1] == spielfeld[2] == spielfeld[3]:
        print(f"{spielfeld[1]} hat Gewonnen")
        spiel_aktiv = False
    elif spielfeld[4] == spielfeld[5] == spielfeld[6]:
        print(f"{spielfeld[4]} hat Gewonnen")
        spiel_aktiv = False
    elif spielfeld[7] == spielfeld[8] == spielfeld[9]:
        print(f"{spielfeld[7]} hat Gewonnen")
        spiel_aktiv = False
    elif spielfeld[1] == spielfeld[5] == spielfeld[9]:
        print(f"{spielfeld[1]} hat Gewonnen")
        spiel_aktiv = False
    elif spielfeld[7] == spielfeld[5] == spielfeld[3]:
        print(f"{spielfeld[7]} hat Gewonnen")
        spiel_aktiv = False
    elif spielfeld[1] == spielfeld[4] == spielfeld[7]:
        print(f"{spielfeld[4]} hat Gewonnen")
        spiel_aktiv = False
    elif spielfeld[2] == spielfeld[5] == spielfeld[8]:
        print(f"{spielfeld[2]} hat Gewonnen")
        spiel_aktiv = False
    elif spielfeld[3] == spielfeld[6] == spielfeld[9]:
        print(f"{spielfeld[3]} hat Gewonnen")
        spiel_aktiv = False



    return spiel_aktiv


def unentschieden_check(spiel_aktiv):
    if (spielfeld[1] == "X" or  spielfeld[1] == "O") and \
       (spielfeld[2] == "X" or  spielfeld[2] == "O") and \
       (spielfeld[3] == "X" or  spielfeld[3] == "O") and \
       (spielfeld[4] == "X" or  spielfeld[4] == "O") and \
       (spielfeld[5] == "X" or  spielfeld[5] == "O") and \
       (spielfeld[6] == "X" or  spielfeld[6] == "O") and \
       (spielfeld[7] == "X" or  spielfeld[7] == "O") and \
       (spielfeld[8] == "X" or  spielfeld[8] == "O") and \
       (spielfeld[9] == "X" or  spielfeld[9] == "O"):
        print("Das Spiel ist unentschieden ausgegangen")
        spiel_aktiv = False


    return spiel_aktiv




spielfeld_output()

while spiel_aktiv:
    spieler_input(Aktueller_Spieler)
    Aktueller_Spieler = spieler_wechsel(Aktueller_Spieler)
    spiel_aktiv = gewonnen_check(spiel_aktiv)
    spiel_aktiv = unentschieden_check(spiel_aktiv)
    spielfeld_output()






