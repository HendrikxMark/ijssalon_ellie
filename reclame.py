from algemene_functies import mijn_functie_2

def aanbieding_1(Smaak, Prijs, Korting):
    nieuwe_prijs = f"{Prijs - (Prijs * Korting):.2f}" . replace(".", ",")
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {Smaak}, van {Prijs} euro voor {nieuwe_prijs} euro."
    return uitvoer

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = f"{sum(inkomsten) / (1 + btw):.2f}" .replace(".", ",")
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

def gemiddelde(mijn_lijst):
    aantal = len(mijn_lijst)
    gemiddelde_inkomsten = f"{sum(mijn_lijst) / aantal:.2f}" .replace(".", ",")
    uitvoer = f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro."
    return uitvoer

def meervoudig(invoerlijst):
    return laag_en_hoog(invoerlijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])


print("Aanbieding: ", aanbieding_1("aardbei", 4, 0.1))
print("Totale inkomsten: ", inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))
print("Hoogste en laagste: ", laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))
print("Gemiddelde: ", gemiddelde([220, 430, 125, 160, 205, 90, 345]))
print("Meervoudig: ", meervoudig([10,5,3,2,1,2,9]))
print("Combinatie: ", combinatie([10,5,3,2,1,2,9]))
