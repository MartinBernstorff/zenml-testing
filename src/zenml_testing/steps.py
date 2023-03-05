from zenml.steps import step


@step
def sleep() -> None:
    import time

    pass
    time.sleep(5)
