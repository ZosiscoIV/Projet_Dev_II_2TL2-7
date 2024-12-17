import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Pillow for image handling


class RestaurantManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestion du Restaurant")
        self.master.geometry("800x600")

        # Data
        self.tables = {i: {"status": "libre"} for i in range(1, 21)}
        self.status_colors = {
            "libre": "green",
            "occupée": "red",
            "nettoyage": "yellow",
            "réservée": "blue",
            "fusionnée": "purple"
        }

        # Store images to prevent garbage collection
        self.images = {}

        # Layout (centrer le canvas)
        self.main_frame = tk.Frame(self.master, bg="white")
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # Canvas pour afficher les tables
        self.content_frame = tk.Canvas(self.main_frame, bg="white")
        self.content_frame.pack(expand=True, fill=tk.BOTH)

        # Affichage des tables
        self.view_tables()

        # Contrôles pour changer manuellement l'état des tables
        self.control_frame = tk.Frame(self.master, bg="white")
        self.control_frame.pack(fill=tk.X, pady=10)
        self.add_controls()

    def view_tables(self):
        """Display tables on a tiled background."""
        # Draw the tiled background
        self.draw_tiled_background()

        # Draw tables
        x, y = 50, 50
        for table_number in self.tables:
            self.draw_table(x, y, table_number)
            x += 150
            if x > 650:  # Move to next row
                x = 50
                y += 150

    def draw_tiled_background(self):
        """Draw the tiled background (checkerboard pattern)."""
        tile_size = 50
        for i in range(0, 800, tile_size):
            for j in range(0, 600, tile_size):
                color = "lightgray" if (i // tile_size + j // tile_size) % 2 == 0 else "white"
                self.content_frame.create_rectangle(i, j, i + tile_size, j + tile_size, fill=color, outline="")

    def draw_table(self, x, y, table_number):
        """Draw a table with an image background and a color overlay."""
        status = self.tables[table_number]["status"]

        # Draw the table image (wood texture or similar)
        table_image = Image.open("table.png")  # Replace with your image path
        table_image = table_image.resize((100, 100))  # Resize if necessary
        table_photo = ImageTk.PhotoImage(table_image)
        self.images[table_number] = table_photo  # Keep a reference to avoid garbage collection

        # Draw the table image
        self.content_frame.create_image(x + 50, y + 50, image=table_photo, anchor="center", tags=f"table_{table_number}")

        # Add a colored overlay with simulated transparency
        color = self.get_table_color(status)
        self.content_frame.create_rectangle(
            x, y, x + 100, y + 100,
            fill=color, stipple="gray50", outline="", tags=f"table_{table_number}"
        )

        # Add table number
        self.content_frame.create_text(
            x + 50, y + 50,
            text=f"Table {table_number}",
            fill="white",
            font=("Arial", 12, "bold"),
            tags=f"table_{table_number}"
        )

        # Bind click event to the table
        self.content_frame.tag_bind(f"table_{table_number}", "<Button-1>", lambda event, t=table_number: self.change_table_status(t))

    def get_table_color(self, status):
        """Return the color representing table status."""
        return self.status_colors.get(status, "gray")

    def change_table_status(self, table):
        """Change the status of a table."""
        current_status = self.tables[table]["status"]
        next_status = {
            "libre": "occupée",
            "occupée": "nettoyage",
            "nettoyage": "libre",
            "réservée": "occupée",
            "fusionnée": "libre"
        }
        self.tables[table]["status"] = next_status[current_status]
        self.refresh_tables()

    def refresh_tables(self):
        """Refresh the tables view to update colors and statuses."""
        self.content_frame.delete("all")
        self.view_tables()

    def add_controls(self):
        """Add manual controls for changing table statuses."""
        tk.Label(self.control_frame, text="Numéro de table:", bg="white").pack(side=tk.LEFT, padx=5)
        self.table_entry = tk.Entry(self.control_frame, width=5)
        self.table_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(self.control_frame, text="Statut:", bg="white").pack(side=tk.LEFT, padx=5)
        self.status_selector = ttk.Combobox(
            self.control_frame,
            values=list(self.status_colors.keys()),
            state="readonly",
            width=10
        )
        self.status_selector.pack(side=tk.LEFT, padx=5)
        self.status_selector.current(0)  # Set default selection to "libre"

        tk.Button(
            self.control_frame,
            text="Appliquer",
            command=self.apply_status_change
        ).pack(side=tk.LEFT, padx=10)

    def apply_status_change(self):
        """Apply the selected status to the specified table."""
        try:
            table_number = int(self.table_entry.get())
            if table_number in self.tables:
                selected_status = self.status_selector.get()
                self.tables[table_number]["status"] = selected_status
                self.refresh_tables()
            else:
                tk.messagebox.showerror("Erreur", "Numéro de table invalide.")
        except ValueError:
            tk.messagebox.showerror("Erreur", "Veuillez entrer un numéro de table valide.")



# Create the application
root = tk.Tk()
app = RestaurantManager(root)
root.mainloop()
