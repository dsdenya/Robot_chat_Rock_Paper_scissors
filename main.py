import random
from rps import rps

print("Bot: Hello! What is your name?")
user_name = input()

print(f"BOT: Nice to meet you {user_name}")

print ("BOT:Ask a question! \n Examples: \n - Whats the weather \n - Play a game\n - are you a robot?")
WEATHER = "rainy"
RESPONSES = {
  "Whats the weather?":[
    f"The weather is {WEATHER}",
    f"It's {WEATHER} out",
    f"Let me check, it looks {WEATHER}"
  ],

  "Are you a robot?" : [
    "What do you think?",
    "Maybe yes, maybe no?",
    "Yes a robot with human feelings"
  ],

  "exit": "Bye see you later",

  "default": "Sorry I don't understand. "
}

#Functions

def respond(message):
    if message in RESPONSES:
      bot_message = random.choice( RESPONSES[message])
    else:
      bot_message = RESPONSES ["default"]
    return bot_message

def related(message):
    if "weather" in message:
      y_text = "Whats the weather?"
    elif "robot" in message:
      y_text = "Are you a robot?"
    elif "exit" in message: 
      y_text = "exit"
    elif "game" in message:
      rps()
    else:
      y_text = ""
    return y_text

def send_message(message):
    print(f"USER: {message}")
    response = respond(message)
    print(f"BOT: {response}")

# hi shoya this is Bibi- your code works now! thank you for joining us! and hope to see you again in the future! you could delete this comment haha, just didn't know how to reach you XD

while True: 
    my_input = input()

    related_text = related (my_input)
    send_message(related_text)

    if my_input == "exit":
      exit()