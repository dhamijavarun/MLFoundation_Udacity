# Machine Learning Foundation

## Overview

These projects were implemeted for the Machine Learning Foundation course from Udacity.
## Project 1: [Predicting Bikeshare Data](https://github.com/dhamijavarun/MLFoundation_Udacity/tree/master/Project_1_Predicting_Bikeshare_data)

## Project 2: [Testing a perceptual phenomenon](https://github.com/dhamijavarun/MLFoundation_Udacity/tree/master/Project_2_Test_a_perceptual_phenomenon)

## Project 3: [Investigating a dataset : Exploratory Data Analysis](https://github.com/dhamijavarun/MLFoundation_Udacity/tree/master/Project_3_Investigate_a_dataset)

## Project 4: [Predicting Boston Housing Prices](https://github.com/dhamijavarun/MLFoundation_Udacity/tree/master/Project_4_Boston_House_pricing)

### Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included. 

### Code

Template code is provided in the `boston_housing.ipynb` notebook file. You will also be required to use the included `visuals.py` Python file and the `housing.csv` dataset file to complete your work. While some code has already been implemented to get you started, you will need to implement additional functionality when requested to successfully complete the project. Note that the code included in `visuals.py` is meant to be used out-of-the-box and not intended for students to manipulate. If you are interested in how the visualizations are created in the notebook, please feel free to explore this Python file.

### Run

In a terminal or command window, navigate to the top-level project directory `boston_housing/` (that contains this README) and run one of the following commands:

```bash
ipython notebook boston_housing.ipynb
```  
or
```bash
jupyter notebook boston_housing.ipynb
```

This will open the Jupyter Notebook software and project file in your browser.

### Data

The modified Boston housing dataset consists of 489 data points, with each datapoint having 3 features. This dataset is a modified version of the Boston Housing dataset found on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Housing).

**Features**
1.  `RM`: average number of rooms per dwelling
2. `LSTAT`: percentage of population considered lower status
3. `PTRATIO`: pupil-teacher ratio by town

**Target Variable**
4. `MEDV`: median value of owner-occupied homes
