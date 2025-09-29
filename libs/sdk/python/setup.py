from setuptools import setup, find_packages
from pathlib import Path

try:
    README = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")
except FileNotFoundError:
    README = "Duruzi SDK: Python client for Duruzi Serve API."

setup(
    name="duruzi-sdk",
    version="0.1.0",
    description="Python client for Duruzi Serve API",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Duruzi Network",
    author_email="dev@duruzi.ai",
    url="https://github.com/duruzi-network/duruzi-sdk",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=["httpx>=0.27"],
    include_package_data=True,
    entry_points={"console_scripts": ["duruzi=duruzi.client:main"]},
)