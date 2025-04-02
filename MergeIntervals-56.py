class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        map = [0] * 20001

        for interval in intervals:
            for i in range(interval[0], interval[1]):
                map[2*i] = 1
                map[2*i+1] = 1
            map[2*interval[1]] = 1
        
        merged_intervals = []
        if map[0] == 1:
            start = 0
        for i in range(1, 20001):
            if map[i] == 1 and map[i-1] == 0:
                start = i/2
            elif map[i] == 0 and map[i-1] == 1:
                merged_intervals.append([start, (i-1)/2])
        if map[20000] == 1:
            merged_intervals.append([start, 10000])
        
        return merged_intervals
