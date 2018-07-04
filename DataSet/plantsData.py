from google_images_download import google_images_download as gid

plants = []

fileRead = open('plantNames.csv')

for i in fileRead:
	plants.append(i)

response = gid.googleimagesdownload()

for i in plants:
	arguments = {"keywords": i, "limit": 10, "print_urls": True}
	paths = response.download(arguments)
	print(paths)
