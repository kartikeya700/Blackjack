from art import logo
import random as r
import time
import functions as b

def main():
    while True:
        # Asks user if he wants to play the game
        choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if choice.lower().strip() == "y":
            print("\n" * 20)
            break
            # blackjack()
        else:
            print("You have exited the game!")
            return 0

    print(logo)
    players = int(input("Enter the number of players: "))
    player_cards = []
    player_score = []

    # gives each player an initial hand of two cards and displays their starting hand
    for i in range(players):
        hand = b.deal_card([], 2)
        print("-" * 160)
        print(f"Player {i + 1}")
        time.sleep(1)
        print(f"Your cards: {hand}, Current score: {b.calculate_score(hand)}")
        # if player recieves a pair he is given option of splitting
        if hand[0] == hand[1]:
            splitting = input("Do you want to split your cards, type 'y' or 'n': ")
            if splitting.lower().strip() == 'y':
                player_cards.append(b.strip_cards(hand))
                # displays new set of cards of player after splitting
                for j in range(2):
                    print(f"Player {i + 1} - Hand {j + 1}")
                    time.sleep(1)
                    print(f"Your cards: {player_cards[i][j]}, Current score: {b.calculate_score(player_cards[i][j])}")
            else:
                player_cards.append([hand])
        else:
            player_cards.append([hand])
        player_score.append([])
        # add player score of each hand to the score list
        for j in range(len(player_cards[i])):
            player_score[i].append(b.calculate_score(player_cards[i][j]))
        print("-" * 160)
        time.sleep(1.75)
        print("\n" * 20)

    # gives dealer his initial two cards
    dealer_cards = b.deal_card([], 2)
    dealer_score = b.calculate_score(dealer_cards)

    for i in range(players):
        for j in range(len(player_cards[i])):
            print("-" * 160)
            # ask players without blackjack if they want to draw another card
            if player_score[i][j] != 0:
                choose_card = True
                while choose_card:
                    # displays scores and cards of player after each draw
                    b.display_scores(i + 1, j + 1, player_cards[i][j], player_score[i][j])
                    print(f"Dealer's first card: {dealer_cards[0]}")
                    card_choice = input("Type 'y' to get another card and 'n' to pass. ")
                    if card_choice.lower().strip() == "y":
                        time.sleep(1)
                        player_cards[i][j] = b.deal_card(player_cards[i][j], 1)
                        player_score[i][j] = b.calculate_score(player_cards[i][j])
                        # stop the card drawing process if score crosses 21 and display final hand
                        if player_score[i][j] > 21:
                            choose_card = False
                            b.final_scores(i + 1, j + 1, player_cards[i][j], player_score[i][j])
                    elif card_choice.lower().strip() == "n":
                        choose_card = False
                    else:
                        print("Type 'y' or 'n'.")
                        continue
        print("-" * 160)
        time.sleep(1.5)
        if i != players - 1:
            print("\n" * 20)
        else:
            print("\n" * 10)    
                        
    # dealer draws cards until dealer score = 17  
    while sum(dealer_cards) < 17:
        dealer_cards = b.deal_card(dealer_cards, 1)
        # check for dealer logic
        dealer_cards = b.dealer_logic(dealer_cards)
    dealer_score = b.calculate_score(dealer_cards)

    time.sleep(0.5)

    for i in range(players):
        for j in range(len(player_cards[i])):
            # display scores of each hand of each player and give the final result
            print("-" * 160)
            b.display_scores(i + 1, j + 1, player_cards[i][j], player_score[i][j])
            time.sleep(0.5)
            b.compare(player_score[i][j], dealer_score, dealer_cards)
            time.sleep(0.5)
        print("-" * 160)
        time.sleep(0.5)
        if i != players - 1:
                print("\n" * 2)
            
if __name__ == "__main__":
    main()