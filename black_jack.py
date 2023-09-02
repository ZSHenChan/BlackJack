import random
from time import sleep


def sort_cards(x):
    for i in x:
        if i == 'A':
            x.remove(i)
            x.append("A")


def calculate_points(x):
    point = 0
    sort_cards(x)
    for i in x:
        if isinstance(i,int):
            point += i
        elif i == 'A':
            if len(x) == 2:
                if point == 11:
                    point += 10
                else:
                    point += 11
            elif len(x) == 3:
                if x.count('A') == 2:
                    if point <= 11:
                        point += 10
                    elif point == 21:
                        point -= 8
                    else:
                        point += 1
                elif x.count('A') == 1:
                    if point <= 11:
                        point += 10
                    else:
                        point += 1
            else:
                point += 1
        else:
            point += 10
    return point


def draw_card(x):
    random_card = random.choice(deck)
    x.append(random_card)
    deck.remove(random_card)
    print("card drawed")
    print("...")
    sleep(2)
    print("cards in hand: ", end="")
    for i in x:
        print(str(i) , end = " ")
    print("")


def host_draw(x):
    random_card = random.choice(deck)
    x.append(random_card)
    deck.remove(random_card)


def display():
    print("Your cards: ", end="")
    for cc in player_cards:
        print(cc, end=" ")
    print("")


def points_cal(x, y):
    if len(x)==5 or len(y)==5:
        if calculate_points(x) == 21 and len(x)==5:
            return 3
        elif calculate_points(x) < 21 and len(x) ==5:
            return 2
        elif calculate_points(y) == 21 and len(y) == 5:
            return -3
        elif calculate_points(y) < 21 and len(y) ==5:
            return -2
        else:
            pass

    if len(x) == 2 and calculate_points(x) == 21:
        if x == ["A","A"]:
            return 3
        else:
            return 2

    elif len(y) == 2 and calculate_points(y) == 21:
            if y == ["A","A"]:
                return -3
            else:
                return -2

    elif calculate_points(x) > 21:
        if calculate_points(y) > 21:
            return 0
        elif calculate_points(y) == 21:
            return -2
        else:
            return -1

    elif calculate_points(y) > 21:
        if calculate_points(x) == 21:
            return 2
        else:
            return 1

    else:
        if calculate_points(x) == calculate_points(y):
            return 0
        if calculate_points(x) > calculate_points(y):
            return 1
        else:
            return -1


def run():
    for i in omg:
        for _ in range(2):
            random_card = random.choice(deck)
            i.append(random_card)
            deck.remove(random_card)

    point = 0
    display()
    dragon = False

    while calculate_points(player_cards)<=21 and len(player_cards) <= 5:
        respond = input("Draw card? (y/n): ")
        if respond == 'y':
            draw_card(player_cards)
            if len(player_cards)==5:
                if calculate_points(player_cards)<=21:
                    print("You won with DRAGON!!!!")
                    display()
                    dragon = True
                    if calculate_points(player_cards) == 21:
                        point = 3
                    else:
                        point = 2
                    break
                else:
                    print("BOOM!!\nYou Lost!!")
                    dragon = True
                    display()
                    point = -2
                    break

            elif calculate_points(player_cards)>21:
                sleep(1)
                print("Oh Shit...")
                sleep(1)
                break

            elif calculate_points(player_cards) == 21:
                print("perfect!")
                sleep(1)
                break

            else:
                continue
        else:
            break

    while calculate_points(host) <17 and len(host)<5 and not dragon:
        host_draw(host)
        print("host drawing card...")
        sleep(1)
        if len(host) == 5:
            if calculate_points(host)<=21:
                print("Host Won with dragon!!!")
                print("Host Cards: ", end="")
                for dd in host:
                    print(dd, end=" ")
                    print("")
                dragon = True
                break
            else:
                print("BOM!!")
                print("You Won!")
                print("Host Cards: ", end="")
                for dd in host:
                    print(dd, end=" ")
                    print("")
                dragon = True
                break

    print("Your cards: ", end="")
    for cc in player_cards:
        print(cc, end=" ")
    print("={}".format(calculate_points(player_cards)))
    if not dragon:
        print("Host Cards: ", end="")
    for dd in host:
        print(dd, end=" ")
    print("={}".format(calculate_points(host)))
    point = points_cal(player_cards, host)
    sleep(2)

    if not dragon:
        print("")
        player_points = calculate_points(player_cards)
        host_points = calculate_points(host)

        if host_points > player_points:
            if host_points <= 21:
                print("You Lost!")
            else:
                print("You Won!")

        elif host_points == player_points or (host_points>21 and player_points>21):
            print("Tie!")

        elif player_points > host_points:
            if player_points > 21:
                print("You Lost!")
            else:
                print("You Won!")

        else:
            print("You win!")

    return point


while True:
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    deck = 4 * cards
    host = []
    player_cards = []
    omg = [host, player_cards]
    points = 0
    point = run()
    points += point
    print("your score:",str(point))
    x = input("continue?(enter x to exit)\n")
    if x == 'x':
        break
