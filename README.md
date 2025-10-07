# Treti_projekt_Python_Analytik
Finální projekt do kurzu Python Akademie
------------------------------------------
    Popis projektu
Elections Scraper stáhne výsledky voleb zadaný územní celek a uloží je do CSV. Skript přijímá přes příkazovou řádku přesně dva argumenty: URL územního celku a název výstupního CSV souboru.
------------------------------------------
    Struktura repozitáře
  * main.py — hlavní skript (spouští se s 2 argumenty)
  * requirements.txt — seznam knihoven
  * README.md — tato dokumentace
------------------------------------------
    Požadavky
  * Python 3.8 nebo novější.
  * Virtuální prostředí doporučeno.
  * Knihovny: requests, beautifulsoup4.
------------------------------------------
    Instalace závislostí
* Vytvořte a aktivujte virtuální prostředí:
  * Windows:
    * python -m venv venv
    * venv\Scripts\activate
  * macOS / Linux:
    * python3 -m venv venv
    * source venv/bin/activate
* Nainstalujte závislosti ze souboru requirements.txt:
  * pip install -r requirements.txt
------------------------------------------
    Spuštění skriptu
Skript se spouští s dvěma argumenty: URL územního celku (musí být plná URL začínající http:// nebo https://) a název výstupního CSV souboru (končí .csv).
  * python main.py "<URL_UZEMNIHO_CELKU>" "<vystupni_soubor.csv>"
  * python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv
Pokud nejsou zadány oba argumenty nebo mají nesprávný formát, skript oznámí chybu a nepokračuje.
------------------------------------------
    Příklad výstupu:
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA,ODPOVĚDNÉ
506741,Albrechtice,205,145,144,2,1,0,0
589281,Bělá,264,172,171,1,0,0,0
589282,Bělá-Belkovice-Lašťan,205,145,144,2,1,0,0
...
589308,Dědice,1239,748,742,4,3,1,1
