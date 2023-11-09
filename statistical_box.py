def probability_for_greater_in_n(face: int, d_faces: int, number_of_dices: int) -> float:
    probabilistic_volumen_for_face = pow(face, number_of_dices)
    probabilistic_volumen_for_previous_face = pow(face - 1, number_of_dices)
    full_probabilistic_volumen=pow(d_faces, number_of_dices)
    probabilistic_volumen_substraction_for_face = probabilistic_volumen_for_face - probabilistic_volumen_for_previous_face

    return probabilistic_volumen_substraction_for_face/full_probabilistic_volumen

def calculate_probability_for_faces_of_least_in_n():
    pass