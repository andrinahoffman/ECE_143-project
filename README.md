# ECE_143-project

Billionaires - Who are they?

Group project for ECE 143 created by:
- Andrina Hoffman
- Jerry Yan
- Aram Chemishkian
- Tung Hsiao
- Haoxuan Sun

## Project structure

- `environment.yml`: Conda environment file specifying dependencies.
- `main.py`: Main script to run the project.
- `notebooks/`: Contains Jupyter notebooks for exploratory data analysis and experimentation.
- `src/`: Source code directory.
    - `data/`: Stores datasets used in the project.
    - `scripts/`: Contains scripts for data processing and analysis.
        - `visualizations/`: Scripts for generating various types of visualizations.

Our slide deck PDF is `G7 Economic weight of billionaires.pdf`. Otherwise, you can find the Google Slides link [here](https://docs.google.com/presentation/d/1VdvrQg08m6uUTCLlAsP6u_VqpEd5nsiVNy3cqLDTe2g/edit?usp=sharing).

## Environment setup

It is suggested to use [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) to set up the environment with the following command.

```shell
conda env create -f environment.yml
```

If there are any problems, here are the list of 3rd-party packages we use.
- matplotlib
- pandas
- numpy
- cartopy
- geopandas
- requests

These can be installed in any Python 3.10 environment.

## Running the code

The main notebook used to generate plots is in [`plot-notebook.ipynb`](notebooks/plot-notebook.ipynb). Select the correct Python kernel and run the whole notebook.

Otherwise, there is code that can be run to make some of the animated bar plots.

```shell
python main.py
```

Download data by removing comment on line 22 of `main.py` to call `fetch_and_save_data(year)`.

## Data

Data can be obtained from this [Google Drive link](https://drive.google.com/drive/folders/1E3aN3VhF5CzZvnIywYGE5IZiaKmX6j7T?usp=drive_link). The data should be put into `src/data`.
