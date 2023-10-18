from data import lab_examination


def lab_examine_backend(patient_id, examination, conn):
    patient_id = int(patient_id)

    target_patient = conn.find_one({'patient_id': patient_id}, {'_id': 0})

    res = _lab_examine(target_patient, examination)

    conn.update_one({'patient_id': patient_id}, {"$set": {"examined." + examination: ''.join(res)}})


def _lab_examine(target_patient, examination):
    set_patient_sym = set(target_patient['symptoms'])
    set_exam_result = set(lab_examination[examination])

    return set_patient_sym.intersection(set_exam_result)
