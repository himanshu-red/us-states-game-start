import pandas
import turtle

from State_locator import States_on_map

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_turtle = States_on_map()

data = pandas.read_csv("50_states.csv")
state_data = data["state"]  # state_data is in series format
state_list = state_data.to_list()  # state_list is in array format

game_on = True
state_list_guessed = []
score = 0
print_string = "Guess the States"
total_states = len(state_list)

while len(state_list_guessed) < 50 and game_on:
    answer_state = screen.textinput(title=print_string, prompt="What's another state's name: ").title()

    if answer_state == "Exit":
        # states = []
        # for state in state_list :
        #     if state not in state_list_guessed:
        #         states.append(state)
        states = [state for state in state_list if state not in state_list_guessed]
        missed_states = {"Missed States": states}
        pandas.DataFrame(missed_states).to_csv("Missed_States.csv")
        break

    elif answer_state in state_list and answer_state not in state_list_guessed:
        row_data = data[data.state == answer_state]
        x_cor = int(row_data.x)
        y_cor = int(row_data.y)
        state_turtle.point_on_map(answer_state, x_cor, y_cor)
        state_list_guessed.append(answer_state)
        score += 1
        print_string = f"{score}/{total_states}"

        # df.to_csv("Missed_States.csv")

screen.exitonclick()
