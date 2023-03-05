from zenml.steps import step
    import time


@step
def sleep() -> None:
    """Imitated zenml step"""
    time.sleep(5)
