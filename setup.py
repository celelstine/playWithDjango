import io

from setuptools import setup, find_packages

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.md')
setup(
    name='PlayWithDjango',
    version='1.0',
    packages=find_packages(),
    scripts=['manage.py'], # this would add manage.py to the $PATH of the virtualenv
    author='Okoro Okwudiri Celestine',
    author_email='okorocelestine@gmail.com',
    description='A module to play with django',
    long_description=long_description,
    keywords="Django python learn Explore web",
    url='https://github.com/celelstine/playWithDjango',
    license="MIT",
    install_requires=[
        'dj-database-url==0.5.0',
        'Django==2.1.3',
        'psycopg2-binary==2.7.6.1',
        'pytz==2018.7',
        'djangorestframework==3.9.0'
    ],
    tests_require=['tox']
)
