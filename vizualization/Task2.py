#Хто частіше повідомляє про вживання алкоголю – чоловіки чи жінки?

import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

sns.set()
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker

sns.set_context(
    "notebook", font_scale=1.5, rc={"figure.figsize": (11, 8), "axes.titlesize": 18}
)

from matplotlib import rcParams

rcParams["figure.figsize"] = 11, 8

df = pd.read_csv('vizualization/mlbootcamp5_train.csv')

