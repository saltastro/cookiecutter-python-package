# cookiecutter-python-package

A boilerplate for Python packages that can be installed via `pip`. It is based on [Audrey Roy Greenfeld's pypackage cookiecutter](https://github.com/audreyr/cookiecutter-pypackage).

## Getting started

Ensure that [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) is installed on your computer.

You can then create a new web components project by using cookiecutter with this template:

```bash
cookiecutter https://github.com/saltastro/cookiecutter-python-package.git
```

Once the files have been generated, you have to install the new package. Change to its directory,

```bash
cd you_package_name
```

and (optionally, but wisely perhaps) create and and activate a new virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

You can then install the package.

```bash
pip install -e .
```

Note the `-e` flag, which makes sure that during development always the latest version of your code is used.

If you are planning to deploy to PyPI with Travis, you should also generate the encrypted password for the deployment.

```bash
travis encrypt --add deploy.password
```

## cookiecutter input

When using the template, cookiecutter asks you for various input:

`full_name`. Your full name, as it should appear in the license file and in `setup.py`.

`email`. Your email address. This is included as the value of `author_email` in `setup.py`.

`project_name`. The name of the project. This should be a human-friendly name and may contain spaces.

`package_name`. The name of the package. This must be a valid Python package name.

`project_short_description`. A brief description of the project.

`version`. The version.

`github_username`. Your Github username. This is used for generating the URL of the project's repository.

`github_repository`. The Github repository for the project.

`command_line_interface`. The command line interface to use. You currently only have the choice between using `Click` or no interface at all. If you opt to use an interface, a file `cli.py` is generated in your package folder and and entry point to its `main` function is included in the `setup.py` file. You should use this option if you are planning to include a command line tool with your package.

`open_source_license`. The open source license to use for the project. For all choices other than "Not open source" a license file will be generated.

`install_project`. Whether to install this project and its requirement. The project will be installed into a virtual environment `venv` in the project's root folder.

## Configuring the project

Once the project has been created, you should tweak various parts of it.

### Modify the Python content

The Python package has been generated with a module file in the project's `src/` folder. The module file contains an excample function, which yiou should remove. You may edit the package folder's con tent as required.

It is a good idea to export public classes and methods in the package's `__init__.py` folder, so that they can be imported more easily.

Take note of the warning in the section on documentation below.

### Check setup.py and setup.cfg

You may update the details for the build and distribution process by making changes to the `setup.py` and `setup.cfg` file. If you are planning to support Python 2.7, you should add it it to `sertup.py`.

### Modify the test content

The project's `/tests` folder contains an example test file. Its functions aren't particularly useful, and ypu should replace them with the appropriate unit tests. You may add other files in the `/tests` folder. Their name should start with `test_` so that `pytest` can access their tests.

### Check the tox configuration

While this might not be necessary, you may tweak the configuration of tox by updating its configuration file `tox.ini`. In particular, you should add testing for Python 2.7 if you are planning to support this version.

### What about Python 3.7?

Python 3.7 is included in the `tox.ini` but not in the `.travis.yml` file. The reason for the latter is that Travis does not support "out of the box". If you want to include it, you have to modify the configuration file in line with the recipe given at the end of [https://github.com/travis-ci/travis-ci/issues/9069#issuecomment-425720905](https://github.com/travis-ci/travis-ci/issues/9069#issuecomment-425720905).

### Create documentation

First, a warning. When Sphinx generates the documentation, it will import the Python modules. **Make sure that all code with side effects such as changing files or updating a database is protected by an `if __name__ == '__main__` condition.**

Documentation should be created in three places.

* Add docstrings to your code. All the docstrings should follow the [Numpy](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) or [Google](https://google.github.io/styleguide/pyguide.html#Comments). An API reference is automatically generated from your docstrings; see the file `docs/api.rst`.

* Add documentation in the `docs/` folder. When adding new files to this folder, you should remember to add them to the `toctree` directive in `docs/index.rst`. Both reStructuredText and Markdown (CommonMark, to be precise) files are supported, and they must have the suffix `.rst` abd `.md`, respectively.

* And of course you should update the `README.md` file. While this file is not included in the documentation generated by Sphinx, it is what users will seev when they navigate to your project's Github repository.

### Update the linting rules

[[Flake8](http://flake8.pycqa.org/en/latest/) is used for linting. If you need to configure any of its rules, modify the Flake8 section in `setup.cfg` accordingly. One rule which is tweaked in the configuration file is the maximum line length. It is set to 120 characters.

## Support for the development process

### Using a virtual environment

While this is not strictly necessary, it is a good idea to use a dedicated virtual environment when doing development work on this project. Chances are that one has been set up in a `venv` folder within the project's root folder when the project files were generated. Remember that you have to activate it.

```bash
source venv/bin/activate
```

You may deactivate it again when you are finished working.

```bash
deactivate
```

If no virtual environment has been created, you may do this yourself and install the project and its required packages.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
```

### The Makefile

The project's root folder contains a `Makefile` defining vartious useful tasks. You run a task (\some_task', say) by using the `make` command.

```bash
make some_target
```

The most important tasks are:

`help`. List all the available tasks.

`clean`. Remove all automatically generated artifacts.

`test`. Run pytest.

`lint`. Run Flake8 on the files in the `src/` and `tests` folders (and their subfolders).

`coverage`. Check the test coverage and display the results in the terminal and in a browser.

`tox`. Run tox, using pytest and Flake8 for several Python versions.

`docs`. Create html documentation from the files in the `docs/` folder and open it in a browser. The documentation includes an API reference generated from the docstrings in the source code. See the warning in the section on documentation before using this task. 

`install`. Install the project in editable mode (i.e. installing it with pip's `-e / --editable` flag).

`build`. Build a source and wheel package for the project.

`test-release`. Build a source and wheel package for the project and release it to the test PyPI.

`release`. Package the project with the `build` task and release it to PyPI.

These tasks may clean up existing artificats before they run.

### Bumping the version

The project version is included both in `setup.py` and in the package folder's `__init__.py` file. So rather than manually updating it, it is easier to use [bumpversion](https://github.com/peritus/bumpversion).

```bash
bumpversion part
```

`part` must be 'major', 'minor' or 'patch', depending on the kind of version change you want to make. For example:

``` bash
# current version is 0.1.0
bump patch  # version is now 0.1.1
bump minor  # version is now 0.2.0
bump major  # version is now 1.0.0
```

bumpversion takes the current version from `setup.cfg`, and it replaces it with the new version aftyer updating the other files.

## Releasing the project

While your workflow may differ, here is one option.

1. Run all the tests and make sure they pass.

```bash
make test
make tox
```

2. Check that you are happy with the test coverage.

```bash
make coverage
```

3. Bump the version number.

```bash
bumpversion part
```

3. Create a release branch in Git.

4. Release your package to the test Python Package Index (PyPI).

```bash
make test-release
```

5. Install your package from the test PyPI and test. Preferably ask other people to do the same. Fix bugs as required. Remember to run all tests again at the end.

6. Merge your release into the master branch and ensure the master branch on Github is updated. Make sure all Travis tests are passing.

7. Create a release on Github.

8. Release your package to the real PyPI.

```bash
make release
```
