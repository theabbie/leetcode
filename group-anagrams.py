import hashlib
import pickle

def hash(obj):
    serialized_obj = pickle.dumps(obj)
    hash_object = hashlib.md5()
    hash_object.update(serialized_obj)
    md5_hash = hash_object.hexdigest()
    return md5_hash

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            h = hash(sorted(s))
            if h not in res:
                res[h] = []
            res[h].append(s)
        return res.values()