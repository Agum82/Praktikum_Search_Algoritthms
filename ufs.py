# -*- coding: utf-8 -*-
"""ufs

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jXT8SaaaaJtr3XzWchXTYiW9D64qgR1L
"""

# Python3 implementation of Uniform Cost Search (UCS)

# Function to return the minimum cost in a vector (if there are multiple goal states)
def uniform_cost_search(goal, start):
    global graph, cost
    answer = []

    # Create a priority queue
    queue = []

    # Set the answer vector to max value
    for i in range(len(goal)):
        answer.append(10**8)

    # Insert the starting index
    queue.append([0, start])

    # Map to store visited nodes
    visited = {}

    # Count of goals reached
    count = 0

    # While the queue is not empty
    while len(queue) > 0:
        # Get the top element of the queue
        queue = sorted(queue)
        p = queue[-1]

        # Remove the element from queue
        del queue[-1]

        # Get the original value
        p[0] *= -1

        # Check if the element is part of the goal list
        if p[1] in goal:
            index = goal.index(p[1])

            # If a new goal is reached
            if answer[index] == 10**8:
                count += 1

            # If the cost is less, update the answer
            if answer[index] > p[0]:
                answer[index] = p[0]

            # If all goals are reached, return the answer
            if count == len(goal):
                return answer

        # Check for the non-visited adjacent nodes
        if p[1] not in visited:
            for i in range(len(graph[p[1]])):
                queue.append([ (p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])

        # Mark node as visited
        visited[p[1]] = 1

    return answer

# Main function
if __name__ == '__main__':
    # Create the graph
    graph, cost = [[] for i in range(8)], {}

    # Add edges to the graph
    graph[0].append(1)
    graph[0].append(3)
    graph[3].append(1)
    graph[3].append(6)
    graph[3].append(4)
    graph[1].append(6)
    graph[4].append(2)
    graph[4].append(5)
    graph[2].append(1)
    graph[5].append(2)
    graph[5].append(6)
    graph[6].append(4)

    # Add cost of edges
    cost[(0, 1)] = 2
    cost[(0, 3)] = 5
    cost[(1, 6)] = 1
    cost[(3, 1)] = 5
    cost[(3, 6)] = 6
    cost[(3, 4)] = 2
    cost[(2, 1)] = 4
    cost[(4, 2)] = 4
    cost[(4, 5)] = 3
    cost[(5, 2)] = 6
    cost[(5, 6)] = 3
    cost[(6, 4)] = 7

    # Define goal state
    goal = []
    goal.append(6)

    # Get the answer
    answer = uniform_cost_search(goal, 0)

    # Print the result
    print("Minimum cost from 0 to 6 is =", answer[0])