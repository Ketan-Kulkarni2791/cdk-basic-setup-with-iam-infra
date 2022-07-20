"""Main python file_key for adding resources to the application stack."""
from typing import Dict, Any
from aws_cdk import (
    core
)
from constructs import Construct
from .iam_construct import IAMConstruct
from .kms_construct import KMSConstruct

class CdkBasicSetupStack(core.Stack):
    """Build the app stacks and its resources."""
    def __init__(self, env_var: str, scope: core.Construct, 
                 app_id: str, config: dict, **kwargs: Dict[str, Any]) -> None:
        """Creates the cloudformation templates for the projects."""
        super().__init__(scope, app_id, **kwargs)
        self.env_var = env_var
        self.config = config
        CdkBasicSetupStack.create_stack(self, self.env_var, config=config)
        
    @staticmethod
    def create_stack(stack: core.Stack, env: str, config: dict) -> None:
        """Create and add the resources to the application stack"""
        CdkBasicSetupStack.create_iam_user_infra(
            stack=stack, env=env, config=config
        )
        
        kms_key = KMSConstruct.create_kms_key_from_arn(
            stack=stack, env=env, config=config
        )
        
    @staticmethod
    def create_iam_user_infra(
        stack: core.Stack,
        env: str,
        config: dict) -> None:
        """Create IAM user and required attributes"""
        user = IAMConstruct.create_user(stack=stack)
        group = IAMConstruct.create_group(stack=stack)
        group.add_user(user)
        access_policy = IAMConstruct.create_managed_policy(
            stack=stack,
            policy_name="cdk-basic-data-access-policy",
            statements=[
                IAMConstruct.get_access_key_mgmt_polict(stack=stack)
            ]
        )
        user.add_managed_policy(access_policy)
