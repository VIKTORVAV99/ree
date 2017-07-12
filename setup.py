from distutils.core import setup

setup(
    name='reescraper',
    version='0.0.1',
    packages=['reescraper'],
    install_requires=[
        'arrow',
        'beautifulsoup4',
        'selenium'
      ],
    url='https://github.com/blackleg/reescrapper',
    license='MIT',
    author='blackleg',
    author_email='hectorespertpardo@gmail.com',
    description='Red electrica de España scrapper'
)
