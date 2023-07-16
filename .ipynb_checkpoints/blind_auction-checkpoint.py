bidding_info = {}


def declare_highest_bidder(bidding_log):
    # global result
    highest_bid = 0
    for new_bidder in bidding_log:
        bid = bidding_log[new_bidder]
        if bid > highest_bid:
            highest_bid = bid
            result = f'{new_bidder} is the winner of the auction with a bid of ${bid}'
    print(result)


not_end_of_bid = True
while not_end_of_bid:
    name = input("Enter your name: ").capitalize()
    bid_amt = int(input("Enter your bid: $"))
    bidding_info[name] = bid_amt
    anymore_bidders = input("Are there any more bidders? yes or no: ").lower()

    if anymore_bidders == 'no':
        not_end_of_bid = False
        declare_highest_bidder(bidding_info)
    else:
        print("You gave a wrong input. Try again with the right input.")
