import os
import sys
import requests
import argparse
from secrets import token

path = 'C:/Coding/my-repositories'


def arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('--name', '-n', type=str, dest='name', required=True)
	parser.add_argument('--private', '-p', dest='private', action='store_true')
	arguments = parser.parse_args()
	return arguments


def create_dir():
	project_name = arguments().name
	os.system(f'cd {path} && mkdir {project_name}')


def create_repo():
	project_name = arguments().name
	is_private = arguments().private
	print(is_private)
	
	url = 'https://api.github.com'
	if is_private:
		data = '{"name": "' + project_name + '", "private": true}'
	else:
		data = '{"name": "' + project_name + '", "private": false}'
	headers = {
		'Authorization': 'token ' + token,
		'Accept': 'application/vnd.github.v3+json'
	}
	response = requests.request('POST', f'{url}/user/repos', data = data, headers = headers)


def setup():
	project_name = arguments().name
	get_path = f'cd {path}/{project_name}'
	url = f'https://github.com/scaldings/{project_name}.git'
	os.system(f'{get_path} && echo # {project_name} > README.md')
	os.system(f'{get_path} && git init')
	os.system(f'{get_path} && git add .')
	os.system(f'{get_path} && git commit -m "Initial commit"')
	os.system(f'{get_path} && git init')
	os.system(f'{get_path} && git remote add origin {url}')
	os.system(f'{get_path} && git push -u origin master')


if __name__ == '__main__':
	create_dir()
	create_repo()
	setup()