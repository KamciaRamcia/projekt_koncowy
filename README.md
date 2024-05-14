## Spis treści
* [Informacje ogólne](#info-ogólne)
* [Technologia](#tech)
* [Uruchomienie aplikacji](#Uruchomienie-aplikacji)
* [Interfejsy aplikacji](#Interfejsy-aplikacji)

## Informacje ogólne

Aplikacja pomaga w nauce słówek poprzez popularną grę Memo. Użytkownik, oprócz zagrania w przykładową grę, ma możliwość wgrać do programu własną listę słówek (fiszek) , aby posłużyła ona w rozgrywce.

Program przekształca podany przez użytkownika plik csv na słownik. Na jego podstawie algorytm kalkuluje jak powinny zostać ułożone elementy gry, po czym generuje siatkę elementów, gdzie każdy z elementów jest przyciskiem z tekstem - atrybutem lub kluczem słownika.
Gra opiera się na podstawowych zasadach gry Memo. Użytkownik szuka par słowo - tłumaczenie, poprzez wybanie dwóch przycisków. Gdy para jest poprawna, przyciski zmieniają kolor na zielony. W przypadku błędnie wybranej pary, przyciski zmianają kolor na czewony.
Użytkownik ma również możliwość usuwania zbioru fiszek - wtedy plik ze słownikiem zostanie trwale usunięty z projektu.

Aplikacja posiada następujące główne funkcjonalności: 
* generowanie gry memo na podstawie słownika
* dodawanie listy fiszek poprzez wgrywanie pliku csv
* usuwanie listy fiszek 

## Technologia
Aplikacja została napisana za pomocą biblioteki Tkinter - jest to biblioteka do tworzenia interfejsu graficznego. Oprócz tego, zostały wykorzystane takie biblioteki jak importlib, os csv oraz math.
Do interfejsu graficznego została wykorzystana czcionka Amatic SC, która nie jest czcionką domyślną w systemie windows. Jest ona udostępniona na zasadach otwartej licencji.

## Uruchomienie aplikacji
W celu uruchomienia aplikacji należy uruchomic skrypt 'interface_main.py'
W przypadku braku zainstalowanej czcionki Amatic SC interfejs może stać się nieprzejrzysty. W celu poprawnego wyświetlania zalecane jest zainstalowanie tej czcionki.

## Interfejsy aplikacji
### 2.1. Menu główne

Menu główne jest ekranem powitalnym, z którego użytkownik może przejść do innych interfejsów programu: przykładowej gry, listy fiszek oraz dodawania fiszek. Może również zamknąć aplikacje.

Kod znajduje się w skrypcie,,interface_main.py”.

Klasy, które zostały stworzone na potrzeby skryptu:
* FirstPage
  
<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/5a89e7fb-0ea2-48f2-af63-7382e031b2d2">

### 2.2. Przykładowa gra

Jako przykładowa gra generowana jest siatka na podstawie słownika, znajdującego się w folderze ,,Example_fishcard.py”. 

Kod znajduje się w skryptach:
* ,,feature_memo_game.py”
* ,,interface_memo_game.py”
* ,,interface_winner_window.py”
  
Klasy, które zostały stworzone na potrzeby skryptów:
* MemoGamePage 
* ButtonWithWord

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/24c9c249-d21b-45d0-a907-b7eaf95e08bc">

Podany słownik przekształcany jest na listę. Funkcja ,,shuffle_dictionary" miesza jej elementy. Następnie kolejne elementy listy są wykorzystywane do generowania elementów gry.

Podczas rozgrywki użytkownik wybiera dwa elementy. Jeżeli nie były one już wczesniej poprawnie zaznaczone, program sprawdza czy wybrane elementy pasują do elementu słownika klucz:atrybut - odpowiada za to funkcja ,,check_pair" klasy ButtonWithWord. Po wybraniu poprawnej pary, zostaje sprawdzana ilość znalezionych par. Jeżeli użytkownik znalazł wszystkie pary, ukazuje się okno ze statystykami.

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/8aeaae06-dbeb-4630-b43a-b9a7f9a44ed7">

### 2.3. Dodawanie fiszek

Użytkownik mam możliwość wgrać swoją liste słówek, aby wykorzystywać je do rozgrywki. Aby wgrać plik, użytkownik musi podać ścieżkę do pliku ( w polu ,,Ścieżka do pliku .csv") oraz nazwę pod jaką zbiór fiszek ma figurować na liście w aplikacji (w polu ,,Nazwa").

Kod znajduje się w skryptach:
* ,,feature_add_fishcard.py”
* ,,interface_add_fishcard.py”
* ,,interface_upload_status_window.py”
  
Klasy, które zostały stworzone na potrzeby skryptów:
* AddFishcardPage
* NewFishcardSet

Przed wgraniem pliku, aplikacja sprawdza czy są spełnione podane wymogi:
* pierwszy wiersz posiada w dwóch pierwszych komórkach nazwy: angielski, polski
* plik jest w formacie .csv
* plik posiada maksymalnie 25 par słowo-tłumaczenie
* ścieżka do pliku jest poprawna
* plik nie posiada duplikatów słów
* najdłuższe słowo posiada 40 znaków
* nazwa zbioru fiszek (podawane przez użytkownika) posiada maksymalnie 30 znaków
* nazwa zbioru fiszek (podana przez użytkownika) jest unikalna - nie istnieje plik z podana nazwą w aplikacji
  
Za sprawdzenie zawartości, ścieżki oraz nazwy pliku odpowiada funkcja ,,set_of_checks" klasy NewFishcardSet. 

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/7c6814c8-547b-4b37-a435-a015ee040abc">

Po wybraniu przycisku ,,Wgraj" zostaje otwarte nowe okno. W przypadku, gdy plik nie spełnia wymogów -  wyświetlają się informacja co należy zmienić, aby wgrać plik z fiszkami. Gdy plik spełnia wymogi - ukazuje się informacja o wgraniu pliku.

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/04b2e6b7-c7b4-498d-b725-2c97fd6df6c2">

### 2.4. Lista fiszek

Zostaje wygenerowana lista fiszek, które zostały wgrane do aplikacji. Aplikacja może maksymalnie posiadać 10 wgranych plików. Poprzez wybranie przycisku ,,Zagraj" zostaje wygenerowana gra Memo z wybraną listą fiszek. Gdy użytkownik wybiera przycisk ,,Usuń", plik zostaje usunięty i nie pojawi się już na liście.

Kod znajduje się w skryptach:
* ,,feature_fishcard_list.py”
* ,,interface_delete_fishcard.py”
* ,,interface_fishcard_list.py”
  
Klasy, które zostały stworzone na potrzeby skryptów:
* FishCardListPage
* NewListElement

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/7b83d59b-8cbf-4b68-9898-a963705bc95c">

Użytkownik może usunąć zbiór fiszek poprzez wybranie przycisku ‘usuń’.

<img src="https://github.com/KamciaRamcia/projekt_koncowy/assets/61707204/894c38b9-70de-4642-a19d-73799c95b4b0">



