from setuptools import setup, find_packages


setup(
    name='yamltools',
    version='0.0.1',
    description='YAML <-> JSON.',
    long_description=open('README.rst').read(),
    author='Mikko Hellsing',
    author_email='mikko@hellsing.me',
    license='ISC',
    url='https://github.com/sorl/yamltools',
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    install_requires=['PyYAML>=3.11'],
    zip_safe=False,
    test_suite='yamltools.tests.TestYamlTools',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
