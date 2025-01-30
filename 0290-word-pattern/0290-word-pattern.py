class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.strip().split(" ")
        if len(words) != len(pattern): return False
        p_dict = {}
        pi = 0
        for word in words:
            if word in p_dict:
                if pattern[pi] != p_dict[word]:
                    return False
            else:
                if pattern[pi] in p_dict.values():
                    return False
                p_dict[word] = pattern[pi]
            pi+=1
        return True