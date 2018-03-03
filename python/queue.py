import Queue
import collections

def breadth_first_search(root_node, fn):
    # Returns the first node for which fn(node) is truthy
    queue = collections.deque([root_node]) # Python queue object
    while len(queue) > 0:
        node = queue.popleft() # Grab the first element in queue
        print node.value
        if fn(node.value):
            return node
        else:
            # (Fill in the missing line here)
            queue.extend(node.children)
        print queue
    return None


class Node(object):
	def __init__(self, data):
		self.value = data
		self.children = []

	def add_child(self, obj):
		self.children.append(obj)

def fn(node_value):
    return node_value is "seven"

root = Node("one")
node2 = Node("two")
node3 = Node("three")
node4 = Node("four")
node5 = Node("five")
node6 = Node("six")
node7 = Node("seven")
node8 = Node("eight")

#L = [node2,node3,node4,node5,node6]
#for l in L:
#	root.add_child(l)

root.add_child(node2)
root.add_child(node3)
node2.add_child(node4)
node2.add_child(node5)
node4.add_child(node6)
node4.add_child(node7)
node4.add_child(node8)

print breadth_first_search(root, fn) #success

