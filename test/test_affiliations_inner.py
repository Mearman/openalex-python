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

from mearman_openalex_api.models.affiliations_inner import AffiliationsInner

class TestAffiliationsInner(unittest.TestCase):
    """AffiliationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AffiliationsInner:
        """Test AffiliationsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AffiliationsInner`
        """
        model = AffiliationsInner()
        if include_optional:
            return AffiliationsInner(
                institution = mearman_openalex_api.models.dehydrated_institution.dehydratedInstitution(
                    country_code = null, 
                    display_name = null, 
                    id = null, 
                    lineage = null, 
                    ror = null, 
                    type = null, ),
                years = [
                    56
                    ]
            )
        else:
            return AffiliationsInner(
                institution = mearman_openalex_api.models.dehydrated_institution.dehydratedInstitution(
                    country_code = null, 
                    display_name = null, 
                    id = null, 
                    lineage = null, 
                    ror = null, 
                    type = null, ),
                years = [
                    56
                    ],
        )
        """

    def testAffiliationsInner(self):
        """Test AffiliationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
