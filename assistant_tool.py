import random
import os

# Define all possible questions
questions_pool = {
    "name": "What is your name?",
    "age": "How old are you?",
    "color": "What is your favorite colour?",
    "food": "What is your favorite food?",
    "city": "Which city do you live in?",
    "shs": "Which SHS did you attend?",
    "team": "What is your favorite soccer team?",
    "hobby": "What is a hobby you enjoy?",
    "music": "What’s your favorite music genre?",
    "dream": "What’s your dream job?"
}

def get_random_questions():
    # Always ask name, and randomly choose 4 others
    keys = list(questions_pool.keys())
    keys.remove("name")
    selected = random.sample(keys, 4)
    return ["name"] + selected

def collect_user_data():
    user_data = {}
    random_questions = get_random_questions()
    for key in random_questions:
        answer = input(f"{questions_pool[key]} ").strip()
        user_data[key] = answer
    return user_data

def create_summary(data):
    name = data.get("name", "User")
    summary = f"\nHello, {name}!\n"

    if "age" in data:
        summary += f"You are {data['age']} years old, "
    if "color" in data:
        summary += f"you love the color {data['color']}, "
    if "food" in data:
        summary += f"and enjoy eating {data['food']}.\n"
    if "city" in data:
        summary += f"Life must be awesome in {data['city']}!\n"
    if "shs" in data:
        summary += f"Cool that you attended {data['shs']} SHS.\n"
    if "team" in data:
        summary += f"Go {data['team']}! That's a great team.\n"
    if "hobby" in data:
        summary += f"In your free time, you enjoy {data['hobby']}.\n"
    if "music" in data:
        summary += f"You vibe to {data['music']} music.\n"
    if "dream" in data:
        summary += f"Dream big! {data['dream']} sounds amazing.\n"
    
    return summary

def save_to_file(name, summary, rating):
    filename = f"{name}.txt"
    with open(filename, 'w') as file:
        file.write(summary)
        file.write(f"\nUser Rating: {rating} stars\n")
    print(f"\nSummary saved to '{filename}'.")

def main():
    while True:
        print("\n🎉 Welcome to Your Personal Assistant 🎉\n")
        data = collect_user_data()
        summary = create_summary(data)
        print("\n📝 Here is your fun summary:\n")
        print(summary)

        # Save option
        save = input("Would you like to save this summary to a text file? (yes/no): ").strip().lower()
        if save == 'yes':
            # Ask for a fun rating
            while True:
                try:
                    rating = int(input("Please rate this assistant (1 to 5 stars): "))
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            save_to_file(data['name'], summary, rating)

        # Restart option
        again = input("\nWould you like to start over with new questions? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\nThanks for using the assistant! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
