# --------------------------------------------------------------------------------------
# Part of the interTwin Project: https://www.intertwin.eu/
# Created by: Oleksandr Krochak
# --------------------------------------------------------------------------------------

"""Tests for radio-astronomy use case.

Intended to be integration tests, to make sure that updates in the code base
do not break use cases' workflows.

This is meant to be run from the main itwinai directory, not the use-case folder !!!
"pytest use-cases/radio-astronomy/tests/test_radio-astronomy.py"

NOTE FOR DEVELOPERS: if you are editing this file, make sure that entries in
use-cases/radio-astronomy/.config-test.yaml are updated accordingly !!!
"""

import os
import subprocess
from pathlib import Path

import pytest

USECASE_FOLDER = Path("tests").resolve()


@pytest.fixture
def torch_env() -> str:
    """
    Returns absolute path to torch virtual environment.
    """
    env_path = Path(os.environ.get("TORCH_ENV", ".venv-juwels-cluster"))
    return str(env_path.resolve())


def test_radio_astronomy_syndata(torch_env):
    """
    Test synthetic data generation by running it end-to-end
    via the config-test.yaml configuration file.
    """

    cmd = (
        f"{torch_env}/bin/itwinai exec-pipeline "
        f"--config-name .config-test "
        f"+pipe_key=syndata_pipeline "
    )

    ## Run the pipeline and check file generation in the use-case folder
    subprocess.run("./.pytest-clean", shell=True, check=True, cwd=USECASE_FOLDER)
    subprocess.run("rm -rf ./models/*", shell=True, check=True, cwd=USECASE_FOLDER)
    subprocess.run(cmd.split(), check=True, cwd=USECASE_FOLDER)
    ## Clean up the use-case folder
    subprocess.run("rm -rf syndata_test", shell=True, check=True, cwd=USECASE_FOLDER)


def test_radio_astronomy_unet(torch_env):
    """
    Test U-Net Pulsar-DDT trainer by running it end-to-end
    via the config-test.yaml configuration file.
    """

    cmd = (
        f"{torch_env}/bin/itwinai exec-pipeline "
        f"--config-name .config-test "
        f"+pipe_key=unet_pipeline "
    )

    ## Run the pipeline and check file generation in the use-case folder
    subprocess.run(cmd.split(), check=True, cwd=USECASE_FOLDER)
    ## Clean up the use-case folder
    subprocess.run("./.pytest-clean", shell=True, check=True, cwd=USECASE_FOLDER)


def test_radio_astronomy_filtercnn(torch_env):
    """
    Test Filter-CNN Pulsar-DDT trainer by running it end-to-end
    via the config-test.yaml configuration file.
    """

    cmd = (
        f"{torch_env}/bin/itwinai exec-pipeline "
        f"--config-name .config-test "
        f"+pipe_key=fcnn_pipeline "
    )

    ## Run the pipeline and check file generation in the use-case folder
    subprocess.run(cmd.split(), check=True, cwd=USECASE_FOLDER)
    ## Clean up the use-case folder
    subprocess.run("./.pytest-clean", shell=True, check=True, cwd=USECASE_FOLDER)


def test_radio_astronomy_cnn1d(torch_env):
    """
    Test CNN-1D Pulsar-DDT trainer by running it end-to-end
    via the config-test.yaml configuration file.
    """

    cmd = (
        f"{torch_env}/bin/itwinai exec-pipeline "
        f"--config-name .config-test "
        f"+pipe_key=cnn1d_pipeline "
    )

    ## Run the pipeline and check file generation in the use-case folder
    subprocess.run(cmd.split(), check=True, cwd=USECASE_FOLDER)
    ## Clean up the use-case folder
    subprocess.run("./.pytest-clean", shell=True, check=True, cwd=USECASE_FOLDER)
    subprocess.run("rm -rf ./models/*", shell=True, check=True, cwd=USECASE_FOLDER)


# def test_radio_astronomy_evaluate(torch_env):
#     """
#     Test the evaluate pipeline by running it end-to-end
#     via the config-test.yaml configuration file.
#     """

#     cmd = (
#         f"{torch_env}/bin/itwinai exec-pipeline "
#         f"--config-name .config-test "
#         f"+pipe_key=evaluate_pipeline "
#     )

#     ## Run the pipeline and check file generation in the use-case folder
#     subprocess.run(cmd.split(), check=True, cwd=USECASE_FOLDER)
#     ## Clean up the use-case folder
#     subprocess.run("./.pytest-clean", shell=True, check=True, cwd=USECASE_FOLDER)
