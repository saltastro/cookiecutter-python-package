# Installation

## Stable release

To install {{ cookiecutter.project_name }}, run this command in your terminal:

```bash
pip install {{ cookiecutter.package_name }}
```

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed, this [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/) can guide you through the process.

## From sources

The sources for {{ cookiecutter.project_name }} can be downloaded from the [Github repo](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}).

You can either clone the public repository:

```bash
git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}
```

Or download the [tarball](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/tarball/master):

```bash
curl  -OL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/tarball/master
```

Once you have a copy of the source, you can install it with:

```bash
python setup.py install
```
