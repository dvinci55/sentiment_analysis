
#!/usr/bin/python

import matplotlib
matplotlib.use( 'Agg' )
import pylab

with open('count.txt', 'r') as my_file:
	text = my_file.read()
	#text = text.replace(",", "\n")

word=text.split(",")
print(word[0])
print(word[1])
x = [1] 
y = [word[0]] 
x2 = [2] 
y2 = [word[1]] 
pylab.bar(x, y, align = 'center') 
pylab.bar(x2, y2, color = 'g', align = 'center') 
pylab.title('Sentimental Analysis on Amazon Product Review') 
pylab.ylabel('Percentage(%)') 
pylab.xlabel('Positive & Negative Reviews')  
pylab.savefig("image.png")


