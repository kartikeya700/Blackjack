import random as r

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def display_scores(player_num, hand_num, player_cards, player_score):
    """Function to display scores of the players"""
    print(f"Player {player_num} - Hand {hand_num}")
    print(f"Your cards: {player_cards}, Current score: {player_score}")

def deal_card(user_cards, no_of_cards):
    """Deals card and adds it to the players card list"""
    for i in range(no_of_cards):
        user_cards.append(r.choice(cards))
        # deal with aces while drawing cards
        user_cards = ace_check(user_cards)
    return user_cards

def calculate_score(card_list):
    """Calculates score of the player and checks for blackjack"""
    score = sum(card_list)
    # if first two cards' sum is 21 then score is 0 as its a blackjack
    if len(card_list) == 2 and score == 21:
        return 0
    return score

def compare(user_score, dealer_score, dealer_cards):
    """Function to compare dealer and player score"""
    # player loses if he goes bust
    if user_score > 21:
        print(f"Dealer's final hand: {dealer_cards[0]}, Final score: {dealer_score}")
        print("You went over. You lose 😭")
        return 0
    # player wins in case he has a blackjack and dealer doesn't
    elif user_score == 0:
        if user_score == dealer_score:
            greeting = "Draw 🙃"
        else:
            greeting = "Win with a Blackjack 😎"
    else:
        if dealer_score == 0:
            greeting = "Dealer has a Blackjack. You lose 😭"
        elif dealer_score == user_score:
            greeting = "Draw 🙃"
        elif dealer_score > 21:
            greeting = "Dealer went over. You win 😁"        
        elif dealer_score < user_score:
            greeting = "You win 😃"
        else:
            greeting = "You lose 😤"
    print(f"Dealer's final hand: {dealer_cards}, Final score: {dealer_score}")
    print(greeting)

def strip_cards(user_card):
    """To separate a pair and treat them as two different hands"""
    temp1 = [user_card[0]]
    temp2 = [user_card[1]]
    # draw another card for both hands and complete the two hands
    temp1 = deal_card(temp1, 1)
    temp2 = deal_card(temp2, 1)
    return [temp1, temp2]

def ace_check(card_list):
    """Function to check if ace should be treated as 11 or 1"""
    while sum(card_list) > 21 and 11 in card_list:
        index = card_list.index(11)
        card_list[index] = 1
    return card_list

def dealer_logic(dealer_cards):
    """Function to replace 11 by 1 in case of soft 17 (Ace + 6)"""
    if sum(dealer_cards) == 17 and 11 in dealer_cards and 6 in dealer_cards:
        index = dealer_cards.index(11)
        dealer_cards[index] = 1
    return dealer_cards

