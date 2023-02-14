class TextEditor(object):
    def __init__(self):
        self.cursor = 0
        self.s = ""

    def addText(self, text):
        self.s = self.s[:self.cursor] + text + self.s[self.cursor:]
        self.cursor += len(text)

    def deleteText(self, k):
        new_cursor = max(0, self.cursor - k)
        if self.cursor - k >= 0:
            num_of_chars = k
        else:
            num_of_chars = self.cursor
        self.s = self.s[:new_cursor] + self.s[self.cursor:]
        self.cursor = new_cursor
        return num_of_chars

    def cursorLeft(self, k):
        self.cursor = max(0, self.cursor - k)
        start = max(0, self.cursor - 10)
        return self.s[start:self.cursor]

    def cursorRight(self, k):
        self.cursor = min(len(self.s), self.cursor + k)
        start = max(0, self.cursor - 10)
        return self.s[start:self.cursor]