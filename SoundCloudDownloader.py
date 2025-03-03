import os
import yt_dlp
import tkinter as tk
from tkinter import messagebox

def download_soundcloud_song():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Fehler", "Bitte eine SoundCloud-URL eingeben!")
        return
    
    output_dir = os.path.abspath("downloads"
    os.makedirs(output_dir, exist_ok=True)
                                 
    output_file = os.path.join(output_dir, "%(title)s.%(ext)s")

    status_label.config(text=f"Lade herunter: {url}")
    
    try:
        ydl_opts = {'outtmpl': output_file}
        with yt_dlp.YouTubeDL(ydl_opts) as ydl:
            ydl.download([url])

        status_label.config(text=f"Download abgeschlossen! Datei in '{output_dir}' gespeichert.")
    except Exception as e:
        status_label.config(text="Fehler beim Download.")
        messagebox.showerror("Fehler", f"Download fehlgeschlagen:\n{str(e)}")

def clear_input():
    url_entry.delete(0, tk.END) #Löscht die Eingabe

# GUI erstellen
root = tk.Tk()
root.title("SoundCloud Downloader")
root.geometry("400x250")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="SoundCloud URL eingeben:").pack()
url_entry = tk.Entry(frame, width=50)
url_entry.pack(pady=5)

button_frame = tk.Frame(frame)
button_frame.pack(pady=10)

download_button = tk.Button(button_frame, text="Download starten", command=download_soundcloud_song)
download_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Eingabe löschen", command=clear_input)
clear_button.pack(side=tk.LEFT, padx=5)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
