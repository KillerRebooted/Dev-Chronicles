from time import sleep

def display_grid(sudoku):
    print("_"*25, flush=True)
    for i in range(0, len(sudoku), 3):
        for j in range(3):
            print("| ", end="", flush=True)
            for k in range(3):
                print(*sudoku[i+k][j], sep=" ", end = " | ", flush=True)
            print("", flush=True)
        print("_"*25, flush=True)

def make_sudoku(inp):

    grid = {i:{j:[0, 0, 0] for j in range(3)} for i in range(9)}

    for idx, i in enumerate(inp):
        if i.isdigit():
            inp[idx] = int(i)
    
    iter = 0

    for i in range(0, len(grid), 3):
        for j in range(3):
            for k in range(3):
                grid[i+k][j] = [inp[iter], inp[iter + 1], inp[iter + 2]]
                iter += 3

    return grid

def solve(sudoku):

    horizontal_listing = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    vertical_listing = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]

    unsolved = True

    def check_surroundings(coords):

        found_numbers = set()

        #Adding Numbers of Same Box to Set

        for line in sudoku[coords[0]].values():
            for num in range(3):
                found_numbers.add(line[num])

        #Finding the Boxes in Horizontal and Vertical Line

        for boxes in horizontal_listing:
            for num in boxes:
                if num == box_num:
                    horizontal_boxes = boxes

        for boxes in vertical_listing:
            for num in boxes:
                if num == box_num:
                    vertical_boxes = boxes

        #Checking Horizontal and Vertical Lines

        for box in horizontal_boxes:
            for num in sudoku[box][coords[1]]:
                found_numbers.add(num)

        for box in vertical_boxes:
            for line in sudoku[box].values():
                found_numbers.add(line[coords[2]])

        found_numbers.remove(" ")

        return found_numbers

    while unsolved:
        
        #Checking Boxes

        for box_num in (range(len(sudoku))):
            for line_num in range(3):
                for column_num in range(3):

                    digit = sudoku[box_num][line_num][column_num]

                    if digit == " ":
                        coords = [box_num, line_num, column_num]
                        vicinity = check_surroundings(coords)

                        possible_digit = 45 - sum(vicinity)

                        if possible_digit <= 9 and len(vicinity) == 8:
                            sudoku[box_num][line_num][column_num] = possible_digit

        #Check if Solved

        unsolved = False

        for box_num in (range(len(sudoku))):
            for line_num in range(3):
                for column_num in range(3):

                    digit = sudoku[box_num][line_num][column_num]

                    if digit == " ":
                        unsolved = True

#inp = list(input("Enter Sudoku: "))
inp = list("8 6 1      3 64 9 9     816 8 396   7 2 4 3 9   572 8 521     4 3 75 2      2 1 5")

sudoku = make_sudoku(inp)

display_grid(sudoku)
solve(sudoku)
display_grid(sudoku)