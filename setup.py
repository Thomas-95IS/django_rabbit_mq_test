import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="django_rabbitmq_test",
    version="0.0.1",
    author="Thomas Stokes",
    author_email="",
    description="A package to handle the message queuing for some Django project.",
    long_description=long_description,
    url="",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)

