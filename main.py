import sys
import re
from urllib.request import urlopen
from lxml import etree

def checkInputParams():
    # Zkontroluji počet argumentů (musí být 3 -> jinak skončí chybou)
    if (len(sys.argv) != 3):
       sys.exit("Nesprávný počet argumentů.")
    # Zkontroluji zda je výstupní soubor csv
    if (len(re.findall('^[\\w,\\s-]+\\.[A-Za-z]{3}$', sys.argv[2])) != 1):
        sys.exit("Název souboru není validní.")
    # Zkontroluji jestli výstupní soubor končí na .csv
    if (sys.argv[2].lower().endswith(".csv") == False):
        sys.exit("Název výstupního souboru musí být typu .csv.")
    print("Kontrola vstupních parametrů - OK")

# Načtení z webu
def loadFromWeb(): 
    obce = []
    urlBase = "https://www.volby.cz/pls/ps2017nss/"
    try:
        response = urlopen(sys.argv[1])
    except:
        sys.exit("URL adresa nebyla načtena, pravděpodobně neodpovídá formátu URL adresy.")
    if (response.code != 200):
       sys.exit(f"Nebyla vrácena data: {response.msg}.")
    htmlParser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse(response, htmlParser)

    for obec in tree.xpath(".//div[@class='t3']//tr[.//td]"):

        cislo = getFirstEl(obec.xpath(".//td[@class='cislo']/a/text()"))
        nazev = getFirstEl(obec.xpath(".//td[@class='overflow_name']/text()"))
        href = getFirstEl(obec.xpath(".//td[@class='cislo']/a/@href"))

        # přeskočení prázdných buněk
        if cislo == "" or nazev == "" or href == "":
            continue

        obce.append({
           "cislo": cislo,
           "nazev": nazev,
           "url": f"{urlBase}{href}"
        })

    if (len(obce) == 0):
        sys.exit("Z webové stránky se nepodařilo načíst obce. Je pravděpodobné že stránka neobsahuje obce v požadovaném formátu.")
    print("Načtení obcí - OK")
    return obce

# Načtu kandidující strany
def loadKandidujiciStrany(obec): 
    kandidujiciStrany = []
    response = urlopen(obec["url"])
    htmlParser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse(response, htmlParser)
    for strana in tree.xpath(".//td[@class='overflow_name']/text()"): 
        kandidujiciStrany.append(strana)
    print("Přehled kandidujících stran - OK")
    return kandidujiciStrany

# Načtu jednotlivá data za obce
def loadDataZaObce(obce: dict):
    poradiobec = 1
    for obec in obce:
        print(f"probíhá načítání dat za obec {obec['nazev']} ({poradiobec} / {len(obce)})")
        response = urlopen(obec["url"])
        htmlParser = etree.HTMLParser()
        tree = etree.parse(response, htmlParser)
        del obec["url"]
        obec["registered"] = getFirstEl(tree.xpath(".//table//td[@headers='sa2']/text()"))
        obec["envelopes"] = getFirstEl(tree.xpath(".//table//td[@headers='sa3']/text()"))
        obec["valid"] = getFirstEl(tree.xpath(".//table//td[@headers='sa6']/text()"))
        index = 1
        for strana in tree.xpath(".//td[@headers='t1sa2 t1sb3']/text()"): 
            obec[str(index)] = strana
            index += 1
        for strana in tree.xpath(".//td[@headers='t2sa2 t2sb3']/text()"): 
            obec[str(index)] = strana
            index += 1
        poradiobec += 1
    print("Data za jednotlivé obce - OK")
    return obce

# Uložení načtených dat do souboru
def saveDataToFile(kandidujiciStrany: dict, dataZaObce: dict): 
    content = "code;location;registered;envelopes;valid;"
    for kandidujiciStrana in kandidujiciStrany:
       content += f"{kandidujiciStrana};"
    content += "\n"
    for dataZaObec in dataZaObce:
        dataZaObec = upravitNecitelneZnaky(dataZaObec)
        for item in dataZaObec:
            content += f"{dataZaObec[item]};"
        content += "\n"
    with open(sys.argv[2], "w", encoding="windows-1250") as f:
        f.write(content)
    print(f"Data byla uložena do souboru: {sys.argv[2]} - OK")

# Funkce na úpravu nečitelných znaků 
def upravitNecitelneZnaky(data: dict) -> dict:
    cleaned = {}
    for key, value in data.items():
        if isinstance(value, str):
            val = value.replace("\xa0", "").replace(" ", "")
            if val.isdigit():
                cleaned[key] = int(val)
            else:
                cleaned[key] = value.replace("\xa0", " ") 
        else:
            cleaned[key] = value
    return cleaned

# Získání prvního elementu (neskončí chybou)
def getFirstEl(data) -> str:
    if (len(data) > 0):
       return data[0]
    return ""

# Main
checkInputParams()
# Na4tení obcí
obce = loadFromWeb()
# Načtení kandidujících stran
kandidujicistrany = loadKandidujiciStrany(obce[0])
# Načtení jednotlivýc obcí
dataZaObce = loadDataZaObce(obce)
# Uložení do souboru
saveDataToFile(kandidujicistrany, dataZaObce)