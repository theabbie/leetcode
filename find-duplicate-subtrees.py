from collections import defaultdict
import hashlib
import pickle

def hash(obj):
    serialized_obj = pickle.dumps(obj)
    hash_object = hashlib.md5()
    hash_object.update(serialized_obj)
    md5_hash = hash_object.hexdigest()
    return md5_hash

class Solution:
    def postorder(self, root, trees):
        s = "#"
        if root:
            s = f"{root.val},{self.postorder(root.left, trees)},{self.postorder(root.right, trees)}"
            trees[hash(s)].append(root)
        return s
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        trees = defaultdict(list)
        self.postorder(root, trees)
        return [trees[s][0] for s in trees if len(trees[s]) > 1]