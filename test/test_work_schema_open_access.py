# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  This OpenAPI specification is derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).

    The version of the OpenAPI document: 0.0.4-3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from mearman_openalex_api.models.work_schema_open_access import WorkSchemaOpenAccess

class TestWorkSchemaOpenAccess(unittest.TestCase):
    """WorkSchemaOpenAccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkSchemaOpenAccess:
        """Test WorkSchemaOpenAccess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkSchemaOpenAccess`
        """
        model = WorkSchemaOpenAccess()
        if include_optional:
            return WorkSchemaOpenAccess(
                any_repository_has_fulltext = None,
                is_oa = None,
                oa_status = None,
                oa_url = None
            )
        else:
            return WorkSchemaOpenAccess(
                any_repository_has_fulltext = None,
                is_oa = None,
                oa_status = None,
                oa_url = None,
        )
        """

    def testWorkSchemaOpenAccess(self):
        """Test WorkSchemaOpenAccess"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()