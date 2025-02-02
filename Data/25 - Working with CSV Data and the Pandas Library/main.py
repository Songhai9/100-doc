import turtle
import pandas

score = 0
guessed_states = []
to_learn_states = []

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
jim = turtle.Turtle()
jim.penup()
jim.hideturtle()
jim.speed("fastest")

title = "Guess a State"

turtle.shape(img)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()


game_is_on = True
while game_is_on:
    answer_state = screen.textinput(
        title=title, prompt="What's another State's name ? "
    ).capitalize()
    if (answer_state in states) and (answer_state not in guessed_states):
        score += 1
        title = f"{score}/50 Correct Answer"
        coords = (
            data[data.state == answer_state].x.item(),
            data[data.state == answer_state].y.item(),
        )
        jim.goto(coords)
        jim.write(answer_state)
        guessed_states.append(answer_state)
    elif answer_state == "Exit":
        game_is_on = False
        to_learn_states = [
            state for state in data.state.to_list() if (state not in guessed_states)
        ]
    elif answer_state in guessed_states:
        title = f"{score}/50 Already guessed"
    else:
        title = f"{score}/50 Wrong Answer"


print(to_learn_states)
to_learn_data = pandas.DataFrame(to_learn_states)
to_learn_data.to_csv("states_to_learn.csv")
