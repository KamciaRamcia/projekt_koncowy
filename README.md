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
### 2.1. Menu główne

Menu główne jest ekranem powitalnym, z którego użytkownik może przejść do innych interfejsów programu. 
Kod znajduje się w skrypcie,,interface_main.py”.
Klasy, które zostały stworzone na potrzeby skryptu:
* FirstPage - skrypt tworzy graficzny interfejs oraz posiada funkcje, dzięki którym wybranie przycisku otwiera inne interfejsy
<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/5a89e7fb-0ea2-48f2-af63-7382e031b2d2">

### 2.2. Przykładowa gra

Jako przykładowa gra generowana siatka na podstawie słownika, znajdującego się w folderze ,,Example_fishcard.py”.

Kod znajduje się w skryptach:
* ,,feature_memo_game.py”
* ,,interface_memo_game.py”
* ,,interface_winner_window.py”
Klasy, które zostały stworzone na potrzeby skryptów:
* MemoGamePage 
* ButtonWithWord

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/24c9c249-d21b-45d0-a907-b7eaf95e08bc">

Podany słownik przekształcany jest na listę, aby przemieszać słowa, a następnie tworzyć przyciski z kolejnymi elementami przemieszanej listy


	
Użytkownik grając, naciska przyciski, aby znaleźć poprawną parę słowo-tłumaczenie.
Gdy para jest błędna, wybrane przyciski zmieniają kolor na czerwony

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/00a22921-dffd-4194-aa51-d4a0c9b6f058">

Gdy para jest poprawna - przyciski zmieniaja kolory na zielony

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/3b3d8be2-810e-4b9b-954d-963367538f14">

Gdy użytkownik odnajdzie wszystkie pary. Zostaje ukazane okno ze statystyką. 

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/8aeaae06-dbeb-4630-b43a-b9a7f9a44ed7">

### 2.3. Dodawanie fiszek

Kod znajduje się w skryptach:
* ,,feature_add_fishcard.py”
* ,,interface_add_fishcard.py”
* ,,interface_upload_status_window.py”
Klasy, które zostały stworzone na potrzeby skryptów:
* AddFishcardPage
* NewFishcardSet

Użytkownik może dodawać swoje fiszki. Wystarczy wgrać plik, który spełnia podane wymogi:
* pierwszy wiersz posiada w dwóch pierwszych komórkach nazwy: angielski, polski
* plik jest w formacie .csv
* plik posiada maksymalnie 25 par słowo-tłumaczenie
* ścieżka do pliku jest poprawna
* plik nie posiada zduplikowanych słów
* najdłuższe słowo posiada 40 znaków
* nazwa zbioru fiszek (podawane przez użytkownika) posiada maksymalnie 30 znaków
* nazwa pliku nie duplikuje się z plikiem już istniejącym
  
Program sprawdza czy wszystkie warunki zostały spełnione, aby dodać fiszki i zapisać je w pliku jako słownik.

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/7c6814c8-547b-4b37-a435-a015ee040abc">

W przypadku, gdy plik nie spełnia wymogów - nowe okno zostaje otwarte. Wyświetlają się informacje co należy zmienić, aby wgrać słownik

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/04b2e6b7-c7b4-498d-b725-2c97fd6df6c2">

### 2.4. Lista fiszek
Kod znajduje się w skryptach:
* ,,feature_fishcard_list.py”
* ,,interface_delete_fishcard.py”
* ,,interface_fishcard_list.py”
  
Klasy, które zostały stworzone na potrzeby skryptów:
* FishCardListPage
* NewListElement

Program generuje listę fiszek, które zostały wgrane do aplikacji.

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/7b83d59b-8cbf-4b68-9898-a963705bc95c">

Użytkownik może usunąć zbiór fiszek poprzez wybranie przycisku ‘usuń’.

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/894c38b9-70de-4642-a19d-73799c95b4b0">

Gdy użytkownik wybiera opcję ,,Zagraj”, program otwiera okno z grą Memo używając wybranego słownika. Algorytm oblicza ile wiersz i kolumn powinno zostać wygenerowane dla danej liczby słów w słowniku.

