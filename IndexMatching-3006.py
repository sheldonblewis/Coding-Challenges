class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # find instances of a in s
        beautiful_indices = []

        pis = []
        for pi in range(len(s)-len(a)+1):
            if s[pi:pi+len(a)] == a:
                pis.append(pi)

        # find instances of b in s
        pjs = []
        for pj in range(len(s)-len(b)+1):
            if s[pj:pj+len(b)] == b:
                pjs.append(pj)

        # for each instance of a, check if there's a b in range
        if len(pis) == 0:
            return []
        else:
            if pis[0] - k <= 0:
                start = 0
            else:
                start = pis[0] - k
            for i in pis:
                if start < i - k:
                    if i - k >= 0:
                        start = i - k
                    else:
                        start = 0
                
                if i + k >= len(s):
                    end = len(s)
                else:
                    end = i + k + 1
                
                found = False
                for j in range(start, end):
                    if j in pjs:
                        beautiful_indices.append(i)
                        found = True
                        start = j
                        break

                if not found:
                    start = end
        
        return beautiful_indices
