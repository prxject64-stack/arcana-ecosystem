import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# In a multi-node setup, these would be fetched via SSH/API
# For now, we simulate the 'Cluster View'
def generate_heatmap():
    data = {
        'Node_ID': ['Node-01', 'Node-01', 'Node-02', 'Node-02', 'Node-03', 'Node-03'],
        'Metric': ['Net_Yield', 'Fees_Collected', 'Net_Yield', 'Fees_Collected', 'Net_Yield', 'Fees_Collected'],
        'Value': [995000, 5000, 995000, 5000, 995000, 5000] # Simulated for scaling
    }
    
    df = pd.DataFrame(data)
    pivot_df = df.pivot(index="Node_ID", columns="Metric", values="Value")

    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_df, annot=True, fmt=".0f", cmap="YlOrRd")
    plt.title("Arcana Ecosystem: Global Node Performance (ARC)")
    
    # Save to file for Cloud Vault viewing
    plt.savefig('global_performance_heatmap.png')
    print("Heatmap generated: global_performance_heatmap.png")

if __name__ == "__main__":
    generate_heatmap()
