import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

__version__ = '0.0.1'

REPONAME = 'Text-Summarizer'
AUTHOR = 'Ladi Yusuph'
SRC_REPO = 'text-summarizer'

setuptools.setup(
    name=f"{REPONAME}",
    version=__version__,
    author=AUTHOR,
    author_email="",
    description="A text summarizer app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)