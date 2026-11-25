"""Generic vegetation-index demonstration. All reflectances are artificial."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def normalized_difference(a, b):
    """Calculate (a-b)/(a+b), masking zero denominators and invalid inputs."""
    a, b = np.broadcast_arrays(np.asarray(a, float), np.asarray(b, float))
    den = a + b
    valid = np.isfinite(a) & np.isfinite(b) & (np.abs(den) > 1e-12)
    return np.divide(a - b, den, out=np.full(a.shape, np.nan), where=valid)


def artificial_reflectance(n=100):
    """Produce a fictional pixel grid with smooth reflectance variation."""
    x, y = np.meshgrid(np.linspace(-1, 1, n), np.linspace(-1, 1, n))
    signal = np.exp(-3 * (x*x + y*y))
    red = 0.30 - 0.20 * signal
    nir = 0.25 + 0.45 * signal
    return red, nir


def main():
    red, nir = artificial_reflectance()
    index = normalized_difference(nir, red)
    fig, ax = plt.subplots(figsize=(7, 5), layout='constrained')
    im = ax.imshow(index, vmin=-1, vmax=1)
    fig.colorbar(im, ax=ax, label='Normalized difference')
    ax.set(title='Synthetic vegetation-index raster (not observations)',
           xlabel='Pixel column', ylabel='Pixel row')
    out = Path(__file__).resolve().parents[1] / 'outputs'
    out.mkdir(exist_ok=True)
    fig.savefig(out / 'synthetic_spectral.png', dpi=150)
    plt.close(fig)


if __name__ == '__main__':
    main()
