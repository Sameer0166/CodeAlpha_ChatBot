import random
import datetime
def greet_user():
    greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!", "What's up?"]
    return random.choice(greetings)
def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("It's %I:%M %p on %A, %B %d, %Y.")
def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
        "Why was the computer cold? It left its Windows open!"
    ]
    return random.choice(jokes)
def get_weather():
    # Static response to simulate a weather reply
    return "The weather today is sunny with a light breeze. Perfect day to code!"
def chatbot_response(user_input, turn_count):
    user_input = user_input.lower().strip()
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return greet_user()
    elif "time" in user_input:
        return get_current_time()
    elif "joke" in user_input:
        return tell_joke()
    elif "weather" in user_input:
        return get_weather()
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! It was nice chatting with you."
    else:
        if turn_count % 3 == 0:
            # Every third unrecognized input, give a helpful tip
            return ("Sorry, I didn't get that. You can say things like 'tell me a joke', "
                    "'what's the time', or 'what's the weather'.")
        else:
            return "Hmm... can you please rephrase that?"
def run_chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. You can say 'hello', ask for 'time', "
          "'tell me a joke', 'weather', or 'bye' to exit.") 
    turn_count = 0
    while True:
        user_message = input("You: ")
        turn_count += 1      
        reply = chatbot_response(user_message, turn_count)
        print("Chatbot:", reply) 
        if user_message.lower().strip() in ["bye", "exit", "quit"]:
            break
if __name__ == "__main__":
    run_chatbot()
