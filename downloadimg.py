import urllib.request
import random

#function to download web image through url

def download_img(url):
	name = random.randrange(1,1000)
	full_name = str(name) + ".jpg"
	urllib.request.urlretrieve(url,full_name)

#now pass the url of the image
download_img("https://images.unsplash.com/photo-1583483425038-23300a72b937?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80")
#now an image with random file name will be downloaded in your present working directory
