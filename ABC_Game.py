import random
import tkinter as tk
import tkinter.messagebox as messagebox
import os
import re

# Name: Ali Nazari - student id: 610304180
# Global variables
grid = [[],[],[],[]]
grid_size = 4
grid_font = ('Tahoma', 28, 'bold')
game_over = False
win = False
random_flag = False
pushed = False
merged = False
simple_graphic = False
current_score = 0
best_score = 0
letter_image = ""
simple_bg_color = '#ffcd00'
graphical_bg_color = '#ffcd00'
image_dict = dict()
saved_runs = dict({"run_1": [],"run_2": []})
grid_color_dict = {
    'A': ['#ffd2d2','#705e6c'],
    'B': ['#ff9595','#ffffff'],
    'C': ['#f65e3b','#ffffff'],
    'D': ['#bf5c1a','#ffffff'],
    'E': ['#b30f0f','#ffffff'],
    'F': ['#830f0f','#ffffff'],
    'G': ['#804000','#ffffff'],
    'H': ['#edcc61','#705e6c'],
    'I': ['#eb00a0','#705e6c'],
    'J': ['#aa0777','#ffffff'],
    'K': ['#88035f','#ffffff'],
    'L': ['#690249','#ffffff'],
    'M': ['#a460dc','#ffffff'],
    'N': ['#a460dc','#ffffff'],
    'O': ['#9357c4','#ffffff'],
    'P': ['#7f4aab','#ffffff'],
    'Q': ['#6b3b82','#ffffff'],
    'R': ['#9cd6ff','#705e6c'],
    'S': ['#7fb7de','#ffffff'],
    'T': ['#5e9ecb','#ffffff'],
    'U': ['#4789b8','#ffffff'],
    'V': ['#306c97','#ffffff'],
    'W': ['#d2f6d0','#705e6c'],
    'X': ['#00d8bf','#ffffff'],
    'Y': ['#069f8e','#ffffff'],
    'Z': ['#315718','#ffffff'],
    '0': ['#feddb9','#ffffff']}

#---------------------------------------------------------------------
def main():

    def list_to_file_4dim(inp_list, path):
        with open(path, "w", encoding="utf-8") as f:
            for item in inp_list:
                f.write("{0},{1},{2},{3}\n".format(item[0], item[1], item[2], item[3]))

    # ---------------------------------------------------------------------
    def file_to_list_4dim(file_path):
        item_list = list()
        if os.path.isfile(file_path):
            with open(file_path, encoding="utf-8") as f:
                lines = f.readlines()
                lines_count = len(lines)
            k = 0
            while k < lines_count:
                item = re.split(',', lines[k])
                item_list.append([item[0], item[1], item[2], item[3].strip('\n')])
                k += 1
        return item_list

    # ---------------------------------------------------------------------
    def list_to_file(words, file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            for word in words:
                if len(word) > 0:
                    f.write(word + "\n")

    # ---------------------------------------------------------------------
    def file_to_list(file_name):
        results = list()
        if os.path.isfile(file_name):
            with open(file_name, 'rt', encoding="utf-8") as f:
                for line in f:
                    my_str = line.replace('\n', '').strip(' ')
                    if len(my_str) > 0:
                        results.append(my_str)
        return results

    # ---------------------------------------------------------------------
    def write_file(path, data):
        try:
            with open(path, 'w', encoding="utf-8") as f:
                f.write(data)
                return True
        except IOError as e:
            print(f"Couldn't open or write to file ({e})")  # py3 f-strings
            return False

    # ---------------------------------------------------------------------
    def read_file(path):
        data = ''
        if os.path.isfile(path):
            with open(path, 'rt', encoding="utf-8", errors='ignore') as f:
                data = f.read()
        return data

    # ---------------------------------------------------------------------
    def get_score(letter):
        match letter:
            case 'A':
                return 2**1
            case 'B':
                return 2**2
            case 'C':
                return 2**3
            case 'D':
                return 2**4
            case 'E':
                return 2**5
            case 'F':
                return 2**6
            case 'G':
                return 2**7
            case 'H':
                return 2**8
            case 'I':
                return 2**9
            case 'J':
                return 2**10
            case 'K':
                return 2**11
            case 'L':
                return 2**12
            case 'M':
                return 2**13
            case 'N':
                return 2**14
            case 'O':
                return 2**15
            case 'P':
                return 2**16
            case 'Q':
                return 2**17
            case 'R':
                return 2**18
            case 'S':
                return 2**19
            case 'T':
                return 2**20
            case 'U':
                return 2**21
            case 'V':
                return 2**22
            case 'W':
                return 2**23
            case 'X':
                return 2**24
            case 'Y':
                return 2**25
            case 'Z':
                return 2**26
            case _:
                return 0

    # ---------------------------------------------------------------------
    def grid_display():
        global letter_image
        for i in range(grid_size):
            for j in range(grid_size):
                cell_text = str(grid[i][j])
                bg_color = grid_color_dict.get(cell_text)[0]
                fg_color = grid_color_dict.get(cell_text)[1]
                image = image_dict.get(cell_text)
                if simple_graphic:
                    if cell_text == '0':
                        cell_text = ""
                    game_area.configure(bg="#ffffff")
                    grid_labels[i][j].configure(
                        text=cell_text,
                        anchor="center",
                        height=2,
                        width=4,
                        bd=2,
                        font=grid_font,
                        padx=2,
                        pady=2,
                        justify="center",
                        relief="ridge",
                        wraplength=250,
                        image="",
                        bg=bg_color,
                        fg=fg_color)
                else:
                    game_area.configure(bg="#ffffff")
                    grid_labels[i][j].configure(
                        text=cell_text,
                        anchor="center",
                        height=100,
                        width=100,
                        bd=0,
                        font=grid_font,
                        padx=0,
                        pady=0,
                        justify="center",
                        relief="flat",
                        wraplength=250,
                        image = image,
                        bg=bg_color,
                        fg=fg_color)

    # ---------------------------------------------------------------------
    def merge_letters(letter):
        match letter:
            case 'A':
                return "B"
            case 'B':
                return "C"
            case 'C':
                return "D"
            case 'D':
                return "E"
            case 'E':
                return "F"
            case 'F':
                return "G"
            case 'G':
                return "H"
            case 'H':
                return "I"
            case 'I':
                return "J"
            case 'J':
                return "K"
            case 'K':
                return "L"
            case 'L':
                return "M"
            case 'M':
                return "N"
            case 'N':
                return "O"
            case 'O':
                return "P"
            case 'P':
                return "Q"
            case 'Q':
                return "R"
            case 'R':
                return "S"
            case 'S':
                return "T"
            case 'T':
                return "U"
            case 'U':
                return "V"
            case 'V':
                return "W"
            case 'W':
                return "X"
            case 'X':
                return "Y"
            case 'Y':
                return "Z"
            case _:
                return 0

    # ---------------------------------------------------------------------
    def push_to(direction):
        global grid, pushed
        pushed = False
        new_grid = [['0'] * grid_size for _ in range(grid_size)]
        match direction:
            case 'left':
                for i in range(grid_size):
                    col = 0
                    for j in range(grid_size):
                        if grid[i][j] != '0':
                            new_grid[i][col] = grid[i][j]
                            if col != j:
                                pushed = True
                            col += 1
                grid = new_grid
            case 'right':
                for i in range(grid_size):
                    col = grid_size -1
                    for j in range(grid_size - 1,-1,-1):
                        if grid[i][j] != '0':
                            new_grid[i][col] = grid[i][j]
                            if col != j:
                                pushed = True
                            col -= 1
                grid = new_grid
            case 'up':
                for j in range(grid_size):
                    row = 0
                    for i in range(grid_size):
                        if grid[i][j] != '0':
                            new_grid[row][j] = grid[i][j]
                            if row != i:
                                pushed = True
                            row += 1
                grid = new_grid
            case 'down':
                for j in range(grid_size):
                    row = grid_size - 1
                    for i in range(grid_size - 1,-1,-1):
                        if grid[i][j] != '0':
                            new_grid[row][j] = grid[i][j]
                            if row != i:
                                pushed = True
                            row -= 1
                grid = new_grid

    # ---------------------------------------------------------------------
    def do_merge(direction):
        global current_score, merged
        merged = False
        match direction:
            case 'left' | 'right':
                for i in range(grid_size):
                    for j in range(grid_size - 1):
                        if grid[i][j] == grid[i][j + 1] and grid[i][j] != '0':
                            grid[i][j] = merge_letters(grid[i][j])
                            grid[i][j + 1] = '0'
                            current_score += get_score(grid[i][j])
                            merged = True
            case 'up' | 'down':
                for i in range(grid_size - 1):
                    for j in range(grid_size):
                        if grid[i][j] == grid[i+1][j] and grid[i][j] != '0':
                            grid[i][j] = merge_letters(grid[i][j])
                            grid[i+1][j] = '0'
                            current_score += get_score(grid[i][j])
                            merged = True

    # ---------------------------------------------------------------------
    def add_random_cell():
        global grid
        empty_cells = []
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] == '0':
                    empty_cells.append((i, j))
        row , col = random.choice(empty_cells)
        grid[row][col] = "A" if random.random() < 0.9 else "B"

    # ---------------------------------------------------------------------
    def is_game_over():
        # check has empty cells in grid
        has_empty = False
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] == '0':
                    has_empty = True
        # Check can do merge two cells
        can_merge = False
        for i in range(grid_size):
            for j in range(grid_size - 1):
                if grid[i][j] == grid[i][j + 1]:
                    can_merge = True
        for j in range(grid_size):
            for i in range(grid_size - 1):
                if grid[i][j] == grid[i + 1][j]:
                    can_merge = True
        return not has_empty and not can_merge

    # ---------------------------------------------------------------------
    def seen_z():
        seen = False
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] == 'Z':
                    seen = True
        return seen

    # ---------------------------------------------------------------------
    def score_display():
        top_label1.configure(text="Score: {}".format(current_score))
        top_label2.configure(text="Best: {}".format(best_score))
        print('=' * 20)
        for i in range(grid_size):
            for j in range(grid_size):
                print("{}\t".format(grid[i][j]), end='')
            print()
        print('=' * 20)
        print('Score: {}'.format(current_score))

     # ---------------------------------------------------------------------
    def save_clicked():
        list_to_file_4dim(grid, "files/save.txt")
        data = [str(current_score) , str(merged) , str(random_flag) , str(pushed)]
        list_to_file(data, "files/save_var.txt")
        messagebox.showinfo('ABC Games', 'Game is saved from File')

    # ---------------------------------------------------------------------
    def load_clicked():
        global grid, merged, random_flag, pushed, current_score
        if messagebox.askyesno('ABC Games', 'You are going to load previous saved game.\nAre you sure?'):
            grid = file_to_list_4dim("files/save.txt")
            v = file_to_list("files/save_var.txt")
            current_score = int(v[0])
            merged, random_flag, pushed = v[1], v[2], v[3]
            saved_runs["run_1"].clear()
            saved_runs["run_2"].clear()
            grid_display()
            score_display()

    # ---------------------------------------------------------------------
    def method_clicked():
        global simple_graphic
        v = variable.get()
        color_name = ""
        if v == "Simple buttons":
            simple_graphic = True
            color_name = simple_bg_color
        elif v == "Graphical buttons":
            simple_graphic = False
            color_name = graphical_bg_color

        root.configure(bg = color_name)
        main_label.configure(bg = color_name)
        result_label.configure(bg = color_name)
        rdb_labels[0].configure(bg = color_name, activebackground=color_name)
        rdb_labels[1].configure(bg = color_name, activebackground=color_name)
        grid_display()

    # ---------------------------------------------------------------------
    def undo_clicked():
        global grid, current_score, merged, random_flag, pushed, game_over, win
        if len(saved_runs["run_2"]) != 0:
            grid = saved_runs["run_2"][0]
            current_score = saved_runs["run_2"][1]
            merged = saved_runs["run_2"][2]
            pushed = saved_runs["run_2"][3]
            random_flag = saved_runs["run_2"][4]
            saved_runs["run_2"].clear()
            print("\nUndone one rounds")
        elif len(saved_runs["run_1"]) != 0:
            grid = saved_runs["run_1"][0]
            current_score = saved_runs["run_1"][1]
            merged = saved_runs["run_1"][2]
            pushed = saved_runs["run_1"][3]
            random_flag = saved_runs["run_1"][4]
            saved_runs["run_1"].clear()
            print("\nUndone one rounds")

        grid_display()
        score_display()
        game_over = False
        win = False

    # ---------------------------------------------------------------------
    def new_clicked():
        global  current_score, game_over, win, pushed, random_flag, merged
        if messagebox.askyesno('ABC Games', 'A new game is starting.\nAre you sure?'):
            game_over = False
            win = False
            current_score = 0
            pushed = False
            merged = False
            random_flag = False
            for i in range(grid_size):
                for j in range(grid_size):
                    grid[i][j] = '0'
            for _ in range(2):
                add_random_cell()
            grid_display()
            score_display()

    # ---------------------------------------------------------------------

    def key_handler(event):
        global game_over, win, random_flag, pushed, merged
        if game_over or win:
            return
        # Save two latest move
        if len(saved_runs["run_1"]) == 0:
            saved_runs["run_1"] = [grid, current_score, merged, pushed, random_flag]
        elif len(saved_runs["run_2"]) == 0:
            saved_runs["run_2"] = [grid, current_score, merged, pushed, random_flag]
        else:
            saved_runs["run_1"].clear()
            saved_runs["run_1"] = saved_runs["run_2"].copy()
            saved_runs["run_2"].clear()
            saved_runs["run_2"] = [grid, current_score, merged, pushed, random_flag]
        # Reset flags
        pushed = False
        merged = False
        random_flag = False
        # Check Key Press Event
        key = event.keysym
        print('\n{} key pressed'.format(key))
        if key in {'w', 'W', 'Up'}:
            push_to("up")
            do_merge("up")
            random_flag = pushed or merged
            push_to("up")
        elif key in {'s', 'S', 'Down'}:
            push_to("down")
            do_merge("down")
            random_flag = pushed or merged
            push_to("down")
        elif key in {'a', 'A', 'Left'}:
            push_to("left")
            do_merge("left")
            random_flag = pushed or merged
            push_to("left")
        elif key in {'d', 'D', 'Right'}:
            push_to("right")
            do_merge("right")
            random_flag = pushed or merged
            push_to("right")
        # Refresh game area
        grid_display()
        # Check if 'Z' have seen
        if seen_z():
            if not win:
                print('You Win the game')
                result_label.configure(text='You Win!')
                write_file("files/highscore.txt", current_score)
                messagebox.showinfo('ABC Games', 'Congratulations: You Win the game')
                win = True
            return
        # Add new random cell
        if random_flag:
            add_random_cell()
        grid_display()
        score_display()
        # Check if Game Over occurred
        if is_game_over():
            game_over = True
            print("Game over")
            print("You managed to break the previous record.")
            result_label.configure(text='Sorry! Game over')
            if current_score > best_score:
                write_file("files/highscore.txt", str(current_score))
                messagebox.showinfo('ABC Games', 'Sorry! Game Over\nYou managed to break the previous record')
            else:
                messagebox.showinfo('ABC Games', 'Sorry! Game Over')

    # ---------------------------------------------------------------------
    # Main Function Block
    global grid, image_dict, best_score
    highscore = read_file("files/highscore.txt")
    if highscore:
        best_score = int(highscore)
    else:
        best_score = 0
    root = tk.Tk()
    grid = [['0'] * grid_size for _ in range(grid_size)]
    root.geometry('465x670+500+70')
    root.title('ABC Games')
    root.resizable(False, False)

    choices = ["Graphical buttons" , "Simple buttons"]
    if simple_graphic:
        choice = choices[1]
        main_bg_color = simple_bg_color
    else:
        choice = choices[0]
        main_bg_color = graphical_bg_color
    variable = tk.StringVar(root, f"{choice}")
    x = 0
    rdb_labels = []
    for choice in choices:
        radio = tk.Radiobutton(root,
            text=choice,
            variable=variable,
            value=choice,
            command=method_clicked,
            bg=main_bg_color,
            activebackground=main_bg_color)
        radio.place(x=15, y=x + 95)
        rdb_labels.append(radio)
        x += 20

    root.configure(bg=main_bg_color)
    game_picture = tk.PhotoImage(file="images/abc.png")
    abc_label = tk.Label(root, image=game_picture)

    main_label = tk.Label(root,
                            text="ABC\nGames",
                            anchor="nw",
                            height=3,
                            width=15,
                            bd=0,
                            font=("Arial", 14, "bold"),
                            cursor="hand2",
                            fg="#ff0066",
                            bg=main_bg_color,
                            padx=1,
                            pady=1,
                            justify="left",
                            relief="flat",
                            wraplength=250
                            )

    top_label1 = tk.Label(root,
                         text="Score: 0",
                         anchor="nw",
                         bg="light gray",
                         height=1,
                         width=16,
                         bd=2,
                         font=("Arial", 12, "bold"),
                         fg="black",
                         padx=5,
                         pady=5,
                         justify="center",
                         relief="ridge",
                         wraplength=250
                         )

    top_label2 = tk.Label(root,
                         text="Best: 0",
                         anchor="nw",
                         bg="light gray",
                         height=1,
                         width=16,
                         bd=2,
                         font=("Arial", 12, "bold"),
                         fg="black",
                         padx=5,
                         pady=5,
                         justify="center",
                         relief="ridge",
                         wraplength=250
                         )

    undo_button = tk.Button(root,
                       text="undo",
                       command=undo_clicked,
                       activebackground="gray",
                       activeforeground="white",
                       anchor="center",
                       bd=3,
                       bg="light gray",
                       cursor="hand2",
                       disabledforeground="gray",
                       fg="black",
                       font=("Arial", 12),
                       height=1,
                       highlightbackground="black",
                       highlightcolor="green",
                       highlightthickness=2,
                       justify="center",
                       overrelief="raised",
                       padx=10,
                       pady=0,
                       width=3,
                       wraplength=100)

    new_game = tk.Button(root,
                       text="New Game",
                       command=new_clicked,
                       activebackground="gray",
                       activeforeground="white",
                       anchor="center",
                       bd=3,
                       bg="light gray",
                       cursor="hand2",
                       disabledforeground="gray",
                       fg="black",
                       font=("Arial", 12),
                       height=1,
                       highlightbackground="black",
                       highlightcolor="green",
                       highlightthickness=2,
                       justify="center",
                       overrelief="raised",
                       padx=10,
                       pady=0,
                       width=8,
                       wraplength=100)

    game_area = tk.Frame(root, bd = 3, relief="flat")
    grid_labels = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            cell_label = tk.Label(game_area, text="")
            cell_label.grid(row=i, column=j, padx=5, pady=5)
            row.append(cell_label)
        grid_labels.append(row)

    save_button = tk.Button(root,
                       text="Save",
                       command=save_clicked,
                       activebackground="gray",
                       activeforeground="white",
                       anchor="center",
                       bd=3,
                       bg="light gray",
                       cursor="hand2",
                       disabledforeground="gray",
                       fg="black",
                       font=("Arial", 12),
                       height=1,
                       highlightbackground="black",
                       highlightcolor="green",
                       highlightthickness=2,
                       justify="center",
                       overrelief="raised",
                       padx=10,
                       pady=0,
                       width=4,
                       wraplength=100)

    load_button = tk.Button(root,
                       text="Load",
                       command=load_clicked,
                       activebackground="gray",
                       activeforeground="white",
                       anchor="center",
                       bd=3,
                       bg="light gray",
                       cursor="hand2",
                       disabledforeground="gray",
                       fg="black",
                       font=("Arial", 12),
                       height=1,
                       highlightbackground="black",
                       highlightcolor="green",
                       highlightthickness=2,
                       justify="center",
                       overrelief="raised",
                       padx=10,
                       pady=0,
                       width=4,
                       wraplength=100)

    result_label = tk.Label(root,
                         text="Use Arrow Keys to move",
                         anchor="center",
                         bg=main_bg_color,
                         height=1,
                         width=28,
                         bd=0,
                         font=("Arial", 12, "bold"),
                         fg="red",
                         padx=5,
                         pady=5,
                         justify="center",
                         relief="flat",
                         wraplength=250
                         )

    # Place Widgets on the tkinter form
    abc_label.place(x=20, y=5)
    main_label.place(x=110, y=45)
    top_label1.place(x=280, y=10)
    top_label2.place(x=280, y=50)
    undo_button.place(x=280, y=100)
    new_game.place(x=350, y=100)
    game_area.place(x=10, y=142)
    save_button.place(x=18, y=610)
    load_button.place(x=90, y=610)
    result_label.place(x=160, y=613)

    # Load Letters image File to dictionary
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0":
        image_dict[char] = tk.PhotoImage(file="./images/" + str(char) + ".png")

    for _ in range(2):
        add_random_cell()
    grid_display()
    score_display()
    root.bind('<Key>', key_handler)
    root.mainloop()

if __name__ == '__main__':
    main()