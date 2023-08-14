class LambdaManager:
    _lambda_client = None

    def __init__(self):
        self._lambda_client = self.get_lambda_client()

    @staticmethod
    def get_lambda_client():
        return
