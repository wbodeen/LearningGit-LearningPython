try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'Project Info',
    'author' : 'William J. Bodeen',
    'url' : '',
    'download_url' : '',
    'author_email' : 'wbodeen@gmail.com',
    'version' : '',
    'install_requires' : ['nose'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'projectname'
}

setup(**config)
