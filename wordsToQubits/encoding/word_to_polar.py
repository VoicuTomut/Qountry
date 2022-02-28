"""
encode a word on the bloc sphere.
"""
from typing import Any, Union

import pennylane as qml
from pennylane import numpy as np


def put_word_on_sphere(params, qubit):
    """

    :param params: [x, y ,z ]
    :param qubit:
    """

    if params[2] != 0:
        theta = np.arctan(np.sqrt(params[0] * params[0] + params[1] * params[1]) / params[2])
    else:
        theta = np.pi / 2

    if params[0] != 0:
        phi = np.arctan(params[1] / params[0])
    else:
        phi = np.pi / 2

    if params[1] * params[1] == 1:
        phi = np.pi / 2
        theta = -params[1] * np.pi / 2

    if (params[0] > 0) and (params[1] >= 0) and (params[2] > 0):
        theta = theta

    elif (params[0] < 0) and (params[1] >= 0) and (params[2] > 0):
        theta = 2 * np.pi - theta

    elif (params[0] > 0) and (params[1] <= 0) and (params[2] > 0):
        theta = -2 * np.pi + theta

    elif (params[0] < 0) and (params[1] <= 0) and (params[2] > 0):
        theta = 2 * np.pi - theta

    elif (params[0] < 0) and (params[1] <= 0) and (params[2] < 0):
        theta = np.pi - theta

    elif (params[0] < 0) and (params[1] >= 0) and (params[2] < 0):
        theta = np.pi - theta

    elif (params[0] > 0) and (params[1] <= 0) and (params[2] < 0):
        theta = np.pi + theta

    else:  # (params[0] > 0) and (params[1] > 0) and (params[2] < 0)
        theta = -np.pi + theta

    qml.RY(theta, wires=qubit)
    qml.RZ(phi, wires=qubit)



"""
EXAMPLE:

dev = qml.device("default.qubit", wires=1)

# encode the world
@qml.qnode(dev)
def w_encode(word_params, obs='z'):
    
    put_word_on_sphere(word_params, qubit=0)
    
    # measure 
    if obs=='z':
        return  qml.expval(qml.PauliZ(0))
    if obs=='x':
        return qml.expval(qml.PauliX(0))
    if obs=='y':
        return qml.expval(qml.PauliY(0))
        
def get_word_prediction(pred_vector,parameterize_vovabulary):
  
    dist= 999.0 # max possible distance is <=3
    extract_word="-"
    for w in parameterize_vovabulary :
        w_param=parameterize_vovabulary[w]
        new_d= np.sqrt((w_param[0]-pred_vector[0])**2+(w_param[1]-pred_vector[1])**2+(w_param[2]-pred_vector[2])**2)
        if new_d<dist:
            next_word = str(w)
            dist=new_d

    return next_word

word=parameterize_vovabulary['are']
w_decode_param = [ w_encode(word, obs=o) for o in ['x', 'y', 'z']]
print("pred:",w_decode_param)
print("original:",word)

"""