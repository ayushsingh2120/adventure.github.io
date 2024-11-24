def start_game():
    print("Welcome to 'The Zodiac Files'!")
    print("You are a journalist investigating the case of a mysterious serial killer.")
    print("Your decisions will determine if you uncover the truth or become the next victim.")
    print()

    first_choice()

def first_choice():
    print("You receive a cryptic letter with a strange cipher from someone claiming to be the killer.")
    print("Do you:")
    print("1. Publish the letter in the newspaper, hoping someone deciphers it.")
    print("2. Keep the letter confidential and analyze it yourself.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        public_reaction()
    elif choice == "2":
        analyze_cipher()
    else:
        print("Invalid choice. Try again.")
        first_choice()

def public_reaction():
    print("\nThe letter is published, causing public panic.")
    print("A reader deciphers part of the code, leading to a potential location.")
    print("Do you:")
    print("1. Visit the location immediately.")
    print("2. Inform the police and wait for backup.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        lone_investigation()
    elif choice == "2":
        police_backup()
    else:
        print("Invalid choice. Try again.")
        public_reaction()

def analyze_cipher():
    print("\nYou spend hours analyzing the cipher and uncover a chilling message.")
    print("'I will strike again at midnight.'")
    print("Do you:")
    print("1. Notify the police immediately.")
    print("2. Go to the scene you believe the killer is referencing.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        police_involvement()
    elif choice == "2":
        midnight_encounter()
    else:
        print("Invalid choice. Try again.")
        analyze_cipher()

def lone_investigation():
    print("\nYou arrive at the location alone and find an abandoned cabin.")
    print("Inside, you discover disturbing drawings and another cipher.")
    print("Suddenly, you hear footsteps behind you.")
    print("Do you:")
    print("1. Hide and observe.")
    print("2. Confront whoever is there.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("You hide and see a figure entering the cabin. It's the killer!")
        print("You sneak out and report to the police, leading to his capture.")
        print("Congratulations! You solved the case!")
    elif choice == "2":
        print("You confront the figure, but it's the killer! You're overpowered.")
        print("Game Over! The killer escapes, and you're never seen again.")
    else:
        print("Invalid choice. Try again.")
        lone_investigation()

def police_backup():
    print("\nThe police arrive at the location and investigate.")
    print("They find no evidence, and the killer mocks you in another letter.")
    print("You feel defeated. The case remains unsolved.")
    print("Game Over!")

def police_involvement():
    print("\nThe police use your findings to set up a trap at midnight.")
    print("The killer is spotted but escapes into the night.")
    print("The case remains open, but you've gained valuable clues.")
    print("To be continued...")

def midnight_encounter():
    print("\nYou go to the scene alone and find yourself in a deserted park.")
    print("A shadowy figure approaches. It's the killer!")
    print("Do you:")
    print("1. Try to talk to him.")
    print("2. Run away and call for help.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("The killer mocks you and vanishes into the shadows.")
        print("You're left with more questions than answers. The case remains unsolved.")
        print("Game Over!")
    elif choice == "2":
        print("You escape and inform the police. They investigate and find evidence.")
        print("Your bravery leads to a breakthrough in the case!")
        print("Congratulations! You made progress!")
    else:
        print("Invalid choice. Try again.")
        midnight_encounter()

# Start the game
start_game()
