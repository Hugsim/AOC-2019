import typing
from lib import *


class Node:
    def __init__(self, name: str):
        self.name = name
        self.parent = None
        self.distanceToCentre = 0
        self.children: [Node] = []

    def __str__(self):
        if len(self.children) > 0:
            emptyString = ""
            return f"{self.name} \n {f'|-- {mapList(lambda node: str(node), self.children)}, {self.parent.name if self.parent is not None else emptyString}'}"
        else:
            return f"{self.name}, {self.parent.name if self.parent is not None else ''}"

    def updateDistance(self):
        if self.parent is not None:
            self.distanceToCentre = self.parent.distanceToCentre + 1
        for node in self.children:
            node.updateDistance()


class Tree:
    def __init__(self):
        self.nodes = {}

    def addNode(self, node: Node, parent: Node):
        self.nodes[node.name] = node
        node.parent = parent
        if parent is not None:
            parent.children.append(node)
        node.distanceToCentre += 1

    def hasNode(self, nodeName: str):
        return nodeName in self.nodes.keys()

    def getNode(self, nodeName: str):
        return self.nodes[nodeName]


data: [str] = mapList(lambda x: tuple(x.strip().split(")")),
                      fileIntoArray("data6.txt"))

tree = Tree()

for (centre, orbiter) in data:
    if not tree.hasNode(centre):
        tree.addNode(Node(centre), None)
    if not tree.hasNode(orbiter):
        tree.addNode(Node(orbiter), tree.getNode(centre))


for name, node in tree.nodes.items():
    node.updateDistance()

for name, node in tree.nodes.items():
    print(f"{str(node)} -> {node.distanceToCentre}")

print(sum(map(lambda node: node.distanceToCentre, tree.nodes.values()
              )))
