from distutils.core import setup

setup(
    name='pypie',
    version='0.1.0',
    author='Acer.Yang',
    author_email='yangacer@gmail.com',
    packages=['pypie'],
    scripts=['pie.py'],
    license='LICENSE',
    description='Slim you markdown with pie.',
    long_description=open('README.md').read(),
    install_requires=[ 'click>=3.2' ],
)
