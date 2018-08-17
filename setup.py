from setuptools import setup

with open('README.md', mode='r', encoding='utf-8') as fd:
    long_description = fd.read()

setup(
    name='torch_attention',
    version='0.1.0',
    packages=['torch_attention'],
    install_requires=['torch'],
    url='https://github.com/speedcell4/torch_attention',
    license='MIT',
    author='speedcell4',
    author_email='speedcell4@gmail.com',
    description='attention mechanism',
    long_description=long_description,
)