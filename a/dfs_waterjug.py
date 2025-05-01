def water_jug_dfs(cap_x, cap_y, target, target_jug):
    # Initialize variables
    initial_state = (0, 0)
    stack = [initial_state]  # Stack for DFS
    visited = set()  # To track visited states
    path = []  # To store the solution path
    goal_state = None  # To store the goal state

    while stack:
        x, y = stack.pop()

        # Check if the target is reached in the selected jug
        if (target_jug == 'A' and x == target) or (target_jug == 'B' and y == target):
            goal_state = (x, y)
            path.append((x, y))
            # Print the solution path
            print("\n✅ Solution Path (DFS):")
            for step in path:
                print(f"A={step[0]}, B={step[1]}")
            # Display the initial and goal states
            print("\n🚩 Initial State: A=0, B=0")
            print(f"🏁 Goal State: A={goal_state[0]}, B={goal_state[1]}")
            return True

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path.append((x, y))

        # Generate valid states with correct water transfer operations
        # 1. Fill Jug A
        stack.append((cap_x, y))

        # 2. Fill Jug B
        stack.append((x, cap_y))

        # 3. Empty Jug A
        stack.append((0, y))

        # 4. Empty Jug B
        stack.append((x, 0))

        # 5. Transfer water from A → B
        transfer = min(x, cap_y - y)
        stack.append((x - transfer, y + transfer))

        # 6. Transfer water from B → A
        transfer = min(y, cap_x - x)
        stack.append((x + transfer, y - transfer))

        # 7. Transfer some water from B → A till A gets full
        if x + y >= cap_x:
            stack.append((cap_x, x + y - cap_x))

        # 8. Transfer some water from A → B till B gets full
        if x + y >= cap_y:
            stack.append((x + y - cap_y, cap_y))

    print("\n❌ No solution found.")
    return False


# ✅ User Input
print("Water Jug Problem using - Depth First Search (DFS)")

try:
    # Get jug capacities
    cap_x = int(input("Enter capacity of Jug A: "))
    cap_y = int(input("Enter capacity of Jug B: "))

    # Ask the user which jug should hold the target amount
    target_jug = input("Which jug should hold the target amount? (A/B): ").upper()

    # Validate the input
    while target_jug not in ['A', 'B']:
        print("❌ Invalid choice. Please enter 'A' or 'B'.")
        target_jug = input("Which jug should hold the target amount? (A/B): ").upper()

    # Get the target amount
    target = int(input(f"Enter the target amount for Jug {target_jug}: "))

    # Check if the target is achievable
    if (target_jug == 'A' and target > cap_x) or (target_jug == 'B' and target > cap_y):
        print("\n❌ Target amount cannot be larger than the jug capacity.")
    else:
        water_jug_dfs(cap_x, cap_y, target, target_jug)

except ValueError:
    print("❌ Please enter valid numerical inputs.")
