from pathlib import Path

import utils


def abs_path_from_project(relative_path: str):
    return (
        Path(utils.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
