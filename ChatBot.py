import json
import re
import random_responses

def load_json(file):
   try: 
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)
   except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return [] 
response_data = load_json("bot.json")

# def message_probability(user_message,recognised_words,single_response=False, required_words=[]):
#     message_certainty = 0
#     has_required_words = True
    
#     # counts how many word in predefined message
#     for word in user_message:
#         if word in recognised_words:
#             message_certainty +=1
    
#     # calculates percent of recognised words in a user message
#     percentage = float(message_certainty)/float(len(recognised_words))
    
#     for word in required_words:
#         if word not in user_message:
#             has_required_words = False
#             break
#     if has_required_words or single_response:
#         return int(percentage*100)
#     else:
#         return 0
    
# def check_all_messages(message):
#     highest_prob_list = {}

#     # simplifies response crestion
#     def response(bot_response,list_of_words, single_response=False, required_words=[]):
#          nonlocal highest_prob_list
#          highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    
#     #responses------------------------------------------------------------------------ 
#     response('Hello!',['hello','hi','sup', 'hey', 'heyo'], single_response=True)
#     response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'] )
#     response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
#     response('thank you!', ['i', 'love', 'code', 'palace'], required_words=['code','palace'])

#     # Longer responses
#     response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
#     response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

#     best_match = max(highest_prob_list, key=highest_prob_list.get)
#     #print(highest_prob_list)

#     return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# # used to get the response
# def get_response(user_input):
#     split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
#     response = check_all_messages(split_message)
#     return response

def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []
    
    # check all responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score +=1

        if required_score == len(required_words):
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1

        score_list.append(response_score)

    best_response = max(score_list)
    response_index = score_list.index(best_response)

    if input_string == "":
        return "please type something so we can chat :)"

    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return random_responses.random_string()              

while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))

