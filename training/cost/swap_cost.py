"""
This is a cost that's able to train the circuit when the output is a measurement of a swap test.
"""


def fid_func(output):
    # Implemented as the Fidelity Loss
    # output[0] because we take the probability that the state after the
    # SWAP test is ket(0), like the reference state
    fidelity_loss = 1 / output[0]
    return fidelity_loss


def sw_cost(encoder_params, input_data, circuit, reinit_state=None):
    """
    :encoder parameters:
    :X:

    """
    #print("input_data:",input_data)
    loss = 0.0
    for x in input_data:
        output = circuit(init_params=x, encoder_params=encoder_params, reinit_state=reinit_state)[0]
        f = fid_func(output)
        loss = loss + f
    return loss / len(input_data)


def sw_fidelity(encoder_params, input_data, circuit, reinit_state=None):
    """

    """
    loss = 0.0
    for x in input_data:
        output = circuit(init_params=x, encoder_params=encoder_params, reinit_state=reinit_state)[0]
        f = output[0]
        loss = loss + f
    return loss / len(input_data)