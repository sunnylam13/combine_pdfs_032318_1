try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'You merge several PDF files and only specifically chosen pages into a single PDF file.',
	'author': 'Sunny Lam',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['PyPDF2,logging,os'],
	'scripts': [],
	'name': 'Combine Chosen Pages from Many PDFs'
}

setup(**config)