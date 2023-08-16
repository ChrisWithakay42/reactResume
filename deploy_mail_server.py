import os

from cicd.aws_wrapper import LambdaWrapper


def main():
    # client = LambdaWrapper('lambda')
    # deployment_package = client.create_deployment_package(source_dir='/', destination_file='/')
    # client.create(
    #     function_name='codewithakay_mail_server',
    #     handler_name='send_mail',
    #     iam_role=os.getenv('AWS_LAMBDA_IAM_ROLE'),
    #     deployment_package=deployment_package
    # )
    print("Hello Lamda!")


if __name__ == '__main__':
    main()
