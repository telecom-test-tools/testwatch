from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="testwatch",
    version="1.0.0",
    author="gbvk312",
    description="A simple but powerful log monitoring tool for parsing test results",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/telecom-test-tools/testwatch",
    packages=find_packages(),
    install_requires=[
        line.strip()
        for line in open("requirements.txt", "r").readlines()
        if line.strip() and not line.startswith("#")
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: Software Development :: Testing",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "testwatch=testwatch.main:main",
        ],
    },
)
