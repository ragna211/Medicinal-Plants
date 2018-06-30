import google_images_download as gid

plants = ["Tailspatra", "Ulatkambal", "Gunja", "Kankati", "Babul", "Catechu", "Shikakai", "Gandana", "Apamarga", "Atis", "Bachnag", "Bach", "Adulsa", "Bael", "Siris", "Onions", "Garlic", "Ghrita Kumari", "Khulanjan", "Saptaparna", "Akarkara", "Kalmegh", "Suwa", "Rohitika", "Ajmod", "Samudra Palak"]

response = gid.googleimagesdownload()

for i in plants:
	arguments = {"keywords": i, "limit": 10, "print_urls": True}
	paths = response.download(arguments)
	print(paths)
