

class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str
        #you may add data structures to improve the search
        self.state_list = self.state_str.split(',')
        self.states_integers = [int(x) for x in self.state_list]

    def list_reverse(self, lst, start, end):
        while start < end:
            temp = lst[start]
            lst[start] = lst[end]
            lst[end] = temp
            start += 1
            end -= 1
        return lst

    #returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1), (pancake _state2, cost2)...]
    def get_neighbors(self):
        neighbors_state_list = []  #new list for tuples
        pancake_amount = len(self.state_list)  #length of the given pancakes list
        current_sum = self.states_integers[pancake_amount-1]  #value of the pancake on the top
        current_list = self.states_integers.copy()  #copy of the beginning state
        for i in range(pancake_amount-2, -1, -1):  #loop from the top of the pancakes
            current_sum += current_list[i]  #adding next pancake
            new_state = self.list_reverse(current_list, i, pancake_amount-1)  #pancake heap after flip
            new_state_string = [str(x) for x in new_state]  #converting from int to str
            new_state_list_to_string = ','.join(new_state_string)  #converting from list to string
            new_pancake_state = pancake_state(new_state_list_to_string)  #initializing new pancake_state
            #print(new_pancake_state.get_state_str())
            current_tuple = (new_pancake_state, current_sum)  #creating tuple that contains the pancake_state and the cost
            current_list = self.states_integers.copy()  # copy of the beginning state
            neighbors_state_list.append(current_tuple)  #adding the state to the list
        return neighbors_state_list



    #you can change the body of the function if you want
    def __hash__(self):
        return hash(self.state_str)

    #you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str

    def get_state_str(self):
        return self.state_str
