import unittest
from unittest.mock import MagicMock, patch

from src.app.infra.s3 import S3Provider


class TestCaseS3Provider(unittest.TestCase):
    
    @patch("src.app.infra.s3.boto3")
    def test_upload_file(
        self,
        boto3_mock  : MagicMock
    ):
        s3_provider = S3Provider()
        file_mock = str.encode(str(MagicMock()))
        key_mock = str(MagicMock())
        s3_provider.upload_file(
            file=file_mock,
            key=key_mock
        )
        boto3_mock.client.return_value.put_object.assert_called_once_with(
            Bucket="user-folders",
            Body=file_mock,
            Key=key_mock
        )
