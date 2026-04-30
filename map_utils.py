import osmnx as ox
import folium
import webbrowser
from dijkstra import dijkstra

def find_and_show_route(source, destination, mode):

    try:
        orig = ox.geocode(source)
        dest = ox.geocode(destination)
    except:
        return "Invalid location"

    # Midpoint for faster loading
    mid_lat = (orig[0] + dest[0]) / 2
    mid_lon = (orig[1] + dest[1]) / 2

    #graph loading ke liye
    try:
        G = ox.graph_from_point((mid_lat, mid_lon), dist=15000, network_type='drive')
        if len(G.edges) == 0:
            raise Exception()
    except:
        
        G = ox.graph_from_point((mid_lat, mid_lon), dist=50000, network_type='drive')

    # speeds
    G = ox.add_edge_speeds(G, fallback=40, hwy_speeds={
        "residential": 20,
        "primary": 80,
        "secondary": 60,
        "tertiary": 50
    })

    G = ox.add_edge_travel_times(G)

    # nearest nodes obtain karne ke liye
    orig_node = ox.distance.nearest_nodes(G, orig[1], orig[0])
    dest_node = ox.distance.nearest_nodes(G, dest[1], dest[0])

    # Mode selection
    if mode == "Shortest":
        weight = "length"
        color = "green"

    elif mode == "Fastest":
        weight = "travel_time"
        color = "blue"

    else:
        # Emergency mode
        for u, v, k, data in G.edges(keys=True, data=True):
            road_priority = {
                "primary": 1,
                "secondary": 1.2,
                "tertiary": 1.5,
                "residential": 2
            }

            hwy = data.get("highway", "residential")

            if isinstance(hwy, list):
                hwy = hwy[0]

            factor = road_priority.get(hwy, 2)
            data["emergency"] = data.get("travel_time", 1) * factor

        weight = "emergency"
        color = "red"


    route = dijkstra(G, orig_node, dest_node, weight)

    if not route:
        return "No route found"

   
    coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route]

    # Create map
    m = folium.Map(
        location=coords[len(coords)//2],
        zoom_start=13,
        tiles="CartoDB positron"
    )

    # Draw route
    folium.PolyLine(coords, color=color, weight=5).add_to(m)

    # Markers
    folium.Marker(coords[0], popup="Source",
                  icon=folium.Icon(color="green")).add_to(m)

    folium.Marker(coords[-1], popup="Destination",
                  icon=folium.Icon(color="red")).add_to(m)

    # Save + open
    m.save("route_map.html")
    webbrowser.open("route_map.html")

    return "Success"