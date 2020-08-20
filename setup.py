import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="denton",
    version="0.0.1",
    author="Max Lugo D",
    author_email="maxlugo20@gmail.com",
    description="function to interpolate data using the denton procedure.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaxLugo/denton",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
















