konto = {
    'imie': 'Artur',
    'nazwisko': 'Siepietowski',
    'stan': 0,
    'numer_telefonu': 123456775
}

konto1 = {
    'imie': 'Kamil',
    'nazwisko': 'Martynek',
    'stan': 1000,
}


def wplac(kwota, _konto):
    _konto['stan'] += kwota
    # _konto['stan'] = _konto['stan'] + kwota


def pokaz_detale(_konto):
    print(_konto['imie'], _konto['nazwisko'])
    print(_konto['stan'])

wplac(100, konto)
pokaz_detale(konto)
wplac(500, konto1)
pokaz_detale(konto1)


def wyplac(kwota, _konto):
    if _konto['stan'] >= kwota:
        _konto['stan'] -= kwota
        return kwota
    else:
        raise Exception("Nie masz wystarczająco srodków na koncie")


def wyplac_przez_bankomat(kwota, _konto):
    try:
        return wyplac(kwota, _konto)
    except Exception:
        print("EKRAN BANKOMATU: Brak środków")


def przelej(kwota, konto_nadawcy, konto_odbiorcy):
    try:
        temp = wyplac(kwota, konto_nadawcy)
        wplac(temp, konto_odbiorcy)
    except Exception:
        print("EKRAN STRONY INTERENTOWEJ: Brak środków do przelewu")


wyplac(100, konto)
przelej(200, konto, konto1)
print(konto)
print(konto1)
