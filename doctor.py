class Doctor:
    def __init__(self, did, name, specialization):
        self.did = did
        self.name = name
        self.specialization = specialization

    def get_details(self):
        return f"{self.did} | {self.name} | {self.specialization}"