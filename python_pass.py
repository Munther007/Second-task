class StringOperations:
    def __init__(self, to_be_reversed):
      self.to_be_reversed = to_be_reversed

    def reverse(self):
        return self.to_be_reversed[::-1]
        raise NotImplemented(
'This is the method need to be implemented')

class ReveredString(StringOperations):
    def __init__(self):
        word = input("Enter any word to reverse it : ")
        StringOperations.__init__(self, word)

ReverseWord = ReveredString()
print(ReverseWord.reverse())


