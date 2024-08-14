# Implement a mock of cd (change directory) command on Unix. The code doesn't have to change actual directories,
# just return the new path after cd was executed.
# The function takes two arguments (current working directory and directory to change to), and return the output directory
# as if cd command was executed. There's no filesystem underneath; all path are valid
# Examples
# | cwd     | cd (arg)  | output
# | /           | foo          |/foo
# |/baz      |/bar          |/bar
# |/foo/bar |../../../../..  |/
# |/x/y       |../p/../q      |/x/q
# |/x/y       |/p/./q         |/p/q

class Solution(object):
    def changeWorkingDirectory(self, cwd, cd):
        if cd[0] == "/":
            cwd = ""
        stack = filter(lambda x: x.strip(), cwd.split('/'))
        op = filter(lambda x: x.strip(), cd.split('/'))
        for o in op:
            if o == '.':
                continue
            elif o =='..':
                if stack:
                    stack.pop()
            else:
                stack.append(o)
        return '/' + '/'.join(stack)

test = Solution()
print test.changeWorkingDirectory('/', 'foo')
print test.changeWorkingDirectory('/baz', '/bar')
print test.changeWorkingDirectory('/foo/bar', '../../../../..')
print test.changeWorkingDirectory('/x/y', '../p/../q')
print test.changeWorkingDirectory('/x/y', '/p/./q')