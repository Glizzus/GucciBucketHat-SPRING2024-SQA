import datetime
import random
import tempfile
from empirical.report import Average
from empirical.frequency import getAllSLOC
from mining.mining import checkPythonFile, cloneRepo, days_between


naughty_strings = []
naughty_path = __file__ + '/../naughty.txt'
for line in open(naughty_path, 'r', encoding='utf-8'):
    if line.startswith('#'):
        continue
    naughty_strings.append(line)


def fuzzAverage():
    for _ in range(100000):
        num = random.randint(0, 100)
        values = [random.randint(0, 100) for _ in range(num)]
        Average(values)


def fuzzCloneRepo():
    for string in naughty_strings[:5]:
        tempdir = tempfile.mkdtemp()
        cloneRepo(string, tempdir)


def fuzzCheckPythonFile():
    for string in naughty_strings[45:50]:
        tempdir = tempfile.mkdtemp()
        checkPythonFile(tempdir + '/' + string)


def fuzzDaysBetween():
    for _ in range(100000):
        start = datetime.datetime.now()
        end = datetime.datetime.now() + datetime.timedelta(days=random.randint(0, 1000))
        days_between(start, end)


def fuzzGetAllSLOC():
    for string in naughty_strings[5:10]:
        tempdir = tempfile.mkdtemp()
        getAllSLOC(string, tempdir)
        
funcs = [
    fuzzAverage,
    fuzzCloneRepo,
    fuzzCheckPythonFile,
    fuzzDaysBetween,
    fuzzGetAllSLOC
]

for func in funcs:
    try:
        func()
    except Exception as e:
        print('Error in function:', func.__name__)
        print(e)
