class TrieNode:
    def __init__(self):
        self.children = {}
        self.duplicate = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]

        serial_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            items = []
            for name in sorted(node.children):
                child_serial = serialize(node.children[name])
                items.append(f"({name}{child_serial})")
            serial = ''.join(items)
            serial_map[serial].append(node)
            return serial

        serialize(root)

        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.duplicate = True

        res = []

        def collect(node, path):
            for name, child in node.children.items():
                if not child.duplicate:
                    new_path = path + [name]
                    res.append(new_path)
                    collect(child, new_path)

        collect(root, [])
        return res