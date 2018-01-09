# Prediction-of-Outcomes-in-Animal-Shelter
Built prediction models for animal shelter data, 140,000 records, using several machine learning approaches- logistic regression, decision tree, and random forest. The accuracy rate was around 80%.

## Authors
* Shih-Ting Huang (sh3964@rit.edu)
* Wei-Yao Ku (wxk6489@rit.edu) 

## Data Source: 
https://data.louisvilleky.gov/dataset/animal-service-intake-and-outcome


## File list
* report.pdf          : final project report file
* divide.py           : extract cat and dog data from source data
* cleanData_cat.py    : generate correct format file(.csv) for predictionModel.py
* cleanData_dog.py    : generate correct format file(.csv) for predictionModel.py
* predictionModel.py  : prediction model implementation


## Steps
0. Download file from source:
   https://data.louisvilleky.gov/dataset/animal-service-intake-and-outcome
   (If using other correct format file, user can directly run step 4.)

1. Run divide.py
   - input: (enter file name without ‘.csv’)
   - output: cat.csv, dog.csv

2. Run cleanData_cat.py
    - output: CAT_data.csv

3. Run cleanData_dog.py
    - output: DOG_data.csv

4. Run predictionModel.py
   - input: (enter file name without ‘.csv’)
   - output: (filename)_result_acc.csv     : accuracy of each prediction model
             (filename)_result_time.csv    : running time of each prediction model
             (filename)_tree.pdf           : decision tree(depth = 5) picture
             (filename)_varTable.csv       : input file’s attribute table

(predictionModel.py only require one input file, it will automatically divide input data into 70% for training, 30% for testing.)
