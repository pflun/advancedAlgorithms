# -*- coding: utf-8 -*-
# https://leetcode.com/problems/dinner-plate-stacks/discuss/366331/C%2B%2BPython-Two-Solutions
# 这个heap里会存重复的available index，但是会在L18 - L20清理掉满了/不符合的index
import heapq
class DinnerPlates:
    def __init__(self, capacity):
        self.c = capacity
        self.q = [] # record the available stack, will use heap to quickly find the smallest available stack
        # if you are Java or C++ users, tree map is another good option.
        self.stacks = [] # record values of all stack of plates, its last nonempty stack are the rightmost position

    def push(self, val):
        # To push, we need to find the leftmost available position
        # first, let's remove any stacks on the left that are full
        # 1) self.q: if there is still available stack to insert plate
        # 2) self.q[0] < len(self.stacks): the leftmost available index self.q[0] is smaller than the current size of the stacks
        # 3) len(self.stacks[self.q[0]]) == self.c: the stack has reached full capacity
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.c:
            # we remove the filled stack from the queue of available stacks
            heapq.heappop(self.q)

        # now we reach the leftmost available stack to insert

        # if the q is empty, meaning there are no more available stacks
        if not self.q:
            # open up a new stack to insert
            heapq.heappush(self.q, len(self.stacks))

        # for the newly added stack, add a new stack to self.stacks accordingly
        if self.q[0] == len(self.stacks):
            self.stacks.append([])

        # append the value to the leftmost available stack
        self.stacks[self.q[0]].append(val)

    def pop(self):
        # To pop, we need to find the rightmost nonempty stack
        # 1) stacks is not empty (self.stacks) and
        # 2) the last stack is empty
        while self.stacks and not self.stacks[-1]:
            # we throw away the last empty stack, because we can't pop from it
            self.stacks.pop()

        # now we reach the rightmost nonempty stack

        # we pop the plate from the last nonempty stack of self.stacks by using popAtStack function
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        # To pop from an stack of given index, we need to make sure that it is not empty
        # 1) the index for inserting is valid and，
        # 2) the stack of interest is not empty
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            # we add the index into the available stack
            heapq.heappush(self.q, index)
            # take the top plate, pop it and return its value
            return self.stacks[index].pop(), self.q, len(self.stacks)

        # otherwise, return -1 because we can't pop any plate
        return -1

test = DinnerPlates(2)
print test.push(1)
print test.push(2)
print test.push(3)
print test.popAtStack(1)
print test.push(4)
print test.push(5)
print test.push(6)
print test.popAtStack(1)