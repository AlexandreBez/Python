from collections import deque

deq = deque('arduino')
print(deq)

deq.append('u')
deq.append('n')
deq.append('o')
deq.appendleft('1')
print(deq)

print(deq.pop())
print(deq.popleft())
