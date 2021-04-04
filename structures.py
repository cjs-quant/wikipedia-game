
# FILE: structures.py
# AUTHOR: Christopher Simard
# DESCRIPTION: defines the tree class used to store wikipedia game solution

class Tree(object):
    def __init__(self, name, level=0, children=None, parent=None):
        self.name = name
        self.parent = parent
        self.children = children or []
        self.level = level

    def __repr__(self):
        return self.name

    # add child
    def add_child(self, name):
        new_child = Tree(name, level=self.level+1, parent=self)
        self.children.append(new_child)

    # returns path to root
    def get_path(self):
        path = []
        temp = self
        name_temp = temp.name
        path.append(name_temp)
        i = 1
        while name_temp != []:
            temp = temp.parent
            if temp is None:
                break
            name_temp = temp.name
            path.append(name_temp)
        return path

    # returns all nodes in level
    def get_level_nodes(self, level=1):
        if self.level > level:
            return
        if self.level == level:
            yield self
        else:
            for c in self.children:
                for n in c.get_level_nodes(level):
                    yield n
