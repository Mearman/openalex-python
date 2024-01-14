# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  This OpenAPI specification is derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).

    The version of the OpenAPI document: 0.0.4-3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from mearman_openalex_api.api.institutions_api import InstitutionsApi


class TestInstitutionsApi(unittest.TestCase):
    """InstitutionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InstitutionsApi()

    def tearDown(self) -> None:
        pass

    def test_get_autocomplete_institutions(self) -> None:
        """Test case for get_autocomplete_institutions

        /autocomplete/institutions
        """
        pass

    def test_get_institution(self) -> None:
        """Test case for get_institution

        /institutions/{id}
        """
        pass

    def test_get_institutions(self) -> None:
        """Test case for get_institutions

        /institutions
        """
        pass


if __name__ == '__main__':
    unittest.main()