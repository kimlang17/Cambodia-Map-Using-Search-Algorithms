from flask import Flask, render_template, request
import json
from Algorithms import bfs, gbfs, astar, dfs  # Make sure these modules are available
from visualize import visualize_route  # Assuming this is the updated visualization function
import folium

app = Flask(__name__)

# Load district data
with open('data/district_centroids_with_distances.json') as f:
    districts = json.load(f)

# Flask route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    path = None
    total_distance = 0
    straight_line_distance = 0
    map_html = None
    
    if request.method == 'POST':
        start_district = request.form.get('start_district')
        algorithm = request.form.get('algorithm')
        
        # Get the straight line distance from JSON
        straight_line_distance = next(d['distance_from_tuol_kouk'] for d in districts if d['district_name'] == start_district)

        # Perform the search based on the chosen algorithm
        if algorithm == 'bfs':
            path, total_distance = bfs.search(start_district, 'Tuol Kouk', districts)
        elif algorithm == 'gbfs':
            path, total_distance = gbfs.search(start_district, 'Tuol Kouk', districts)
        elif algorithm == 'astar':
            path, total_distance = astar.search(start_district, 'Tuol Kouk', districts)
        elif algorithm == 'dfs':
            path, total_distance = dfs.search(start_district, 'Tuol Kouk', districts)

        # Generate the map
        map_html = visualize_route(path, districts)

    return render_template('index.html', districts=districts, path=path, total_distance=total_distance,
                           straight_line_distance=straight_line_distance, map_html=map_html)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
