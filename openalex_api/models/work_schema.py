# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  [![Open in](https://img.shields.io/badge/Open%20in-Swagger%20UI-85EA2D?style=for-the-badge&logo=Swagger&link=https://mearman.github.io/openalex-swagger-ui-react/)](https://mearman.github.io/openalex-swagger-ui-react/)  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)  [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)  [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ---

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openalex_api.models.apc import Apc
from openalex_api.models.authorships_inner import AuthorshipsInner
from openalex_api.models.counts_by_year_inner import CountsByYearInner
from openalex_api.models.dehydrated_concept import DehydratedConcept
from openalex_api.models.ids import Ids
from openalex_api.models.location import Location
from openalex_api.models.work_biblio import WorkBiblio
from openalex_api.models.work_cited_by_percentile_year import WorkCitedByPercentileYear
from openalex_api.models.work_grants_inner import WorkGrantsInner
from openalex_api.models.work_keywords_inner import WorkKeywordsInner
from openalex_api.models.work_mesh_inner import WorkMeshInner
from openalex_api.models.work_open_access import WorkOpenAccess
from openalex_api.models.work_sustainable_development_goals_inner import WorkSustainableDevelopmentGoalsInner
from typing import Optional, Set
from typing_extensions import Self

class WorkSchema(BaseModel):
    """
    WorkSchema
    """ # noqa: E501
    abstract_inverted_index: Optional[Dict[str, Any]] = None
    apc_list: Optional[Apc] = None
    apc_paid: Optional[Apc] = None
    authorships: Optional[List[AuthorshipsInner]] = None
    best_oa_location: Optional[Location] = None
    biblio: Optional[WorkBiblio] = None
    cited_by_api_url: Optional[StrictStr] = None
    cited_by_count: Optional[StrictInt] = None
    cited_by_percentile_year: Optional[WorkCitedByPercentileYear] = None
    concepts: Optional[List[DehydratedConcept]] = None
    corresponding_author_ids: Optional[List[StrictStr]] = None
    corresponding_institution_ids: Optional[List[StrictStr]] = None
    countries_distinct_count: Optional[StrictInt] = None
    counts_by_year: Optional[List[CountsByYearInner]] = None
    created_date: Optional[StrictStr] = None
    display_name: StrictStr
    doi: Optional[StrictStr] = None
    grants: Optional[List[WorkGrantsInner]] = None
    has_fulltext: Optional[StrictBool] = None
    id: StrictStr
    ids: Optional[Ids] = None
    institutions_distinct_count: Optional[StrictInt] = None
    is_paratext: Optional[StrictBool] = None
    is_retracted: Optional[StrictBool] = None
    keywords: Optional[List[WorkKeywordsInner]] = None
    language: Optional[StrictStr] = None
    locations: Optional[List[Location]] = None
    locations_count: Optional[StrictInt] = None
    mesh: Optional[List[WorkMeshInner]] = None
    ngrams_url: Optional[StrictStr] = None
    open_access: Optional[WorkOpenAccess] = None
    primary_location: Optional[Location] = None
    publication_date: Optional[StrictStr] = None
    publication_year: Optional[StrictInt] = None
    referenced_works: Optional[List[StrictStr]] = None
    referenced_works_count: Optional[StrictInt] = None
    related_works: Optional[List[StrictStr]] = None
    sustainable_development_goals: Optional[List[WorkSustainableDevelopmentGoalsInner]] = None
    title: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    type_crossref: Optional[StrictStr] = None
    updated_date: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["abstract_inverted_index", "apc_list", "apc_paid", "authorships", "best_oa_location", "biblio", "cited_by_api_url", "cited_by_count", "cited_by_percentile_year", "concepts", "corresponding_author_ids", "corresponding_institution_ids", "countries_distinct_count", "counts_by_year", "created_date", "display_name", "doi", "grants", "has_fulltext", "id", "ids", "institutions_distinct_count", "is_paratext", "is_retracted", "keywords", "language", "locations", "locations_count", "mesh", "ngrams_url", "open_access", "primary_location", "publication_date", "publication_year", "referenced_works", "referenced_works_count", "related_works", "sustainable_development_goals", "title", "type", "type_crossref", "updated_date"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
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
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of apc_list
        if self.apc_list:
            _dict['apc_list'] = self.apc_list.to_dict()
        # override the default output from pydantic by calling `to_dict()` of apc_paid
        if self.apc_paid:
            _dict['apc_paid'] = self.apc_paid.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in authorships (list)
        _items = []
        if self.authorships:
            for _item in self.authorships:
                if _item:
                    _items.append(_item.to_dict())
            _dict['authorships'] = _items
        # override the default output from pydantic by calling `to_dict()` of best_oa_location
        if self.best_oa_location:
            _dict['best_oa_location'] = self.best_oa_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of biblio
        if self.biblio:
            _dict['biblio'] = self.biblio.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cited_by_percentile_year
        if self.cited_by_percentile_year:
            _dict['cited_by_percentile_year'] = self.cited_by_percentile_year.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in concepts (list)
        _items = []
        if self.concepts:
            for _item in self.concepts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['concepts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in counts_by_year (list)
        _items = []
        if self.counts_by_year:
            for _item in self.counts_by_year:
                if _item:
                    _items.append(_item.to_dict())
            _dict['counts_by_year'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in grants (list)
        _items = []
        if self.grants:
            for _item in self.grants:
                if _item:
                    _items.append(_item.to_dict())
            _dict['grants'] = _items
        # override the default output from pydantic by calling `to_dict()` of ids
        if self.ids:
            _dict['ids'] = self.ids.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in keywords (list)
        _items = []
        if self.keywords:
            for _item in self.keywords:
                if _item:
                    _items.append(_item.to_dict())
            _dict['keywords'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in locations (list)
        _items = []
        if self.locations:
            for _item in self.locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['locations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in mesh (list)
        _items = []
        if self.mesh:
            for _item in self.mesh:
                if _item:
                    _items.append(_item.to_dict())
            _dict['mesh'] = _items
        # override the default output from pydantic by calling `to_dict()` of open_access
        if self.open_access:
            _dict['open_access'] = self.open_access.to_dict()
        # override the default output from pydantic by calling `to_dict()` of primary_location
        if self.primary_location:
            _dict['primary_location'] = self.primary_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sustainable_development_goals (list)
        _items = []
        if self.sustainable_development_goals:
            for _item in self.sustainable_development_goals:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sustainable_development_goals'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "abstract_inverted_index": obj.get("abstract_inverted_index"),
            "apc_list": Apc.from_dict(obj["apc_list"]) if obj.get("apc_list") is not None else None,
            "apc_paid": Apc.from_dict(obj["apc_paid"]) if obj.get("apc_paid") is not None else None,
            "authorships": [AuthorshipsInner.from_dict(_item) for _item in obj["authorships"]] if obj.get("authorships") is not None else None,
            "best_oa_location": Location.from_dict(obj["best_oa_location"]) if obj.get("best_oa_location") is not None else None,
            "biblio": WorkBiblio.from_dict(obj["biblio"]) if obj.get("biblio") is not None else None,
            "cited_by_api_url": obj.get("cited_by_api_url"),
            "cited_by_count": obj.get("cited_by_count"),
            "cited_by_percentile_year": WorkCitedByPercentileYear.from_dict(obj["cited_by_percentile_year"]) if obj.get("cited_by_percentile_year") is not None else None,
            "concepts": [DehydratedConcept.from_dict(_item) for _item in obj["concepts"]] if obj.get("concepts") is not None else None,
            "corresponding_author_ids": obj.get("corresponding_author_ids"),
            "corresponding_institution_ids": obj.get("corresponding_institution_ids"),
            "countries_distinct_count": obj.get("countries_distinct_count"),
            "counts_by_year": [CountsByYearInner.from_dict(_item) for _item in obj["counts_by_year"]] if obj.get("counts_by_year") is not None else None,
            "created_date": obj.get("created_date"),
            "display_name": obj.get("display_name"),
            "doi": obj.get("doi"),
            "grants": [WorkGrantsInner.from_dict(_item) for _item in obj["grants"]] if obj.get("grants") is not None else None,
            "has_fulltext": obj.get("has_fulltext"),
            "id": obj.get("id"),
            "ids": Ids.from_dict(obj["ids"]) if obj.get("ids") is not None else None,
            "institutions_distinct_count": obj.get("institutions_distinct_count"),
            "is_paratext": obj.get("is_paratext"),
            "is_retracted": obj.get("is_retracted"),
            "keywords": [WorkKeywordsInner.from_dict(_item) for _item in obj["keywords"]] if obj.get("keywords") is not None else None,
            "language": obj.get("language"),
            "locations": [Location.from_dict(_item) for _item in obj["locations"]] if obj.get("locations") is not None else None,
            "locations_count": obj.get("locations_count"),
            "mesh": [WorkMeshInner.from_dict(_item) for _item in obj["mesh"]] if obj.get("mesh") is not None else None,
            "ngrams_url": obj.get("ngrams_url"),
            "open_access": WorkOpenAccess.from_dict(obj["open_access"]) if obj.get("open_access") is not None else None,
            "primary_location": Location.from_dict(obj["primary_location"]) if obj.get("primary_location") is not None else None,
            "publication_date": obj.get("publication_date"),
            "publication_year": obj.get("publication_year"),
            "referenced_works": obj.get("referenced_works"),
            "referenced_works_count": obj.get("referenced_works_count"),
            "related_works": obj.get("related_works"),
            "sustainable_development_goals": [WorkSustainableDevelopmentGoalsInner.from_dict(_item) for _item in obj["sustainable_development_goals"]] if obj.get("sustainable_development_goals") is not None else None,
            "title": obj.get("title"),
            "type": obj.get("type"),
            "type_crossref": obj.get("type_crossref"),
            "updated_date": obj.get("updated_date")
        })
        return _obj


