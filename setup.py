from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='sqlittle',
    version='0.0.4',
    author='Dmitry Bondarenko',
    author_email='dimbnk@gmail.com',
    license='MIT',
    description='Better SQLite CLI',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Mon4ik/sqlittle',
    packages=find_packages(),
    install_requires=["rich"],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['sqlittle=sqlittle:parseArgs'],
    }
)
