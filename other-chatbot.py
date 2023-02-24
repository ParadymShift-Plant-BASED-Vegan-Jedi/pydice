import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True
    
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    
    percentage = float(message_certainty) / float(len(recognised_words))
    
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
     
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0
    
def check_all_messages(message):
    highest_prob_list = {}
    
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
        
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response("I'm doing fine, and you?", ['how', 'are' 'you', 'doing'], required_words=['how', 'you'])
    response("You're so welcome! Happy to help.", ['thank you', 'i', 'love', 'chatbot'], required_words=['thank you'])
    
    response("That's so good to hear!", ["i'm", "fine", "good", "well"], required_words=["i'm"])
    response("You can call me Chatbot.", ['what', 'your', 'name', 'who', 'are', 'you'])
    
    response(long.capabilities, ['what', 'can', 'you', 'do'], required_words=["what", 'you', 'do'])       
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.whoisparadym, ['who', 'is', "who's", 'paradymshift'], required_words=['who', 'paradymshift'])
    response(long.contactparadym, ['how', 'contact', 'paradym', 'ahold'], required_words=['paradymshift', 'contact'])
    response(long.botbirth, ['how', 'old', 'are', 'you', 'when', 'born', 'age'], required_words=['old', 'you'])
    response(long.paradymage, ['how', 'old', 'paradym', 'what', 'age'], required_words=['paradymshift', 'old'])
             
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)
             
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

while True:
    print('Chatbot: ' + get_response(input('Your input: ')))
