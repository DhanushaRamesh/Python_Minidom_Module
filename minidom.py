from xml.dom import minidom
import xml.dom.minidom

f=open("test_minidom.html","r")
document=minidom.parseString(f.read())
f.close()

for index in range(0,9,1):
	print("index",index)
	elem=document.getElementsByTagName("div")[index]
	if elem.getAttribute("id") == "3":
		print(elem.firstChild.nodeValue)
	if elem.getAttribute("attrib") == "1":
		print(elem.firstChild.nodeValue) 
	if elem.getAttribute("anything") == "1":
		print(elem.firstChild.nodeValue)
	if elem.getAttribute("random") == "1":
		print(elem.firstChild.nodeValue)
	if elem.getAttribute("choice") == "1":
		print(elem.firstChild.nodeValue)

for index in range(0,9,1):
	elem=document.getElementsByTagName("div")[index]
	if elem.getAttribute("id") == "3":
		elem.firstChild.nodeValue="LOL"
	if elem.getAttribute("attrib") == "1":
		elem.setAttribute("style","background-color:red;")
	if elem.getAttribute("anything") == "1":
		elem.setAttribute("style","color:blue;")
	if elem.getAttribute("random") == "1":
		elem.setAttribute("class","main")
	if elem.getAttribute("choice") == "1":
		elem.setAttribute("style","background-color:yellow;font-weight:999;")

data=str(document.toprettyxml(indent="", newl="", encoding=None)).replace("<?xml version=\"1.0\" ?>","")
f=open("test_minidom_new.html","w+")    # Writes all the changes into a new html file
f.write(data)
f.close()


	
