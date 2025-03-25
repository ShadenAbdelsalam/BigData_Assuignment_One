import sys
import numpy as np
import pandas as pd
import subprocess
from sklearn.cluster import KMeans



if __name__ == '__main__':
    # Check if the file path is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python load.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    # read data    
    data = pd.read_csv(file_path)

    # model
    kmean = KMeans(n_clusters=3)
    kmean.fit(data)
    data['cluster'] = kmean.labels_
    
    with open("service-result/k.txt", "w") as f:
        f.write(str(data['cluster'].value_counts()))
        

        

