class Stack:
    
    def __init__(self):
        self.stack=[]


    def push(self,val):
        return self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if not self.stack:
            return True
        else:
            return False

    def size(self):
        return len(self.stack)
    
    def get_Stack(self):
        return self.stack


st = Stack()

st.push(2)
st.push(4)
st.push(10)
print(st.get_Stack())

print("Size of Stack:",st.size())

print("The popped element",st.pop())
print(st.get_Stack())

print("The top element",st.peek())

st.pop()
st.pop()
print(st.get_Stack())
print("Is the stack empty:",st.is_empty())



