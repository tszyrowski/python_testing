from distutils.core import setup

setup(
    name='python_testing_workshop',
    version='0.1dev',
    packages=['basic_pytest',],
    licence='MIT License',
    long_description=open('README.md').read(),
    install_requires=[
        "pytest",
        "pytest-bdd",
    ],
)