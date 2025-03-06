import random

def quiz_game():
    questions = [
        {"question": "What is the capital of France?", "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"], "answer": "B"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"], "answer": "B"},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["A) J.K. Rowling", "B) Mark Twain", "C) Harper Lee", "D) Charles Dickens"], "answer": "C"},
        {"question": "What is the square root of 64?", "options": ["A) 6", "B) 7", "C) 8", "D) 9"], "answer": "C"},
        {"question": "Which gas do plants use for photosynthesis?", "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"], "answer": "B"}
    ]
    
    score = 0
    random.shuffle(questions)  # Shuffle questions for randomness
    
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
    
    print(f"\nGame Over! Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    quiz_game()
    break