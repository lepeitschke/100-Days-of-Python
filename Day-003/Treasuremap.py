print("""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           |'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'|U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-/U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||
""")
print("Welcome to Treasure Island! Your mission is to find the Treasure.")

direction = input("left or right? ").lower()




if direction == "left":
  travel = input("You've made the right decision. You may proceed and decide how you want to travel next or if you would lke to waitt. Swim or wait? ").lower()
  
  if travel == "swim":
    door = input("You swam across an ocean and appear at some doors. Which one to take? Blue, Red, Yellow, Green, Black or White? ")

    if door == "Yellow" or door == "yellow":
      print("You win!")
    elif door == "Blue" or door == "blue":
      print("You're eaten by beasts.\nGame over.")
    elif door == "Red" or door == "red":
      print("Burned by fire.\nGame over.")
    else:
      print("Game over.")
  else:
    print("You were attacked by trout.\nGame over.")
else: 
  print("You fell into a whole.\nGame over.")
    