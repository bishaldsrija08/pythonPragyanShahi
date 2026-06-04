import pandas as pd

print(pd.__version__)

mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}

mydata = pd.DataFrame(mydataset)
print(mydata)