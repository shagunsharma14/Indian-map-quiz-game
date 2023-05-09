# Indian Quiz Game

This code snippet creates a quiz game using the Turtle graphics library and the pandas library in Python. The game displays an image of the Indian map and prompts the user to guess the names of the Indian states and union territories (UTs).

## Prerequisites

Before running the code, make sure you have the following:

- The "Indian-map.gif" image file.
- The "Indian-States-UT.csv" file containing the list of Indian states and UTs.

## Usage

1. Ensure that the "Indian-map.gif" and "Indian-States-UT.csv" files are in the same directory as your Python script.

2. Import the necessary libraries:

```python
import turtle
import pandas
```

3. Set up the Turtle screen and configure its properties:

```python
screen = turtle.Screen()
screen.title("Indian Quiz Game")
screen.setup(width=925, height=700)
```

4. Add the Indian map image as a shape to the Turtle:

```python
image = "Indian-map.gif"
screen.addshape(image)
turtle.shape(image)
```

5. Read the state data from the "Indian-States-UT.csv" file using pandas:

```python
data = pandas.read_csv("Indian-States-UT.csv")
all_states_ut = data.state.to_list()
```

6. Play the quiz game by guessing the names of the states and UTs:

```python
guessed_states_ut = []
while len(guessed_states_ut) < 37:
    answer_state_ut = screen.textinput(title=f"{len(guessed_states_ut)}/36 States and UT Correct",
                                       prompt="What's another state's or UT's name?").title()
    if answer_state_ut == "Exit":
        missing_states = []
        for states in all_states_ut:
            if states not in guessed_states_ut:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_and_ut_to_learn.csv")
        break

    if answer_state_ut in all_states_ut:
        guessed_states_ut.append(answer_state_ut)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state_ut]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state_ut)
```

## Notes

- Ensure that you have the necessary dependencies installed, including Turtle and pandas.
- The code relies on the "Indian-States-UT.csv" file to load the state and UT data. Make sure the file is accurate and up-to-date.
- Customize the game as needed by modifying the prompts, screen dimensions, or any additional functionalities.
- Have fun playing and learning about the Indian states and UTs!

## License

This code is licensed under the [MIT License](LICENSE).

Feel free to modify and enhance this code according to your requirements.
