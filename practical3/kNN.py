import numpy as np
import pandas as pd

class KNN:
    def __init__(self):
        pass
    
    def fit(self, dict):
        self.dict = dict
    
    def predict(self, testData):
        predictions = []
        for test in testData:
            artist = [test[0]]
            country = [test[1]]
            sex = [test[2]]
            age = [test[3]]

            if artist[0] not in self.dict:
                artist = self.dict.keys()
            if country[0] not in self.dict[artist[0]]:
                country = self.dict[artist[0]].keys()
            if sex[0] not in self.dict[artist[0]][country[0]]:
                sex = self.dict[artist[0]][country[0]].keys()
            if age[0] not in self.dict[artist[0]][country[0]][sex[0]]:
                age = self._findClosestAge(age[0], self.dict[artist[0]][country[0]][sex[0]])
                
            plays = []
            for a in artist:
                for c in country:
                    for s in sex:
                        for ag in age:
                            try:
                                p = self.dict[a][c][s][ag]
                            except KeyError:
                                    continue
                            for e in p:
                                plays.append(e)
            predictions.append(1.0 * sum(plays) / len(plays))
        return predictions
    
    def _findClosestAge(self, target, d):
        ages = d.keys()
        min_v = ages[0]
        for val in ages:
            if abs(target - val) < abs(target - min_v):
                min_v = val
        return [min_v]