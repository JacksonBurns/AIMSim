import os.path
import codecs
import pathlib
from setuptools import setup, find_packages
import os

core_only = os.environ.get("CORE_ONLY", False)


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


if not core_only:
    name = "aimsim"
    desc = "Python command line and GUI tool to analyze molecular similarity."
    reqs = read("requirements.txt").split("\n")
    packages = find_packages(exclude=["docs", "tests", "examples"])
    entry_points = {
        "console_scripts": [
            "aimsim=aimsim.__main__:start_AIMSim",
        ]
    }
    cwd = pathlib.Path(__file__).parent
    README = (cwd / "README.md").read_text()
else:
    name = "aimsim_core"
    desc = "Core AIMSim molecular featurization and comparison utilities."
    reqs = read("requirements_core.txt").split("\n")
    packages = find_packages(
        exclude=["docs", "tests", "examples", "interfaces", "aimsim.tasks"],
    )
    entry_points = {}
    README = (
        "This is a subset of the larger AIMSim cheminformatics software containing only the core "
        "molecular featurization and comparison tools, intended for use by developers looking to extend "
        "AIMSim without all the extra dependencies for plotting and visualization. For the full AIMSim "
        "package, visit https://pypi.org/project/aimsim/."
    )

setup(
    name=name,
    python_requires=">=3.8",
    version=get_version("aimsim/__init__.py"),
    description=desc,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/VlachosGroup/AIMSim",
    author="Himaghna Bhattacharjee, Jackson Burns",
    license="MIT",
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=reqs,
    packages=packages,
    include_package_data=True,
    entry_points=entry_points,
    package_dir={name: "aimsim"},
)
