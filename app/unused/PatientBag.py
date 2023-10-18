from pathlib import Path
from patient import Patient


class PatientBag:
  """
  PatientBag is a collection of Patients, parse out from folder.

  Patients can be loaded to a database for persistency.
  """

  def __int__(
      self,
      generated_patient_folder: str | Path | None = None,
      load_patient_from_db: bool = True,
  ):
    self.patient_folder = generated_patient_folder
    self.patients: dict[str, Patient] = {}
    self.load_patient_from_db = load_patient_from_db

  def size(self) -> int:
    """:return: the amount of dags contained in this dagbag"""
    return len(self.dags)

  def patient_ids(self) -> list[str]:
    """
    Get all the patient ids.

    :return: a list of DAG IDs in this bag
    """
    return list(self.dags)
