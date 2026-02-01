import tkinter as tk
from tkinter import messagebox, scrolledtext


total_propertie = {
    "B12-3AB": {"cost": 153450, "mortgage": 112345},
    "B13-4CD": {"cost": 212130, "mortgage": 180234},
    "B14-5GH": {"cost": 120100, "mortgage": 85980},
    "B15-6JK": {"cost": 135230, "mortgage": 101321},
    "B16-7MO": {"cost": 183230, "mortgage": 130234}
}

property_entries = {
    "B12-3AB": [],
    "B13-4CD": [],
    "B14-5GH": [],
    "B15-6JK": [],
    "B16-7MO": []
}



def add_entry():
    prop_id = entry_id.get().strip().upper()
    description = entry_desc.get().strip()

    if prop_id not in total_propertie:
        messagebox.showerror("Error", "Invalid Property ID")
        return

    try:
        amount = float(entry_amount.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a numeric amount")
        return

    entry = {"description": description, "amount": amount}
    property_entries[prop_id].append(entry)

    messagebox.showinfo("Success", "Entry Added Successfully")

    entry_desc.delete(0, tk.END)
    entry_amount.delete(0, tk.END)


def show_summary():
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, "Property Summary\n\n")

    for prop_id in total_propertie:
        cost = total_propertie[prop_id]["cost"]
        mortgage = total_propertie[prop_id]["mortgage"]
        repairs = 0
        rents = 0

        for entry in property_entries[prop_id]:
            value = entry["amount"]
            if value >= 0:
                rents += value
            else:
                repairs += abs(value)

        amended_cost = cost + repairs
        rent_percent = (rents / mortgage * 100) if mortgage != 0 else 0

        text_box.insert(tk.END,
            f"{prop_id} | Cost: {cost} | Repairs: {repairs} | "
            f"Amended: {amended_cost} | Mortgage: {mortgage} | "
            f"Rents: {rents} | Rent%: {rent_percent:.2f}%\n"
        )



root = tk.Tk()
root.title("Property Rental Management System")
root.geometry("650x500")

tk.Label(root, text="Property ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Description").pack()
entry_desc = tk.Entry(root)
entry_desc.pack()

tk.Label(root, text="Amount (+rent / -expense)").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Button(root, text="Add Entry", command=add_entry).pack(pady=5)
tk.Button(root, text="Show Summary", command=show_summary).pack(pady=5)

text_box = scrolledtext.ScrolledText(root, width=75, height=15)
text_box.pack(pady=10)

root.mainloop()
