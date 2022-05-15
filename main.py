import datetime

from twarc.client2 import Twarc2
from twarc.expansions import ensure_flattened

import pandas as pd

data = pd.read_csv('tweets.csv', low_memory=False)

print(data.columns)
# print(type(data))

# print(data.shape())
