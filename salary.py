import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from statsmodels.formula.api import ols


def salary_prediction(experience):

    df = pd.read_csv('Salary_dataset.csv')

    ols_formula = "salary ~ yoe"

    ols_data = df

    model = ols(formula=ols_formula, data=ols_data).fit()

    pred = model.predict(pd.DataFrame({'yoe' : [experience]})).to_numpy()[0]

    return pred

