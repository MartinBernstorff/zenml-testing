import time

from zenml.steps import step


@step
def sleep() -> None:
    """Imitated zenml step"""
    time.sleep(5)
