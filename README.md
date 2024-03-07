# ECE_143-project

Group project for ECE 143 created by:
- Andrina Hoffman
- Jerry Yan
- Aram Chemishkian
- Tung Hsiao
- Haoxuan Sun

## Code structure

- `environment.yml`: Conda environment file specifying dependencies.
- `main.py`: Main script to run the project.
- `notebooks/`: Contains Jupyter notebooks for exploratory data analysis and experimentation.
- `src/`: Source code directory.
    - `data/`: Stores datasets used in the project.
    - `scripts/`: Contains scripts for data processing and analysis.
        - `visualizations/`: Scripts for generating various types of visualizations.

## Environment setup

```shell
conda env create -f environment.yml
```

## Running the code
```shell
python main.py # download data by removing comment on line 22 of main.py to call fetch_and_save_data(year)
```

## Data

Data can be obtained from this [Google Drive link](https://drive.google.com/drive/folders/1E3aN3VhF5CzZvnIywYGE5IZiaKmX6j7T?usp=drive_link). The data should be put into `src/data`.
