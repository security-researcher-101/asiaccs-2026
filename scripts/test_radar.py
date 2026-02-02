import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def generate_radar_plot(labels, values, title, filename):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # Complete the circle
    values = values + values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='red', alpha=0.25)
    ax.plot(angles, values, color='red', linewidth=2)
    
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    
    plt.title(title, size=14, color='darkred', y=1.1)
    
    # Ensure plots directory exists
    if not os.path.exists('plots'):
        os.makedirs('plots')
        
    plt.savefig(f'plots/{filename}.png')
    print(f"Success! Chart saved as plots/{filename}.png")

if __name__ == "__main__":
    # 1. Load your CSV data
    try:
        df = pd.read_csv('data/results.csv')
        
        # 2. Define labels (The 5 Dimensions)
        labels = ['Knowledge', 'Interaction', 'Auxiliary', 'Adaptivity', 'Observability']
        
        # 3. Test with 'Closed World' values (Row 0)
        # We simulate scores based on the 'adversary_knowledge' column
        closed_world_scores = [5, 4, 5, 2, 4] 
        generate_radar_plot(labels, closed_world_scores, "Evaluation A: Closed World", "radar_closed")
        
    except FileNotFoundError:
        print("Error: data/results.csv not found. Check your file path.")