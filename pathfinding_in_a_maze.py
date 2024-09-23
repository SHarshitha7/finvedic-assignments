from collections import deque

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])  
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == goal: 
            break
        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != 0 and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = current

    path = []
    current = goal
    while current:
        path.append(current)
        current = parent[current]
    path.reverse() 
    return path

def input_maze():
    maze = []
    start, goal = None, None

    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    print("Enter the maze (rows separated by new lines, S for start, F for finish):")

    for r in range(rows):
        row = input().strip()  
        maze_row = []
        for i, cell in enumerate(row.split()): 
            if cell == 'S':
                start = (r, i)  
                maze_row.append(1)  
            elif cell == 'F':
                goal = (r, i)  
                maze_row.append(1)  
            else:
                maze_row.append(int(cell))  
        maze.append(maze_row)  
    return maze, start, goal  


maze, start, goal = input_maze()

if start and goal:
    path = bfs(maze, start, goal)
    if path:
        print("Shortest path:", path)
    else:
        print("No path found.")
else:
    print("Invalid maze: Start or goal not specified.")
