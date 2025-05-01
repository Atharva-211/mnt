def crossword_backtrack(grid, words, idx): 
    if idx == len(words): 
        return True 
    
    word = words[idx] 
    for i in range(len(grid)): 
        for j in range(len(grid[0])): 
            if can_place_word(grid, word, i, j, 'horizontal'): 
                placed = place_word(grid, word, i, j, 'horizontal') 
                if crossword_backtrack(grid, words, idx + 1): 
                    return True 
                remove_word(grid, placed) 
                
            if can_place_word(grid, word, i, j, 'vertical'): 
                placed = place_word(grid, word, i, j, 'vertical') 
                if crossword_backtrack(grid, words, idx + 1): 
                    return True 
                remove_word(grid, placed) 
    return False 


def can_place_word(grid, word, x, y, direction): 
    if direction == 'horizontal': 
        if y + len(word) > len(grid[0]): 
            return False 
        for i in range(len(word)): 
            if grid[x][y+i] not in ('-', word[i]): 
                return False 
    else: 
        if x + len(word) > len(grid): 
            return False 
        for i in range(len(word)): 
            if grid[x+i][y] not in ('-', word[i]): 
                return False 
    return True 


def place_word(grid, word, x, y, direction): 
    placed = [] 
    for i in range(len(word)): 
        if direction == 'horizontal': 
            if grid[x][y+i] == '-': 
                grid[x][y+i] = word[i] 
                placed.append((x, y+i)) 
        else: 
            if grid[x+i][y] == '-': 
                grid[x+i][y] = word[i] 
                placed.append((x+i, y)) 
    return placed 


def remove_word(grid, placed): 
    for x, y in placed: 
        grid[x][y] = '-' 


# Example usage: 
grid = [['-' for _ in range(5)] for _ in range(5)] 
words = ['APPLE', 'EAR'] 

if crossword_backtrack(grid, words, 0): 
    for row in grid: 
        print(''.join(row)) 
else: 
    print("No solution found.")
