from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Word list
word_list = ["python", "programming", "developer", "scramble", "function", "variable", "algorithm", "debug"]

def scramble_word(word):
    """Scrambles the letters of a word."""
    word_letters = list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)

# Global score variable
score = 0

@app.route("/", methods=["GET", "POST"])
def home():
    global score

    if request.method == "POST":
        original_word = request.form["original_word"]
        user_guess = request.form["user_guess"].strip().lower()

        if user_guess == original_word:
            result = "Correct! Great job."
            score += 1
        else:
            result = f"Incorrect. The correct word was '{original_word}'."

        # Generate a new scrambled word
        original_word = random.choice(word_list)
        scrambled_word = scramble_word(original_word)

        return render_template("index.html", result=result, scrambled_word=scrambled_word, original_word=original_word, score=score)

    # Initial load of the page
    original_word = random.choice(word_list)
    scrambled_word = scramble_word(original_word)
    return render_template("index.html", scrambled_word=scrambled_word, original_word=original_word, score=score)

if __name__ == "__main__":
    app.run(debug=True)
