import os
import sys
import requests
from secrets import token, username

path = 'C:/Coding/my-repositories'


def prompt():
	project_name = input("Enter your project's name: ")
	private_input = input('Do you want your repository to be private? (Y/N): ')
	private = False

	if private_input == 'N':
			private = True

	create_dir(project_name)
	create_repo(project_name, private)
	setup(project_name)


def create_dir(project_name):
	project_name = 
	os.system(f'cd {path} && mkdir {project_name}')


def create_repo(project_name, private):
	url = 'https://api.github.com'
	if private:
		data = '{"name": "' + project_name + '", "private": true}'
	else:
		data = '{"name": "' + project_name + '", "private": false}'
	headers = {
		'Authorization': 'token ' + token,
		'Accept': 'application/vnd.github.v3+json'
	}
	response = requests.request('POST', f'{url}/user/repos', data = data, headers = headers)


def setup(project_name):
	get_path = f'cd {path}/{project_name}'
	url = f'https://github.com/{username}/{project_name}.git'
	os.system(f'{get_path} && echo # {project_name} > README.md')
	os.system(f'{get_path} && git init')
	os.system(f'{get_path} && git add .')
	os.system(f'{get_path} && git commit -m "Initial commit"')
	os.system(f'{get_path} && git init')
	os.system(f'{get_path} && git remote add origin {url}')
	os.system(f'{get_path} && git push -u origin master')
	os.system(f'{get_path} && code .')


if __name__ == '__main__':
	prompt()
