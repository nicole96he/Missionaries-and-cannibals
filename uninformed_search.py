# Created by Ningxiang He on 01/09/2019

from collections import deque
from SearchSolution import SearchSolution

class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    '''
    define attributes of SearchNode
        Args: state, parent
    '''
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        # you write this part


'''
bfs_search search path for problem
    Args: search_problem
    Returns: SearchSolution
'''
def bfs_search(search_problem):
    solution = SearchSolution(search_problem,"BFS")
    Node = SearchNode(search_problem.start_state,None) # Transfer state to node.
    order_node = deque()
    order_node.append(Node)
    order_state = deque() # create order_state to store future explore state sequence
    order_state.append(search_problem.start_state)
    check = set()
    # check is a set,used to store all the states that have been visited unrepeatedly
    while order_state: # loop until order_state is empty
        curr_state = order_state.popleft() # get first state out from quene
        curr_node = order_node.popleft() # get first node out from quene
        check.add(curr_state) # add current state into check set
        solution.nodes_visited +=1
        children = search_problem.get_successors(curr_state)
        # children is a list of all legal next states of current state
        if search_problem.goal_test(curr_state):
            backchaining(curr_node,solution) # use backchaining to track path
            return solution
        for child in children: # traverse all legal states
            if child in check: # judge if the state has been searched before
                continue # if the state has been searched before, go to next state(child)
            else:
                order_state.append(child)
                new_node = SearchNode(child,curr_node) # record parent of every state
                order_node.append(new_node)
    return solution

'''
extract the path from graph after search has found goal node
    Args: Final_node,SearchSolution
'''
def backchaining(end_node,solution):
    path = []
    while end_node:
        path.append(end_node.state)
        end_node = end_node.parent  # move to next node
    path.reverse()
    solution.path = path


# We pass the solution along to each new recursive call to dfs_search
#  so that statistics like number of nodes visited or recursion depth
#  might be recorded
'''
Path-checking dfs search solution
    Args: search_problem, depth_limit, node, solution
    return: solution
'''
store = set()
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")
    if depth_limit<0:
        return solution
    store.add(node.state) # store states which have been visited
    solution.nodes_visited +=1
    if search_problem.goal_test(node.state):
        backchaining(node,solution)
        return solution
    for n in search_problem.get_successors(node.state): # traverse successors of current state
        if n not in store:
            n_node = SearchNode(n,node)
            dfs_search(search_problem, depth_limit-1,n_node,solution) # recursive
    store.remove(node.state)
    return solution


'''
iterative deepening search solution
    Args: search_problem,depth_limit
    returns: SearchSolution
'''
def ids_search(search_problem, depth_limit=100):
    store.clear() # have to clear the store set, or it will be influenced by former run
    node = SearchNode(search_problem.start_state)
    solution = SearchSolution(search_problem,"IDS")

    for depth in range(0,100):
        dfs_search(search_problem,depth,node,solution) # call dfs_search to search path in limited depth
        if(len(solution.path)>0):
            return solution
    return solution

