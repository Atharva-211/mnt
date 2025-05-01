def is_valid(state, color, neighbor_map, assignment):
    for neighbor in neighbor_map[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, states, colors, neighbor_map):
    if len(assignment) == len(states):
        return assignment

    unassigned = [s for s in states if s not in assignment]
    state = unassigned[0]

    for color in colors:
        if is_valid(state, color, neighbor_map, assignment):
            assignment[state] = color
            result = backtrack(assignment, states, colors, neighbor_map)
            if result:
                return result
            del assignment[state]
    return None

states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
neighbor_map = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}
colors = ['Red', 'Green', 'Blue']

solution = backtrack({}, states, colors, neighbor_map)
print("Map Coloring Solution:")
print(solution)