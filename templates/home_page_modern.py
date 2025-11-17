import customtkinter as ctk
import os
from tkinter import messagebox

# ================= PROJECT FUNCTIONS =================
def open_eye_tracking():
    try:
        messagebox.showinfo("Launching", "Opening Eye Tracking Cursor...")
        os.system("python eye_tracking_cursor.py")
    except Exception as e:
        messagebox.showerror("Error", f"Cannot open project:\n{e}")

def open_invisible_cloak():
    try:
        messagebox.showinfo("Launching", "Opening Invisible Cloak...")
        os.system("python invisible_cloak.py")
    except Exception as e:
        messagebox.showerror("Error", f"Cannot open project:\n{e}")

# ================= MAIN WINDOW =================
ctk.set_appearance_mode("Dark")   # Modes: Dark, Light, System
ctk.set_default_color_theme("blue")  # Themes: blue, dark-blue, green

root = ctk.CTk()
root.geometry("700x500")
root.title("AI Innovation Projects")

# ================= TITLE =================
title_label = ctk.CTkLabel(
    root, text="AI INNOVATION PROJECTS", 
    font=ctk.CTkFont(size=24, weight="bold")
)
title_label.pack(pady=20)

# ================= EYE TRACKING PROJECT =================
eye_frame = ctk.CTkFrame(root, corner_radius=15, border_width=2, fg_color="#4a69bd")
eye_frame.pack(padx=20, pady=15, fill="x")

eye_label = ctk.CTkLabel(
    eye_frame, text="👁️ Eye Tracking Cursor",
    font=ctk.CTkFont(size=18, weight="bold"), fg_color="#4a69bd"
)
eye_label.pack(anchor="w", padx=15, pady=8)

eye_desc = ctk.CTkLabel(
    eye_frame,
    text="Control your computer mouse using your eye movement with AI and webcam.",
    font=ctk.CTkFont(size=13), wraplength=650, justify="left", fg_color="#4a69bd"
)
eye_desc.pack(anchor="w", padx=15)

eye_button = ctk.CTkButton(
    eye_frame, text="Open Project", command=open_eye_tracking,
    corner_radius=10, fg_color="#1e3799", hover_color="#162b66", width=150
)
eye_button.pack(pady=10)

# ================= INVISIBLE CLOAK PROJECT =================
cloak_frame = ctk.CTkFrame(root, corner_radius=15, border_width=2, fg_color="#8c7ae6")
cloak_frame.pack(padx=20, pady=10, fill="x")

cloak_label = ctk.CTkLabel(
    cloak_frame, text="🧥 Harry Potter Invisible Cloak",
    font=ctk.CTkFont(size=18, weight="bold"), fg_color="#8c7ae6"
)
cloak_label.pack(anchor="w", padx=15, pady=8)

cloak_desc = ctk.CTkLabel(
    cloak_frame,
    text="Make yourself invisible using a special color cloak with computer vision.",
    font=ctk.CTkFont(size=13), wraplength=650, justify="left", fg_color="#8c7ae6"
)
cloak_desc.pack(anchor="w", padx=15)

cloak_button = ctk.CTkButton(
    cloak_frame, text="Open Project", command=open_invisible_cloak,
    corner_radius=10, fg_color="#6c5ce7", hover_color="#5a4bcf", width=150
)
cloak_button.pack(pady=10)

# ================= EXIT BUTTON =================
exit_button = ctk.CTkButton(
    root, text="Exit", command=root.destroy,
    corner_radius=10, fg_color="#eb4d4b", hover_color="#c0392b", width=120
)
exit_button.pack(pady=20)

root.mainloop()
