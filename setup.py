from pathlib import Path

from setuptools import find_packages, setup

readme_file = Path(__file__).parent / 'README.md'
if readme_file.exists():
    with readme_file.open() as f:
        long_description = f.read()
else:
    # When this is first installed in development Docker, README.md is not available
    long_description = ''

setup(
    name='numerical-methods-toolkit',
    version='1.0.0',
    description='Numerical Methods Toolkit',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Farhan Ahmed',
    author_email='farhan.ahmed.1@stonybrook.com',
    keywords='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python',
    ],
    python_requires='>=3.8',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    extras_require={'dev': ['tox']},
)
