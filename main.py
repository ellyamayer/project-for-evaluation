def guess_number():
    """
    Gra polegająca na odgadnięciu liczby wylosowanej przez komputer w zakresie od 1 do 10.
    """
    import random
    number = random.randint(1, 10)
    while True:
        guess = int(input("Odgadnij liczbę od 1 do 10: "))
        if guess == number:
            print("Gratulacje, zgadłeś numer!")
            break
        else:
            print("Spróbuj jeszcze raz!")

def rock_paper_scissors():
    """
    Gra w 'Kamień, nożyczki, papier' dla dwóch graczy.
    Gracz 1 i Gracz 2 dokonują wyboru, a następnie ogłaszany jest wynik.
    """
    player1 = input("Gracz 1, wybierz: kamień, nożyczki lub papier: ")
    player2 = input("Gracz 2, wybierz: kamień, nożyczki lub papier: ")
    if player1 == player2:
        print("To remis!")
    elif (player1 == "kamień" and player2 == "nożyczki") or (player1 == "nożyczki" and player2 == "papier") or (player1 == "papier" and player2 == "kamień"):
        print("Gracz 1 wygrał!")
    else:
        print("Gracz 2 wygrał!")

def dice_roll():
    """
    Symulator rzutu kostką. Generuje losową liczbę od 1 do 6 i wyświetla wynik.
    """
    import random
    dice = random.randint(1, 6)
    print("Liczba wypadła:", dice)

while True:
    print("Wybierz grę: ")
    print("1. Zgadnij liczbę")
    print("2. Kamień, nożyczki, papier")
    print("3. Rzut kostką")
    choice = int(input("Wprowadź numer gry lub 0, aby wyjść: "))
    if choice == 1:
        guess_number()
    elif choice == 2:
        rock_paper_scissors()
    elif choice == 3:
        dice_roll()
    elif choice == 0:
        break
    else:
        print("Zły wybór. Spróbuj jeszcze raz.")