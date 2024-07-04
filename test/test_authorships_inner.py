# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  [![Open in](https://img.shields.io/badge/Open%20in-Swagger%20UI-85EA2D?style=for-the-badge&logo=Swagger&link=https://mearman.github.io/openalex-swagger-ui-react/)](https://mearman.github.io/openalex-swagger-ui-react/)  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)  [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)  [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ---

    The version of the OpenAPI document: 0.2.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openalex_api.models.authorships_inner import AuthorshipsInner

class TestAuthorshipsInner(unittest.TestCase):
    """AuthorshipsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthorshipsInner:
        """Test AuthorshipsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthorshipsInner`
        """
        model = AuthorshipsInner()
        if include_optional:
            return AuthorshipsInner(
                author = openalex_api.models.authorships_inner_author.authorships_inner_author(
                    display_name = '', 
                    id = '', 
                    orcid = '', ),
                author_position = '',
                countries = [
                    ''
                    ],
                institutions = [
                    openalex_api.models.authorships_inner_institutions_inner.authorships_inner_institutions_inner(
                        country_code = '', 
                        display_name = '', 
                        id = '', 
                        lineage = [
                            ''
                            ], 
                        ror = '', 
                        type = '', )
                    ],
                is_corresponding = True,
                raw_affiliation_string = '',
                raw_affiliation_strings = [
                    ''
                    ],
                raw_author_name = ''
            )
        else:
            return AuthorshipsInner(
                author = openalex_api.models.authorships_inner_author.authorships_inner_author(
                    display_name = '', 
                    id = '', 
                    orcid = '', ),
                author_position = '',
                countries = [
                    ''
                    ],
                institutions = [
                    openalex_api.models.authorships_inner_institutions_inner.authorships_inner_institutions_inner(
                        country_code = '', 
                        display_name = '', 
                        id = '', 
                        lineage = [
                            ''
                            ], 
                        ror = '', 
                        type = '', )
                    ],
                is_corresponding = True,
                raw_affiliation_strings = [
                    ''
                    ],
                raw_author_name = '',
        )
        """

    def testAuthorshipsInner(self):
        """Test AuthorshipsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
