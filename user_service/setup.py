from setuptools import setup, find_namespace_packages, find_packages
import re
import pathlib
import pkg_resources

requirements = [
"annotated-types==0.7.0",
"anyio==4.4.0",
"certifi==2024.7.4",
"click==8.1.7",
"dnspython==2.6.1",
"email_validator==2.2.0",
"fastapi==0.112.2",
"fastapi-cli==0.0.5",
"h11==0.14.0",
"httpcore==1.0.5",
"httptools==0.6.1",
"httpx==0.27.2",
"idna==3.8",
"Jinja2==3.1.4",
"markdown-it-py==3.0.0",
"MarkupSafe==2.1.5",
"mdurl==0.1.2",
"pydantic==2.8.2",
"pydantic_core==2.20.1",
"Pygments==2.18.0",
"python-dotenv==1.0.1",
"python-multipart==0.0.9",
"PyYAML==6.0.2",
"rich==13.8.0",
"shellingham==1.5.4",
"sniffio==1.3.1",
"starlette==0.38.2",
"typer==0.12.5",
"typing_extensions==4.12.2",
"uvicorn==0.30.6",
"uvloop==0.20.0",
"watchfiles==0.24.0",
"websockets==13.0.1"

    ]
# Retrieve package list
PACKAGES = (find_namespace_packages(include=["users*"], exclude=['tests']))

# Add extra virtual shortened package for each of namespace_pkgs
namespace_pkgs = ["users"]

# Run python setup
setup(
    name="users",
    version="1.0.6",
    description=(
        "user service pip package"
    ),
    install_requires=requirements,
    include_package_data=True,
    packages=PACKAGES,
)