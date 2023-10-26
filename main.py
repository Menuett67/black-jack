def blackjack():
  import random
  from art import logo
  import os
  def clear():
    os.system('clear')
  ask_continue=input("do you want to play a game of Blackjack? Type 'y' or 'no':")
  if ask_continue=="y":
    clear()
    print(logo)
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]  
  user_cards=[]
  computer_cards=[]
  user_score=0
  computer_score=0
  def deal_card():
   random_card=random.choice(cards)
   return random_card
  def calculate_score(deck_of_cards):
    score=0
    for i in range(len(deck_of_cards)):
      temp=deck_of_cards[i]
      score=score+temp
    if deck_of_cards[0]==11 and deck_of_cards[1]==10 or deck_of_cards[0]==10 and deck_of_cards[1]==11:
       score=0
    j=11  
    f=1
    if score>21:
      if j in deck_of_cards:
        deck_of_cards.remove(j)
        deck_of_cards.append(f)
        score=sum(deck_of_cards)
    return score 
  for i in range(0,2):
    user_cards.append(deal_card())
  for i in range(0,2):
    computer_cards.append(deal_card())
  user_score=calculate_score(deck_of_cards=user_cards)  
  computer_score=calculate_score(deck_of_cards=computer_cards)
  print(f"your cards:{user_cards},current score:{user_score}")
  print(f"computer's first card:{computer_cards[0]}")
  if computer_score==0:
   print(f"your final hand:{user_cards},final score:{user_score}")
   print(f"computer's final hand:{computer_cards},final_score:{computer_score}") 
   print("lose, opponent has blackjack.")
   blackjack()
  if user_score==0:
    computer_cards.append(deal_card())
    print(f"your final hand:{user_cards},final score:{user_score}")
    print(f"computer's final hand:{computer_cards},final_score:{computer_score}") 
    print("win with a blackjack.")
    blackjack()
  should_continue=True
  while should_continue:
    ask_another_card=input("type'y' to get another card, type'n' to pass:")
    if ask_another_card=="y":
      user_cards.append(deal_card())
      user_score=calculate_score(deck_of_cards=user_cards)
      print(f"your cards:{user_cards},current score:{user_score}")
      print(f"computer's first card:{computer_cards[0]}")
      if user_score>21:
        print(f"your cards:{user_cards},current score:{user_score}")
        print(f"computer's final card:{computer_cards},final score:{computer_score}")
        print("you lose.")
        blackjack()
      if computer_score>21:
        print(f"your cards:{user_cards},current score:{user_score}")
        print(f"computer's final card:{computer_cards},final score:{computer_score}")
        print("you win.")
        blackjack()
    elif ask_another_card=="n":
      computer_cards.append(deal_card())
      computer_score=calculate_score(deck_of_cards=computer_cards)
      if computer_score<16:
        computer_cards.append(deal_card())
        computer_score=calculate_score(deck_of_cards=computer_cards)
      print(f"your cards:{user_cards},your final score:{user_score}")
      print(f"computer's final card:{computer_cards}, final score:{computer_score}")
      if user_score>21:
        print("you lose.")
        blackjack()
      elif computer_score>21:
        print("you win.")
        blackjack()
      elif user_score>computer_score:
         print("you win.")
         blackjack()
      elif user_score<computer_score:
         print("you lose.")
         blackjack()
      should_continue=False
      blackjack()
blackjack()
