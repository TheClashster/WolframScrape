from bs4 import BeautifulSoup
import requests

url = 'http://education.wolfram.com/summer/camp/alumni/2017/'
page = requests.get(url)
html = BeautifulSoup(page.text, "html.parser")
# TODO: Add error handling
data_path = html.find("div", class_="col main alumni-list").find_all('li')
data = {}
for link in data_path:
	data[link.string] = 'http://education.wolfram.com/summer/camp/alumni/2017/{}'.format(link.find('a').get('href'))
	
def getProject(url):
	page = requests.get(url)
	html = BeautifulSoup(page.text, "html.parser")
	proj = html.find("div", class_="alumni-copy add-img-border")
	return proj
f = open('um_only_the_projects.txt', 'w')
i = 1
for key in data.keys():
	value = data[key]
	try:
		project = getProject(value)
		project_link = project.find('a')
		f.write(str(i) + '.' + ' ' + key.encode('ascii', 'ignore').decode('utf-8') + '\n')
		if project_link is not None:
			f.writelines(project_link.get_text().encode('ascii', 'ignore').decode('utf-8') + '\n')
			f.write(project_link.get('href'))
		f.write('\n'+'-'*15+'\n')
	except UnicodeError:
		print(f'Error for {key}')
		continue
	i+=1
	print(f'Wrtten to file for {key}')
f.close()
print('done.')