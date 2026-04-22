class Patient:
    def __init__(self, pid, name, age, disease):
        self.pid = pid
        self.name = name
        self.age = age
        self.disease = disease

    def get_details(self):
        return f"{self.pid} | {self.name} | {self.age} | {self.disease}"