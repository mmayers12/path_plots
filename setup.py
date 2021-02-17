from setuptools import setup, find_packages

install_requires = [
    'pandas',
    'networkx>=2.5',
    'matplotlib>=3.1.1',
    'seaborn',
]

setup(
    name='path_plots',
    author='Mike Mayers',
    author_email='mmayers@scripps.edu',
    url='https://github.com/mmayers12/path_plots',
    version='0.0.3',
    packages=find_packages(),
    license='LICENSE',
    description='Tools for plotting paths within graphs',
    long_description=open('README.md').read(),
    install_requires=install_requires,
    python_requires='>=3.6',
)
