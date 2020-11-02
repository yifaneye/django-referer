import pathlib

from setuptools import setup

CWD = pathlib.Path(__file__).parent
README = (CWD / "README.rst").read_text()

setup(
    name='django-referer',
    version='0.0.1',
    description='Keep HTTP referer information on query parameter and display referer information',
    packages=["referer", "referer/middleware"],
    include_package_data=True,
    install_requires=["Django"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description=README,
    long_description_content_type='text/x-rst',
    url='https://github.com/yifaneye/django-referer',
    author='Yifan Ai',
    author_email='yifanai@aol.com'
)
