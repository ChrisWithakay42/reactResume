import click
from flask.cli import with_appcontext

from cicd.bucket_api import create_bucket


@click.command('create_s3_bucket')
@with_appcontext
def create_s3_bucket():
    create_bucket(bucket_name='test_bucket', region='eu-west-2')
