# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)  [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)  [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ---

    The version of the OpenAPI document: 0.0.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from openalex_api.models.apc import Apc
from openalex_api.models.ids import Ids
from openalex_api.models.location import Location
from openalex_api.models.work_schema_biblio import WorkSchemaBiblio
from openalex_api.models.work_schema_cited_by_percentile_year import WorkSchemaCitedByPercentileYear
from openalex_api.models.work_schema_open_access import WorkSchemaOpenAccess
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkSchema(BaseModel):
    """
    WorkSchema
    """ # noqa: E501
    abstract_inverted_index: Optional[Any] = None
    apc_list: Optional[Apc] = None
    apc_paid: Optional[Apc] = None
    authorships: Optional[Any] = None
    best_oa_location: Optional[Location] = None
    biblio: Optional[WorkSchemaBiblio] = None
    cited_by_api_url: Optional[Any] = None
    cited_by_count: Optional[Any] = None
    cited_by_percentile_year: Optional[WorkSchemaCitedByPercentileYear] = None
    concepts: Optional[Any] = None
    corresponding_author_ids: Optional[Any] = None
    corresponding_institution_ids: Optional[Any] = None
    countries_distinct_count: Optional[Any] = None
    counts_by_year: Optional[Any] = None
    created_date: Optional[Any] = None
    display_name: Optional[Any]
    doi: Optional[Any] = None
    grants: Optional[Any] = None
    has_fulltext: Optional[Any] = None
    id: Optional[Any]
    ids: Optional[Ids] = None
    institutions_distinct_count: Optional[Any] = None
    is_paratext: Optional[Any] = None
    is_retracted: Optional[Any] = None
    keywords: Optional[Any] = None
    language: Optional[Any] = None
    locations: Optional[Any] = None
    locations_count: Optional[Any] = None
    mesh: Optional[Any] = None
    ngrams_url: Optional[Any] = None
    open_access: Optional[WorkSchemaOpenAccess] = None
    primary_location: Optional[Location] = None
    publication_date: Optional[Any] = None
    publication_year: Optional[Any] = None
    referenced_works: Optional[Any] = None
    referenced_works_count: Optional[Any] = None
    related_works: Optional[Any] = None
    sustainable_development_goals: Optional[Any] = None
    title: Optional[Any] = None
    type: Optional[Any] = None
    type_crossref: Optional[Any] = None
    updated_date: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["abstract_inverted_index", "apc_list", "apc_paid", "authorships", "best_oa_location", "biblio", "cited_by_api_url", "cited_by_count", "cited_by_percentile_year", "concepts", "corresponding_author_ids", "corresponding_institution_ids", "countries_distinct_count", "counts_by_year", "created_date", "display_name", "doi", "grants", "has_fulltext", "id", "ids", "institutions_distinct_count", "is_paratext", "is_retracted", "keywords", "language", "locations", "locations_count", "mesh", "ngrams_url", "open_access", "primary_location", "publication_date", "publication_year", "referenced_works", "referenced_works_count", "related_works", "sustainable_development_goals", "title", "type", "type_crossref", "updated_date"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WorkSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of apc_list
        if self.apc_list:
            _dict['apc_list'] = self.apc_list.to_dict()
        # override the default output from pydantic by calling `to_dict()` of apc_paid
        if self.apc_paid:
            _dict['apc_paid'] = self.apc_paid.to_dict()
        # override the default output from pydantic by calling `to_dict()` of best_oa_location
        if self.best_oa_location:
            _dict['best_oa_location'] = self.best_oa_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of biblio
        if self.biblio:
            _dict['biblio'] = self.biblio.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cited_by_percentile_year
        if self.cited_by_percentile_year:
            _dict['cited_by_percentile_year'] = self.cited_by_percentile_year.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ids
        if self.ids:
            _dict['ids'] = self.ids.to_dict()
        # override the default output from pydantic by calling `to_dict()` of open_access
        if self.open_access:
            _dict['open_access'] = self.open_access.to_dict()
        # override the default output from pydantic by calling `to_dict()` of primary_location
        if self.primary_location:
            _dict['primary_location'] = self.primary_location.to_dict()
        # set to None if abstract_inverted_index (nullable) is None
        # and model_fields_set contains the field
        if self.abstract_inverted_index is None and "abstract_inverted_index" in self.model_fields_set:
            _dict['abstract_inverted_index'] = None

        # set to None if authorships (nullable) is None
        # and model_fields_set contains the field
        if self.authorships is None and "authorships" in self.model_fields_set:
            _dict['authorships'] = None

        # set to None if cited_by_api_url (nullable) is None
        # and model_fields_set contains the field
        if self.cited_by_api_url is None and "cited_by_api_url" in self.model_fields_set:
            _dict['cited_by_api_url'] = None

        # set to None if cited_by_count (nullable) is None
        # and model_fields_set contains the field
        if self.cited_by_count is None and "cited_by_count" in self.model_fields_set:
            _dict['cited_by_count'] = None

        # set to None if concepts (nullable) is None
        # and model_fields_set contains the field
        if self.concepts is None and "concepts" in self.model_fields_set:
            _dict['concepts'] = None

        # set to None if corresponding_author_ids (nullable) is None
        # and model_fields_set contains the field
        if self.corresponding_author_ids is None and "corresponding_author_ids" in self.model_fields_set:
            _dict['corresponding_author_ids'] = None

        # set to None if corresponding_institution_ids (nullable) is None
        # and model_fields_set contains the field
        if self.corresponding_institution_ids is None and "corresponding_institution_ids" in self.model_fields_set:
            _dict['corresponding_institution_ids'] = None

        # set to None if countries_distinct_count (nullable) is None
        # and model_fields_set contains the field
        if self.countries_distinct_count is None and "countries_distinct_count" in self.model_fields_set:
            _dict['countries_distinct_count'] = None

        # set to None if counts_by_year (nullable) is None
        # and model_fields_set contains the field
        if self.counts_by_year is None and "counts_by_year" in self.model_fields_set:
            _dict['counts_by_year'] = None

        # set to None if created_date (nullable) is None
        # and model_fields_set contains the field
        if self.created_date is None and "created_date" in self.model_fields_set:
            _dict['created_date'] = None

        # set to None if display_name (nullable) is None
        # and model_fields_set contains the field
        if self.display_name is None and "display_name" in self.model_fields_set:
            _dict['display_name'] = None

        # set to None if doi (nullable) is None
        # and model_fields_set contains the field
        if self.doi is None and "doi" in self.model_fields_set:
            _dict['doi'] = None

        # set to None if grants (nullable) is None
        # and model_fields_set contains the field
        if self.grants is None and "grants" in self.model_fields_set:
            _dict['grants'] = None

        # set to None if has_fulltext (nullable) is None
        # and model_fields_set contains the field
        if self.has_fulltext is None and "has_fulltext" in self.model_fields_set:
            _dict['has_fulltext'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if institutions_distinct_count (nullable) is None
        # and model_fields_set contains the field
        if self.institutions_distinct_count is None and "institutions_distinct_count" in self.model_fields_set:
            _dict['institutions_distinct_count'] = None

        # set to None if is_paratext (nullable) is None
        # and model_fields_set contains the field
        if self.is_paratext is None and "is_paratext" in self.model_fields_set:
            _dict['is_paratext'] = None

        # set to None if is_retracted (nullable) is None
        # and model_fields_set contains the field
        if self.is_retracted is None and "is_retracted" in self.model_fields_set:
            _dict['is_retracted'] = None

        # set to None if keywords (nullable) is None
        # and model_fields_set contains the field
        if self.keywords is None and "keywords" in self.model_fields_set:
            _dict['keywords'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if locations (nullable) is None
        # and model_fields_set contains the field
        if self.locations is None and "locations" in self.model_fields_set:
            _dict['locations'] = None

        # set to None if locations_count (nullable) is None
        # and model_fields_set contains the field
        if self.locations_count is None and "locations_count" in self.model_fields_set:
            _dict['locations_count'] = None

        # set to None if mesh (nullable) is None
        # and model_fields_set contains the field
        if self.mesh is None and "mesh" in self.model_fields_set:
            _dict['mesh'] = None

        # set to None if ngrams_url (nullable) is None
        # and model_fields_set contains the field
        if self.ngrams_url is None and "ngrams_url" in self.model_fields_set:
            _dict['ngrams_url'] = None

        # set to None if publication_date (nullable) is None
        # and model_fields_set contains the field
        if self.publication_date is None and "publication_date" in self.model_fields_set:
            _dict['publication_date'] = None

        # set to None if publication_year (nullable) is None
        # and model_fields_set contains the field
        if self.publication_year is None and "publication_year" in self.model_fields_set:
            _dict['publication_year'] = None

        # set to None if referenced_works (nullable) is None
        # and model_fields_set contains the field
        if self.referenced_works is None and "referenced_works" in self.model_fields_set:
            _dict['referenced_works'] = None

        # set to None if referenced_works_count (nullable) is None
        # and model_fields_set contains the field
        if self.referenced_works_count is None and "referenced_works_count" in self.model_fields_set:
            _dict['referenced_works_count'] = None

        # set to None if related_works (nullable) is None
        # and model_fields_set contains the field
        if self.related_works is None and "related_works" in self.model_fields_set:
            _dict['related_works'] = None

        # set to None if sustainable_development_goals (nullable) is None
        # and model_fields_set contains the field
        if self.sustainable_development_goals is None and "sustainable_development_goals" in self.model_fields_set:
            _dict['sustainable_development_goals'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if type_crossref (nullable) is None
        # and model_fields_set contains the field
        if self.type_crossref is None and "type_crossref" in self.model_fields_set:
            _dict['type_crossref'] = None

        # set to None if updated_date (nullable) is None
        # and model_fields_set contains the field
        if self.updated_date is None and "updated_date" in self.model_fields_set:
            _dict['updated_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WorkSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "abstract_inverted_index": obj.get("abstract_inverted_index"),
            "apc_list": Apc.from_dict(obj.get("apc_list")) if obj.get("apc_list") is not None else None,
            "apc_paid": Apc.from_dict(obj.get("apc_paid")) if obj.get("apc_paid") is not None else None,
            "authorships": obj.get("authorships"),
            "best_oa_location": Location.from_dict(obj.get("best_oa_location")) if obj.get("best_oa_location") is not None else None,
            "biblio": WorkSchemaBiblio.from_dict(obj.get("biblio")) if obj.get("biblio") is not None else None,
            "cited_by_api_url": obj.get("cited_by_api_url"),
            "cited_by_count": obj.get("cited_by_count"),
            "cited_by_percentile_year": WorkSchemaCitedByPercentileYear.from_dict(obj.get("cited_by_percentile_year")) if obj.get("cited_by_percentile_year") is not None else None,
            "concepts": obj.get("concepts"),
            "corresponding_author_ids": obj.get("corresponding_author_ids"),
            "corresponding_institution_ids": obj.get("corresponding_institution_ids"),
            "countries_distinct_count": obj.get("countries_distinct_count"),
            "counts_by_year": obj.get("counts_by_year"),
            "created_date": obj.get("created_date"),
            "display_name": obj.get("display_name"),
            "doi": obj.get("doi"),
            "grants": obj.get("grants"),
            "has_fulltext": obj.get("has_fulltext"),
            "id": obj.get("id"),
            "ids": Ids.from_dict(obj.get("ids")) if obj.get("ids") is not None else None,
            "institutions_distinct_count": obj.get("institutions_distinct_count"),
            "is_paratext": obj.get("is_paratext"),
            "is_retracted": obj.get("is_retracted"),
            "keywords": obj.get("keywords"),
            "language": obj.get("language"),
            "locations": obj.get("locations"),
            "locations_count": obj.get("locations_count"),
            "mesh": obj.get("mesh"),
            "ngrams_url": obj.get("ngrams_url"),
            "open_access": WorkSchemaOpenAccess.from_dict(obj.get("open_access")) if obj.get("open_access") is not None else None,
            "primary_location": Location.from_dict(obj.get("primary_location")) if obj.get("primary_location") is not None else None,
            "publication_date": obj.get("publication_date"),
            "publication_year": obj.get("publication_year"),
            "referenced_works": obj.get("referenced_works"),
            "referenced_works_count": obj.get("referenced_works_count"),
            "related_works": obj.get("related_works"),
            "sustainable_development_goals": obj.get("sustainable_development_goals"),
            "title": obj.get("title"),
            "type": obj.get("type"),
            "type_crossref": obj.get("type_crossref"),
            "updated_date": obj.get("updated_date")
        })
        return _obj


