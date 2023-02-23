import random

R_EATING = "I don't like eating anything because I'm a bot, duh!"

def unknown():
  response = ['Could you please re-phrase that?',
              "... Ummm",
              "What does that mean?"][random.randrange(4)]
  return response
