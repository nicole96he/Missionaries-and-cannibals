# Missionaries and cannibals
***
## Introduction
**Problem description:**

Three missionaries and three cannibals come to the bank of a river. They would like to cross to the other side of the river. There is one boat. The boat can carry up to two people at one time, but doesn't row itself -- at least one person must be in the boat for the boat to move. If at any time there are more cannibals than missionaries on either side of the river, then those missionaries get eaten. In this assignment, you'll implement algorithms that will make plans to get everyone across the river in time for lunch, without any missionaries becoming lunch.

**Analysis:**

The total number of states is 32 when there are three missionaries and three cannibals. The number of missionaries has four possibilities: 0,1,2,3, while the number of cannibals has four possibilities as well: 0,1,2,3, and boat number has two possibilities:0,1. So the total number of states is 4* 4 * 2 = 32. When considering more general situation, if there are m missionaries, c cannibals and b boats, the total number of states would be (m+1) * (b+1) * (c+1).

The picture in appendex[0] shows the first state, all actions from that state and all actions from those first-reached states. Red nodes represent illegal states while white nodes represent legal states. Root node is start state (3,3,1). There are five possible actions from this state: 
1. move two missionaries and a boat.
This action is illegal. After this action, the state is (1,3,0). Since the number of cannibals exceeds that of missionaries, the left missionary will get eaten.
2. move one missionary and one cannibals and a boat.
This action is legal.New state is (2,2,0)
3. move two cannibals and a boat.
This action is legal.New state is (3,1,0)
4. move one missionary and a boat.
This action is illegal. After this action, the state becomes (2,3,0). Since the number of cannibals exceeds that of missionaries, the left missionaries will get eaten.
5. move one cannibal and a boat.
This action is legal.New state is (3,2,0)

Now, there are 3 legal states: (2,2,0),(3,1,0),(3,2,0). 
For state(2,2,0), the possible actions are:
1. move one cannibal and a boat.
This is illegal. The state after this action is (2,3,1). Since the cannibals exceeds missionaries, missionaries are not safe.
2. move one missionary and one cannibal.
Legal. New state is (3,3,1).
3. move one cannibal.
Legal. New state is (3,2,1).

For state(3,1,0), there are two possible actions same as the second and third above. New state would be(3,3,1) or (3,2,1). Both of actions is legal.
For state(3,2,0), the only action is moving one cannibal and go back to the root state(3,3,1). This action is legal.

## Building the model
In this section, i build model in CannibalProblem.py. In this class, _init_ is used to define some basic information such as start_state, goal_state, total number of missionaries, cannibals and boats; get_successors can generate all legal states from given state; safe function will detect whether a state is legal or not; goal_test function can detect if a state is the final state.

## Breadth-first search
BFS always used in finding shortest path or in small scale path-searching. BFS always find best dolution because BFS proceeds level by level.

**Code implement:**

The basic idea of bfs:
    --add starting node to new quene;
    --create quene to store future visited sequence;
    --create set() to put visited node;
    *while* quene is not empty:
    --deque current current node from the quene
    --get successors node
    *if* current node is the goal:
    --backchain
    *for each* adjacent node that is not in set():
    --add node to quene
    --mark where node was reached from
    
**Using a linked list to keep track of which states have been visited is a poor choice. Why?**

Linked list put elements in order, so track a specific element has to search in order, which will waste much time. The least time search cost using linked list is O(n). However, I use set to keep track of which states have been visited. Hashtable() search is quite easy and cost less time, the least time it cost is O(1). So, using linked list to keep track states which have been visited is a poor choice.

## Memoizing depth-first search
DFS first traverses nodes going through one adjacent of root, then next adjacent.
**Dose memorizing dfs save significant memory with respect to bfs? Why or Why not?**

No. From my perspective, their memories are not much different. In this situation, both bfs and memorizing dfs store states that has been visited. However, in some extreme, their memories may vary a lot. When the graph is extra wide, BFS would use more memory than DFS. When the graph is extremely deep, DFS would use more memory than BFS.

## Path-checking depth-first search
**code implement:**

--create a set() to store visited nodes;
*if* current state is goal state: success
  --backchain
  --for each adjacent node that is not in the set();
  --call dfs  (recursive)
  
 **backchain code:**
 
 Args: node, solution (node represents goal node)
 return: path
 --create path tuple;
 while node is not None:
 --add node into path
 --move to parent node 
 reverse the whole path.
 
 
**Dose path-checking depth-first search save significant memory with respect to breadth-first search?**

Yes. For breadth-first search, the memory is the size of set(), which store all visited nodes unrepeatedly. For path-checking DFS, the memory is size of set(),which only store current path nodes. Obviously, the memory of path-checking DFS is much smaller than that of BFS.

**This picture in appendex[1] is an example of a graph where path-checking DFS takes much more run-time than breadth-first search:**

In this graph, if using BFS, we can find goal node very quickly. Because bfs proceeds level by level, it will find goal node in level 2. However, if using path-checking dfs, it would cost much more run time. Because the end node is close to root, but not in first few subtrees explored bu dfs, then dfs reaches that node very late. So in this graph, dfs costs much more time.

## Iterative deepening search
**code implement:**

for each depth in range(depth_limit):
--call dfs function
--if path is not empty: return

**Would it make sense to use path-checking dfs or memoizing dfs in iterative deepening search or bfs?**

Personally, I think bfs is the best obviously because it costs least time and always return optimal solution. However, bfs uses much memory comparing to dfs. 
For run time, bfs costs least time, and path-checking dfs costs most time. The speed of ids is between path-checking dfs and bfs. For memory, bfs uses more memory than others. Ids uses more memory than dfs. Iterative deepening search combines dfs's space-efficiency and bfs's fast search (especially for nodes closer to root).

## Discussion question: Lossy missionaries and cannibals
**Considering the situation that no more than E missionaries could be eaten**

The state for this peoblem would be *(M,C,E,B)*, where M represents total number of missionaries, C represents total number of cannibals, E represents left number of missionaries that could be eaten, B represents total number of boats.
For implementing a solution, considering the states change, get_successors function and safe function(used to check if the state is legal) need to be changed. 
For get_successors function, based on original 10 states, in the state which number of cannibals exceeds number of missionaries, the current number of missionaries has to subtract E if current number of missionaries is not less than E. If current number of missionaries is less than E, change current number of missionaries as 0.
For safe function, which is used to judge if the state is legal. In my understanding, after eating E missionaries, cannibals are full and they cannot eat missionaries any more. As a result, for this problem, there is no illegal state. All states are legal.
*The total number of possible states for this problem:*
(M+1) * (C+1) * (E+1) * (B+1)
