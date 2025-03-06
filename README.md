# Quiz Game in Python

This is an interactive Python-based quiz game that randomly selects questions from a JSON file. It includes a user login system, tracks performance, and generates a weekly report of top performers.

## Features
✅ User Login System
✅ Randomized Questions
✅ Saves User Scores and Time Taken
✅ Weekly Performance Report
✅ Error Handling for Invalid Inputs

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yukti-says/Quiz-Game-App.git
   cd quiz-game-python
   ```
2. Ensure you have Python installed (3.x recommended).
3. Install required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `questions.json` file and add quiz questions in the following format:
   ```json
   {
       "questions": [
           {
               "question": "What is the capital of France?",
               "options": ["Paris", "London", "Berlin", "Madrid"],
               "answer": "Paris"
           }
       ]
   }
   ```

## Usage

Run the script using:
```bash
python main.py
```

Users will be prompted to enter their name, select the number of questions, and play the quiz. At the end, their performance will be stored, and they can view a weekly report of the best-performing user.

## Contributing
Feel free to fork the repository and submit pull requests for new features or improvements!

## License
This project is licensed under the MIT License.

## Connect with Me
🔗 [LinkedIn](https://www.linkedin.com/in/YuktiSahu)  
🔗 [GitHub](https://github.com/yukti-says)


