import tkinter as tk
from tkinter import messagebox


class RestaurantManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestion du Restaurant")
        self.master.geometry("800x600")

        # Data
        self.tables = {i: {"status": "libre", "orders": []} for i in range(1, 21)}
        self.reservations = []
        self.current_view = "tables"

        # Layout
        self.menu_buttons()
        self.content_frame = tk.Frame(self.master)
        self.content_frame.pack(expand=True, fill=tk.BOTH)
        self.update_view()

    def menu_buttons(self):
        """Create top navigation buttons."""
        menu_frame = tk.Frame(self.master)
        menu_frame.pack(fill=tk.X)

        tk.Button(menu_frame, text="Tables", command=lambda: self.switch_view("tables")).pack(side=tk.LEFT, padx=5)
        tk.Button(menu_frame, text="Réservations", command=lambda: self.switch_view("reservations")).pack(side=tk.LEFT,
                                                                                                          padx=5)
        tk.Button(menu_frame, text="Commandes", command=lambda: self.switch_view("orders")).pack(side=tk.LEFT, padx=5)

    def switch_view(self, view):
        """Change the active view."""
        self.current_view = view
        self.update_view()

    def update_view(self):
        """Refresh content based on the current view."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if self.current_view == "tables":
            self.view_tables()
        elif self.current_view == "reservations":
            self.view_reservations()
        elif self.current_view == "orders":
            self.view_orders()

    def view_tables(self):
        """Display tables and their statuses."""
        # Créer un cadre pour contenir les tables et le centrer
        table_frame = tk.Frame(self.content_frame)
        table_frame.pack(expand=True)

        # Créer une grille pour les tables (4 lignes x 5 colonnes)
        row = 0
        col = 0
        for table, data in self.tables.items():
            btn = tk.Button(
                table_frame,
                text=f"Table {table}\n{data['status']}",
                bg=self.get_table_color(data['status']),
                command=lambda t=table: self.change_table_status(t),
                width=15, height=3
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

            # Passer à la colonne suivante
            col += 1
            # Si la colonne atteint 5, on passe à la ligne suivante
            if col == 5:
                col = 0
                row += 1

        # Faire en sorte que les colonnes et lignes occupent tout l'espace disponible, mais avec une taille contrôlée
        for i in range(4):  # 4 lignes
            table_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):  # 5 colonnes
            table_frame.grid_columnconfigure(i, weight=1)

    def view_reservations(self):
        """Display and manage reservations."""
        # Afficher les réservations existantes
        for res in self.reservations:
            res_frame = tk.Frame(self.content_frame)
            res_frame.pack(pady=5)

            tk.Label(res_frame, text=f"Client: {res['client']} - Table: {res['table']} - Date: {res['date']} - "
                                     f"Heure: {res['time']} - Tél: {res['phone']}").pack(side=tk.LEFT, padx=5)

            # Boutons "Modifier" et "Annuler"
            tk.Button(res_frame, text="Modifier", command=lambda r=res: self.modify_reservation(r)).pack(side=tk.LEFT,
                                                                                                          padx=5)
            tk.Button(res_frame, text="Annuler", command=lambda r=res: self.cancel_reservation(r)).pack(side=tk.LEFT,
                                                                                                        padx=5)

        # Formulaire pour ajouter une réservation
        add_res_frame = tk.Frame(self.content_frame)
        add_res_frame.pack(pady=20)

        tk.Label(add_res_frame, text="Nom du client:").pack(side=tk.LEFT, padx=5)
        self.client_entry = tk.Entry(add_res_frame)
        self.client_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(add_res_frame, text="Table:").pack(side=tk.LEFT, padx=5)
        self.table_entry = tk.Entry(add_res_frame, width=5)
        self.table_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(add_res_frame, text="Date (JJ/MM/AAAA):").pack(side=tk.LEFT, padx=5)
        self.date_entry = tk.Entry(add_res_frame, width=10)
        self.date_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(add_res_frame, text="Heure (HH:MM):").pack(side=tk.LEFT, padx=5)
        self.time_entry = tk.Entry(add_res_frame, width=8)
        self.time_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(add_res_frame, text="Numéro de téléphone:").pack(side=tk.LEFT, padx=5)
        self.phone_entry = tk.Entry(add_res_frame, width=15)
        self.phone_entry.pack(side=tk.LEFT, padx=5)

        tk.Button(add_res_frame, text="Ajouter", command=self.add_reservation).pack(side=tk.LEFT, padx=5)

    def view_orders(self):
        """Display and manage orders."""
        tk.Label(self.content_frame, text="Section commandes à venir...").pack(pady=10)

    def get_table_color(self, status):
        """Return the color representing table status."""
        return {"libre": "green", "occupée": "red", "réservée": "yellow"}.get(status, "gray")

    def change_table_status(self, table):
        """Change the status of a table."""
        current_status = self.tables[table]["status"]
        next_status = {"libre": "occupée", "occupée": "réservée", "réservée": "libre"}
        self.tables[table]["status"] = next_status[current_status]
        self.update_view()

    def add_reservation(self):
        """Add a new reservation after confirmation."""
        client = self.client_entry.get()
        try:
            table = int(self.table_entry.get())
            date = self.date_entry.get()
            time = self.time_entry.get()
            phone = self.phone_entry.get()

            # Vérifier si les champs sont remplis
            if not client or not date or not time or not phone:
                messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
                return

            # Confirmation des informations avant ajout
            confirm_msg = f"Confirmer la réservation ?\nClient: {client}\nTable: {table}\nDate: {date}\nHeure: {time}\nTél: {phone}"
            if messagebox.askyesno("Confirmation", confirm_msg):
                if table in self.tables and self.tables[table]["status"] == "libre":
                    self.reservations.append({"client": client, "table": table, "date": date, "time": time, "phone": phone})
                    self.tables[table]["status"] = "réservée"
                    self.update_view()
                else:
                    messagebox.showerror("Erreur", "Table non disponible ou invalide.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un numéro de table valide.")

    def cancel_reservation(self, reservation):
        """Cancel an existing reservation."""
        # Annuler la réservation
        self.reservations.remove(reservation)
        self.tables[reservation["table"]]["status"] = "libre"
        self.update_view()

    def modify_reservation(self, reservation):
        """Modify an existing reservation."""
        # Modifier une réservation
        self.client_entry.delete(0, tk.END)
        self.client_entry.insert(0, reservation["client"])

        self.table_entry.delete(0, tk.END)
        self.table_entry.insert(0, reservation["table"])

        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, reservation["date"])

        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, reservation["time"])

        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, reservation["phone"])

        # Changer le bouton "Ajouter" en "Mettre à jour"
        add_button = tk.Button(self.content_frame, text="Mettre à jour", command=lambda: self.update_reservation(reservation))
        add_button.pack(side=tk.LEFT, padx=5)

    def update_reservation(self, reservation):
        """Update an existing reservation."""
        client = self.client_entry.get()
        table = int(self.table_entry.get())
        date = self.date_entry.get()
        time = self.time_entry.get()
        phone = self.phone_entry.get()

        # Vérifier si les champs sont remplis
        if not client or not date or not time or not phone:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        # Confirmation avant la mise à jour
        confirm_msg = f"Confirmer la mise à jour de la réservation ?\nClient: {client}\nTable: {table}\nDate: {date}\nHeure: {time}\nTél: {phone}"
        if messagebox.askyesno("Confirmation", confirm_msg):
            reservation["client"] = client
            reservation["table"] = table
            reservation["date"] = date
            reservation["time"] = time
            reservation["phone"] = phone
            self.update_view()


# Create the application
root = tk.Tk()
app = RestaurantManager(root)
root.mainloop()
