N = int(input())
dic = {}
for _ in range(N):
    node, left, right = input().split()
    dic[node] = [left, right]

def preorder(current_node):
    if current_node != '.':
        print(current_node, end='')
        preorder(dic[current_node][0])
        preorder(dic[current_node][1])

def inorder(current_node):
    if current_node != '.':
        inorder(dic[current_node][0])
        print(current_node, end='')
        inorder(dic[current_node][1])

def postorder(current_node):
    if current_node != '.':
        postorder(dic[current_node][0])
        postorder(dic[current_node][1])
        print(current_node, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
