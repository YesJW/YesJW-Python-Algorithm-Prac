stack = []
stack.aapend(5) # 5 2 3 7 삭제 1 4 삭제
stack.aapend(2)
stack.aapend(3)
stack.aapend(7)
stack.pop()
stack.aapend(1)
stack.aapend(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력