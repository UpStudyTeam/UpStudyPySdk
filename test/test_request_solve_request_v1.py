# coding: utf-8

"""
    api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from upstudy_py_sdk.models.request_solve_request_v1 import RequestSolveRequestV1

class TestRequestSolveRequestV1(unittest.TestCase):
    """RequestSolveRequestV1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestSolveRequestV1:
        """Test RequestSolveRequestV1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestSolveRequestV1`
        """
        model = RequestSolveRequestV1()
        if include_optional:
            return RequestSolveRequestV1(
                input = 'x+1=2',
                lang = 'EN'
            )
        else:
            return RequestSolveRequestV1(
                input = 'x+1=2',
        )
        """

    def testRequestSolveRequestV1(self):
        """Test RequestSolveRequestV1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
