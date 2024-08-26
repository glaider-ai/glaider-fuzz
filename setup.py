import os
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="glaider-fuzzer",
    version=os.getenv('PKG_VERSION', '0.0.6'),
    author="Glaider",
    author_email="info@glaider.it",
    description="LLM and System Prompt vulnerability scanner tool",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/glaider-ai/glaider-fuzz",
    packages=find_packages(),
    package_data={
        'glaider_fuzz': ['attack_data/*'],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ],
    python_requires='>=3.7',
    install_requires=[
        "openai==1.6.1",
        "langchain==0.0.353",
        "langchain-community==0.0.7",
        "langchain-core==0.1.4",
        "argparse==1.4.0",
        "python-dotenv==1.0.0",
        "tqdm==4.66.1",
        "colorama==0.4.6",
        "prettytable==3.10.0",
        "pandas==2.2.2",
        "inquirer==3.2.4",
        "prompt-toolkit==3.0.43",
        "fastparquet==2024.2.0"
    ],
    extras_require={
        "dev": ["pytest==7.4.4"]
    },
    entry_points={
        'console_scripts': [
            'glaider-fuzzer=glaider_fuzz.cli:main',
        ],
    },
    license="MIT",
)
