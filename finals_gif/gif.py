import imageio as iio
# Get files and store in list
# empty list for quick gif creation
# put first picture then second picture
# duration

file_names = [r'C:\Users\NOYE\Desktop\Codedex\Finals\team-pic1.png', r'C:\Users\NOYE\Desktop\Codedex\Finals\team-pic2.png']

image = []

for file in file_names:
    image.append(iio.imread(file))

iio.mimwrite('team.gif', image, plugin='pillow', plugin_kwargs={'duration': 0.5, 'loop': 0})


import os
print("GIF saved to:", os.path.abspath('team.gif'))
os.startfile('team.gif')

#I think the gif created doesn't run more than once in windows photo viewers or I'm wrong