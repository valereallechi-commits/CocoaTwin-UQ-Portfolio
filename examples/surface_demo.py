"""A mathematical surface visualization; no images or real UAV data."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def artificial_surface(n=50):
    """Return points sampled from an arbitrary analytical function."""
    x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))
    z = np.sin(x) * np.cos(y) + 0.1 * x
    return np.column_stack((x.ravel(), y.ravel(), z.ravel()))


def main():
    points = artificial_surface()
    fig = plt.figure(figsize=(7, 5), layout='constrained')
    ax = fig.add_subplot(projection='3d')
    dots = ax.scatter(*points.T, c=points[:, 2], s=4)
    ax.set(xlabel='Synthetic X', ylabel='Synthetic Y', zlabel='Synthetic Z',
           title='Mathematical point cloud (no UAV measurements)')
    fig.colorbar(dots, ax=ax, label='Artificial Z', shrink=0.7)
    out = Path(__file__).resolve().parents[1] / 'outputs'
    out.mkdir(exist_ok=True)
    fig.savefig(out / 'synthetic_surface.png', dpi=150)
    plt.close(fig)


if __name__ == '__main__':
    main()
