import sys
import pandas as pd
import numpy as np
import subprocess


if __name__ == "__main__":
    # Check if the file path is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python eda.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Read the DataFrame from the CSV file
    df = pd.read_csv(file_path)
    
    summary_stats = df.describe()

    # Save the output to a text file
    with open("service-result/summary_statistics.txt", "w") as f:
        f.write("Summary Statistics:\n")
        f.write(str(summary_stats))
    
    numeric_cols = df.select_dtypes(include=np.number).columns
    z_scores = df[numeric_cols].apply(lambda x: (x - x.mean()) / x.std())

    # Determine the threshold for Z-scores (e.g., 3)
    z_score_threshold = 3

    # Identify outliers based on the threshold
    outliers = (z_scores > z_score_threshold) | (z_scores < -z_score_threshold)

    with open("service-result/outliers_z_score.txt", "w") as f:
        f.write("Outliers Detected using Z-Score (Threshold = {}):\n\n".format(z_score_threshold))
        for col in outliers.columns:
            f.write("Column: {}\n".format(col))
            for idx in outliers.index:
                is_outlier = outliers.loc[idx, col]
                if is_outlier:
                    f.write("    - Row {}: Z-Score = {:.2f}\n".format(idx, z_scores.loc[idx, col]))

    # Calculate correlation coefficients
    corr_matrix = df.corr()

    # Identify positively and negatively correlated variables
    positive_corr = {}
    negative_corr = {}
    for col in corr_matrix.columns:
        for idx, corr in corr_matrix[col].items():
            if col != idx:
                if corr > 0:
                    if col not in positive_corr:
                     positive_corr[col] = [(idx, corr)]
                    else:
                        positive_corr[col].append((idx, corr))
                elif corr < 0:
                    if col not in negative_corr:
                        negative_corr[col] = [(idx, corr)]
                    else:
                        negative_corr[col].append((idx, corr))

    
    # Save the results to a text file
    with open("service-result/correlation_analysis.txt", "w") as f:
        f.write("Correlation Analysis:\n\n")

        f.write("Positively Correlated Variables:\n")
        for col, correlations in positive_corr.items():
            f.write("    - {}: {}\n".format(col, ", ".join(["{} ({:.2f})".format(var, corr) for var, corr in correlations])))
        f.write("\n")

        f.write("Negatively Correlated Variables:\n")
        for col, correlations in negative_corr.items():
            f.write("    - {}: {}\n".format(col, ", ".join(["{} ({:.2f})".format(var, corr) for var, corr in correlations])))
    
    genderCount = df['gender'].value_counts()
    lunchCount = df['lunch'].value_counts()
    with open("service-result/count_results.txt", "w") as f:
        f.write("Lunch Count:\n")
        f.write(str(lunchCount) + "\n\n")

        f.write("Gender Count:\n")
        f.write(str(genderCount) + "\n\n")
    
    subprocess.run(["python3", "vis.py", file_path])
