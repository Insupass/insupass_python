from distutils.core import setup

setup(
    name='IsoPass',
    version='0.1.0',
    author='Yu Gui',
    author_email='yugui923@gmail.com',
    packages=['isopass'],
    scripts=['isopass.py'],
    url='http://pypi.python.org/pypi/IsoPass/',
    license='LICENSE',
    description='Isolated Secure Offline Password Manager',
    long_description=open('README.md').read(),
    install_requires=[
    ],
)
