import random


def game_stats(users_cards, dealers_cards, userTotal, dealerTotal):
    print("\nGame Stats:")
    print(f"User Cards: {users_cards}")
    print(f"Dealers Cards: {dealers_cards}\n")
    print(f"User Total: {userTotal}")
    print(f"Dealers Total: {dealerTotal}")


def compare_cards(user_total, dealers_total):
    if user_total < dealers_total <= 21:
        print("House Wins!")
    elif user_total > dealers_total <= 21:
        print("You Win!")
    elif user_total == dealers_total:
        print("It's a Push")
    else:
        print("You Win!")


def check_for_eleven(cards_in_hand):
    cards_total = sum(cards_in_hand)
    if 11 in cards_in_hand and cards_total > 21:
        for i in range(len(cards_in_hand)):
            if cards_in_hand[i] == 11:
                cards_in_hand[i] = 1
                break


def deal_1card(dealt_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealt_cards.append(cards[random.randint(0, len(cards) - 1)])


def deal_2cards(user_cards, dealer_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for x in range(0, 2):
        user_cards.append(cards[random.randint(0, len(cards) - 1)])  # Deals 2 cards to user
        dealer_cards.append(cards[random.randint(0, len(cards) - 1)])  # Deals 2 cards to house


def main():
    user_cards = []
    dealer_cards = []

    deal_2cards(user_cards, dealer_cards)

    check_for_eleven(user_cards)
    check_for_eleven(dealer_cards)
    user_total = sum(user_cards)
    dealers_total = sum(dealer_cards)

    print(f"Your cards: {user_cards} | Current total: {user_total}")
    print(f"Dealer's card: [{dealer_cards}]")
    while user_total <= 21:
        ask_user_choice = input("Hit (y) or stand (n)? (y/n): ").lower()
        print("")
        if ask_user_choice == 'y':
            deal_1card(user_cards)
            check_for_eleven(user_cards)
            user_total = sum(user_cards)

            print(f"Your cards: {user_cards}, current total: {user_total}")
            print(f"Dealer's card: [{dealer_cards[0]}]")
            if user_total > 21:
                game_stats(user_cards, dealer_cards, user_total, dealers_total)
                print("House Wins!")

        else:
            while dealers_total <= 21:
                if dealers_total <= 16:
                    deal_1card(dealer_cards)
                    check_for_eleven(dealer_cards)
                    dealers_total = sum(dealer_cards)
                else:
                    check_for_eleven(dealer_cards)
                    dealers_total = sum(dealer_cards)
                break

            game_stats(user_cards, dealer_cards, user_total, dealers_total)
            compare_cards(user_total, dealers_total)
            break


if __name__ == '__main__':
    print("Welcome to Blackjack!")
    user_input = input("Do you want to play a game of Blackjack? (y/n): \n").lower()

    while user_input == 'y':
        main()
        user_input = input("Do you want to play a game of Blackjack? (y/n): ").lower()
    print("\nThank you for playing!")
