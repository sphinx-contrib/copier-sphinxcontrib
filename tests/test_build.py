"""test the build of the ccookie"""

import subprocess
from pathlib import Path

from pytest_cookies.plugin import Cookies
import yaml


def test_build_default(cookies: Cookies) -> None:
    """Build the cookiecutter with default parameters and perform small checks

    Args:
        cookies: the cookies to build
    """

    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "package-skeleton"
    assert result.project_path.is_dir()

def test_build_nox(cookies: Cookies) -> None:
    """Build the documentation and run the nox processes

    Args:
        cookies: the cookies to build
    """

    result = cookies.bake()

    # init git to make pre-commit checks work
    subprocess.check_call(["git", "config", "--global", "init.defaultBranch", "main"])
    subprocess.check_call(["git", "init"], cwd=result.project_path)

    # nox check
    assert subprocess.check_call(["nox"], cwd=result.project_path) == 0

def test_build_yaml(cookies: Cookies) -> None:
    """Build the documentation and check github actions files

    Args:
        cookies: the cookies to build
    """
    result = cookies.bake()

    # will raise an error if the file is ill shaped
    workflows_path = Path(result.project_path)/".github"/"workflows"
    data = yaml.safe_load((workflows_path/"unit.yaml").read_text())
    data = yaml.safe_load((workflows_path/"release.yaml").read_text())





