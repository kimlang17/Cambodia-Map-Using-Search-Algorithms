from heapq import heappop, heappush

def heuristic(district, goal, districts):
    return next(d['distance_from_tuol_kouk'] for d in districts if d['district_name'] == district)

def search(start, goal, districts):
    open_list = []
    heappush(open_list, (0, [start]))  # (total estimated cost, path)
    visited = set()

    while open_list:
        _, path = heappop(open_list)
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
                g_cost = current_distance + next(
                    d['distances_to_neighbors'].get(neighbor, 0) for d in districts if d['district_name'] == district
                )
                f_cost = g_cost + heuristic(neighbor, goal, districts)
                new_path = path + [neighbor]
                heappush(open_list, (f_cost, new_path))

    return None, 0
