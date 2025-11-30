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

    def plot_bar(self, column, title, xlabel, colors=None, mapping=None, as_percentage=False):
        """
        Ritar stapeldiagram över vald kolum.
        Kan hantera namnbyte och procent.
        """
        if as_percentage:
            counts = self.df[column].value_counts(normalize=True).round(4) * 100
            ylabel = "Andel (%)"
        else:
            counts = self.df[column].value_counts()
            ylabel = "Antal deltagare"

        if mapping:
            counts = counts.rename(index=mapping)

        fig, ax = plt.subplots(figsize=(9, 7))
        ax.bar(counts.index, counts.values, color=colors)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        return fig 
    
    def calc_confidence_interval(self, column, n_boot=5000, confidence=0.95):
        """
        Beräknar konfidensintervall med Bootstrap-metoden för en given kolumn    
        """
        data = self.df[column]
        n = len(data)
        boot_means = np.empty(n_boot)

        for b in range(n_boot):
            boot_sample = np.random.choice(data, size=n, replace=True)
            boot_means[b] = np.mean(boot_sample)

        lower_p = ((1.0 - confidence) / 2.0) * 100
        upper_p = (confidence + ((1.0 - confidence) / 2.0)) * 100

        ci_min = np.percentile(boot_means, lower_p)
        ci_max = np.percentile(boot_means, upper_p)

        return ci_min, ci_max