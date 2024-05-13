## Spis treści
* [Informacje ogólne](#info-ogólne)
* [Technologia](#tech)
* [Uruchomienie aplikacji](#Uruchomienie-aplikacji)
* [Funkcje aplikacji](#Funkcje-aplikacji)

## Informacje ogólne

Aplikacja pomaga w nauce słówek poprzez popularną grę Memo. Użytkownik, oprócz zagrania w przykładową grę, ma możliwość wgrać do programu własną listę słówek, aby na ich podstawie. 
Program przekształca podane fiszki na słownik, który jest podawany do algorytmu tworzącego grę Memo. Na podstawie słowników jest tworzona siatka, w której każdy element jest słowem (kluczem lub atrybutem) słownika.
Elementy są umieszczane na siatce, po uprzednim określeniu przez algorytm ilości kolumn i wierszy odpowiednich dla danej ilości słów.
Użytkownik ma również możliwość usuwania zbioru fiszek - wtedy plik ze słownikiem zostanie trwale usunięty z projektu.

Aplikacja posiada następujące funkcjonalności: 
* generowanie gry memo na podstawie słownika
* dodawanie listy fiszek poprzez wgrywanie pliku csv
* usuwanie listy fiszek 

## Technologia
Aplikacja została napisana za pomocą biblioteki Tkinter - jest to biblioteka do tworzenia interfejsu graficznego. Oprócz tego zostały wykorzystane między innymi takie biblioteki jak importlib, os csv oraz math, jednakże zostały one wykorzystane w mniejszym stopniu.
Do interfejsu graficznego została wykorzystana czcionka Amatic SC, która nie jest czcionką domyślną w systemie windows. Jest ona udostępniona na zasadach otwartej licencji.

## Uruchomienie aplikacji
W celu uruchomienia aplikacji należy uruchomic skrypt 'interface_main.py'


## Funkcje aplikacji
2.1. Menu główne

Menu główne jest ekranem powitalnym, z którego użytkownik może przejść do innych interfejsów programu. 
Kod znajduje się w skrypcie,,interface_main.py”.
Klasy, które zostały stworzone na potrzeby skryptu:
FirstPage - skrypt tworzy graficzny interfejs oraz posiada funkcje, dzięki którym wybranie przycisku otwiera inne interfejsy



	




