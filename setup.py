from setuptools import setup, find_packages

setup(
    name='shellrosetta',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'shellrosetta=shellrosetta.cli:main',
        ],
    },
    author='David Donohue',
    description='Translate Linux/Bash commands to PowerShell and vice versa, with flag and pipeline support.',
    url='https://github.com/sdirishguy/shellrosetta',
    license='MIT',
    python_requires='>=3.7',
)
