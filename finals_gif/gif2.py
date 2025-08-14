import imageio as io

file_name = [r'C:\Users\NOYE\Desktop\Codedex\Finals\chicklet1.png', r'C:\Users\NOYE\Desktop\Codedex\Finals\chicklet2.png',
             r'C:\Users\NOYE\Desktop\Codedex\Finals\chicklet3.png', r'C:\Users\NOYE\Desktop\Codedex\Finals\chicklet4.png']

image = []

for file in file_name:
    image.append(io.imread(file))


io.mimwrite('team2.gif', image, plugin='pillow', plugin_kwargs={'duration': 0.5, 'loop': 0})

#to run the file and print where it was saved to:
import os
print("GIF saved to:", os.path.abspath('team2.gif'))
os.startfile('team2.gif')