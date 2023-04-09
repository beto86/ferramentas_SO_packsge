from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ferramentas_SO",
    version="0.0.1",
    author="Roberto_Rocha",
    author_email="beto.brava@gmail.com",
    description="ferramentas usadas para redes geralmente",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/beto86/ferramentas_SO_packsge.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
