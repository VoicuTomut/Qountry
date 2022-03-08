"""
encode the word on a pure state.
"""
import pennylane as qml


def put_word_on_qubits(word_rep, qubits, base="X"):
    """

    :param word_rep: "00..10..0"
    :param qubits:
    :param base:
    """
    word_rep = str(word_rep)
    if base == "X":
        for i in range(len(word_rep)):

            if word_rep[i] == '1':
                qml.PauliX(qubits[i])
    if base == "Y":
        for i in range(len(word_rep)):
            if word_rep[i] == '1':
                qml.PauliY(qubits[i])
    if base == "Z":
        for i in range(len(word_rep)):
            if word_rep[i] == '1':
                qml.PauliZ(qubits[i])
