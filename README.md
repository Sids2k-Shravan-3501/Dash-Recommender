# Dash Recommender

## About
Dash Recommender takes an input of user names, `dash` names and the corresponding rating. It then trains feature vectors for each user and `dash` using collaborative filtering techniques. And then one can find the top _x_ `dashes` for a given user or predict what that user would rate the `dash`.

In the given sample input, we are able to achieve 75% accuracy and reach a mean_squared_loss of 0.05. This number is bound to increase in more exhaustive datasets.

`Dash` simply implies that our project can be used for any kind of system where a user rates an entity and the entity have features that some users may prefer. For example it can work with restaurants and movies but also with a match making system where a person rates the other.

## Usage
The input.py script should be run to train the collaborative filtering model for your own dataset. (This data set needs to overwrite the already given Dash-Recommender/data/input.csv and follow the same structure as the given Dash_Recommender/data/input.csv)

After input.py finishes running, one can use the predict.py script to either predict what that user would rate the `dash` or what the top _x_ `dashes` for a user will be.

## Features Used
The features used are just the ratings what a user gave to the a `dash` and the unique identifier for each user and `dash`.

This unique identifier is built from the user name and `dash` name that is inputted. 

## Model
The trained model can be loaded from Dash-Recommender/model/model.tf and the data that was fed into it is at Dash-Recommender/data/input.csv.

## Requirements 
* numpy

* tensorflow

* Keras

## Owners
Siddhant Sharma: https://github.com/Sids2k

Shravan Nawandar: https://github.com/Shravan-3501

## License
Copyright - 2020 - Siddhant Sharma and Shravan Nawandar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
