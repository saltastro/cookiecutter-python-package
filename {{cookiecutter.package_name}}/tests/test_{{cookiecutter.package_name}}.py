"""Tests for `{{ cookiecutter.package_name }}` package."""

import pytest
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner
{%- endif %}

from {{ cookiecutter.package_name }} import {{ cookiecutter.package_name }}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from {{ cookiecutter.package_name }} import cli
{%- endif %}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')
    pass


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    assert True == True
{%- if cookiecutter.command_line_interface|lower == 'click' %}


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.package_name }}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
{%- endif %}