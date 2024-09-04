# import folium

# def visualize_route(path, districts):
#     if not path:
#         print("No path found")
#         return

#     map_center = [11.5686353722197, 104.8969161077831]  # Tuol Kouk centroid
#     route_map = folium.Map(location=map_center, zoom_start=8)

#     for district_name in path:
#         district = next(d for d in districts if d['district_name'] == district_name)
#         centroid = district['centroid']
#         folium.Marker(
#             location=[centroid['latitude'], centroid['longitude']],
#             popup=district_name,
#             icon=folium.Icon(color='blue' if district_name == 'Tuol Kouk' else 'red')
#         ).add_to(route_map)

#     # Draw lines between the points
#     for i in range(len(path) - 1):
#         start_district = next(d for d in districts if d['district_name'] == path[i])
#         end_district = next(d for d in districts if d['district_name'] == path[i+1])
#         folium.PolyLine(
#             locations=[
#                 [start_district['centroid']['latitude'], start_district['centroid']['longitude']],
#                 [end_district['centroid']['latitude'], end_district['centroid']['longitude']]
#             ],
#             color='blue'
#         ).add_to(route_map)

#     # Save map to an HTML file
#     route_map.save("route_map.html")
#     print("Map has been saved as route_map.html")

import folium

def visualize_route(path, districts):
    if not path:
        return None

    map_center = [11.5686353722197, 104.8969161077831]  # Tuol Kouk centroid
    route_map = folium.Map(location=map_center, zoom_start=8)

    for district_name in path:
        district = next(d for d in districts if d['district_name'] == district_name)
        centroid = district['centroid']
        folium.Marker(
            location=[centroid['latitude'], centroid['longitude']],
            popup=district_name,
            icon=folium.Icon(color='blue' if district_name == 'Tuol Kouk' else 'red')
        ).add_to(route_map)

    # Draw lines between the points
    for i in range(len(path) - 1):
        start_district = next(d for d in districts if d['district_name'] == path[i])
        end_district = next(d for d in districts if d['district_name'] == path[i+1])
        folium.PolyLine(
            locations=[
                [start_district['centroid']['latitude'], start_district['centroid']['longitude']],
                [end_district['centroid']['latitude'], end_district['centroid']['longitude']]
            ],
            color='blue'
        ).add_to(route_map)

    # Return the map as an HTML string
    return route_map._repr_html_()
