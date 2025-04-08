from setuptools import setup, find_packages

setup(
    name='UltraTools',
    version='1.0.0',
    author='Izza',
    author_email='',
    description='UltraTools: Solusi Lengkap untuk Berbagai Kebutuhan Otomatisasi dan Tools Multifungsi.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/UltraTools',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)