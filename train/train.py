import numpy as np
from keras.layers import Add
from keras.models import Model
from keras.layers import Input, Reshape, Dot
from keras.layers.embeddings import Embedding
from keras.optimizers import Adam
from keras.regularizers import l2

def training(Xtrain,ytrain):
    user_embeddings = Input(shape = (1,))
    ue = Embedding(len(np.unique(Xtrain[0]))+1,100,embeddings_initializer='he_normal', embeddings_regularizer=l2(1e-6))(user_embeddings)

    dash_embeddings = Input(shape = (1,))
    de = Embedding(len(np.unique(Xtrain[1]))+1,100,embeddings_initializer='he_normal', embeddings_regularizer=l2(1e-6))(dash_embeddings)

    dot = Dot(axes = 2)([ue,de])

    final = Reshape((1,))(dot)

    model = Model(inputs = [user_embeddings,dash_embeddings], outputs = final)
    model.compile(loss = 'mean_squared_error',optimizer = Adam(lr = 0.0005),metrics = ['accuracy'])

    history = model.fit(Xtrain, np.reshape(np.array(ytrain),(len(Xtrain[0]),1)), epochs=30, verbose=1)
    
    model.save("model/model.tf")
    return 
