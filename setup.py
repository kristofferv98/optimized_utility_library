from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='optimized-utility-library',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pillow',
        'ujson',
        'matplotlib',
        'setuptools',
    ],
    extras_require={
        'dev': [
            'pytest',
            'flake8'
        ]
    },
    author='Kristoffer Vatnehol',
    author_email='kristoffer.vatnehol@gmail.com',
    description='An optimized utility library for directory, file, image, and JSON operations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kristofferv98/optimized-utility-library',  # Update with your GitHub repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
