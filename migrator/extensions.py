import boto3
from cloudfoundry_client.client import CloudFoundryClient

from migrator.config import config_from_env


config = config_from_env()


commercial_session = boto3.Session(
    region_name=config.AWS_COMMERCIAL_REGION,
    aws_access_key_id=config.AWS_COMMERCIAL_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_COMMERCIAL_SECRET_ACCESS_KEY,
)
cloudfront = commercial_session.client("cloudfront")
iam_commercial = commercial_session.client("iam")
route53 = commercial_session.client("route53")

govcloud_session = boto3.Session(
    region_name=config.AWS_GOVCLOUD_REGION,
    aws_access_key_id=config.AWS_GOVCLOUD_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_GOVCLOUD_SECRET_ACCESS_KEY,
)
iam_govcloud = govcloud_session.client("iam")
