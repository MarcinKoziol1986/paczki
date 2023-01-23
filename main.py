"""
Napisz program do obsługi ładowarki paczek.
Po uruchomieniu, aplikacja pyta ile elementów chcesz wysłać,
a następnie wymaga podania wagi dla każdego z nich.

Na koniec działania program powinien wyświetlić w podsumowaniu:

Liczbę paczek wysłanych
Liczbę kilogramów wysłanych
Suma "pustych" - kilogramów (brak optymalnego pakowania).
Liczba paczek * 20 - liczba kilogramów wysłanych
Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik

Restrykcje:

Waga elementów musi być z przedziału od 1 do 10 kg.
Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
W przypadku, jeżeli dodawany element przekroczy wagę towaru,
ma zostać dodany do nowej paczki, a obecna wysłana.
W przypadku podania wagi elementu mniejszej od 1kg lub większej od 10kg,
dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane.
Wyświetlane jest podsumowanie.

"""
"""
restrykcje:
1 <=waga elementu <=10
waga aktualnej paczki <=20 0
max_waga_paczki = 20
# szablon = (f"Wysłano paczek; {paczka}, Wysłano;  kg, "
#           f"Suma pustych kilogramów: ," \
#          "Najwięcej pustych kilogramów ma paczka {}")
#
# print(szablon)
"""
print("Witam "
      "Przygotuj dane potrzebne do wysyłki")

liczba_paczek_wyslanych = 0
liczba_kilogramow_wyslanych = 0
waga_najlzejszej_paczki = 20
numer_najlzejszej_paczki = None
waga_aktualnej_paczki = None
# dodaj waga_elementu do waga_aktuaalnej_paczki


ilosc_elementow = int(input("Ile elementów chcesz wysłać ?:"))
for numer_elementu in range(ilosc_elementow):
    waga_elementu = int(input("Podaj wagę elementu: "))
    if not (1 <= waga_elementu <= 10):
        break
    waga_aktualnej_paczki = int(waga_elementu)
    if waga_aktualnej_paczki >= 20:
        waga_aktualnej_paczki -= int(waga_elementu)
        liczba_paczek_wyslanych = liczba_paczek_wyslanych + 1
        if waga_aktualnej_paczki <= waga_najlzejszej_paczki:
            waga_najlzejszej_paczki = waga_aktualnej_paczki
            numer_najlzejszej_paczki = liczba_paczek_wyslanych
        liczba_kilogramow_wyslanych += waga_aktualnej_paczki
        waga_aktualnej_paczki = int(waga_elementu)
    if waga_aktualnej_paczki == 20:
        liczba_paczek_wyslanych = liczba_paczek_wyslanych + 1
        if waga_aktualnej_paczki <= waga_najlzejszej_paczki:
            waga_najlzejszej_paczki = waga_aktualnej_paczki
            numer_najlzejszej_paczki = liczba_paczek_wyslanych
        liczba_kilogramow_wyslanych += waga_aktualnej_paczki
        waga_aktualnej_paczki = 0
    if waga_aktualnej_paczki <= 20:
        pass
if waga_aktualnej_paczki >= 0:
    liczba_paczek_wyslanych = liczba_paczek_wyslanych + 1
    if waga_aktualnej_paczki <= waga_najlzejszej_paczki:
        waga_najlzejszej_paczki = waga_aktualnej_paczki
        numer_najlzejszej_paczki = liczba_paczek_wyslanych
    liczba_kilogramow_wyslanych += waga_aktualnej_paczki
print(f'Liczba paczek wyslanych ;{liczba_paczek_wyslanych}')
print(f'Liczba Kilogramow wyslanych ;{liczba_kilogramow_wyslanych}')
print(
    f'Suma pustych kilogramow; '
    f'{liczba_paczek_wyslanych * 20 - liczba_kilogramow_wyslanych}')
print(f'Numer najlzejszej paczki; {numer_najlzejszej_paczki}')
print(f'Waga najlzejszej paczki; {waga_najlzejszej_paczki}')
print('Dziekujemy za skorzystanie z naszego programu')
