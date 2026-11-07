# Day 21 - Level 1

class Statistics():
    def __init__(self, ages):
        self.ages = sorted(ages)
    def count(self):
        return len(self.ages)
    
    def sum(self):
        return sum(self.ages)
    
    def min(self):
        return min(self.ages)
    
    def max(self):
        return max(self.ages)
    
    def range(self):
        return self.ages[-1] - self.ages[0]

    def mean(self):
        return self.sum()/self.count()

    def median(self):
        return self.ages[self.count()//2]

    def mode(self):
        mode_dict = dict()
        for a in self.ages:
            if a in mode_dict.keys():
                mode_dict[a] += 1
            else:
                mode_dict[a] = 1
        return [(x[0], x[1]) for x in sorted(mode_dict.items(), key=lambda x: x[1], reverse=True)][0]

    def var(self):
        result = 0
        for a in ages:
            result += ((a-self.mean())/self.count())
        return result

    def std(self):
        return self.var() ** 0.5

    def freq_dist(self):
        freq_dict = dict()
        for a in ages:
            if a in freq_dict.keys():
                freq_dict[a] += 100/self.count()
            else:
                freq_dict[a] = 100/self.count()
        return [(x[1], x[0]) for x in sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)]
            


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Variance: ', data.var()) # 17.5
print('Standard Deviation: ', data.std()) # 4.2
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
