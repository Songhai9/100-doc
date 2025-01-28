from flask import Flask
import random

app = Flask(__name__)

# Number to guess
num = random.randint(0, 9)


@app.route("/")
def home():
    return ('<h1>Guess a number between 0 and 9</h1> \
            <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>')


@app.route('/guess/<int:guessed>')
def print_result(guessed):
    if guessed == num:
        return (f'<h1 style="color: green">You found me! {guessed}</h1> \
                <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZW03eHVpNTE1aHFyM2dqczZ3ZWlweW1oN2dmeHcxNzlzd211M3FuNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TqN4Zy26L7wjtriu2u/giphy.gif"/>'
                )
    elif guessed > num:
        return (f'<h1 style="color: red">Too high, retry later {guessed}</h1> \
                <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjZpMWYwNjI4NGZmOWlpNHlxNnUxYnlnaGxsc3R4YXdmZmJibncxaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wdh1SvEn0E06I/giphy.gif"/>'
                )
    elif guessed < num:
        return (f'<h1 style="color: yellow">Too low, retry later {guessed}</h1> \
                <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnN1eWc1MWVoaHJqaGEzbjMxamd4cWJ5dHNlcjRqNnhvczBrZjRkOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rS2uLYRGkGWySNX69v/giphy.gif"/>')


if __name__ == '__main__':
    app.run(debug=True)
    print(num)
