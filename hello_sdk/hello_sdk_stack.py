import aws_cdk.aws_s3 as s3
from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct


class HelloSdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "MyFirstBucket", versioned=True)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "HelloSdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
