#this is scartch code for hw 4 to brute force runs and extract by no means is this complete needs total overhaul and refactor to match design pattern this is a todo
#not part of the assignment or class but just needed something to brute force run and extract 
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def run():
    columns = ["NUMUORS"
        , "NUMUANDS"
        , "TOTOTORS"
        , "TOTOPANDS"
        , "VG"
        , "NLOGIC"
        , "LOC"
        , "ELOC"
        , "FAULTS"]
    p = np.arange(0.00, 1.05, 0.05)
    lis = os.listdir()
    files = [i for i in os.listdir() if i[-3:] == 'txt']

    for i in files:
        name = i.split(".")[0]
        train = pd.read_csv(i, header=None)
        train.columns = columns
        for j in ['m5', 'greedy']:
            filename = "{0}_{1}.xlsx".format(name, j)
            if j == 'm5':
                train[
                    "PRED"] = - 0.0516 * train.NUMUORS + 0.0341 * train.NUMUANDS - 0.0027 * train.TOTOTORS - 0.0372 * train.VG + 0.2119 * train.NLOGIC + 0.0018 * train.LOC + 0.005 * train.ELOC - 0.3091
                train.loc[train["PRED"] <= 0, "PRED"] = 0
            else:
                train[
                    "PRED"] = - 0.0482 * train.NUMUORS + 0.0336 * train.NUMUANDS - 0.0021 * train.TOTOTORS - 0.0337 * train.VG + 0.2088 * train.NLOGIC + 0.0019 * train.LOC - 0.3255
                train.loc[train["PRED"] <= 0, "PRED"] = 0
            calc_df = pd.DataFrame(index=p)
            faults = train[['FAULTS', 'PRED']]
            faults = faults.sort_values(by="FAULTS", ascending=False)
            faults["Perfect_Percentile"] = 1 - np.arange(1, len(faults) + 1) / len(faults)
            faults = faults.sort_values(by="PRED", ascending=False)
            faults["Predicted_Percentile"] = 1 - np.arange(1, len(faults) + 1) / len(faults)
            faults.sort_values(by="Perfect_Percentile")
            for k in calc_df.index:
                calc_df.loc[k, "Gc"] = faults.loc[faults["Perfect_Percentile"] >= k, "FAULTS"].sum()
                calc_df.loc[k, "Gcp"] = faults.loc[faults["Predicted_Percentile"] >= k, "FAULTS"].sum()
                calc_df["Gc_Gtot"] = calc_df.Gc / faults["FAULTS"].sum()
                calc_df["Gcp_Gtot"] = calc_df.Gcp / faults["FAULTS"].sum()
                calc_df["theta"] = calc_df.Gcp_Gtot / calc_df.Gc_Gtot
                calc_df['modules_perc'] = 1 - calc_df.index
                calc_df = calc_df.sort_index(ascending=True)
            calc_df.to_excel(filename, index_label=False)
if __name__ == '__main__':
    run()