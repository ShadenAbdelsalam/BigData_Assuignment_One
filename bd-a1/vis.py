import sys
import pandas as pd
import numpy as np
import subprocess
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Check if the file path is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python eda.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Read the DataFrame from the CSV file
    df = pd.read_csv(file_path)


    # Calculate the average score
    df['average'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(15, 7))

    # Plot histograms
    sns.histplot(data=df, x='average', bins=30, kde=True, color='g', ax=axes[0])
    sns.histplot(data=df, x='average', bins=30, kde=True, hue='gender', ax=axes[1])

    # Set titles and labels
    axes[0].set_title('Distribution of Average Grades')
    axes[0].set_xlabel('Average Grade')
    axes[0].set_ylabel('Frequency')

    axes[1].set_title('Distribution of Average Grades by Gender')
    axes[1].set_xlabel('Average Grade')
    axes[1].set_ylabel('Frequency')

    # Adjust layout
    plt.tight_layout()

    # Save the visualization as vis.png
    plt.savefig('service-result/vis.png')


    fig, axes = plt.subplots(1, 3, figsize=(25, 6))

    # Plot histograms for all genders
    sns.histplot(data=df, x='average', kde=True, hue='lunch', ax=axes[0])
    axes[0].set_title('Distribution of Average Grades (All)')
    axes[0].set_xlabel('Average Grade')
    axes[0].set_ylabel('Frequency')

    # Filter the DataFrame by gender
    female_df = df[df.gender == 1]
    male_df = df[df.gender == 0]

    # Plot histograms for female gender
    if not female_df.empty:
        sns.histplot(data=female_df, x='average', kde=True, hue='lunch', ax=axes[1])
        axes[1].set_title('Distribution of Average Grades (Female)')
        axes[1].set_xlabel('Average Grade')
        axes[1].set_ylabel('Frequency')
    else:
        axes[1].set_title('No Data Available for Female Gender')

    # Plot histograms for male gender
    if not male_df.empty:
        sns.histplot(data=male_df, x='average', kde=True, hue='lunch', ax=axes[2])
        axes[2].set_title('Distribution of Average Grades (Male)')
        axes[2].set_xlabel('Average Grade')
        axes[2].set_ylabel('Frequency')
    else:
        axes[2].set_title('No Data Available for Male Gender')

    # Adjust layout
    plt.tight_layout()

    # Save the visualization as vis2.png
    plt.savefig('service-result/vis2.png')



    subprocess.run(["python3", "model.py", file_path])
