#test stack
import Stack2

newStack = Stack2.Stack2()
#add 4,5,6,1,34,5,6
#how do you produce the list using stack (6 should be at the bottom)
newStack.push(4)
newStack.push(5)
print(newStack.is_empty())
print(newStack.peek())
print(newStack.size())
print(newStack.pop())
print(newStack.size())
