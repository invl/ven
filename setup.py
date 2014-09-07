from setuptools import setup


setup(
    name='ven',
    version='0.4.1',
    description='Easy way to use virtualenv.',
    long_description=open('README.rst').read(),
    license='Apache License 2.0',
    url='https://github.com/invl/ven',
    py_modules=['ven'],
    install_requires=['Click', 'virtualenv'],
    entry_points="""
    [console_scripts]
    ven = ven:main
    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: Implementation :: PyPy",
    ]
)
