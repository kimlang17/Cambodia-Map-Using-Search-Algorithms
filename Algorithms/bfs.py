from collections import deque

def search(start, goal, districts):
    queue = deque([[start]])
    visited = set()
    paths_distances = deque([0])  # Queue to keep track of cumulative distances
    
    while queue:
        path = queue.popleft()
        current_distance = paths_distances.popleft()  # Get the corresponding cumulative distance
        district = path[-1]

        print(f"Visiting: {district}, Current Path: {' -> '.join(path)}, Current Distance: {current_distance:.2f} km")  # Debugging line

        if district in visited:
            continue

        if district == goal:
            return path, current_distance

        # Find the neighbors of the current district
        for neighbor in next(d['neighbors'] for d in districts if d['district_name'] == district):
            # Find the distance from the current district to this neighbor
            distance_to_neighbor = next(
                d['distances_to_neighbors'].get(neighbor, 0) for d in districts if d['district_name'] == district
            )
            
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
            
            # Add the distance to this neighbor to the cumulative distance
            paths_distances.append(current_distance + distance_to_neighbor)

        visited.add(district)
    
    return None, 0
