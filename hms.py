import tkinter as tk
from tkinter import messagebox, ttk
import uuid

# ---------------- DATA STORAGE ----------------
patients = {}
appointments = {}
bills = {}
equipment = {}

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("800x600")

# ---------------- FUNCTIONS ----------------

# ---- PATIENT ----
def add_patient():
    name = entry_name.get()
    age = entry_age.get()
    gender = combo_gender.get()
    contact = entry_contact.get()

    if name == "" or age == "":
        messagebox.showerror("Error", "Fill all required fields")
        return

    pid = "PAT-" + str(uuid.uuid4())[:5]

    patients[pid] = {
        "name": name,
        "age": age,
        "gender": gender,
        "contact": contact
    }

    messagebox.showinfo("Success", f"Patient Added: {pid}")
    clear_patient()

def search_patient():
    pid = entry_search.get()

    if pid in patients:
        p = patients[pid]
        result.set(f"{p}")
    else:
        result.set("Patient not found")

def clear_patient():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_contact.delete(0, tk.END)

# ---- APPOINTMENT ----
def book_appointment():
    pid = entry_pid.get()
    doctor = entry_doctor.get()
    date = entry_date.get()
    time = entry_time.get()

    if pid not in patients:
        messagebox.showerror("Error", "Invalid Patient ID")
        return

    # Overlap check
    for a in appointments.values():
        if a["doctor"] == doctor and a["date"] == date and a["time"] == time:
            messagebox.showerror("Error", "Slot already booked")
            return

    aid = "APT-" + str(uuid.uuid4())[:5]
    appointments[aid] = {
        "patient": pid,
        "doctor": doctor,
        "date": date,
        "time": time
    }

    messagebox.showinfo("Success", f"Appointment Booked: {aid}")

# ---- BILLING ----
def generate_bill():
    pid = entry_bill_pid.get()

    try:
        consult = float(entry_consult.get())
        lab = float(entry_lab.get())
        proc = float(entry_proc.get())
    except:
        messagebox.showerror("Error", "Enter valid numbers")
        return

    total = consult + lab + proc
    bid = "BILL-" + str(uuid.uuid4())[:5]

    bills[bid] = {
        "patient": pid,
        "total": total
    }

    messagebox.showinfo("Bill", f"{bid} | Total: ₹{total}")

# ---- EQUIPMENT ----
def add_equipment():
    name = entry_eq_name.get()
    model = entry_eq_model.get()

    eid = "EQ-" + str(uuid.uuid4())[:5]
    equipment[eid] = {
        "name": name,
        "model": model,
        "status": "Working"
    }

    messagebox.showinfo("Success", f"Equipment Added: {eid}")

def update_equipment():
    eid = entry_eq_id.get()
    status = combo_status.get()

    if eid in equipment:
        equipment[eid]["status"] = status
        messagebox.showinfo("Updated", "Status Updated")
    else:
        messagebox.showerror("Error", "Not found")

# ---------------- TABS ----------------
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# ---------------- PATIENT TAB ----------------
frame1 = tk.Frame(notebook)
notebook.add(frame1, text="Patient")

tk.Label(frame1, text="Name").pack()
entry_name = tk.Entry(frame1)
entry_name.pack()

tk.Label(frame1, text="Age").pack()
entry_age = tk.Entry(frame1)
entry_age.pack()

tk.Label(frame1, text="Gender").pack()
combo_gender = ttk.Combobox(frame1, values=["Male", "Female"])
combo_gender.pack()

tk.Label(frame1, text="Contact").pack()
entry_contact = tk.Entry(frame1)
entry_contact.pack()

tk.Button(frame1, text="Add Patient", command=add_patient).pack(pady=5)

tk.Label(frame1, text="Search Patient ID").pack()
entry_search = tk.Entry(frame1)
entry_search.pack()

result = tk.StringVar()
tk.Label(frame1, textvariable=result).pack()

tk.Button(frame1, text="Search", command=search_patient).pack()

# ---------------- APPOINTMENT TAB ----------------
frame2 = tk.Frame(notebook)
notebook.add(frame2, text="Appointment")

tk.Label(frame2, text="Patient ID").pack()
entry_pid = tk.Entry(frame2)
entry_pid.pack()

tk.Label(frame2, text="Doctor").pack()
entry_doctor = tk.Entry(frame2)
entry_doctor.pack()

tk.Label(frame2, text="Date").pack()
entry_date = tk.Entry(frame2)
entry_date.pack()

tk.Label(frame2, text="Time").pack()
entry_time = tk.Entry(frame2)
entry_time.pack()

tk.Button(frame2, text="Book Appointment", command=book_appointment).pack(pady=10)

# ---------------- BILLING TAB ----------------
frame3 = tk.Frame(notebook)
notebook.add(frame3, text="Billing")

tk.Label(frame3, text="Patient ID").pack()
entry_bill_pid = tk.Entry(frame3)
entry_bill_pid.pack()

tk.Label(frame3, text="Consultation").pack()
entry_consult = tk.Entry(frame3)
entry_consult.pack()

tk.Label(frame3, text="Lab Charges").pack()
entry_lab = tk.Entry(frame3)
entry_lab.pack()

tk.Label(frame3, text="Procedure Cost").pack()
entry_proc = tk.Entry(frame3)
entry_proc.pack()

tk.Button(frame3, text="Generate Bill", command=generate_bill).pack(pady=10)

# ---------------- EQUIPMENT TAB ----------------
frame4 = tk.Frame(notebook)
notebook.add(frame4, text="Equipment")

tk.Label(frame4, text="Equipment Name").pack()
entry_eq_name = tk.Entry(frame4)
entry_eq_name.pack()

tk.Label(frame4, text="Model").pack()
entry_eq_model = tk.Entry(frame4)
entry_eq_model.pack()

tk.Button(frame4, text="Add Equipment", command=add_equipment).pack(pady=5)

tk.Label(frame4, text="Equipment ID").pack()
entry_eq_id = tk.Entry(frame4)
entry_eq_id.pack()

tk.Label(frame4, text="Status").pack()
combo_status = ttk.Combobox(frame4, values=["Working", "Maintenance"])
combo_status.pack()

tk.Button(frame4, text="Update Status", command=update_equipment).pack(pady=10)

# ---------------- RUN ----------------
root.mainloop()