import numpy as np
from train.hashing import hashpredict
from train.hashing import hashinput
from train.train import training

user_ratings = np.loadtxt(open("data/input.csv"), delimiter=",", skiprows=1)
Xtrain = [user_ratings[:,0],user_ratings[:,1]]
Xtrain[0],Xtrain[1] = hashinput(Xtrain[0],Xtrain[1])
ytrain = [user_ratings[:,2]]
training(Xtrain,ytrain)
