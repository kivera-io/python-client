import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kivera-sdk",
    author="Kivera",
    author_email="support@kivera.io",
    description="Python library to interact with the Kivera Graphql API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kivera-io/python-client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ],
    keywords='kivera graphql gql sdk client',
    packages=setuptools.find_packages(exclude=["tests", "gen"]),
    python_requires=">=3.6",
    install_requires=[
        'requests',
        'gql[aiohttp]>=3.4.0',
        'charset-normalizer<3.0,>=2.0',
        'python-jose'
    ]
)