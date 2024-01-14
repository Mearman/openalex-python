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

from mearman_openalex_api.models.concept import Concept

class TestConcept(unittest.TestCase):
    """Concept unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Concept:
        """Test Concept
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Concept`
        """
        model = Concept()
        if include_optional:
            return Concept(
                ancestors = None,
                cited_by_count = None,
                counts_by_year = None,
                created_date = None,
                description = None,
                display_name = None,
                id = None,
                ids = mearman_openalex_api.models.concept_ids.concept_ids(
                    mag = null, 
                    openalex = null, 
                    umls_cui = null, 
                    wikidata = null, 
                    wikipedia = null, ),
                image_thumbnail_url = None,
                image_url = None,
                international = mearman_openalex_api.models.international_display_name_and_description.international_display_name_and_description(
                    description = mearman_openalex_api.models.international_description.international_description(), 
                    display_name = mearman_openalex_api.models.international_display_name.international_display_name(), ),
                level = None,
                related_concepts = None,
                summary_stats = mearman_openalex_api.models.summary_stats.summary_stats(
                    2yr_mean_citedness = null, 
                    h_index = null, 
                    i10_index = null, ),
                updated_date = None,
                wikidata = None,
                works_api_url = None,
                works_count = None
            )
        else:
            return Concept(
                display_name = None,
                id = None,
        )
        """

    def testConcept(self):
        """Test Concept"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()