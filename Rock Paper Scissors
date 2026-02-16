import random
import matplotlib.pyplot as plt
dash = '------------------------------------------------------------------------------'

start = input('Choose: rock (R), paper (P) or scissors (S): ')

if start == 'R':
    start = 'Rock'
if start == 'P':
    start = 'Paper'
if start == 'S':
    start = 'Scissors'

dict = {'Rock': 0, 'Paper': 1, 'Scissors': 2}

choice = ['Rock','Paper','Scissors']
pc_choice = random.choice(choice)
print(f'You chose {start}!')
print(f'Enemy chose {pc_choice}!')

# if choice = rock, pc_choice = paper, => loss | if choice = scissors, pc_choice = paper, => win
determinant = dict[start] - dict[pc_choice]

def rps(start, pc_choice, determinant):
    if determinant == 0:
        return 'Draw'
    elif determinant == 1 or determinant == -2: # Need to compare the determinant AGAIN!
        return 'Win!'
    elif determinant == -1 or determinant == 2:
        return 'Loss!'


func = rps(start, pc_choice, determinant)
print(func)

# Simulation

count_win = 0
count_loss = 0
count_draw = 0

n = int(input('How many simulations to run?: '))

print(dash)
print('Random Choice:')

for i in range(n):
    start = random.choice(choice)
    pc_choice = random.choice(choice)
    determinant = dict[start] - dict[pc_choice]
    sim = rps(start, pc_choice, determinant)

    if sim == 'Win!':
        count_win += 1
    if sim == 'Loss!':
        count_loss += 1
    if sim == 'Draw':
        count_draw += 1

win_rate = round(count_win / (count_win + count_loss + count_draw) * 100, 1)

print(f'You got {count_win} wins, {count_loss} losses and {count_draw} draws.')
print(f'Win rate = {win_rate:.1f}%')

print(dash)

types = ['Rock', 'Paper', 'Scissors', 'Random']

rock_win = []
paper_win = []
scissors_win = []
random_win = [win_rate]
rand_win = []
wins = [rock_win, paper_win, scissors_win, random_win]

def single_sim(chosen, chosen_list):
    print(chosen + ' Only:')
    count_win = 0
    count_loss = 0
    count_draw = 0

    r_weight = 1
    p_weight = 1
    s_weight = 1

    for i in range(n):
        start = chosen
        pc_choice = random.choices(choice, weights = [r_weight, p_weight, s_weight])
        determinant = dict[start] - dict[pc_choice[0]] # random.choices makes a list, not element, need to index to get element
        sim = rps(start, pc_choice, determinant)

        if sim == 'Win!':
            count_win += 1
        if sim == 'Loss!':
            count_loss += 1
        if sim == 'Draw':
            count_draw += 1

        if chosen == 'Rock':
            p_weight += 1
        if chosen == 'Paper':
            s_weight += 1
        if chosen == 'Scissors':
            r_weight += 1

    print(f'{chosen} weight: ', )

    win_rate = round(count_win / (count_win + count_loss + count_draw) * 100, 1)

    print(f'You got {count_win} wins, {count_loss} losses and {count_draw} draws.')
    print(f'Win rate = {win_rate:.1f}%')
    print(dash)
    return chosen_list.append(win_rate)
    return r_weight + count_s, p_weight + count_r, s_weight + count_p


# -----------------------------------------------------------------------------------------------

rock = single_sim('Rock', rock_win)
paper = single_sim('Paper', paper_win)
scissors = single_sim('Scissors', scissors_win)

results = [rock_win[0], paper_win[0], scissors_win[0], random_win[0]]

for i in range(len(types)):
    plt.text(i, max(results) + 5, results[i], ha = 'center', size = 16)


plt.bar(types, results, color = 'C4', width = 0.8)
plt.ylabel('Win rate (%)')
plt.ylim(0, max(results) + 10)
plt.title(f'No. of Simulations = {n}')

plt.show()

# Prediction based model using index values of rps.

# -------------------------------------------------------------------------------------------------------------------------------

def random_sim(chosen_list):
    print('Random only:')
    count_win = 0
    count_loss = 0
    count_draw = 0

    r_weight = 1
    p_weight = 1
    s_weight = 1

    for i in range(n):
        start = random.choice(choice)
        pc_choice = random.choices(choice, weights = [r_weight, p_weight, s_weight])
        determinant = dict[start] - dict[pc_choice[0]] # random.choices makes a list, not element, need to index to get element
        sim = rps(start, pc_choice, determinant)

        if sim == 'Win!':
            count_win += 1
        if sim == 'Loss!':
            count_loss += 1
        if sim == 'Draw':
            count_draw += 1

        if start == 'Rock':
            p_weight += 1
        if start == 'Paper':
            s_weight += 1
        if start == 'Scissors':
            r_weight += 1

    print('Rock, paper and scissor weight: ', r_weight, p_weight, s_weight)

    win_rate = round(count_win / (count_win + count_loss + count_draw) * 100, 1)

    print(f'You got {count_win} wins, {count_loss} losses and {count_draw} draws.')
    print(f'Win rate = {win_rate:.1f}%')
    print(dash)
    return chosen_list.append(win_rate)
    return r_weight + count_r, p_weight + count_p, s_weight + count_s

random_sim = random_sim(rand_win)

# -----------------------------------------------------------------------------------------


def play_game():
    count_win = 0
    count_loss = 0
    count_draw = 0

    r_weight = 1
    p_weight = 1
    s_weight = 1
    while True:
        start = input('Choose rock (R), paper (P) or scissors (S): ')
        if start == 'R':
            start = 'Rock'
        if start == 'P':
            start = 'Paper'
        if start == 'S':
            start = 'Scissors'

        pc_choice = random.choices(choice, weights=[r_weight, p_weight, s_weight])
        determinant = dict[start] - dict[pc_choice[0]]  # random.choices makes a list, not element, need to index to get element

        if start == 'Rock':
            p_weight += 1
        if start == 'Paper':
            s_weight += 1
        if start == 'Scissors':
            r_weight += 1

        #print('Your choice: ', start, 'PC choice: ', pc_choice)

        if determinant == 0:
            print('Draw')
            count_draw += 1
        elif determinant == 1 or determinant == -2:
            print('Win!')
            count_win += 1
        elif determinant == -1 or determinant == 2:
            print('Loss!')
            count_loss += 1
        #print(r_weight, s_weight, p_weight)
        print(dash)
        print('Wins:',count_win, 'Losses:',count_loss)
        print('% Winrate w/draws:',round(count_win / (count_win + count_loss + count_draw) * 100, 1),'%')
        print('% Winrate w/out draws:',round(count_win / (count_win + count_loss) * 100, 1),'%')

play = play_game()



