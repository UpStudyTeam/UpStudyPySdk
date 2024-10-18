# coding: utf-8

"""
    api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from upstudy_py_sdk.models.solver_step import SolverStep

class TestSolverStep(unittest.TestCase):
    """SolverStep unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SolverStep:
        """Test SolverStep
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SolverStep`
        """
        model = SolverStep()
        if include_optional:
            return SolverStep(
                children = [
                    upstudy_py_sdk.models.solver/step.solver.Step(
                        description = upstudy_py_sdk.models.description.description(), 
                        image_url = '', 
                        latex = '', )
                    ],
                description = upstudy_py_sdk.models.solver/description.solver.Description(
                    content = '', 
                    format = 'txt', ),
                image_url = '',
                latex = ''
            )
        else:
            return SolverStep(
        )
        """

    def testSolverStep(self):
        """Test SolverStep"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
