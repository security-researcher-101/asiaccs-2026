import matplotlib.pyplot as plt
import numpy as np

def generate_radar_plot(labels, values, title):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='blue', alpha=0.25)
    ax.plot(angles, values, color='blue', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    plt.title(title, size=15, color='blue', y=1.1)
    plt.savefig('plots/radar_chart.png')
    print("Radar chart saved to plots/radar_chart.png")

if __name__ == "__main__":
    # The 5 dimensions from the AsiaCCS Framework
    dimensions = ['Knowledge', 'Interaction', 'Auxiliary Info', 'Adaptivity', 'Observability']
    # Example values for a 'Weak' evaluation (Closed World WF)
    scores = [5, 2, 1, 1, 4] 
    generate_radar_plot(dimensions, scores, "Security Boundary Analysis")