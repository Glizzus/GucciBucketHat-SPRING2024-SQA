import random
from empirical.report import Average

def fuzzAverage():
    for _ in range(100000):
        num = random.randint(0, 100)
        values = [random.randint(0, 100) for _ in range(num)]
        Average(values)


fuzzAverage()