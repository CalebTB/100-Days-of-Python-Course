def auction_bidder(auction_dict):
    highest_bid = 0
    winner = ""

    for bidder in auction_dict:
        bid_amount = auction_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of {highest_bid}.")


def auction_adder_editor(auction_dict, name, bidder):
    auction_dict.update({name: bidder})
    return auction_dict


def main():
    isFinished = False
    auction_dict = {}

    while not isFinished:
        answer = ""
        name = str(input("What is your name? "))
        bid_number = int(input("How much would you like to bid? "))
        auction_adder_editor(auction_dict, name, bid_number)
        while answer not in ['y', 'n']:
            answer = str(input("Would another user like to bid? 'y' or 'n' ")).lower()

        if answer == 'n':
            isFinished = True
            auction_bidder(auction_dict)
        else:
            pass


if __name__ == '__main__':
    print("Welcome to Secret Auction!")
    main()
