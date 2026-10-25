from collections import deque

def is_valid(m, c):
    # Check number of people
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False

    # Left bank safety
    if m > 0 and c > m:
        return False

    # Right bank safety
    rm = 3 - m
    rc = 3 - c

    if rm > 0 and rc > rm:
        return False

    return True


def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    # Boat can carry these combinations
    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution found!")
            print("Total steps:", len(path))

            for i, step in enumerate(path, 1):
                print("Step", i, ":", step)

            return

        for dm, dc in moves:

            if boat == 0:
                new_m = m - dm
                new_c = c - dc
                new_boat = 1
            else:
                new_m = m + dm
                new_c = c + dc
                new_boat = 0

            new_state = (new_m, new_c, new_boat)

            if is_valid(new_m, new_c) and new_state not in visited:
                visited.add(new_state)

                action = (
                    f"{dm} Missionary and {dc} Cannibal "
                    f"crossing"
                )

                queue.append(
                    (new_state, path + [action])
                )

    print("No solution found.")


solve()
