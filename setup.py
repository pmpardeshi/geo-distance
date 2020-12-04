from setuptools import find_packages, setup
setup(
    name='geodistlib',
    packages=find_packages(include=['geodistlib']),
    version='0.1.0',
    description='Python library to find distance between two geo coordinates',
    author='Pramod Pardeshi',
    license='MIT',
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)