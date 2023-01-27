import random


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return "tie"
    if user == 'r' and computer == 'p':
        return "computer wins!"
    else:
        return "user wins!"
    if user == 'p' and computer == 'r':
        return "user wins!"
    else:
        return "computer wins!"
    if user == 's' and computer == 'r':
        return "computer wins!"
    else:
        return "user wins!"

def main():
    print(play())

if __name__ == "__main__":
    main()