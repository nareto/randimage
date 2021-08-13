import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="randimage",
    version="1.1",
    description="Creates random images",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nareto/randimage",
    author="Renato Budinich",
    author_email="rennabh@gmail.com",
    license="MIT",
    packages=["randimage"],
    install_requires=["numpy", "matplotlib", "scipy"],
)
