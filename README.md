# Pulsar Segmentation and Analysis for Radio-Astronomy (HTW Berlin)

[![GitHub Super-Linter](https://github.com/interTwin-eu/itwinai-plugin-template/actions/workflows/lint.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![GitHub Super-Linter](https://github.com/interTwin-eu/itwinai-plugin-template/actions/workflows/check-links.yml/badge.svg)](https://github.com/marketplace/actions/markdown-link-check)
[![SQAaaS source code](https://github.com/EOSC-synergy/itwinai-plugin-template.assess.sqaaas/raw/main/.badge/status_shields.svg)](https://sqaaas.eosc-synergy.eu/#/full-assessment/report/https://raw.githubusercontent.com/eosc-synergy/itwinai-plugin-template.assess.sqaaas/main/.report/assessment_output.json)

This plug-in is part of [itwinai](https://github.com/interTwin-eu/itwinai). Its purpose is
to provide integration with AI pipelines developed at HTW Berlin for the purposes
of pulsar analysis and detection (radio-astronomy).
Please visit the [original repository](https://gitlab.com/ml-ppa) for more technical
details on the application.

Integration Author: Alex Krochak, FZJ

Plug-in description

-----------------------------------------------------------------------------------------------
itwinai implements a *plugin* architecture, allowing the community to independently develop
sub-packages for itwinai. These sub-packages can later be installed from PyPI and imported
into Python code as if they were part ofitwinai. This is made possible by
[namespace packages](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/).

Itwinai plugins are developed by assuming that the plugin logic,
once installed alongside itwinai, will be accessible under
the `itwinai.plugins.*` namespace. Example:

```python
from itwinai.plugins.pulsar import data, trainer

# Instantiate a class implemented by the plugin
my_dataset = data.PulsarDataset(...)
my_trainer = trainer.PulsarTrainer(...)
```

Plug-in installation

-----------------------------------------------------------------------------------------------

A straightforward way to install the plug-in on local machine is as follows:

1. Clone this repository on your local machine or server.
2. Create a new Python virtual environment: `python -m venv .venv`.
3. Activate this virtual environment `source .venv/bin/activate`.
4. (Recommmended) Install `uv` for accelerated package management: `pip install uv`.
More information can be found [here](https://docs.astral.sh/uv/).
5. Then run from the top directory: `(uv) pip install .`. This will install the plug-in.
NOTE: itwinai itself is also installed automatically,
as it is a plug-in dependency (see `pyproject.toml`)
6. Done ! Now you can either run itwinai from CLI, i.e.:
`itwinai exec-pipeline +pipe_key=syndata_pipeline`.
Alternatively, you can unpack the `exec.zip` outside the plug-in directory and run `exec.py`.
Make sure you are using the virtual environment installed at the plug-in,
but operate outside the plug-in directory !.


Plug-in installation on Juwels-Booster

-----------------------------------------------------------------------------------------------

When installing on Juwels-Booster at FZJ, additional steps need to be taken.

1. Load the necessary modules for Python 3.11.3 (recommended):
   `module --force purge`
   `ml Stages/2024  GCCcore/.12.3.0 Python/3.11.3`
   Verify the Python version by `python --version`.
3. Clone this repository in your personal project folder.
4. Create a new Python virtual environment: `python -m venv .venv`.
5. Activate this virtual environment `source .venv/bin/activate`.
6. Verify correct Python and Pip path with:
7. `which pip` and `which python`.
8. (Recommmended) Install `uv` for accelerated package management:
   `pip install uv --no-cache-dir`.
   The argument `--no-cache-dir` is necessary whenever installing with pip to prevent
   the `~/.cache` folder to fill up your home quota.
   More information on UV can be found [here](https://docs.astral.sh/uv/).
10. Then run from the top directory: `(uv) pip install . --no-cache-dir`.
    This will install the plug-in.
    NOTE: itwinai itself is also installed automatically,
    as it is a plug-in dependency (see `pyproject.toml`)
12. Extract `exec.tar.gz` with `tar -xvzf exec.tar.gz` outside the plug-in folder.
    Navigate to the exec folder and test the plug-in execution:
    `itwinai exec-pipeline +pipe_key=syndata_pipeline`.


Running from a configuration file

-----------------------------------------------------------------------------------------------

You can run the full pipeline sequence by executing the following commands locally.
Please note that it is recommended to run these commands outside the plug-in repository for
organizational reasons. You just need to make sure that the correct Python virtual environment
is activated.

itwinai will read these commands from the `config.yaml` file.

1. Generate the synthetic data            - `itwinai exec-pipeline +pipe_key=syndata_pipeline`
2. Initialize and train a UNet model      - `itwinai exec-pipeline +pipe_key=unet_pipeline`
3. Initialize and train a FilterCNN model - `itwinai exec-pipeline +pipe_key=fcnn_pipeline`
4. Initialize and train a CNN1D model     - `itwinai exec-pipeline +pipe_key=cnn1d_pipeline`
5. Compile a full pipeline and test it    - `itwinai exec-pipeline +pipe_key=evaluate_pipeline`

When running on HPC, you can use the `batch.sh` SLURM script to run these commands.

Logging with MLflow

-----------------------------------------------------------------------------------------------

By default, the `config.yaml` ensures that the MLflow logging is enabled during the training.
During or after the run, you can launch an MLflow server by executing
`mlflow server --backend-store-uri mllogs/mlflow` and connecting to `http://127.0.0.1:5000/`
in your browser.

Test suite

-----------------------------------------------------------------------------------------------

The test suite is located in the `tests/` folder.

Before running the test suite, you should make sure that the pytorch fixture in:
`tests/test_pulsar.py`:torch_env()  
is correctly defined and corresponds to the virtual environment where itwinai is
installed on your system.

It contains integration tests for each of the pipelines 1-5 mentioned above. The configuration
and execution of the test suite is defined in: `tests/test_pulsar.py` and
in the configuration file: `tests/.config-test.yaml`.
If you are updating the test suite, make sure you update both of these files.
