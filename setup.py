from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="deen-api-client",
    version="1.0.0",
    author="Imaniro pvt ltd",
    author_email="info@imaniro.com",
    description="Python client for Deen API from Imaniro.com - Islamic resources API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/imaniro-tech/deen-api-python-client",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "requests-mock>=1.9.0",
            "pytest-cov>=2.0.0",
        ]
    },
    keywords="islamic, api, hadith, quran, dua, muslim",
    project_urls={
        "Documentation": "https://github.com/imaniro-tech/deen-api-python-client",
        "Source": "https://github.com/imaniro-tech/deen-api-python-client",
        "Tracker": "https://github.com/imaniro-tech/deen-api-python-client/issues",
    },
)