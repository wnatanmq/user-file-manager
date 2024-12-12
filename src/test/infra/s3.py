

import unittest
from unittest.mock import MagicMock, patch

from app.infra.s3 import S3Provider


class S3Python(unittest.TestCase):
    @patch("app.infra.s3.boto3")
    def test_upload_file(self):
        s3_provider = S3Provider()
        file_mock = bytes(str(MagicMock()))
        key_mock = str(MagicMock())
        s3_provider.upload_file(
            file=file_mock,
            key=key_mock
        )