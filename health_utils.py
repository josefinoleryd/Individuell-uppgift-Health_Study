import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sc

def load_and_prep_data(filepath):
    """
    Läser in datan från en CSV-fil och ändrar datatyper
    """
    df = pd.read_csv(filepath)

    df["smoker"] = df["smoker"].astype("category")
    df["sex"] = df["sex"].astype("category")

    return df

class HealthAnalyzer:
    def __init__(self, df):
        self.df = df.copy()

    def get_stats(self, columns):
        """Beräknar min, max, medel och median för valda kolumner"""
        stats = (
            self.df[columns]
            .describe()
            .round(1)
            .loc[["min", "max", "mean", "50%"]]
            .rename(index={"50%": "median"})
        )
        return stats
    
    def plot_hist(self, column, title, xlabel, bins=15):
        """Ritar histogram över vald kolum"""
        fig, ax = plt.subplots(figsize=(9, 7))
        ax.hist(self.df[column], bins=bins, edgecolor="black")
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel("Antal deltagare")
        ax.grid(axis="y", alpha=0.5)
        return fig

    def plot_bar(self, column, title, xlabel, colors=None):
        """Ritar stapeldiagram över vald kolum"""
        counts = self.df[column].value_counts()
        fig, ax = plt.subplots(figsize=(9, 7))
        ax.bar(counts.index, counts.values, color=colors)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel("Antal deltagare")
        return fig 