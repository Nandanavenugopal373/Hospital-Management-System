class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def get_details(self):
        return f"{self.patient.name} → {self.doctor.name} on {self.date}"