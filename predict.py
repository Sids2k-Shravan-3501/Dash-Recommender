from tensorflow.keras.models import load_model
from train.hashing import hashpredict
import numpy as np



def predict_bestDashes(user_name,x):
	model = load_model("model/model.tf")
	user_ratings = np.loadtxt(open("data/input.csv"), delimiter=",", skiprows=1)
	users,dashes = user_ratings[:,0],user_ratings[:,1]
	users_dict,dashes_dict = hashpredict(users,dashes)
	user_id = users_dict[user_name]
	n,i = len(dashes_dict),0
	predictions = []
	while(i<n):
		predictions.append(model.predict([np.array([user_id]),np.array([i])]))
		i = i + 1
	appended_list = []
	i = 0
	while(i<n):
		temp = [predictions[i],i]
		appended_list.append(temp)
		i = i + 1
	appended_list.sort()
	dict_dashes = {value:key for key, value in dashes_dict.items()}
	print("The top " + str(x) + " movies recommended for " + str(user_name) + " are:")
	i = 0
	while(i<x):
		print(str(int(dict_dashes[appended_list[i][1]])))


def predicted_rating(user_name,dash_name):
	model = load_model("model/model.tf")
	user_ratings = np.loadtxt(open("data/input.csv"), delimiter=",", skiprows=1)
	users,dashes = user_ratings[:,0],user_ratings[:,1]
	users_dict,dashes_dict = hashpredict(users,dashes)
	user_id,dash_id = users_dict[user_name],dashes_dict[dash_name]
	#print(user_id,dash_id)
	prediction = model.predict([np.array([user_id]),np.array([dash_id])])
	print("The predicted rating " + str(user_name) + " would give to " + str(dash_name) + " is : " + str(prediction[0][0]))

a = int(input("Enter 1 to predict the best dashes for a given user or enter 2 to predict the user's rating for dash: "))

if (a == 1):
	user_name = input("Enter user name: ")
	x = int(input("Enter the number of movies you want as output: "))
	y = int(input("If the user_name is an integer, enter 0 else enter 1: "))
	if(y==0):
		user_name = int(user_name)
	predict_bestDashes(user_name,x)

elif(a == 2):
	user_name = input("Enter user name: ")
	dash_name = input("Enter dash name: ")
	y = int(input("If the user_name and dash_name are integers, enter 0 else enter 1: "))
	if(y==0):
		user_name = int(user_name)
		dash_name = int(dash_name)
	predicted_rating(user_name,dash_name)

else:
	print("Incorrect choice!")