# coding: utf-8

# flake8: noqa
"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  ### Python  [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![CodeSpaces](https://img.shields.io/badge/CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Colab](https://img.shields.io/badge/Colab-gray?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ### Many more coming soon  ---

    The version of the OpenAPI document: 0.0.4-3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from mearman_openalex_api.models.affiliations_inner import AffiliationsInner
from mearman_openalex_api.models.apc import Apc
from mearman_openalex_api.models.associated_institution import AssociatedInstitution
from mearman_openalex_api.models.author import Author
from mearman_openalex_api.models.authors_response_schema import AuthorsResponseSchema
from mearman_openalex_api.models.auto_complete_result_item import AutoCompleteResultItem
from mearman_openalex_api.models.auto_complete_result_schema import AutoCompleteResultSchema
from mearman_openalex_api.models.base_selection_attributes import BaseSelectionAttributes
from mearman_openalex_api.models.concept import Concept
from mearman_openalex_api.models.concept_ids import ConceptIds
from mearman_openalex_api.models.concept_schema import ConceptSchema
from mearman_openalex_api.models.concepts_response_schema import ConceptsResponseSchema
from mearman_openalex_api.models.dehydrated_concept import DehydratedConcept
from mearman_openalex_api.models.dehydrated_institution import DehydratedInstitution
from mearman_openalex_api.models.error_message import ErrorMessage
from mearman_openalex_api.models.funder_schema import FunderSchema
from mearman_openalex_api.models.funders_array import FundersArray
from mearman_openalex_api.models.geo import Geo
from mearman_openalex_api.models.ids import Ids
from mearman_openalex_api.models.institution_schema import InstitutionSchema
from mearman_openalex_api.models.institutions_response_schema import InstitutionsResponseSchema
from mearman_openalex_api.models.international_description import InternationalDescription
from mearman_openalex_api.models.international_display_name import InternationalDisplayName
from mearman_openalex_api.models.international_display_name_and_description import InternationalDisplayNameAndDescription
from mearman_openalex_api.models.internationalisation import Internationalisation
from mearman_openalex_api.models.location import Location
from mearman_openalex_api.models.location_source import LocationSource
from mearman_openalex_api.models.meta import Meta
from mearman_openalex_api.models.ngram_meta import NgramMeta
from mearman_openalex_api.models.person_response_schema import PersonResponseSchema
from mearman_openalex_api.models.publisher_schema import PublisherSchema
from mearman_openalex_api.models.publisher_schema_parent_publisher import PublisherSchemaParentPublisher
from mearman_openalex_api.models.publishers_response_schema import PublishersResponseSchema
from mearman_openalex_api.models.role import Role
from mearman_openalex_api.models.root_response_schema import RootResponseSchema
from mearman_openalex_api.models.source_schema import SourceSchema
from mearman_openalex_api.models.sources_array import SourcesArray
from mearman_openalex_api.models.summary_stats import SummaryStats
from mearman_openalex_api.models.work_attributes import WorkAttributes
from mearman_openalex_api.models.work_ngrams_schema import WorkNgramsSchema
from mearman_openalex_api.models.work_schema import WorkSchema
from mearman_openalex_api.models.work_schema_biblio import WorkSchemaBiblio
from mearman_openalex_api.models.work_schema_cited_by_percentile_year import WorkSchemaCitedByPercentileYear
from mearman_openalex_api.models.work_schema_open_access import WorkSchemaOpenAccess
from mearman_openalex_api.models.works_response_schema import WorksResponseSchema
