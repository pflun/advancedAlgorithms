# https://leetcode.com/discuss/post/770704/amazon-onsite-text-editor-by-anonymous_u-4jov/
# Implement Text Editor Undo Redo
# We aim to implement rudimentary undo & redo.
# You will be provided a set of actions to perform. Once all actions are performed you will return the current state the system should be in after all actions in actions are performed.
# We will be operating on characters and the "state" of the system will be a string that we are building.
# These are the actions possible:
# INSERT: Inserts a single character to the end of the string
# DELETE: Removes the last character in the string
# UNDO: Reverses the most recent action
# REDO: Redoes the most recent action undone
# Your inputs will only be single characters. There are only 4 input actions as enumerated above.
# Example 1:
# Input:
# INSERT 'a'
# INSERT 'b'
# Output: "ab"
# Example 2:
# Input:
# INSERT 'a'
# INSERT 'b'
# UNDO
# Output: "a"
# Example 3:
# Input:
# INSERT 'a'
# INSERT 'b'
# UNDO
# REDO
# Output: "ab"
# Example 4:
# Input:
# INSERT 'a'
# INSERT 'b'
# UNDO
# REDO
# REDO # Does nothing
# Output: "ab"

class Solution(object):
    # String[][] actions
    def performEditorActions(self, actions):
        self.res = ''
        self.undo = []
        self.redo = []
        for a in actions:
            if a[0] == 'INSERT':
                self.insert(a)
            elif a[0] == 'DELETE':
                self.delete(a)
            elif a[0] == 'UNDO':
                if self.undo:
                    last = self.undo.pop()
                    self.redo.append(last)
                    if last[0] == 'DELETE':
                        self.insert(last)
                    elif last[0] == 'INSERT':
                        self.delete(last)
            elif a[0] == 'REDO':
                if self.redo:
                    last = self.redo.pop()
                    self.undo.append(last)
                    if last[0] == 'INSERT':
                        self.insert(last)
                    elif last[0] == 'DELETE':
                        self.delete(last)
        return self.res

    def insert(self, a):
        self.res += a[1]
        self.undo.append(a)

    def delete(self, a):
        if self.res == '':
            self.undo.append(a)
        else:
            self.res = self.res[:-1]
            self.undo.append(a)

test = Solution()
print test.performEditorActions([['INSERT', 'a'], ['INSERT', 'b'], ['UNDO', ''], ['REDO', ''], ['REDO', '']])