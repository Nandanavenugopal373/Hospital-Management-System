class Billing:
    def __init__(self, patient, consult_fee, treatment_cost):
        self.patient = patient
        self.consult_fee = consult_fee
        self.treatment_cost = treatment_cost

    def calculate_total(self):
        return self.consult_fee + self.treatment_cost