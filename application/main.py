from zenml_testing.pipeline import main_pipeline
from zenml_testing.steps import sleep

if __name__ == "__main__":
    main_pipeline(step=sleep()).run(unlisted=True)
