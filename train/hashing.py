def hashpredict(users,dashes):
	dict_users = {}
	dict_dashes = {}
	n = len(users)
	i,k = 0,0
	while(i<n):
		if users[i] in dict_users.keys():
			i = i + 1
		else:
			dict_users[users[i]] = k
			k = k + 1
			i = i + 1
	i,k = 0,0
	while(i<n):
		if dashes[i] in dict_dashes.keys():
			i = i + 1
		else:
			dict_dashes[dashes[i]] = k
			k = k + 1
			i = i + 1
	#dict_users = {value:key for key, value in dict_users.items()}
	#dict_dashes = {value:key for key, value in dict_dashes.items()}
	return(dict_users,dict_dashes)	

def hashinput(users,dashes):
	dict_users = {}
	dict_dashes = {}
	n = len(users)
	i,k = 0,0
	while(i<n):
		if users[i] in dict_users.keys():
			users[i] = dict_users[users[i]]
			i = i + 1 
		else:
			dict_users[users[i]] = k
			users[i] = k
			k = k + 1
			i = i + 1
	i,k = 0,0
	while(i<n):
		if dashes[i] in dict_dashes.keys():
			dashes[i] = dict_dashes[dashes[i]]
			i = i + 1
		else:
			dict_dashes[dashes[i]] = k
			dashes[i] = k
			k = k + 1
			i = i + 1
	return(users,dashes)

