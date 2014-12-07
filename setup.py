try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Wes Gill', 
    'url': 'Github.com',
    'download_url': 'Where to get it.',
    'author_email': 'jahrik@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname',
}

setup(**config)
