import tkinter as tk
import folium 
import webbrowser

def execute():
	a = float(entry.get())
	b = float(entry1.get())
	map = folium.Map(location = [a,b])
	map.save("Map.html")
	url =  "file:///E:/web/python/project_1/Map.html"
	webbrowser.open(url,new = 1)

root = tk.Tk();

f = tk.Frame(root,height = 50,width = 50)
f.pack()

L1 = tk.Label(f,text = "Enter the latitude")
L1.grid(row=0,column = 0)

entry = tk.Entry(f)
entry.grid(row = 0,column =1)

L2 = tk.Label(f,text = "Enter the longitude")
L2.grid(row = 1,column =0)

entry1 = tk.Entry(f)
entry1.grid(row = 1,column =1)


button = tk.Button(root,text = "Search",command = execute)
button.bind("<Button -1>",execute)
button.pack()

root.mainloop()