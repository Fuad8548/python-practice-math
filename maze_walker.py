maze = [
    ["W", "W", "W", "W", "W"],
    ["W", ".", ".", ".", "W"],
    ["W", ".", "W", ".", "W"],
    ["W", ".", ".", "G", "W"],
    ["W", "W", "W", "W", "W"]
]

player_pos = (0, 4)

for row in enumerate(maze):
    for cell in row:
        while True:
            direction = input("Which way: (Up/ Down/ Left/ Right/ Quit):")

            if direction == "Quit":
                print("Thanks for playing!")
                break

            if direction == "Up":
                delta = (-1, 0)
            elif direction == "Down":
                delta = (1, 0)
            elif direction == "Left":
                delta = (0, -1)
            elif direction == "Right":
                delta = (0, 1)         
            else:
                print("Not a valid direction! Try again")
                continue

            new_row = player_pos[0] + delta[0]
            new_col = player_pos[1] + delta[1]

            if new_row < 0 or 0 <= new_col and new_col < len(maze[0]):
                print("Nay! Out of the border!")
            elif maze[new_row][new_col] == "W":
                print("There is wall, try a different direction")

            player_pos = (new_row, new_col)
            print("Player moved", direction, ": at", player_pos)
    
            if maze[new_row][new_col] == "G":
                print("Voila! you reached the goal!")
                break 





# In Python, maze[-1] doesn't error out — it wraps around and grabs the last row instead.
# (index -1 means "last item" in Python indexing). 
# So maze[-1][new_col] would actually check the bottom row of our maze, not "outside the grid