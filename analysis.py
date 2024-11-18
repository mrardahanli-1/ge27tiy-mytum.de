import pandas as pd
import numpy as np

def principal_strain_max(eps_a: pd.Series, eps_b: pd.Series, eps_c: pd.Series) -> pd.Series:
    eps_max = (eps_a + eps_c) / 2 + np.sqrt(((eps_a - eps_c) / 2) ** 2 + eps_b ** 2)
    return pd.Series(eps_max, name="eps_max")

def principal_strain_min(eps_a: pd.Series, eps_b: pd.Series, eps_c: pd.Series) -> pd.Series:
    eps_min = (eps_a + eps_c) / 2 - np.sqrt(((eps_a - eps_c) / 2) ** 2 + eps_b ** 2)
    return pd.Series(eps_min, name="eps_min")

def principal_strain_angle(eps_a: pd.Series, eps_b: pd.Series, eps_c: pd.Series) -> pd.Series:
    theta = 0.5 * np.arctan2(2 * eps_b, eps_a - eps_c)
    return pd.Series(theta, name="theta")

if __name__ == "__main__":
    
    data = pd.read_csv("strain_data.csv", sep="\t")  # Assuming tab-separated file
    print("Initial Data:")
    print(data.head())

    data["eps_max"] = principal_strain_max(data["eps_a"], data["eps_b"], data["eps_c"])
    data["eps_min"] = principal_strain_min(data["eps_a"], data["eps_b"], data["eps_c"])
    data["theta"] = principal_strain_angle(data["eps_a"], data["eps_b"], data["eps_c"])

    data["theta_max"] = (data["eps_a"] > data["eps_c"]).astype(bool)
    data["theta_min"] = (data["eps_a"] < data["eps_c"]).astype(bool)

    print("Processed Data:")
    print(data.head())

    data.to_csv("output.csv", index=False)
    
