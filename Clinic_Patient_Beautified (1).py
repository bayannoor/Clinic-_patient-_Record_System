import json

FILENAME = "patients data.json"

# ------------------ Data Handling ------------------

def load_data():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

# ------------------ Patient Management ------------------

def register_patient(data):
    print("\n🔹 Register New Patient")
    patient_id = len(data) + 1
    name = input("👤 Enter patient name: ")
    age = input("🎂 Enter age: ")
    gender = input("⚧️ Enter gender (M/F): ")
    symptoms = input("🤒 Enter symptoms: ")

    patient = {
        "ID": patient_id,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Symptoms": symptoms,
        "Status": "Under Observation"
    }

    data.append(patient)
    save_data(data)
    print("✅ Patient registered successfully!\n")

def search_patient(data):
    print("\n🔍 Search Patient Record")
    keyword = input("🔎 Enter patient name or ID to search: ").lower()
    found = False

    for patient in data:
        if str(patient["ID"]) == keyword or patient["Name"].lower() == keyword:
            print("\n✅ Patient Found:")
            for key, value in patient.items():
                print(f"  {key}: {value}")
            found = True
            break

    if not found:
        print("❌ Patient not found.")

def update_status(data):
    print("\n📝 Update Patient Status")
    id_to_update = input("🔁 Enter patient ID to update status: ")

    for patient in data:
        if str(patient["ID"]) == id_to_update:
            new_status = input("🔄 Enter new status (Treated / Under Observation): ")
            patient["Status"] = new_status
            save_data(data)
            print("✅ Status updated successfully.")
            return

    print("❌ Patient ID not found.")

def delete_patient(data):
    print("\n🗑️ Delete Patient Record")
    id_to_delete = input("❗ Enter patient ID to delete: ")

    for patient in data:
        if str(patient["ID"]) == id_to_delete:
            data.remove(patient)
            save_data(data)
            print("✅ Patient record deleted.")
            return

    print("❌ Patient not found.")

def display_all(data):
    print("\n📋 Displaying All Patients")
    if not data:
        print("⚠️ No patient records found.")
    else:
        for patient in data:
            print(f"🆔 ID: {patient['ID']}, 👤 Name: {patient['Name']}, 📌 Status: {patient['Status']}")

# ------------------ Main Menu ------------------

def menu():
    data = load_data()
    while True:
        print("\n" + "=" * 45)
        print("      🏥 Clinic Patient Record System      ")
        print("=" * 45)
        print("1. 📝 Register new Patient")
        print("2. 🔍 Search Patient")
        print("3. 🔄 Update Patient status")
        print("4. 🗑️ Delete Patient Record")
        print("5. 📋 Display all patients")
        print("6. ❌ Exit")

        choice = input("➡️  Enter your choice (1-6): ")

        if choice == "1":
            register_patient(data)
        elif choice == "2":
            search_patient(data)
        elif choice == "3":
            update_status(data)
        elif choice == "4":
            delete_patient(data)
        elif choice == "5":
            display_all(data)
        elif choice == "6":
            print("👋 Exiting system... Thank you!")
            break
        else:
            print("⚠️ Invalid choice, please try again!")

# ------------------ Start Program ------------------

menu()
