"""Test cases for the main module."""

from zenml_testing.steps import sleep


def test_using_entrypoint():
    sleep().entrypoint()
