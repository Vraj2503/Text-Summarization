import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()


__version__ = '0.0.0'

REPO_NAME = 'Text-Summarization'
USER_NAME = 'Vraj2503'
SRC_REPO = 'wordSummerizer'
AUTHOR_EMAIL = 'vrajpatel250304@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package to summarize the text",
    long_description=long_description,
    long_description_content_type= "text/markdown",
    url=f"https://github.com/{USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),

)