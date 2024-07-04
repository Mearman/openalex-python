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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openalex_api.models.associated_institution import AssociatedInstitution
from openalex_api.models.counts_by_year_inner import CountsByYearInner
from openalex_api.models.dehydrated_concept import DehydratedConcept
from openalex_api.models.geo import Geo
from openalex_api.models.ids import Ids
from openalex_api.models.international_display_name import InternationalDisplayName
from openalex_api.models.repositories_array_inner import RepositoriesArrayInner
from openalex_api.models.role import Role
from openalex_api.models.summary_stats import SummaryStats
from typing import Optional, Set
from typing_extensions import Self

class InstitutionSchema(BaseModel):
    """
    InstitutionSchema
    """ # noqa: E501
    associated_institutions: Optional[List[AssociatedInstitution]] = None
    cited_by_count: Optional[StrictInt] = None
    country_code: Optional[StrictStr] = None
    counts_by_year: Optional[List[CountsByYearInner]] = None
    created_date: Optional[StrictStr] = None
    display_name: StrictStr
    display_name_acronyms: Optional[List[StrictStr]] = None
    display_name_alternatives: Optional[List[StrictStr]] = None
    geo: Optional[Geo] = None
    homepage_url: Optional[StrictStr] = None
    id: StrictStr
    ids: Optional[Ids] = None
    image_thumbnail_url: Optional[StrictStr] = None
    image_url: Optional[StrictStr] = None
    international: Optional[InternationalDisplayName] = None
    lineage: Optional[List[StrictStr]] = None
    repositories: Optional[List[RepositoriesArrayInner]] = None
    roles: Optional[List[Role]] = None
    ror: Optional[StrictStr] = None
    summary_stats: Optional[SummaryStats] = None
    type: Optional[StrictStr] = None
    updated_date: Optional[StrictStr] = None
    works_api_url: Optional[StrictStr] = None
    works_count: Optional[StrictInt] = None
    x_concepts: Optional[List[DehydratedConcept]] = None
    __properties: ClassVar[List[str]] = ["associated_institutions", "cited_by_count", "country_code", "counts_by_year", "created_date", "display_name", "display_name_acronyms", "display_name_alternatives", "geo", "homepage_url", "id", "ids", "image_thumbnail_url", "image_url", "international", "lineage", "repositories", "roles", "ror", "summary_stats", "type", "updated_date", "works_api_url", "works_count", "x_concepts"]

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
        """Create an instance of InstitutionSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in associated_institutions (list)
        _items = []
        if self.associated_institutions:
            for _item in self.associated_institutions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['associated_institutions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in counts_by_year (list)
        _items = []
        if self.counts_by_year:
            for _item in self.counts_by_year:
                if _item:
                    _items.append(_item.to_dict())
            _dict['counts_by_year'] = _items
        # override the default output from pydantic by calling `to_dict()` of geo
        if self.geo:
            _dict['geo'] = self.geo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ids
        if self.ids:
            _dict['ids'] = self.ids.to_dict()
        # override the default output from pydantic by calling `to_dict()` of international
        if self.international:
            _dict['international'] = self.international.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in repositories (list)
        _items = []
        if self.repositories:
            for _item in self.repositories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['repositories'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        # override the default output from pydantic by calling `to_dict()` of summary_stats
        if self.summary_stats:
            _dict['summary_stats'] = self.summary_stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in x_concepts (list)
        _items = []
        if self.x_concepts:
            for _item in self.x_concepts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['x_concepts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InstitutionSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associated_institutions": [AssociatedInstitution.from_dict(_item) for _item in obj["associated_institutions"]] if obj.get("associated_institutions") is not None else None,
            "cited_by_count": obj.get("cited_by_count"),
            "country_code": obj.get("country_code"),
            "counts_by_year": [CountsByYearInner.from_dict(_item) for _item in obj["counts_by_year"]] if obj.get("counts_by_year") is not None else None,
            "created_date": obj.get("created_date"),
            "display_name": obj.get("display_name"),
            "display_name_acronyms": obj.get("display_name_acronyms"),
            "display_name_alternatives": obj.get("display_name_alternatives"),
            "geo": Geo.from_dict(obj["geo"]) if obj.get("geo") is not None else None,
            "homepage_url": obj.get("homepage_url"),
            "id": obj.get("id"),
            "ids": Ids.from_dict(obj["ids"]) if obj.get("ids") is not None else None,
            "image_thumbnail_url": obj.get("image_thumbnail_url"),
            "image_url": obj.get("image_url"),
            "international": InternationalDisplayName.from_dict(obj["international"]) if obj.get("international") is not None else None,
            "lineage": obj.get("lineage"),
            "repositories": [RepositoriesArrayInner.from_dict(_item) for _item in obj["repositories"]] if obj.get("repositories") is not None else None,
            "roles": [Role.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None,
            "ror": obj.get("ror"),
            "summary_stats": SummaryStats.from_dict(obj["summary_stats"]) if obj.get("summary_stats") is not None else None,
            "type": obj.get("type"),
            "updated_date": obj.get("updated_date"),
            "works_api_url": obj.get("works_api_url"),
            "works_count": obj.get("works_count"),
            "x_concepts": [DehydratedConcept.from_dict(_item) for _item in obj["x_concepts"]] if obj.get("x_concepts") is not None else None
        })
        return _obj


