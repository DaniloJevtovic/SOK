class TreeNode():
    def __init__(self, object, parent = None, children = None):
        self.object = object
        self.parent = parent
        if children is None:
            self.children = []
        else:
            self.children = children

    def __str__(self):
        if self.object is None:
            return "None"
        return str(self.object)

