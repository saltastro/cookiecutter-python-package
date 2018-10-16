#!/usr/bin/env bash

if [[  "{{ cookiecutter.command_line_interface|lower }}" = *no* ]]
then
    rm src/{{ cookiecutter.package_name }}/cli.py
fi

if [[ "{{ cookiecutter.open_source_license }}" = "Not open source" ]]
then
    rm LICENSE
fi

if [[ "{{ cookiecutter.install_project }}" = "yes" ]]
then
    echo Creating a virtual environment...
    python3 -m venv venv
    source venv/bin/activate
    if [[ $? != 0 ]]
    then
        exit 1
    fi
    pip install -r requirements-dev.txt
    pip install -e .

    echo
    echo "A virtual environment venv with the required packages has been created in the project's root folder."
fi

echo
echo "Please see the README on"
echo
echo "https://github.com/saltastro/cookiecutter-python-package"
echo
echo "for details on how to get started."
echo
echo "TLDR;"
echo
echo "cd {{ cookiecutter.package_name }}"
{% if cookiecutter.install_project %}
echo "source venv/bin/activate"
{% endif %}
echo "make help"
echo


