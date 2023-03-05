"""Test cases for the main module."""

from zenml_testing.steps import sleep


def test_using_entrypoint():
    """Test the main function"""
    sleep().entrypoint()
