import tkinter as tk
import folium 
import webbrowser
def execute():				#this function fetches the value for longitude and latitude 
	a = float(entry.get())	#and then open saved html file in web browser
	b = float(entry1.get())
	map = folium.Map(location = [a,b])
	map.save("Map.html")
	url =  "file:///E:/web/python/project_1/Map.html"
	webbrowser.open(url,new = 1)

def marker():				#when user want to mark a location at that time this fun will mark it 
	a = float(entry.get())	#and then open saved html file in web browser
	b = float(entry1.get())
	fg = folium.FeatureGroup(name = "My map")
	fg.add_child(folium.Marker(location= [a,b],popup = "Welcome to Earth",icon = folium.Icon(color = "green")))
	map = folium.Map(location = [a,b])
	map.add_child(fg)
	map.save("Map.html")
	url =  "file:///E:/web/python/project_1/Map.html"
	webbrowser.open(url,new = 1)


root = tk.Tk();

f = tk.Frame(root,height = 50,width = 50)
f.grid()

L1 = tk.Label(f,text = "Enter the latitude")
L1.grid(row=0,column = 0)

entry = tk.Entry(f)
entry.grid(row = 0,column =1)

L2 = tk.Label(f,text = "Enter the longitude")
L2.grid(row = 1,column =0)

entry1 = tk.Entry(f)
entry1.grid(row = 1,column =1)


button = tk.Button(root,text = "   Search   ",command = execute)
button.bind("<Button -1>",execute)
button.grid(row = 3,column = 0)

markerbutton = tk.Button(root,text = "Mark Location", command = marker)
markerbutton.bind("<Button-1>",marker)
markerbutton.grid(row = 4,column = 0)

root.mainloop()