import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian Quiz Game")

# set screen
screen.setup(width=925, height=700)

# To add new shape in the turtle
image = "Indian-map.gif"
screen.addshape(image)
turtle.shape(image)


# # To get the coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("Indian-States-UT.csv")
all_states_ut = data.state.to_list()

guessed_states_ut = []
while len(guessed_states_ut) < 37:
    answer_state_ut = screen.textinput(title=f"{len(guessed_states_ut)}/36 States and UT Correct",
                                       prompt="What's another state's or UT's name?").title()
    if answer_state_ut == "Exit":
        missing_states = []
        for states in all_states_ut:
            if states not in guessed_states_ut:
                missing_states.append(states)
        # states to learn.csv
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_and_ut_to_learn.csv")
        break

    if answer_state_ut in all_states_ut:
        guessed_states_ut.append(answer_state_ut)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state_ut]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state_ut)

