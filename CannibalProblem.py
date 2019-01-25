# Created by Ningxiang He on 01/08/2019

class CannibalProblem:

    '''
    _init_ declare basic information to the problem
         Args:
              start_state
    '''
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        self.M = start_state[0]
        self.C = start_state[1]
        self.B = start_state[2]

    # get successor states for the given state
    '''
    For given state, find all the legal new state.
        Args:state
        return:a list of states
    '''
    def get_successors(self, state):
        i=state[0] # get current number of missionaries
        j=state[1] # get current number of cannibals
        k=state[2] # get current number of boats
        return_state = [] # create a list to put all the legal states
        if(k==0): # first consider situation that boat number = 0
            next_state=[(i+1,j,1),(i,j+1,1),(i+1,j+1,1),(i+2,j,1),(i,j+2,1)] # put all possible new states in next_state
            for a in next_state:
                if self.safe(a): # use safe function to check if the state is legal
                    return_state.append(a) # if legal,put state into return_state list
        else: # consider situation that boat number is 1
            next_state=[(i,j-2,0),(i-1,j-1,0),(i-2,j,0),(i-1,j,0),(i,j-1,0)] # put all possible new states in next_state
            for b in next_state:
                if(self.safe(b)): # use safe function to check if the state is legal
                    return_state.append(b) # if legal, put legal state into return_state list.
        return return_state # return the list of legal state



    '''
    safe function check if the state is legal or not
        Args: state
        returns: true or false
    '''
    def safe(self,state):
        M = self.M # M represents total number of missionaries
        C = self.C # C represents total number of cannibals
        m = state[0] # m represents current number of missionaries in one side
        c = state[1] # c represents current number of cannibals in one side
        if m>M or m<0 or c>C or c<0 or (m!=0 and m<c) or (m!=M and (M-m)< (C-c)):
            # judge if the state id legal
            # (m!=0 and m<c)represents the situation that there are more cannibals than missionaries on one side,
            # (M-m)<(C-c) represents the situation that there are more cannibals than missionaries on the other side
            return False
        else:
            return True



    '''
    goal_test check if the state is goal_state
        Args: state
        returns: True or False
    '''
    def goal_test(self,state):
        if state[0]==0 and state[1]==0 and state[2]==0: # judge if the number of missionaries and cannibals are 0
            return True
        else:
            return False

    def __str__(self):
        string =  "Missionaries and cannibals problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = CannibalProblem((3, 3, 1))
    print(test_cp.get_successors((3, 3, 1)))
    print(test_cp)
