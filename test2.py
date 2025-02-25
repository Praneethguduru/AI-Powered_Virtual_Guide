import json

def load_data():
    with open("test.json", "r") as file:
        return json.load(file)["tourist_spots"]

def get_location_info(locations, place):
    for loc in locations:
        if place.lower() in loc["name"].lower():
            return (f"Name: {loc['name']}\n"
                    f"Phone: {loc['phone']}\n"
                    f"Description: {loc['description']}\n"
                    f"Visiting Hours: {loc['visiting_hours']}")
    return None

def chatbot():
    locations = load_data()
    print("Welcome to Hyderabad Tourist Bot! Type 'exit' to end the chat.")
    
    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
    farewells = ["bye", "goodbye", "see you", "take care", "exit", "get lost"]
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in greetings:
            print("Bot: Hello! How can I assist you today?")
            continue
        
        if user_input in farewells:
            print("Bot: Goodbye! Have a great day.")
            break
        
        response = get_location_info(locations, user_input)
        if response:
            print(f"Bot: {response}")
        else:
            print("Bot: I can only provide information about Hyderabad tourist spots. Please ask about a location.")

if __name__ == "__main__":
    chatbot()
