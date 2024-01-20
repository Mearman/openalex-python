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
from openalex_api.models.ids import Ids
from openalex_api.models.summary_stats import SummaryStats
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SourceSchema(BaseModel):
    """
    SourceSchema
    """ # noqa: E501
    abbreviated_title: Optional[Any] = None
    alternate_titles: Optional[Any] = None
    apc_prices: Optional[Any] = None
    apc_usd: Optional[Any] = None
    cited_by_count: Optional[Any] = None
    country_code: Optional[Any] = None
    counts_by_year: Optional[Any] = None
    created_date: Optional[Any] = None
    display_name: Optional[Any]
    homepage_url: Optional[Any] = None
    host_organization: Optional[Any] = None
    host_organization_lineage: Optional[Any] = None
    host_organization_name: Optional[Any] = None
    id: Optional[Any]
    ids: Optional[Ids] = None
    is_in_doaj: Optional[Any] = None
    is_oa: Optional[Any] = None
    issn: Optional[Any] = None
    issn_l: Optional[Any] = None
    societies: Optional[Any] = None
    summary_stats: Optional[SummaryStats] = None
    type: Optional[Any] = None
    updated_date: Optional[Any] = None
    works_api_url: Optional[Any] = None
    works_count: Optional[Any] = None
    x_concepts: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["abbreviated_title", "alternate_titles", "apc_prices", "apc_usd", "cited_by_count", "country_code", "counts_by_year", "created_date", "display_name", "homepage_url", "host_organization", "host_organization_lineage", "host_organization_name", "id", "ids", "is_in_doaj", "is_oa", "issn", "issn_l", "societies", "summary_stats", "type", "updated_date", "works_api_url", "works_count", "x_concepts"]

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
        """Create an instance of SourceSchema from a JSON string"""
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
        # set to None if abbreviated_title (nullable) is None
        # and model_fields_set contains the field
        if self.abbreviated_title is None and "abbreviated_title" in self.model_fields_set:
            _dict['abbreviated_title'] = None

        # set to None if alternate_titles (nullable) is None
        # and model_fields_set contains the field
        if self.alternate_titles is None and "alternate_titles" in self.model_fields_set:
            _dict['alternate_titles'] = None

        # set to None if apc_prices (nullable) is None
        # and model_fields_set contains the field
        if self.apc_prices is None and "apc_prices" in self.model_fields_set:
            _dict['apc_prices'] = None

        # set to None if apc_usd (nullable) is None
        # and model_fields_set contains the field
        if self.apc_usd is None and "apc_usd" in self.model_fields_set:
            _dict['apc_usd'] = None

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

        # set to None if display_name (nullable) is None
        # and model_fields_set contains the field
        if self.display_name is None and "display_name" in self.model_fields_set:
            _dict['display_name'] = None

        # set to None if homepage_url (nullable) is None
        # and model_fields_set contains the field
        if self.homepage_url is None and "homepage_url" in self.model_fields_set:
            _dict['homepage_url'] = None

        # set to None if host_organization (nullable) is None
        # and model_fields_set contains the field
        if self.host_organization is None and "host_organization" in self.model_fields_set:
            _dict['host_organization'] = None

        # set to None if host_organization_lineage (nullable) is None
        # and model_fields_set contains the field
        if self.host_organization_lineage is None and "host_organization_lineage" in self.model_fields_set:
            _dict['host_organization_lineage'] = None

        # set to None if host_organization_name (nullable) is None
        # and model_fields_set contains the field
        if self.host_organization_name is None and "host_organization_name" in self.model_fields_set:
            _dict['host_organization_name'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if is_in_doaj (nullable) is None
        # and model_fields_set contains the field
        if self.is_in_doaj is None and "is_in_doaj" in self.model_fields_set:
            _dict['is_in_doaj'] = None

        # set to None if is_oa (nullable) is None
        # and model_fields_set contains the field
        if self.is_oa is None and "is_oa" in self.model_fields_set:
            _dict['is_oa'] = None

        # set to None if issn (nullable) is None
        # and model_fields_set contains the field
        if self.issn is None and "issn" in self.model_fields_set:
            _dict['issn'] = None

        # set to None if issn_l (nullable) is None
        # and model_fields_set contains the field
        if self.issn_l is None and "issn_l" in self.model_fields_set:
            _dict['issn_l'] = None

        # set to None if societies (nullable) is None
        # and model_fields_set contains the field
        if self.societies is None and "societies" in self.model_fields_set:
            _dict['societies'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if updated_date (nullable) is None
        # and model_fields_set contains the field
        if self.updated_date is None and "updated_date" in self.model_fields_set:
            _dict['updated_date'] = None

        # set to None if works_api_url (nullable) is None
        # and model_fields_set contains the field
        if self.works_api_url is None and "works_api_url" in self.model_fields_set:
            _dict['works_api_url'] = None

        # set to None if works_count (nullable) is None
        # and model_fields_set contains the field
        if self.works_count is None and "works_count" in self.model_fields_set:
            _dict['works_count'] = None

        # set to None if x_concepts (nullable) is None
        # and model_fields_set contains the field
        if self.x_concepts is None and "x_concepts" in self.model_fields_set:
            _dict['x_concepts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SourceSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "abbreviated_title": obj.get("abbreviated_title"),
            "alternate_titles": obj.get("alternate_titles"),
            "apc_usd": obj.get("apc_usd"),
            "cited_by_count": obj.get("cited_by_count"),
            "country_code": obj.get("country_code"),
            "counts_by_year": obj.get("counts_by_year"),
            "created_date": obj.get("created_date"),
            "display_name": obj.get("display_name"),
            "homepage_url": obj.get("homepage_url"),
            "host_organization": obj.get("host_organization"),
            "host_organization_lineage": obj.get("host_organization_lineage"),
            "host_organization_name": obj.get("host_organization_name"),
            "id": obj.get("id"),
            "ids": Ids.from_dict(obj.get("ids")) if obj.get("ids") is not None else None,
            "is_in_doaj": obj.get("is_in_doaj"),
            "is_oa": obj.get("is_oa"),
            "issn": obj.get("issn"),
            "issn_l": obj.get("issn_l"),
            "societies": obj.get("societies"),
            "summary_stats": SummaryStats.from_dict(obj.get("summary_stats")) if obj.get("summary_stats") is not None else None,
            "type": obj.get("type"),
            "updated_date": obj.get("updated_date"),
            "works_api_url": obj.get("works_api_url"),
            "works_count": obj.get("works_count"),
            "x_concepts": obj.get("x_concepts")
        })
        return _obj


