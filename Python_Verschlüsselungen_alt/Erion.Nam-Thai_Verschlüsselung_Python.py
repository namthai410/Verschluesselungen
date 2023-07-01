import tkinter as tk
from tkinter import messagebox
import secrets

# Caesar-Verschlüsselung
def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# XOR-Verschlüsselung
def xor_encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return ciphertext

def xor_decrypt(ciphertext, key):
    return xor_encrypt(ciphertext, key)

# Sicherheitsmaßnahmen
def generate_random_key():
    return secrets.token_hex(16)

def validate_key(key):
    if not all(char in "0123456789abcdefABCDEF" for char in key):
        return False
    return True

# Seitenwechsel
def select_encryption():
    selected_encryption = encryption_var.get()
    if selected_encryption == "Caesar":
        caesar_frame.tkraise()
    elif selected_encryption == "XOR":
        xor_frame.tkraise()

# Verschlüsselungsfunktionen
def encrypt_text():
    if encryption_var.get() == "Caesar":
        text = caesar_plaintext_entry.get("1.0", "end-1c")
        shift = int(caesar_shift_entry.get())

        caesar_ciphertext = caesar_encrypt(text, shift)
        caesar_ciphertext_entry.delete("1.0", "end")
        caesar_ciphertext_entry.insert("1.0", caesar_ciphertext)

    elif encryption_var.get() == "XOR":
        text = xor_plaintext_entry.get("1.0", "end-1c")
        key = xor_key_entry.get()

        if not validate_key(key):
            messagebox.showerror("Fehler", "Ungültiger XOR-Schlüssel!")
            return

        xor_ciphertext = xor_encrypt(text, key)
        xor_ciphertext_entry.delete("1.0", "end")
        xor_ciphertext_entry.insert("1.0", xor_ciphertext)

def decrypt_text():
    if encryption_var.get() == "Caesar":
        ciphertext = caesar_ciphertext_entry.get("1.0", "end-1c")
        shift = int(caesar_shift_entry.get())

        caesar_plaintext = caesar_decrypt(ciphertext, shift)
        caesar_plaintext_entry.delete("1.0", "end")
        caesar_plaintext_entry.insert("1.0", caesar_plaintext)

    elif encryption_var.get() == "XOR":
        ciphertext = xor_ciphertext_entry.get("1.0", "end-1c")
        key = xor_key_entry.get()

        if not validate_key(key):
            messagebox.showerror("Fehler", "Ungültiger XOR-Schlüssel!")
            return

        xor_plaintext = xor_decrypt(ciphertext, key)
        xor_plaintext_entry.delete("1.0", "end")
        xor_plaintext_entry.insert("1.0", xor_plaintext)

# GUI erstellen
root = tk.Tk()
root.title("Verschlüsselungstool")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

# Menüseite
menu_frame = tk.Frame(root, bg="#f0f0f0")
menu_frame.pack(pady=10)

menu_label = tk.Label(menu_frame, text="Wählen Sie eine Verschlüsselungsart:", font=("Helvetica", 16), bg="#f0f0f0")
menu_label.pack()

encryption_var = tk.StringVar(value="Caesar")

caesar_radio = tk.Radiobutton(menu_frame, text="Caesar", variable=encryption_var, value="Caesar", font=("Helvetica", 12), bg="#f0f0f0")
caesar_radio.pack(pady=5)

xor_radio = tk.Radiobutton(menu_frame, text="XOR", variable=encryption_var, value="XOR", font=("Helvetica", 12), bg="#f0f0f0")
xor_radio.pack(pady=5)

select_button = tk.Button(menu_frame, text="Auswählen", font=("Helvetica", 12), bg="#0080ff", fg="white", command=select_encryption)
select_button.pack(pady=10)

# Caesar-Seite
caesar_frame = tk.Frame(root, bg="#f0f0f0")

caesar_shift_label = tk.Label(caesar_frame, text="Caesar-Verschiebung:", font=("Helvetica", 12), bg="#f0f0f0")
caesar_shift_label.pack(pady=5)

caesar_shift_entry = tk.Entry(caesar_frame, width=10, font=("Helvetica", 12))
caesar_shift_entry.pack()

caesar_plaintext_label = tk.Label(caesar_frame, text="Klartext:", font=("Helvetica", 12), bg="#f0f0f0")
caesar_plaintext_label.pack(pady=5)

caesar_plaintext_entry = tk.Text(caesar_frame, height=5, width=40, font=("Helvetica", 12))
caesar_plaintext_entry.pack()

caesar_ciphertext_label = tk.Label(caesar_frame, text="Chiffretext:", font=("Helvetica", 12), bg="#f0f0f0")
caesar_ciphertext_label.pack(pady=5)

caesar_ciphertext_entry = tk.Text(caesar_frame, height=5, width=40, font=("Helvetica", 12))
caesar_ciphertext_entry.pack()

caesar_button_frame = tk.Frame(caesar_frame, bg="#f0f0f0")
caesar_button_frame.pack(pady=10)

caesar_encrypt_button = tk.Button(caesar_button_frame, text="Verschlüsseln", font=("Helvetica", 12), bg="#0080ff", fg="white", command=encrypt_text)
caesar_encrypt_button.pack(side="left", padx=5)

caesar_decrypt_button = tk.Button(caesar_button_frame, text="Entschlüsseln", font=("Helvetica", 12), bg="#0080ff", fg="white", command=decrypt_text)
caesar_decrypt_button.pack(side="left", padx=5)

# XOR-Seite
xor_frame = tk.Frame(root, bg="#f0f0f0")

xor_key_label = tk.Label(xor_frame, text="XOR-Schlüssel:", font=("Helvetica", 12), bg="#f0f0f0")
xor_key_label.pack(pady=5)

xor_key_entry = tk.Entry(xor_frame, width=20, font=("Helvetica", 12))
xor_key_entry.pack()

xor_plaintext_label = tk.Label(xor_frame, text="Klartext:", font=("Helvetica", 12), bg="#f0f0f0")
xor_plaintext_label.pack(pady=5)

xor_plaintext_entry = tk.Text(xor_frame, height=5, width=40, font=("Helvetica", 12))
xor_plaintext_entry.pack()

xor_ciphertext_label = tk.Label(xor_frame, text="Chiffretext:", font=("Helvetica", 12), bg="#f0f0f0")
xor_ciphertext_label.pack(pady=5)

xor_ciphertext_entry = tk.Text(xor_frame, height=5, width=40, font=("Helvetica", 12))
xor_ciphertext_entry.pack()

xor_button_frame = tk.Frame(xor_frame, bg="#f0f0f0")
xor_button_frame.pack(pady=10)

xor_encrypt_button = tk.Button(xor_button_frame, text="Verschlüsseln", font=("Helvetica", 12), bg="#0080ff", fg="white", command=encrypt_text)
xor_encrypt_button.pack(side="left", padx=5)

xor_decrypt_button = tk.Button(xor_button_frame, text="Entschlüsseln", font=("Helvetica", 12), bg="#0080ff", fg="white", command=decrypt_text)
xor_decrypt_button.pack(side="left", padx=5)

# Standardseite festlegen
menu_frame.tkraise()

# GUI starten
root.mainloop()
