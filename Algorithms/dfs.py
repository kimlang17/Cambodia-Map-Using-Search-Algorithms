def search(start, goal, districts):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        district = path[-1]

        current_distance = sum(
            next(d['distances_to_neighbors'].get(path[i + 1], 0) for d in districts if d['district_name'] == path[i])
            for i in range(len(path) - 1)
        )

        print(f"Visiting: {district}, Current Path: {' -> '.join(path)}, Current Distance: {current_distance:.2f} km")  # Debugging line

        if district in visited:
            continue

        if district == goal:
            return path, current_distance

        visited.add(district)

        for neighbor in next(d['neighbors'] for d in districts if d['district_name'] == district):
            if neighbor not in visited:
                new_path = path + [neighbor]
                stack.append(new_path)

    return None, 0
