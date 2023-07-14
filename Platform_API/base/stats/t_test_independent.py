import os
import django
from scipy import stats
import numpy as np
import pandas as pd
from django_pandas.io import read_frame

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platform_API.settings')  # replace 'myproject' with your actual project name
django.setup()

from base.models import ReactionTime

# Load data from Django model into DataFrame
qs = ReactionTime.objects.all()
df = read_frame(qs)

# Create two groups
group_cs = df[df['game'] == 'cs']['rt']
group_lol = df[df['game'] == 'lol']['rt']
print(group_cs)
# Perform t-test
t_stat, p_val = stats.ttest_ind(group_cs, group_lol)

print("t-statistic:", t_stat)
print("p-value:", p_val)
