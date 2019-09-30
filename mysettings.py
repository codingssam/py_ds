import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

np.set_printoptions(precision=4, suppress=True)

pd.options.display.max_rows = 15
pd.options.display.precision=4

mpl.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["font.size"] = 9

%matplotlib inline