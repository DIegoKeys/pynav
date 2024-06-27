from setuptools import setup, find_packages

setup(
    name="pynav",
    version="0.1",
    packages=find_packages(),
    install_requires=["tkinter"],
    author="Diego Chaves",
    author_email="diegochavesdds@gmail.com",
    description="Uma biblioteca personalizada para navegação de dados",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/DIegoKeys/pynav",  # opcional, se você tiver um repositório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)