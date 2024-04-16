#  File: Josephus.py
#  Student Name: Akwawo Ekpu
#  Student UT EID: ace2453

import sys


# This class represents one soldier.
class Link(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None


    # Is the list empty
    def is_empty(self):
        return self.first is None



    # Append an item at the end of the list
    def insert(self, data):
        pass

        linker = Link(data)

        if self.is_empty():
            self.first = linker
            self.last = linker
            linker.next = linker

        else:
            linker.next = self.first
            self.last.next = linker
            self.last = linker
           


    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        pass
        if self.is_empty():
            return None

        current = self.first

        while True:
            if current.data == data:
                return current

            current = current.next

            if current == self.first:
                break

        return None


        

    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data):
        pass
        if self.is_empty():
            return None

        past = None
        current = self.first

        
        while True:
            if current.data == data:
                
                if past:
                    past.next = current.next
                    
                    if current == self.last:
                        self.last = past
                        
                else:
                    self.first = current.next
                    
                    if current == self.last:
                        self.last = None

                current.next = None

                return current

            past = current
            current = current.next

            if current == self.first:
                break

        return None



    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after(self, start, step):
        pass
        if self.is_empty():
            return None, None

        current = self.find(start.data)
        if current is None:
            return None, None

    
        past_node = None
        for _ in range(step - 1):
            past_node = current
            current = current.next
            if current is None:
                current = self.first


        deleted = current
        if past_node is not None:
            past_node.next = current.next
        else:
            self.first = current.next

        
        if deleted == self.last:
            self.last = past_node

     
        return deleted.data, current.next


    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        pass
        if self.is_empty():
            return "[]"

        str_list = "["
        current = self.first

        while True:
            str_list += str(current.data)
            current = current.next

            if current == self.first:
                break

            str_list += ", "

        str_list += "]"

        return str_list



# Input: Number of soldiers
# Outupt: Circular list with one link for each soldier
#         Data for first soldier is 1, etc.
def create_circular_list(num_soldiers):
    pass
    my_list = CircularList()
    for i in range(1, num_soldiers + 1):
        my_list.insert(i)
    return my_list
    



# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count):
    pass
    start_node = my_list.find(start_data)
    if start_node is None:
        print("Start node not found in the list.")
        return

    dead_soldiers = []  

    for _ in range(num_soldiers - 1):
        dead, start_node = my_list.delete_after(start_node, step_count)
        if start_node is None:
            print("Invalid step count.")
            break
        dead_soldiers.append(dead)  

    
    for soldier in dead_soldiers:
        print(soldier)

    
    if start_node:
        print(start_node.data)
    


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('josephus.in')
        # in_data = open('autograde/test_cases/input_4.txt')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create cirular list
    my_list = create_circular_list(num_soldiers)

    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)


if __name__ == "__main__":
    main()
