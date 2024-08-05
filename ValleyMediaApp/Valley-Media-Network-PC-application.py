import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("KASHIR MATAMDARI computer app!")

custom_font = ("Helvetica", 16)
label = tk.Label(root, text="Welcome to our computer app!", font=custom_font)
label.pack()

frm = ttk.Frame(root, padding=10)
frm.pack()

ttk.Label(frm, text="""
                Today's news:
        1- Nouha in Budgam was during this year.
        2- Marsya was someday in this year.






 ______   __      
/_  __/  / /  ___ 
 / /    / _ \/ -_)
/_/    /_//_/\__/ 
                  
   ____           __
  / __/  ___  ___/ /
 / _/   / _ \/ _  / 
/___/  /_//_/\_,_/  
                    
  ____    ___
 / __ \  / _/
/ /_/ / / _/ 
\____/ /_/   
             
 ______   __      
/_  __/  / /  ___ 
 / /    / _ \/ -_)
/_/    /_//_/\__/ 
                  
   _  __                  
  / |/ / ___  _    __  ___
 /    / / -_)| |/|/ / (_-<
/_/|_/  \__/ |__,__/ /___/
                          

                
        
""").pack()
ttk.Button(frm, text="Quit", command=root.destroy).pack()
root.mainloop()
