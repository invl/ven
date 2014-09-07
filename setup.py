from setuptools import setup


setup(
    name='ven',
    version='0.4.0',
    description='Easy way to use virtualenv.',
    long_description=open('README.rst').read(),
    license='Apache License 2.0',
    url='https://github.com/invl/venv',
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
        'Programming Language :: Python :: 2.7',
    ]
)
