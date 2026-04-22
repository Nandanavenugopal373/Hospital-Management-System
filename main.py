from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

from patient import Patient
from doctor import Doctor
from appointment import Appointment
from billing import Billing

# Data storage
patients = []
doctors = []
appointments = []

# ---------------- FUNCTIONS ---------------- #

def add_patient():
    if pid.get() == "" or pname.get() == "":
        messagebox.showerror("Error", "Fill all fields")
        return
    if any(p.pid == pid.get().strip() for p in patients):
        messagebox.showerror("Error", "Patient ID already exists")
        return

    p = Patient(pid.get().strip(), pname.get(), age.get(), disease.get())
    patients.append(p)
    messagebox.showinfo("Success", "Patient Added")
    clear_patient()

def delete_patient():
    pid_val = pid.get().strip()

    patient = next((p for p in patients if p.pid == pid_val), None)

    if patient:
        patients.remove(patient)

        # remove related appointments
        global appointments
        appointments = [a for a in appointments if a.patient.pid != pid_val]

        messagebox.showinfo("Success", "Patient Deleted")
        clear_patient()
    else:
        messagebox.showerror("Error", "Patient not found")
def update_patient():
    pid_val = pid.get().strip()

    if pid_val == "":
        messagebox.showerror("Error", "Enter Patient ID")
        return

    patient = next((p for p in patients if p.pid == pid_val), None)

    if patient:
        patient.name = pname.get()
        patient.age = age.get()
        patient.disease = disease.get()

        messagebox.showinfo("Success", "Patient Updated")
        clear_patient()
    else:
        messagebox.showerror("Error", "Patient not found")


def add_doctor():
    if did.get() == "" or dname.get() == "":
        messagebox.showerror("Error", "Fill all fields")
        return
    if any(d.did == did.get().strip() for d in doctors):
        messagebox.showerror("Error", "Doctor ID already exists")
        return

    d = Doctor(did.get().strip(), dname.get(), spec.get())
    doctors.append(d)
    messagebox.showinfo("Success", "Doctor Added")
    clear_doctor()

def update_doctor():
    did_val = did.get().strip()

    if did_val == "":
        messagebox.showerror("Error", "Enter Doctor ID")
        return

    doctor = next((d for d in doctors if d.did == did_val), None)

    if doctor:
        doctor.name = dname.get()
        doctor.specialization = spec.get()

        messagebox.showinfo("Success", "Doctor Updated")
        clear_doctor()
    else:
        messagebox.showerror("Error", "Doctor not found")

def book_appointment():
    pid_val = ap_pid.get().strip()
    did_val = ap_did.get().strip()

    if pid_val == "" or did_val == "":
        messagebox.showerror("Error", "Enter IDs")
        return

    patient = next((p for p in patients if p.pid == pid_val), None)
    doctor = next((d for d in doctors if d.did == did_val), None)

    if patient and doctor:
        a = Appointment(patient, doctor, ap_date.get())
        appointments.append(a)
        messagebox.showinfo("Success", "Appointment Booked")
    else:
        messagebox.showerror("Error", "Invalid IDs")

def generate_bill():
    try:
        patient = next((p for p in patients if p.pid == bill_pid.get().strip()), None)

        if patient:
            b = Billing(patient, float(consult.get()), float(treatment.get()))
            total = b.calculate_total()
            messagebox.showinfo("Bill", f"Total Bill = ₹{total}")
        else:
            messagebox.showerror("Error", "Patient not found")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

def delete_doctor():
    did_val = did.get().strip()

    doctor = next((d for d in doctors if d.did == did_val), None)

    if doctor:
        doctors.remove(doctor)

        global appointments
        appointments = [a for a in appointments if a.doctor.did != did_val]

        messagebox.showinfo("Success", "Doctor Deleted")
        clear_doctor()
    else:
        messagebox.showerror("Error", "Doctor not found")

def clear_patient():
    pid.delete(0, tk.END)
    pname.delete(0, tk.END)
    age.delete(0, tk.END)
    disease.delete(0, tk.END)

def clear_doctor():
    did.delete(0, tk.END)
    dname.delete(0, tk.END)
    spec.delete(0, tk.END)

def show_data():
    for row in tree.get_children():
        tree.delete(row)

    for p in patients:
        tree.insert("", "end", values=(("Patient", p.pid, f"{p.name} | {p.disease}")))

    for d in doctors:
        tree.insert("", "end", values=("Doctor", d.did, d.name))

    for a in appointments:
        tree.insert("", "end", values=("Appointment", a.patient.pid, f"{a.patient.name} → {a.doctor.name}"))
# ---------------- UI ---------------- #

root = tk.Tk()
root.title("Hospital Management System")
root.geometry("800x600")
root.configure(bg="#e6f2ff")

title = tk.Label(root, text="Hospital Management System",
                 font=("Arial", 10, "bold"), bg="#4CAF50", fg="white")
title.pack(pady=10)

# -------- Frames -------- #
frame1 = tk.LabelFrame(root, text="Patient", padx=10, pady=10, bg="#ffffff")
frame1.place(x=20, y=70, width=350, height=220)

frame2 = tk.LabelFrame(root, text="Doctor", padx=10, pady=10, bg="#ffffff")
frame2.place(x=400, y=70, width=350, height=220)

frame3 = tk.LabelFrame(root, text="Appointment", padx=10, pady=10, bg="#ffffff")
frame3.place(x=20, y=260, width=350, height=180)

frame4 = tk.LabelFrame(root, text="Billing", padx=10, pady=10, bg="#ffffff")
frame4.place(x=400, y=260, width=350, height=180)

# -------- Patient -------- #
pid = tk.Entry(frame1); pid.grid(row=0, column=1)
pname = tk.Entry(frame1); pname.grid(row=1, column=1)
age = tk.Entry(frame1); age.grid(row=2, column=1)
disease = tk.Entry(frame1); disease.grid(row=3, column=1)

tk.Label(frame1, text="ID", bg="#ffffff").grid(row=0, column=0)
tk.Label(frame1, text="Name", bg="#ffffff").grid(row=1, column=0)
tk.Label(frame1, text="Age", bg="#ffffff").grid(row=2, column=0)
tk.Label(frame1, text="Disease", bg="#ffffff").grid(row=3, column=0)

tk.Button(frame1, text="Add", bg="#4CAF50", fg="white", width=10,
          command=add_patient).grid(row=4, column=0, pady=5)

tk.Button(frame1, text="Update", bg="blue", fg="white", width=10,
          command=update_patient).grid(row=4, column=1, pady=5)

tk.Button(frame1, text="Delete", bg="red", fg="white", width=10,
          command=delete_patient).grid(row=5, columnspan=2, pady=5)

# -------- Doctor -------- #
did = tk.Entry(frame2); did.grid(row=0, column=1)
dname = tk.Entry(frame2); dname.grid(row=1, column=1)
spec = tk.Entry(frame2); spec.grid(row=2, column=1)

tk.Label(frame2, text="ID", bg="#ffffff").grid(row=0, column=0)
tk.Label(frame2, text="Name", bg="#ffffff").grid(row=1, column=0)
tk.Label(frame2, text="Specialization", bg="#ffffff").grid(row=2, column=0)

tk.Button(frame2, text="Add", bg="#4CAF50", fg="white", width=10,
          command=add_doctor).grid(row=3, column=0, pady=5)

tk.Button(frame2, text="Update", bg="blue", fg="white", width=10,
          command=update_doctor).grid(row=3, column=1, pady=5)

tk.Button(frame2, text="Delete", bg="red", fg="white", width=10,
          command=delete_doctor).grid(row=4, columnspan=2, pady=5)

# -------- Appointment -------- #
ap_pid = tk.Entry(frame3); ap_pid.grid(row=0, column=1)
ap_did = tk.Entry(frame3); ap_did.grid(row=1, column=1)
ap_date = tk.Entry(frame3); ap_date.grid(row=2, column=1)

tk.Label(frame3, text="Patient ID", bg="#ffffff").grid(row=0, column=0)
tk.Label(frame3, text="Doctor ID", bg="#ffffff").grid(row=1, column=0)
tk.Label(frame3, text="Date", bg="#ffffff").grid(row=2, column=0)

tk.Button(frame3, text="Book", bg="#2196F3", fg="white",
          command=book_appointment).grid(row=3, columnspan=2, pady=5)

# -------- Billing -------- #
bill_pid = tk.Entry(frame4); bill_pid.grid(row=0, column=1)
consult = tk.Entry(frame4); consult.grid(row=1, column=1)
treatment = tk.Entry(frame4); treatment.grid(row=2, column=1)

tk.Label(frame4, text="Patient ID", bg="#ffffff").grid(row=0, column=0)
tk.Label(frame4, text="Consult Fee", bg="#ffffff").grid(row=1, column=0)
tk.Label(frame4, text="Treatment Cost", bg="#ffffff").grid(row=2, column=0)

tk.Button(frame4, text="Generate", bg="#FF9800", fg="white",
          command=generate_bill).grid(row=3, columnspan=2, pady=5)

# -------- Output -------- #
# -------- TABLE -------- #
columns = ("Type", "ID/Name", "Details")

tree = ttk.Treeview(root, columns=columns, show="headings", height=8)

tree.heading("Type", text="Type")
tree.heading("ID/Name", text="ID / Name")
tree.heading("Details", text="Details")

tree.column("Type", width=120, anchor="center")
tree.column("ID/Name", width=180, anchor="center")
tree.column("Details", width=350, anchor="center")

tree.place(x=50, y=460)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x=700, y=460, height=180)

tk.Button(root, text="Show All Data", bg="#333", fg="white",
          command=show_data).place(x=320, y=430)
root.mainloop()