from setuptools import setup, find_packages

def get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements

setup(
    name='mlproject-end-to-end',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements(),
    author='Busayo Anthonia',
    author_email='gwitmona@outlook.com',
    description='mlproject-end-to-end',
    url='https://github.com/AnnieThonia/mlproject-end-to-end.git',
)

