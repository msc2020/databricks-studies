import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import seaborn as sns
import numpy as np
import pandas as pd


def plot_correlation_matrix(corr: pd.DataFrame):
    # plot heatmap
    plt.figure(figsize=(20, 8), dpi=90)
    sns.heatmap(
        corr,
        cmap='coolwarm',
        annot=False,
        linewidths=0.5
    )

    plt.title('Corrrelation Map (Phik)')
    plt.show()

