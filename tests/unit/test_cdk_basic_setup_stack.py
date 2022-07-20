import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_basic_setup.cdk_basic_setup_stack import CdkBasicSetupStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_basic_setup/cdk_basic_setup_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkBasicSetupStack(app, "cdk-basic-setup")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
