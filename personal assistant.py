import random
import os

def ask_questions():
    questions = [
        ("What is your name? ", "name"),
        ("How old are you? ", "age"),
        ("What is your favorite color? ", "color"),
        ("What is your favorite food? ", "food"),
        ("Which city do you live in? ", "city"),
        ("Which SHS did you attend? ", "shs"),
        ("What is your favorite soccer team? ", "team")
    ]
    random.shuffle(questions)
    answers = {}
    for prompt, key in questions:
        answer = input(prompt)
        answers[key] = answer
    return answers

def create_summary(data):
    summary = f"""
Hello, {data.get('name', 'Friend')}!
You are {data.get('age', 'unknown')} years old, love the color {data.get('color', 'some color')},
and enjoy eating {data.get('food', 'something delicious')}.
Life must be awesome in {data.get('city', 'your city')}!
It's cool you went to {data.get('shs', 'some SHS')} and support {data.get('team', 'a great soccer team')}!
"""
    return summary.strip()

def save_to_file(data, summary, rating):
    filename = f"{data['name'].capitalize()}.txt"
    with open(filename, "w") as file:
        file.write(summary + "\n")
        file.write(f"\nUser Rating: {rating} star(s)\n")
    print(f"\nSummary saved to {filename}")

def get_valid_rating():
    while True:
        try:
            rating = int(input("Please rate your assistant (1 to 5 stars): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Rating must be between 1 and 5. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

def main():
    while True:
        print("\n--- Welcome to Your Simple Personal Assistant ---\n")
        user_data = ask_questions()
        summary = create_summary(user_data)
        print("\n--- Here's Your Fun Summary ---")
        print(summary)
        save_choice = input("\nWould you like to save this summary to a file? (yes/no): ").strip().lower()
        if save_choice == 'yes':
            rating = get_valid_rating()
            save_to_file(user_data, summary, rating)
        restart = input("\nWould you like to restart the process? (yes/no): ").strip().lower()
        if restart != 'yes':
            print("\nThank you for using the personal assistant. Goodbye!")
            break

if __name__ == "__main__":
    main()