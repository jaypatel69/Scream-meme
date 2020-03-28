import serial
import praw
import config
#logging into reddit
try:
	reddit=praw.Reddit(client_id=config.client_id,
					   client_secret=config.client_secret,
					   username=config.username,
					   password=config.password,
					   user_agent="Scream powered memes")
	print("Login Successful")

except Exception as e:
	print("Login failed")
	print(e)


#defining the serial monitor
arduino=serial.Serial("COM8", 9600, timeout=0.1)


#defining a class for reading serial data from arduino
class GetSerialMonitor:
    def __init__(self):
        pass

    def getSerialData(self):
        self.data = arduino.readline()[:-2]
        if self.data:
            self.data=self.data.decode("utf-8")
            print(self.data)
            return self.data

    def closeSerialData(self):
        arduino.close()


#defining the class object of GetSerialMonitor
def postImage():
	try:
		print("Uploading image to reddit")
		#here r/u_6reposts9 is my own profile
		title = 'My favorite picture'
		image = 'images/yt.jpeg'
		#reddit.subreddit('r/u_6reposts9').submit_image(title, image)
		reddit.redditor("_jaypatel").message("masth ayindi","Orraku ra ayya")
		print("Image upload successful")

	except Exception as e:
		print("Something went wrong")
		print(e)

s=GetSerialMonitor()

while True:
	value=s.getSerialData()
	if value=="TRUE":
		print("sound level exceeded\n")
		print("posting a meme in reddit")
		postImage()
		exit()
	else:
		print("sound level is in threshold\n")












