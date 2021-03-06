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
    url='https://github.com/f4str/number-theory-toolkit',
    license='MIT',
    author='Farhan Ahmed',
    keywords='',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    extras_require={'dev': ['tox']},
)
