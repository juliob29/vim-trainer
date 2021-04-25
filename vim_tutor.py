"""
Vim Trainer gives you a random vim command, and asks you to input the correct 
key! 

TODO: The function asks if you want to continue after each iteration. Fix. 
"""
import keyboard 
import os
import random 

filename = "vim_commands.txt"

def read_commands(filename):
  """
  Reads all the vim commands from a file, and create the table structure for it. 
  """
  table = {}
  with open(filename) as f: 
    for line in f:
        line = line.strip().split(":")
        command = line[0]
        key = line[1]
        table[command] = key
        
  return table; 

def ask_question(command, key):
    answer = input(f"What is the key for the following command?: {command} \n")
    if answer != key: 
      print(f"Oops, that isn't quite right. The answer is: {key}")
      return False

    print("Great job! Correct!")
    return True

def get_yes_or_no(msg):
    yes = {'yes', 'y'}
    no = {'no', 'n'}

    while True: 
        response = input(msg).lower()
        if response in yes:
          return True
        if response in no:
          return False
        print("y/n or yes/no")
      

def main():
    table = read_commands(filename)
    commands = list(table.items())
    welcome_msg = """
    Welcome to Vim-Trainer! This is a quick way to practice your vim commands. 
    The program will show you the name of a command, and you have to input 
    the vim key that will execute the given command. 
    """
    print(welcome_msg)
    
    input("Press any key to begin!");
    
    num_correct = 0

    while True: 
      command, key = random.choice(commands)
      result = ask_question(command, key)
      if result:
        num_correct += 1
      if not get_yes_or_no("Would you like to continue? (y/n) "):
        break 
      

if __name__ == "__main__":
  main()