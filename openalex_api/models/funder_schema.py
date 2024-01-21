# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)  [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)  [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ---

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from openalex_api.models.ids import Ids
from openalex_api.models.summary_stats import SummaryStats
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FunderSchema(BaseModel):
    """
    FunderSchema
    """ # noqa: E501
    alternate_titles: Optional[Any]
    cited_by_count: Optional[Any] = None
    country_code: Optional[Any] = None
    counts_by_year: Optional[Any] = None
    created_date: Optional[Any] = None
    description: Optional[Any] = None
    display_name: Optional[Any]
    grants_count: Optional[Any] = None
    homepage_url: Optional[Any] = None
    id: Optional[Any]
    ids: Optional[Ids] = None
    image_thumbnail_url: Optional[Any] = None
    image_url: Optional[Any] = None
    relevance_score: Optional[Any] = None
    roles: Optional[Any] = None
    summary_stats: Optional[SummaryStats] = None
    updated_date: Optional[Any] = None
    works_count: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["alternate_titles", "cited_by_count", "country_code", "counts_by_year", "created_date", "description", "display_name", "grants_count", "homepage_url", "id", "ids", "image_thumbnail_url", "image_url", "relevance_score", "roles", "summary_stats", "updated_date", "works_count"]

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
        """Create an instance of FunderSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ids
        if self.ids:
            _dict['ids'] = self.ids.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summary_stats
        if self.summary_stats:
            _dict['summary_stats'] = self.summary_stats.to_dict()
        # set to None if alternate_titles (nullable) is None
        # and model_fields_set contains the field
        if self.alternate_titles is None and "alternate_titles" in self.model_fields_set:
            _dict['alternate_titles'] = None

        # set to None if cited_by_count (nullable) is None
        # and model_fields_set contains the field
        if self.cited_by_count is None and "cited_by_count" in self.model_fields_set:
            _dict['cited_by_count'] = None

        # set to None if country_code (nullable) is None
        # and model_fields_set contains the field
        if self.country_code is None and "country_code" in self.model_fields_set:
            _dict['country_code'] = None

        # set to None if counts_by_year (nullable) is None
        # and model_fields_set contains the field
        if self.counts_by_year is None and "counts_by_year" in self.model_fields_set:
            _dict['counts_by_year'] = None

        # set to None if created_date (nullable) is None
        # and model_fields_set contains the field
        if self.created_date is None and "created_date" in self.model_fields_set:
            _dict['created_date'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if display_name (nullable) is None
        # and model_fields_set contains the field
        if self.display_name is None and "display_name" in self.model_fields_set:
            _dict['display_name'] = None

        # set to None if grants_count (nullable) is None
        # and model_fields_set contains the field
        if self.grants_count is None and "grants_count" in self.model_fields_set:
            _dict['grants_count'] = None

        # set to None if homepage_url (nullable) is None
        # and model_fields_set contains the field
        if self.homepage_url is None and "homepage_url" in self.model_fields_set:
            _dict['homepage_url'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if image_thumbnail_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_thumbnail_url is None and "image_thumbnail_url" in self.model_fields_set:
            _dict['image_thumbnail_url'] = None

        # set to None if image_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_url is None and "image_url" in self.model_fields_set:
            _dict['image_url'] = None

        # set to None if relevance_score (nullable) is None
        # and model_fields_set contains the field
        if self.relevance_score is None and "relevance_score" in self.model_fields_set:
            _dict['relevance_score'] = None

        # set to None if roles (nullable) is None
        # and model_fields_set contains the field
        if self.roles is None and "roles" in self.model_fields_set:
            _dict['roles'] = None

        # set to None if updated_date (nullable) is None
        # and model_fields_set contains the field
        if self.updated_date is None and "updated_date" in self.model_fields_set:
            _dict['updated_date'] = None

        # set to None if works_count (nullable) is None
        # and model_fields_set contains the field
        if self.works_count is None and "works_count" in self.model_fields_set:
            _dict['works_count'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FunderSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alternate_titles": obj.get("alternate_titles"),
            "cited_by_count": obj.get("cited_by_count"),
            "country_code": obj.get("country_code"),
            "counts_by_year": obj.get("counts_by_year"),
            "created_date": obj.get("created_date"),
            "description": obj.get("description"),
            "display_name": obj.get("display_name"),
            "grants_count": obj.get("grants_count"),
            "homepage_url": obj.get("homepage_url"),
            "id": obj.get("id"),
            "ids": Ids.from_dict(obj.get("ids")) if obj.get("ids") is not None else None,
            "image_thumbnail_url": obj.get("image_thumbnail_url"),
            "image_url": obj.get("image_url"),
            "relevance_score": obj.get("relevance_score"),
            "roles": obj.get("roles"),
            "summary_stats": SummaryStats.from_dict(obj.get("summary_stats")) if obj.get("summary_stats") is not None else None,
            "updated_date": obj.get("updated_date"),
            "works_count": obj.get("works_count")
        })
        return _obj


