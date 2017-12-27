import random

def main():
  print "Welcome to the number guessing game!"
  number = randint(1,10)
  
  while True:
    guess = raw_input("Guess a number between one and ten: ")
    if int(guess) == number:
      print "That's Right!"
      break
    else:
      print "That's not right. Sorry. Guess Again"
      
      
if __name__ == '__main__':
  main()
  

    
