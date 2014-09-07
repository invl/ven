from setuptools import setup


setup(
    name='venv',
    version='0.2.0',
    description='Easy way to use virtualenv.',
    long_description=open('README.rst').read(),
    license='Apache License 2.0',
    url='https://github.com/invl/venv',
    py_modules=['venv'],
    install_requires=['Click'],
    entry_points="""
    [console_scripts]
    venv = venv:main
    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
    ]
)
