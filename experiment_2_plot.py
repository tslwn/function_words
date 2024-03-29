# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray
import seaborn
from typing import cast

from experiment_2_results import get_parameter_values, get_result, parameter_grid, Parameters
from utils import plot


def callback(ax: plt.Axes, result: tuple[Parameters, NDArray[np.int_]]) -> None:
    parameters, x = result

    protocol_name, _, _, _, _, _ = get_parameter_values(parameters)

    ax.set_title(f"{protocol_name}")

    ax.set_xlabel("Semantic content")

    seaborn.stripplot(x=x, ax=ax)


if __name__ == "__main__":
    results: list[tuple[Parameters, NDArray[np.int_]]] = []

    for parameters in parameter_grid:
        parameters = cast(Parameters, parameters)
        results.append((parameters, get_result(parameters)))

    plot(results, callback)
