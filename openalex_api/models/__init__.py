# coding: utf-8

# flake8: noqa
"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  [![Open in](https://img.shields.io/badge/Open%20in-Swagger%20UI-85EA2D?style=for-the-badge&logo=Swagger&link=https://mearman.github.io/openalex-swagger-ui-react/)](https://mearman.github.io/openalex-swagger-ui-react/)  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)  [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)  [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ---

    The version of the OpenAPI document: 0.2.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from openalex_api.models.apc import Apc
from openalex_api.models.associated_institution import AssociatedInstitution
from openalex_api.models.author import Author
from openalex_api.models.authors import Authors
from openalex_api.models.auto_complete_result_item import AutoCompleteResultItem
from openalex_api.models.auto_complete_result_schema import AutoCompleteResultSchema
from openalex_api.models.base_selection_attributes import BaseSelectionAttributes
from openalex_api.models.concept import Concept
from openalex_api.models.concept_ids import ConceptIds
from openalex_api.models.concepts import Concepts
from openalex_api.models.dehydrated_concept import DehydratedConcept
from openalex_api.models.dehydrated_institution import DehydratedInstitution
from openalex_api.models.domain import Domain
from openalex_api.models.error_message import ErrorMessage
from openalex_api.models.field import Field
from openalex_api.models.funder import Funder
from openalex_api.models.funder_schema import FunderSchema
from openalex_api.models.funders_array import FundersArray
from openalex_api.models.geo import Geo
from openalex_api.models.ids import Ids
from openalex_api.models.institution import Institution
from openalex_api.models.institution_schema import InstitutionSchema
from openalex_api.models.institutions import Institutions
from openalex_api.models.international_description import InternationalDescription
from openalex_api.models.international_display_name import InternationalDisplayName
from openalex_api.models.international_display_name_and_description import InternationalDisplayNameAndDescription
from openalex_api.models.internationalisation import Internationalisation
from openalex_api.models.location import Location
from openalex_api.models.location_source import LocationSource
from openalex_api.models.meta import Meta
from openalex_api.models.ngram_meta import NgramMeta
from openalex_api.models.ngrams import Ngrams
from openalex_api.models.person import Person
from openalex_api.models.publisher import Publisher
from openalex_api.models.publisher_parent_publisher import PublisherParentPublisher
from openalex_api.models.publisher_schema import PublisherSchema
from openalex_api.models.publishers import Publishers
from openalex_api.models.role import Role
from openalex_api.models.root_response_schema import RootResponseSchema
from openalex_api.models.source import Source
from openalex_api.models.source_schema import SourceSchema
from openalex_api.models.sources import Sources
from openalex_api.models.subfield import Subfield
from openalex_api.models.summary_stats import SummaryStats
from openalex_api.models.topic import Topic
from openalex_api.models.topic_level_array_schema import TopicLevelArraySchema
from openalex_api.models.topic_level_schema import TopicLevelSchema
from openalex_api.models.topic_level_schema_id import TopicLevelSchemaId
from openalex_api.models.topics import Topics
from openalex_api.models.topics_meta import TopicsMeta
from openalex_api.models.work import Work
from openalex_api.models.work_attributes import WorkAttributes
from openalex_api.models.work_biblio import WorkBiblio
from openalex_api.models.work_cited_by_percentile_year import WorkCitedByPercentileYear
from openalex_api.models.work_open_access import WorkOpenAccess
from openalex_api.models.work_schema import WorkSchema
from openalex_api.models.works_response import WorksResponse
