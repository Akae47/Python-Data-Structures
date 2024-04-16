#  File: password.py
#  Description: Rotates a linked list to the left (counter-clockwise)
#  Student Name: Akwawo 
#  Student UT EID: ace2453
#  Course Name: CS 313E


import sys


class Link (object):
    # do not change this constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList (object):
    # create a linked list -- do not change this constructor
    def __init__(self):
        self.first = None

    # helper function to add an item at the end of a list
    # you can use this if you want, but do not delete it
    def insert_last(self, data):
        newLink = Link(data)
        current = self.first

        if current is None:
            self.first = newLink
            return

        while current.next is not None:
            current = current.next

        current.next = newLink

    # helper function to copy the contents of the current linked list
    # returns new linked list
    # you can use this if you want, but do not delete it
    def copy_list(self):
        new_list = LinkedList()
        curr = self.first
        while curr:
            new_list.insert_last(curr.data)
            curr = curr.next
        return new_list

    # helper function to count number of links
    # returns number of links
    # you can use this if you want, but do not delete it
    def num_links(self):
        curr = self.first
        res = 0
        while curr:
            res += 1
            curr = curr.next
        return res

    # string representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        curr_items = []
        curr = self.first
        res = ""
        while curr:
            curr_items.append(curr.data)
            if len(curr_items) == 10:
                res += "  ".join(map(str, curr_items)) + "\n"
                curr_items = []
            curr = curr.next
        # print the remaining items
        if len(curr_items):
            res += "  ".join(map(str, curr_items))
        return res

    def delete_link(self, data):
        previous = self.first
        current = self.first

        if current is None:
            return None

        while current.data is not data:
            if current.next is None:
                return None
            else:
                previous = current
                current = current.next

        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next

        return current
    
    # COMPLETE THIS FUNCTION
    # return a new linked list that results from the rotation
    # do not change this linked list


    def rotate(self, r_step, times):
        length = self.num_links()
        step = r_step % length

        old_password = str(self)

        for _ in range(times):
            current = self.first

            while current.next:
                current = current.next

            current.next = self.first
            self.first = self.first.next
            current.next.next = None

            for _ in range(step - 1):
                current = current.next

            current.next = self.first
            self.first = self.first.next
            current.next.next = None

        new_password = str(self)

        return old_password + "\n" + new_password

        # DO NOT CHANGE MAIN


def main():

    # open file
    debug = False
    if debug:
        in_data = open('password.in')
    else:
        in_data = sys.stdin

    ll = LinkedList()
    data = list(map(int, in_data.readline().split()))

    # populate linked list with data
    for d in data:
        ll.insert_last(d)

    step, count = list(map(int, in_data.readline().split()))

    rotated = ll.rotate(step, count)
    # print the original list
    print(ll)
    # print the new list that results from calling rotate()
    print(rotated)


if __name__ == "__main__":
    main()
