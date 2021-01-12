import random

def generate_response(user_input):
  responses = [
    "How interesting! What else happened?",
    "You don't say!",
    "Very cool!",
    "My goodness...continue please!"
  ]
  return random.choice(responses)

def generate_response_1(user_input):
  responses = ["Ah ok. Here's a joke to make you feel better: Did you hear about the actor who fell through the floorboards? He was just going through a stage. Haha! Get it?","Aww. Well, hopefully this cheers you up: Why don’t scientists trust atoms? Because they make up everything. Hilarious, am I right?"]
  return random.choice(responses)

def generate_response_2(user_input):
  responses = ["Ooh, here's another good one: What did the left eye say to the right eye? Between you and me, something smells. Get it? Cause it's the nose? Haha!", "Did that help cheer you up? If not, this one will: A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”"]
  return random.choice(responses)

def init_chat():
  quit_character = 'q'
  user_input = input("Hi! How was your day?\n")
  while user_input != quit_character:

    if user_input == "good":
      user_input = input("That's great! What happened?\n")
      while user_input != quit_character:
        user_input = input(generate_response(user_input) + "\n")
    elif user_input == "decent":
      user_input = input("Oh, did anything happen?\n")     
      while user_input != quit_character:
        user_input = input(generate_response_1(user_input) + "\n")
        user_input = input(generate_response_2(user_input) + "\n")
    elif user_input == "bad":
      user_input = input("Oh my, what happened?\n")
      while user_input != quit_character:
        user_input = input(generate_response_1(user_input) + "\n")
        user_input = input(generate_response_2(user_input) + "\n")
    else:
      user_input = input("Aww, so would you say it was good, decent, or bad?")

  if user_input == quit_character:
    print("It seems both of us got to go. Goodbye!")


if __name__ == "__main__":
  init_chat()
