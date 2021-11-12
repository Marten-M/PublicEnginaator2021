# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.image_url import ImageUrl  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_165c19b6a1574d4c8971af47(self):
        """Test case for 165c19b6a1574d4c8971af47

        Get Batch List (Internal)
        """
        response = self.client.open(
            '/vision/v3.2/batch/analyze',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_56f91f2e778daf14a499f200(self):
        """Test case for 56f91f2e778daf14a499f200

        Tag Image
        """
        body = None
        query_string = [('language', 'en'),
                        ('model_version', 'latest')]
        response = self.client.open(
            '/vision/v3.2/tag',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_56f91f2e778daf14a499f20c(self):
        """Test case for 56f91f2e778daf14a499f20c

        Get Thumbnail
        """
        body = None
        query_string = [('smartCropping', true),
                        ('width', 8.14),
                        ('height', 8.14),
                        ('model_version', 'latest')]
        response = self.client.open(
            '/vision/v3.2/generateThumbnail',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_56f91f2e778daf14a499f20d(self):
        """Test case for 56f91f2e778daf14a499f20d

        OCR
        """
        body = None
        query_string = [('language', 'unk'),
                        ('detectOrientation', true),
                        ('model_version', 'latest')]
        response = self.client.open(
            '/vision/v3.2/ocr',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_56f91f2e778daf14a499f20e(self):
        """Test case for 56f91f2e778daf14a499f20e

        List Domain Specific Models
        """
        response = self.client.open(
            '/vision/v3.2/models',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_56f91f2e778daf14a499f21b(self):
        """Test case for 56f91f2e778daf14a499f21b

        Analyze Image
        """
        body = None
        query_string = [('visualFeatures', 'Categories'),
                        ('details', 'details_example'),
                        ('language', 'en'),
                        ('model_version', 'latest')]
        response = self.client.open(
            '/vision/v3.2/analyze',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_56f91f2e778daf14a499f21f(self):
        """Test case for 56f91f2e778daf14a499f21f

        Describe Image
        """
        body = None
        query_string = [('maxCandidates', '1'),
                        ('language', 'en'),
                        ('model_version', 'latest')]
        response = self.client.open(
            '/vision/v3.2/describe',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_56f91f2e778daf14a499f311(self):
        """Test case for 56f91f2e778daf14a499f311

        Recognize Domain Specific Content
        """
        body = None
        query_string = [('language', 'en'),
                        ('model_version', 'latest')]
        response = self.client.open(
            '/vision/v3.2/models/{model}/analyze'.format(model='model_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_5d9869604be85dee480c8750(self):
        """Test case for 5d9869604be85dee480c8750

        Get Read Result
        """
        response = self.client.open(
            '/vision/v3.2/read/analyzeResults/{operationId}'.format(operationId='operationId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_5d986960601faab4bf452005(self):
        """Test case for 5d986960601faab4bf452005

        Read
        """
        imageUrl = ImageUrl()
        query_string = [('language', 'language_example'),
                        ('pages', 'pages_example'),
                        ('readingOrder', 'readingOrder_example'),
                        ('model_version', 'model_version_example')]
        response = self.client.open(
            '/vision/v3.2/read/analyze',
            method='POST',
            data=json.dumps(imageUrl),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_5e0cdeda77a84fcd9a6d4e1b(self):
        """Test case for 5e0cdeda77a84fcd9a6d4e1b

        Detect Objects
        """
        body = None
        query_string = [('model_version', 'latest')]
        response = self.client.open(
            '/vision/v3.2/detect',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_6255e4f0fe1a47d79b577145(self):
        """Test case for 6255e4f0fe1a47d79b577145

        Batch (Internal)
        """
        response = self.client.open(
            '/vision/v3.2/batch/analyze/{name}'.format(name='name_example'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_650d21697bf6473aa7011a06(self):
        """Test case for 650d21697bf6473aa7011a06

        Get Batch (Internal)
        """
        response = self.client.open(
            '/vision/v3.2/batch/analyzeStatus/{name}'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_b156d0f5e11e492d9f64418d(self):
        """Test case for b156d0f5e11e492d9f64418d

        Get Area of Interest
        """
        body = None
        query_string = [('model_version', 'latest')]
        response = self.client.open(
            '/vision/v3.2/areaOfInterest',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
