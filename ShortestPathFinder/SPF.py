import curses
from curses import wrapper
import queue
import time

# '#' = wall, 'O' = start, 'X' = goal
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(stdscr, maze, path=[], color_id=1):
    """Draws the maze and the current path."""
    DEFAULT_COLOR = curses.color_pair(1)
    PATH_COLOR = curses.color_pair(color_id)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                # Draw '*' for the final path, but keep 'O' and 'X'
                if color_id == 3 and value not in ["O", "X"]:
                    char_to_draw = "*"
                else:
                    char_to_draw = "X"
                stdscr.addstr(i, j * 2, char_to_draw, PATH_COLOR)
            else:
                stdscr.addstr(i, j * 2, value, DEFAULT_COLOR)


def find_start(maze, start_char):
    """Finds the coordinates of the start character."""
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start_char:
                return i, j
    return None


def find_path(maze, stdscr):
    """Finds the shortest path using Breadth-First Search (BFS)."""
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = {start_pos}

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        # Animate the search process
        stdscr.clear()
        print_maze(stdscr, maze, path, color_id=2)  # Red for search
        time.sleep(0.1)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited or maze[neighbor[0]][neighbor[1]] == "#":
                continue

            visited.add(neighbor)
            new_path = path + [neighbor]
            q.put((neighbor, new_path))

    return None


def find_neighbors(maze, row, col):
    """Returns valid neighbors (up, down, left, right)."""
    neighbors = []
    if row > 0: neighbors.append((row - 1, col))
    if row + 1 < len(maze): neighbors.append((row + 1, col))
    if col > 0: neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]): neighbors.append((row, col + 1))
    return neighbors


def main(stdscr):
    """Main function to set up and run the application."""
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  # ID 1: Maze
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # ID 2: Search animation
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)  # ID 3: Final path

    final_path = find_path(maze, stdscr)

    if final_path:
        stdscr.clear()
        print_maze(stdscr, maze, final_path, color_id=3)  # Green for final path
        stdscr.addstr(len(maze) + 1, 0, "Path found! Press any key to exit.")
    else:
        stdscr.addstr(len(maze) + 1, 0, "No path found. Press any key to exit.")

    stdscr.getch()  # Wait for user input before exiting


# The curses wrapper handles initialization and cleanup
wrapper(main)
