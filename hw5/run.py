import sys
import os


# Parse the input file into a dictionary that represents a graph with wrestlers.
# Graph's edges represent rivalry between wrestlers.
def parse():
    # Open the file specified as the first argument in command line after this file name
    file_path = os.path.dirname(os.path.realpath(__file__)) + "/" + sys.argv[1]
    input_file = open(file_path, "r")

    # Read all lines from input file
    lines = input_file.readlines()
    loop_count = 0
    connections_count = 0;
    connections_total = 0;
    wrestlers_number = 0
    wrestlers_graph = {}

    # Store a list of connection for later usage
    connections = []

    for line in lines:
        # Remove new line characters
        line = line.strip()

        # The first line contains the number of wrestlers
        if loop_count == 0:
            wrestlers_number = int(line)

        # Fill the graph dictionary with wrestler names as keys
        if 0 < loop_count <= wrestlers_number:
            if loop_count == 1:
                start = line

            wrestlers_graph[line] = {
                'visited': False,
                'distance': 0,
                'connections': []
            }

        if loop_count == (wrestlers_number + 1):
            connections_total = int(line)

        # Fill rivalries between wrestlers in the graph dictionary
        if loop_count > (wrestlers_number + 1) and connections_count < connections_total:
            # Split names into array for easy access
            line = line.split()
            connections.append(line)
            wrestlers_graph[line[0]]['connections'].append(line[1])
            wrestlers_graph[line[1]]['connections'].append(line[0])
            connections_count = connections_count + 1

        loop_count = loop_count + 1

    return {
        'start': start,
        'graph': wrestlers_graph,
        'connections': connections
    }


# Use BFS algorithm to set the distance for each vertex of the graph from an arbitrary start
def bfs_distance(graph, start):
    queue = [start]
    graph[start]['visited'] = True

    while not len(queue) == 0:
        wrestler = queue.pop(0)
        distance = graph[wrestler]['distance'] + 1

        for next_wrestler in graph[wrestler]['connections']:
            if not graph[next_wrestler]['visited']:
                graph[next_wrestler]['visited'] = True
                graph[next_wrestler]['distance'] = distance
                queue.append(next_wrestler)

    return graph


# Checks that every edge goes between an even and odd vertex
def check_connections(parsed_data):
    graph = parsed_data['graph']
    connections = parsed_data['connections']

    for connection in connections:
        dist1 = graph[connection[0]]['distance']
        dist2 = graph[connection[1]]['distance']
        diff = dist2 - dist1

        if diff % 2 == 0:
            return False

    return True


# Forms two teams using the assumption that all vertices with even distance are baby faces
# and all vertices with odd distance are heels
def get_teams(graph):
    babyfaces = "Babyfaces: "
    heels = "Heels: "

    for wrestler in graph:
        if graph[wrestler]['distance'] % 2 == 0:
            babyfaces = babyfaces + wrestler
            babyfaces = babyfaces + " "
        else:
            heels = heels + wrestler
            heels = heels + " "

    return [babyfaces, heels]


def get_unvisited_wrestler(graph):
    for wrestler in graph:
        if not graph[wrestler]['visited']:
            return wrestler

    return ""


# Parse the input file and try to designate all wrestlers
def run():
    parsed_data = parse()

    # Repeat until all vertices (wrestlers) have been visited
    while True:
        wrestler = get_unvisited_wrestler(parsed_data['graph'])

        if wrestler == "":
            break

        bfs_distance(parsed_data['graph'], wrestler)

    # Now every vertex (wrestler) of the graph has a distance from an arbitrary start
    # Assume that all vertices with even distance are baby faces and all vertices with odd distance are heels
    # Check that every connection goes between an even and odd wrestler
    designation_possible = check_connections(parsed_data)

    if designation_possible:
        print("Yes")
        teams = get_teams(parsed_data['graph'])
        print(teams[0])
        print(teams[1])
    else:
        print("No")

run()
