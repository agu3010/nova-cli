from setuptools import setup, find_packages

setup(
    name='novacli',
    version='0.1',
    author='Matthias Vogelgesang',
    author_email='matthias.vogelgesang@kit.edu',
    url='http://github.com/ufo-kit/nova-cli',
    license='LGPL',
    packages=find_packages(exclude=['*.tests']),
    scripts=['nova'],
    exclude_package_data={'': ['README.rst']},
    description="NOVA command line tool",
    install_requires=[
        'daiquiri',
        'pyxdg',
        'requests',
    ],
)
