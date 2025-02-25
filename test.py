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
    return "Sorry, I couldn't find information on that place."

def chatbot():
    locations = load_data()
    print("Welcome to Hyderabad Tourist Bot! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! Have a great day.")
            break
        response = get_location_info(locations, user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot()
