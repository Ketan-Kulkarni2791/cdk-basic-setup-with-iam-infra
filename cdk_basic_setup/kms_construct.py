"""Module for creating KMS encryption key"""
from typing import List
from aws_cdk import aws_iam as iam
from aws_cdk import aws_kms as kms 
from aws_cdk.core import Stack

class KMSConstruct:
    """Class for methods to create KMS keys"""
    @staticmethod
    def create_kms_key_from_arn(
        stack: Stack,
        env: str,
        config: dict) -> kms.Key:
        """Import KMS key from external stack, used for encrypting AWS resources."""
        return kms.Key.from_key_arn(
            scope=stack,
            id=f"{config['global']['app-name']}-keyId",
            key_arn=config["global"]["cdk-basic-kms-arn"]
        )