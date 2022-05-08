from starting_game import *
if __name__ == "__main__":
   def option():
      print("You have 2 options. Start/End")
      player_choice=input(str("Input your choice\n"))
      if player_choice=="Start":
         start_game()
      elif player_choice=="Exit":
         exit()
      else:
         raise ValueError("This is not a valid option")
   option()
   play_again = str(input())
   if play_again == "Yes":
      option()
   else:
      exit()