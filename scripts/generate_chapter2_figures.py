from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path("docs/assets/images/chapter_2/section_2_1")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def setup_axis(ax, title):
    ax.axhline(0, linewidth=0.8, color="black")
    ax.axvline(0, linewidth=0.8, color="black")
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 6)
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$")
    ax.set_title(title)


def main():
    x = np.linspace(-1, 6, 400)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    # Case 1: exactly one solution
    # x1 + x2 = 5  -> x2 = 5 - x1
    # 2x1 + x2 = 8 -> x2 = 8 - 2x1
    y1 = 5 - x
    y2 = 8 - 2 * x

    axes[0].plot(x, y1, label=r"$x_1 + x_2 = 5$")
    axes[0].plot(x, y2, label=r"$2x_1 + x_2 = 8$")
    axes[0].scatter([3], [2], zorder=5)
    axes[0].annotate(
        r"$(3,2)$",
        xy=(3, 2),
        xytext=(3.2, 2.4),
        arrowprops=dict(arrowstyle="->", linewidth=0.8),
    )
    setup_axis(axes[0], "(a) Exactly one solution")
    axes[0].legend()

    # Case 2: no solution
    # x1 + x2 = 5  -> x2 = 5 - x1
    # x1 + x2 = 3  -> x2 = 3 - x1
    y3 = 5 - x
    y4 = 3 - x

    axes[1].plot(x, y3, label=r"$x_1 + x_2 = 5$")
    axes[1].plot(x, y4, label=r"$x_1 + x_2 = 3$")
    setup_axis(axes[1], "(b) No solution")
    axes[1].legend()

    # Case 3: infinitely many solutions
    # x1 + x2 = 5 and 2x1 + 2x2 = 10 describe the same line
    y5 = 5 - x

    axes[2].plot(x, y5, linewidth=3, label=r"$x_1 + x_2 = 5$")
    axes[2].plot(
        x,
        y5,
        linestyle="--",
        linewidth=2,
        label=r"$2x_1 + 2x_2 = 10$",
    )
    setup_axis(axes[2], "(c) Infinitely many solutions")
    axes[2].legend()

    fig.suptitle(
        "Figure 2.1.1: Geometric interpretation of systems of linear equations",
        fontsize=14,
        y=1.03,
    )
    fig.tight_layout()

    output_path = OUTPUT_DIR / "linear_system_solution_types.png"
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved figure to: {output_path}")


if __name__ == "__main__":
    main()