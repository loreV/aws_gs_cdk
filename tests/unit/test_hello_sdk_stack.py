import aws_cdk as core
import aws_cdk.assertions as assertions

from hello_sdk.hello_sdk_stack import HelloSdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in hello_sdk/hello_sdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = HelloSdkStack(app, "hello-sdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
