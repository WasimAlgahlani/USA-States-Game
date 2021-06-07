import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.hideturtle()
t.penup()

states = pandas.read_csv("50_states.csv")
correct_answers = []

while len(correct_answers) < 50:
    answer = screen.textinput(title=f"{len(correct_answers)}/50 states correct",
                              prompt="Enter the name of a state: ").title()
    if answer == "Exit":
        break
    for i in range(len(states["state"])):
        if answer == states["state"][i] and answer not in correct_answers:
            x_cord = float(states["x"][i])
            y_cord = float(states["y"][i])
            t.goto(x_cord, y_cord)
            t.write(states["state"][i])
            correct_answers.append(answer)

missed_states = []
for i in range(len(states["state"])):
    if states["state"][i] not in correct_answers:
        missed_states.append([states["state"][i]])

missed_states_file = pandas.DataFrame(missed_states)
missed_states_file.to_csv("missed_states.csv")
