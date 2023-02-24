import random

R_EATING = "I don't like eating anything because I'm a bot, duh!"

capabilities = "I am a very simple chatbot that can perform any tasks that I've been programmed to do. Ask ParadymShift about programming new features!"

whoisparadym = "ParadymShift is the creator of this bot and an online vegan content creator. You can find his work at https://linktr.ee/paradymshiftmusic/"

contactparadym = "You can get ahold of ParadymShift on Discord. Eir Discord handle is ParadymShiftVegan#3608"

botbirth = "I was born on Thursday, February 23, 2023, at 3:53:01 PM."

paradymage = "I do not know how old ParadymShift is. I do know that at the time of my creation, ey was 29 years old."

def unknown():
  response = ['Could you please re-phrase that?',
              "... Ummm",
              "What does that mean?"][random.randrange(3)]
  return response
