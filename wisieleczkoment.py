from os import system
from random import randint

lista_hasel = []

with open("wisielec.txt", "r", encoding="utf-8")as plik:
    for linia in plik.readlines():
        lista_hasel.append(linia.strip())
        
        
ilosc_hasel_w_pliku = len(lista_hasel)-1 # ilość haseł 

def znajdz_indeksy(haslo,litera):
    indeksy = []
    for index, litera_w_slowie in enumerate(haslo):
        if litera==litera_w_slowie or str.upper(litera) ==litera_w_slowie: # litera jest zmienną/instrukcja warunkowa jeżeli
            indeksy.append(index)
    return indeksy  # return zwraca nam listę/wartości/indeksy w tym wypadku cyferki 

def kolejna_runda(): #
    while True:
        czy_dalej = input("Czy chcesz zagrac dalej (t/n)")  
        if czy_dalej =="t":      
            return 1
        elif czy_dalej =="n":
            return 0
        else:
            print("Podano nieprawidłową wartość, podaj inną wartość:")
            
def stan_gry():            
    system('cls') #czyści konsole
    print() # pusty print jest po to, aby była przerwa między liniami albo "\n" - dwie puste linie
    print("".join(haslo_uzytkownika)) # join za pomocą znacznika łącznika"".join przyjmuje obiekt literacyjny i zwraca stringa
    print("Liczba zyc:", liczba_zyc) # print oznacza wyświetlenie liczby żyć w naszym wypadku 5
    print("Uzyte litery:", uzyte_litery)   # liczba żyć na sztywno 5 to na dole w liście wyskakuje 
    print()
    
dalej = 1 # zaczynam grę 

while dalej == 1: 
    liczba_zyc = 5
   
    haslo = lista_hasel[randint(0, ilosc_hasel_w_pliku)] # hasło jest zmienną której wartość jest z listy haseł / lista haseł to jest lista w której są hasła; każde hasło znajduje się na danym indeksie i tworzy dane przysłowie; nawias kwadratowy jest od wskazania konkretnego, pojedyńczego indeksu / randit zwraca losowe liczby całkowite z zakresu [0,5]
    system ('cls') # czyścimy konsolę
    
    uzyte_litery = [] # tworzymy pustą liste użyte litery żeby przechować w liście
    
    haslo_uzytkownika = [] # tworzymy pustą listę hasło użytkownika żeby przechować w liście
    
    for _ in haslo: # pętla for ma się wykonać tyle razy ile jest znaków w haśle 
        haslo_uzytkownika.append("_") # hasło to jest ciąg znaków
        
    znalezione_indexy = znajdz_indeksy(haslo," ") # zmienna znalezione_indexy przyjmuje wartość zwróconą przez funkcję znajdź indeksy(hasło i ciąg znaków pusta spacja) / zwróci nam listę indeksów na których są spacje
    if len (znalezione_indexy) == 0: # jeżeli len - długość zmiennych znalezionych indeksów == porównana jest do zera to oznacza, że funkcja jest pusta, nie ma żadnych spacji  
        print() #
    else: # również 
        for index in znalezione_indexy: # dla zmiennej iteracyjnej znajdującej się w znalezione_indexy czyli na tej liście
            haslo_uzytkownika[index] = " " # hasło użytkownika składa się z [index] =  czyli pojedyńczych liter/  = " " przypisujemy wartość spacji
            
    znalezione_indexy = znajdz_indeksy(haslo, ",") # przypisanie wartości z funkcji znajdź indeksy przypisanie/nadpisanie wartości wynikiem jest znalezienie indeksów na którym stoją przecinki w haśle  
    if len(znalezione_indexy) == 0: # jeżeli len - długość zmiennych znalezionych indeksów na których stoją przecinki jest przyrównanie/bądź sprawdzenie, czy jest równe zero/jest pusta to nic się nie dzieję
        print() 
    else: # else wykona się kiedy będą indeksy na których znajdują się przecinki to wtedy nam się wyświetlą te przecinki
        for index in znalezione_indexy: # dla zmiennej literacyjnej index która się znajduje w zbiorze znalezione_indexy 
            haslo_uzytkownika[index]="," # w liście hasło użytkownika na podanym indeksie zapisana jest ta ="," konkretna wartość, którą bierzemy z listy znalezionych indexów
            
    print("wisielec v1.0") # wyświetlenie napisu wersji gry 
    print("".join(haslo_uzytkownika)) # wyświetlenie hasło użytkownika pojedyńczych liter i podłogi w całości w postaci jednego stringa(jednego ciągu znaków)
    
    
    while True: # while True: jest to nieskończona pętla 
        litera = str.lower(input("Podaj litere: ")) # tworzymy zmienną literę, która równa się funkcja input i dzięki temu użytkownik może ją wprowadzić z klawiatury;  przewidujemy, że użytkownikowi mógł się włączyć Caps  Lock  i zamieniamy z wielkiej litery na małą literę
        
        if len (litera)!=1: #  jeżeli długość litery jest różna od jednego (musimy zrobić to założenie, aby użytkownik  wprowadził jedną literę bo inaczej  mógłby wprowadzić 0 albo  więcej niż jedną  literę)
            print("\nWpisz jedna litere\n") # wyświetl pusta linia wpisz jedną literę i pusta linia
            input("Naciśnij enter, aby kontynuowac: ") # input zatrzymujemy konsolę użytkownik naciska enter, aby kontynuować
        else: # w przeciwnym razie się wyświetli, gdy użytkownik wprowadzi jedną literę
            try: # krauzla try jest po to żeby przechwycić błąd 
                uzyte_litery.index(litera) # metoda index zwraca indeks na których znajduje się litera, która znajduje się na liście, uzyte_litery to jest lista na których są zapisane/użyte przy użytkownika litery; po co index litery w liście litery odpowiedź brzmi po nic
                print("\nLitera była już użyta\n") # dana litera o którą pytamy była już użyta
                liczba_zyc -= 1 # jeżeli litera była już użyta to skraca nam się życie
                input("naciśnij enter") # jeżeli liczba naszego życia wyczerpie się to oznacza koniec gry
                if liczba_zyc == 0: # jeżeli liczba  żyć się wyczerpała  to jest koniec gry 
                    print("\nKoniec gry\nSzukane haslo to", haslo) # wyświetla się hasło koniec gry
                    dalej = kolejna_runda() # dalej jest zmienną która przyjmuje wartości kolejna_runda
                    break # break - jest zatrzymaniem w pętli; zatrzymuje pętle while True:
            except ValueError: # except się  wykona wtedy, try zwraca błąd - kiedy nie znajdzie indexu litery w liście użyte litery, mówi to nam, że  nie ma tej litery
                uzyte_litery.append(litera) # do listy uzyte_litery dodaje zmmieną litera
                znalezione_indexy = znajdz_indeksy(haslo, litera) # liście znalezione_indexy przypisujemy wartość funkcji znajdz_indeksy i to generalnie zwraca indexy liter znalezionych w haśle
                if len(znalezione_indexy)==0: # jeżeli długość znalezionych indexów jest pusta to nie ma litery 
                    print ("\nNie ma takiej litery") # wyświetl w nowej linii nie ma takiej litery 
                    liczba_zyc -= 1 # zmienna odejmuje życie 
                    input("Nacisnij enter, aby kontynuować") # input zatrzymuje konsole
                    if liczba_zyc == 0: # sprawdzamy, czy nam odjęło życie ..... DOPISZ  KOMENTARZ
                        print("\nKoniec gry!\nSzukane hasło to:", haslo) # wyświetla się hasło koniec gry
                        dalej = kolejna_runda() # dalej jest zmienną która przyjmuje wartości kolejna_runda
                        break # break - jest zatrzymaniem w pętli; zatrzymuje pętle while True:
                else: # kiedy długość znalezionych indeksów będzie różna od zera to wtedy się wykona dla
                    for index in znalezione_indexy:  # dla pętli for zmienna literacyjna index jest w znalezione_indexy wykonaj
                        haslo_uzytkownika[index] = litera # w haslo_uzytkownika (które jest listą, gdzie są litery na określonych indexach), jeżeli długość będzie inna niż zero to trzeba spisać wartość na określony index i się wyświetli litera w haśle 
                    
                    if "".join(haslo_uzytkownika) == str.lower(haslo): # jeżeli hasło użytkownika jest takie samo jak hasło, którego  szukamy to hura  wygraliśmy grę 
                        print("\nWygrałeś\n Szukane hasło to:", haslo) # print wyświetla że wygrałeś i szukane to: haslo wyświetlamy z wielkimi literkami
                        dalej = kolejna_runda() # zapytamy, czy chcesz zagrać dalej i w zmiennej zapiszę się 1 - to znaczy, że  chcesz grać albo 0 - że  nie chcesz grać
                        break # break - jest zatrzymaniem w pętli; zatrzymuje pętle while True:
        stan_gry() # na samym końcu pętli zostanie wszystko wyświetlone 
                    