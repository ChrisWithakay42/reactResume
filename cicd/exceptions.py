class BucketAlreadyOwnedByYou(Exception):
    def __init__(self, bucket_name):
        self.message = f'You Already Own {bucket_name}.'
