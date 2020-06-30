from setuptools import setup

setup(
    name='django_pip_example',
    version='0.9.9.1',
    packages=['sample_app','sample_project','receipts',],
    description='Sample Django pip Project',
    install_requires=[ 'Django' ],

    entry_points =
    { 'console_scripts':
        [
            'runmyserver = sample_app.run:main',
            'initmyserver = sample_app.init:main',
        ]
    },
)
