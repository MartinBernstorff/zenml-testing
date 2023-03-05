from zenml.pipelines import pipeline


@pipeline
def main_pipeline(step):
    step()
