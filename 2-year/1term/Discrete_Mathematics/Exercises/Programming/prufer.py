def prufer_to_tree(S, n):
    # Create a list of nodes from 1 to n
    nodes = list(range(1, n + 1))
    # Initialize a degree array to count the degree of each node
    degree = [1] * (n + 2)

    edges = []

    # Update the degree array based on the Prüfer code
    for i in S:
        degree[i] += 1

    # Construct the tree
    for i in S:
        for j in nodes:
            if degree[j] == 1:
                # Connect the current node in the Prüfer code to the found node
                edges.append((i, j))
                degree[i] -= 1
                degree[j] -= 1
                break

    # Find the last two nodes and connect them 
    u, v = [node for node in nodes if degree[node] == 1]
    edges.append((u, v))

    return edges


n = int(input("Number of nodes: "))

# Get the Prüfer code 'S' as input, splitting by space
S = list(map(int, input("Prüfer code is: ").split()))

# Check if the length is valid
if len(S) == n - 2:
    tree_edges = prufer_to_tree(S, n)
    print("Edges of the tree:", tree_edges)
else:
    print("The length of Prüfer code must be n - 2.")
