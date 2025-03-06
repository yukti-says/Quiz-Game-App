import random
import json
import time
import os
from datetime import datetime, timedelta

def load_questions():
    with open("questions.json", "r") as f:
        questions = json.load(f)["questions"]
    return questions

def get_random_questions(questions, num_questions):
    if num_questions > len(questions):
        num_questions = len(questions)
    return random.sample(questions, num_questions)

def ask_question(question):
    print("\n" + question["question"])
    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            number = int(input("Select the correct number: "))
            if 1 <= number <= len(question["options"]):
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Please enter a number.")
    
    return question["options"][number - 1] == question["answer"]

def save_summary(user, total_questions, correct, time_taken):
    filename = "quiz_summary.json"
    summary = {
        "user": user,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_questions": total_questions,
        "correct_answers": correct,
        "score": round((correct / total_questions) * 100, 2),
        "time_taken": round(time_taken, 2)
    }
    
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        data = []
    
    data.append(summary)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def show_weekly_report():
    filename = "quiz_summary.json"
    if not os.path.exists(filename):
        print("No quiz history found.")
        return
    
    with open(filename, "r") as f:
        data = json.load(f)
    
    week_ago = datetime.now() - timedelta(days=7)
    weekly_data = [entry for entry in data if datetime.strptime(entry["date"], "%Y-%m-%d %H:%M:%S") > week_ago]
    
    if not weekly_data:
        print("No quizzes taken in the last 7 days.")
        return
    
    best_user = max(weekly_data, key=lambda x: (x["correct_answers"], -x["time_taken"]))
    print("\nWEEKLY REPORT")
    print("User with the best performance:", best_user["user"])
    print("Score:", best_user["score"], "% in", best_user["time_taken"], "seconds")

def main():
    print("Welcome to the Quiz Game!")
    user = input("Enter your name: ")
    
    questions = load_questions()
    total_questions = int(input("Enter the number of questions: "))
    random_questions = get_random_questions(questions, total_questions)
    
    correct = 0
    start_time = time.time()
    
    for question in random_questions:
        if ask_question(question):
            correct += 1
        print("*********************************************************")
    
    completed_time = time.time() - start_time
    print("\n.............SUMMARY.............")
    print("User:", user)
    print("Total Questions:", total_questions)
    print("Correct Answers:", correct)
    print("Score:", f"{round((correct/total_questions)*100, 2)}%")
    print("Time taken:", round(completed_time, 2), "seconds")
    
    save_summary(user, total_questions, correct, completed_time)
    
    print("\nDo you want to see the weekly report?")
    if input("(yes/no): ").strip().lower() == "yes":
        show_weekly_report()

if __name__ == "__main__":
    main()
