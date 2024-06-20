import tkinter as tk
from tkinter import messagebox
import datetime
import sqlite3
 
def check_and_download_data():
    start_date_str = start_date_entry.get()
    end_date_str = end_date_entry.get()
    
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
        
        messagebox.showinfo("Info", f"Daten fuer Zeitraum {start_date_str} bis {end_date_str} werden heruntergeladen.")
        
        # Placeholder for download logic
        # Implement logic to download data and insert into SQLite
        
    except ValueError:
        messagebox.showerror("Fehler", "Ungueltiges Datumsformat. Verwenden Sie das Format YYYY-MM-DD.")
 
def insert_data(date, time, sensor_id, pm25, pm10, location):
    c.execute("INSERT INTO messungen VALUES (?, ?, ?, ?, ?, ?)", (date, time, sensor_id, pm25, pm10, location))
    conn.commit()
 
def calculate_average(start_date, end_date):
    c.execute("SELECT AVG(pm25), AVG(pm10) FROM messungen WHERE datum BETWEEN ? AND ?", (start_date, end_date))
    result = c.fetchone()
    return result
 
def export_graph():
 grafik_canvas.postscript(file="grafik.ps", colormode='color')
 messagebox.showinfo("Export erfolgreich", "Die grafische Darstellung wurde erfolgreich exportiert.")
 
main_window = tk.Tk()
main_window.title("All in One")
main_window.geometry("1100x700")
 
title_label = tk.Label(main_window, text="Feinstaubanalyse", font=("Arial", 20))
title_label.pack(pady=10)
 
frame_zeitraum = tk.Frame(main_window, bd=2, relief="groove")
frame_zeitraum.pack(fill="x", padx=10, pady=10)
 
zeitraum_label = tk.Label(frame_zeitraum, text="Zeitraum auswaehlen: von")
zeitraum_label.grid(row=0, column=0, padx=5, pady=5)
 
start_date_entry = tk.Entry(frame_zeitraum)
start_date_entry.grid(row=0, column=1, padx=5, pady=5)
 
zeitraum_bis_label = tk.Label(frame_zeitraum, text="bis")
zeitraum_bis_label.grid(row=0, column=2, padx=5, pady=5)
 
end_date_entry = tk.Entry(frame_zeitraum)
end_date_entry.grid(row=0, column=3, padx=5, pady=5)
 
frame_durchschnitt = tk.Frame(main_window, bd=2, relief="groove")
frame_durchschnitt.pack(fill="x", padx=10, pady=10)
 
durchschnitt_label = tk.Label(frame_durchschnitt, text="Durchschnittswerte", font=("Arial", 15))
durchschnitt_label.pack(pady=5)
 
frame_grafik = tk.Frame(main_window, bd=2, relief="groove")
frame_grafik.pack(fill="x", padx=10, pady=10)
 
grafik_label = tk.Label(frame_grafik, text="Grafische Darstellung", font=("Arial", 15))
grafik_label.pack(pady=5)
 
grafik_canvas = tk.Canvas(frame_grafik, width=1000, height=400, bg="white")
grafik_canvas.pack(pady=10)
 
export_button = tk.Button(main_window, text="Grafische Darstellung exportieren", command=export_graph)
export_button.pack(pady=10)
 
conn = sqlite3.connect('luftdaten.db')
c = conn.cursor()
 
c.execute('''CREATE TABLE IF NOT EXISTS messungen (
             datum TEXT,
             uhrzeit TEXT,
             sensor_id TEXT,
             pm25 REAL,
             pm10 REAL,
             standort TEXT)''')
 
main_window.mainloop()