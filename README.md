# Treti_projekt_Python_Analytik
Finální projekt do kurzu Python Akademie
------------------------------------------
Popis projektu:
    Tento projekt slouží k extrahování výsledků z parlamentních voleb z roku 2017. 
------------------------------------------
Instalace knihoven:
    Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt. Pro instalaci doporučuji použít nové virtuální prostředím. Spuštění:
  * pip3 --version
  * pip3 install -r requirements.txt
------------------------------------------
Spuštění skriptu
    Skript se spouští dvěma argumenty:
    
    1. argument - https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
    2. argument - vysledky_prostejov.csv
------------------------------------------
Příklad spuštění

	python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv
------------------------------------------
Výsledkem spuštění je stáhnutí souboru vysledky_prostejov.csv

	Průběh stahování Kontrola vstupních parametrů - OK Načtení obcí - OK Přehled kandidujících stran - OK Data za jednotlivé obce - OK
------------------------------------------
Ukázka projektu
Výstup v CSV
<img width="1071" height="383" alt="image" src="https://github.com/user-attachments/assets/3d52c6ba-bcfa-490b-a242-61071e6b8331" />
Výstup CSV v EXCEL
<img width="1550" height="664" alt="image" src="https://github.com/user-attachments/assets/1e7ca177-01f3-4002-b4c3-a4d4dd600dee" />
