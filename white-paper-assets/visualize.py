"""
visualize.py

Utility to visualize before and after images side-by-side
and save publication-quality figures.
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def _read_image(image):
    """
    Reads an image from a file path or returns the numpy array.
    """

    if isinstance(image, str):
        image = np.array(Image.open(image).convert("RGB"))

    return image


def show_comparison(
    before,
    after,
    before_title="Before",
    after_title="After",
    figure_title="Comparison",
    save_path="comparison.png",
    dpi=300,
    figsize=(12, 6),
    show=True,
):
    """
    Display and save a side-by-side comparison.

    Parameters
    ----------
    before : str or ndarray
        Original image.

    after : str or ndarray
        Processed image.

    before_title : str
        Left subplot title.

    after_title : str
        Right subplot title.

    figure_title : str
        Overall figure title.

    save_path : str
        Output filename.

    dpi : int
        Image quality.
        150  -> Screen
        300  -> Paper
        600  -> High-quality publication
        1200 -> Ultra-high quality

    figsize : tuple
        Figure size.

    show : bool
        Whether to display the figure.
    """

    before = _read_image(before)
    after = _read_image(after)

    fig, axes = plt.subplots(
        1,
        2,
        figsize=figsize,
        constrained_layout=True,
    )

    axes[0].imshow(before)
    axes[0].set_title(before_title, fontsize=14)
    axes[0].axis("off")

    axes[1].imshow(after)
    axes[1].set_title(after_title, fontsize=14)
    axes[1].axis("off")

    fig.suptitle(
        figure_title,
        fontsize=18,
        fontweight="bold",
    )

    plt.savefig(
        save_path,
        dpi=dpi,
        bbox_inches="tight",
        pad_inches=0.15,
    )

    if show:
        plt.show()
    else:
        plt.close(fig)

    print(f"✓ Figure saved to: {save_path}")
    print(f"✓ DPI: {dpi}")


if __name__ == "__main__":

    # show_comparison(
    #     before="20240725122127428_sardine_bad_fish_segmented_0.png",
    #     after="fish_cuts.png",
    #     before_title="Segmented Fish",
    #     after_title="Detected Damages",
    #     figure_title="Fish Damage Detection",
    #     save_path="comparison.png",
    #     dpi=600,
    # )
    
    show_comparison(
    before="20240725122127428_sardine_bad.jpeg",
    after="20240725122127428_sardine_bad_fish_segmented_0.png",
    before_title="Original Image",
    after_title="Segmented Fish",
    figure_title="Fish Segmentation",
    save_path="comparison1.png",
    dpi=1200,
    )