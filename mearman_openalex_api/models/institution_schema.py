# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  ### Python  [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![CodeSpaces](https://img.shields.io/badge/CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Colab](https://img.shields.io/badge/Colab-gray?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/demos/notebook.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/demos/notebook.ipynb)  ### Many more coming soon  ---

    The version of the OpenAPI document: 0.0.4-3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from mearman_openalex_api.models.geo import Geo
from mearman_openalex_api.models.ids import Ids
from mearman_openalex_api.models.international_display_name import InternationalDisplayName
from mearman_openalex_api.models.summary_stats import SummaryStats
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class InstitutionSchema(BaseModel):
    """
    InstitutionSchema
    """ # noqa: E501
    associated_institutions: Optional[Any] = None
    cited_by_count: Optional[Any] = None
    country_code: Optional[Any] = None
    counts_by_year: Optional[Any] = None
    created_date: Optional[Any] = None
    display_name: Optional[Any]
    display_name_acronyms: Optional[Any] = None
    display_name_alternatives: Optional[Any] = None
    geo: Optional[Geo] = None
    homepage_url: Optional[Any] = None
    id: Optional[Any]
    ids: Optional[Ids] = None
    image_thumbnail_url: Optional[Any] = None
    image_url: Optional[Any] = None
    international: Optional[InternationalDisplayName] = None
    lineage: Optional[Any] = None
    repositories: Optional[Any] = None
    roles: Optional[Any] = None
    ror: Optional[Any] = None
    summary_stats: Optional[SummaryStats] = None
    type: Optional[Any] = None
    updated_date: Optional[Any] = None
    works_api_url: Optional[Any] = None
    works_count: Optional[Any] = None
    x_concepts: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["associated_institutions", "cited_by_count", "country_code", "counts_by_year", "created_date", "display_name", "display_name_acronyms", "display_name_alternatives", "geo", "homepage_url", "id", "ids", "image_thumbnail_url", "image_url", "international", "lineage", "repositories", "roles", "ror", "summary_stats", "type", "updated_date", "works_api_url", "works_count", "x_concepts"]

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
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of geo
        if self.geo:
            _dict['geo'] = self.geo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ids
        if self.ids:
            _dict['ids'] = self.ids.to_dict()
        # override the default output from pydantic by calling `to_dict()` of international
        if self.international:
            _dict['international'] = self.international.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summary_stats
        if self.summary_stats:
            _dict['summary_stats'] = self.summary_stats.to_dict()
        # set to None if associated_institutions (nullable) is None
        # and model_fields_set contains the field
        if self.associated_institutions is None and "associated_institutions" in self.model_fields_set:
            _dict['associated_institutions'] = None

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

        # set to None if display_name_acronyms (nullable) is None
        # and model_fields_set contains the field
        if self.display_name_acronyms is None and "display_name_acronyms" in self.model_fields_set:
            _dict['display_name_acronyms'] = None

        # set to None if display_name_alternatives (nullable) is None
        # and model_fields_set contains the field
        if self.display_name_alternatives is None and "display_name_alternatives" in self.model_fields_set:
            _dict['display_name_alternatives'] = None

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

        # set to None if lineage (nullable) is None
        # and model_fields_set contains the field
        if self.lineage is None and "lineage" in self.model_fields_set:
            _dict['lineage'] = None

        # set to None if repositories (nullable) is None
        # and model_fields_set contains the field
        if self.repositories is None and "repositories" in self.model_fields_set:
            _dict['repositories'] = None

        # set to None if roles (nullable) is None
        # and model_fields_set contains the field
        if self.roles is None and "roles" in self.model_fields_set:
            _dict['roles'] = None

        # set to None if ror (nullable) is None
        # and model_fields_set contains the field
        if self.ror is None and "ror" in self.model_fields_set:
            _dict['ror'] = None

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
        """Create an instance of InstitutionSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associated_institutions": obj.get("associated_institutions"),
            "cited_by_count": obj.get("cited_by_count"),
            "country_code": obj.get("country_code"),
            "counts_by_year": obj.get("counts_by_year"),
            "created_date": obj.get("created_date"),
            "display_name": obj.get("display_name"),
            "display_name_acronyms": obj.get("display_name_acronyms"),
            "display_name_alternatives": obj.get("display_name_alternatives"),
            "geo": Geo.from_dict(obj.get("geo")) if obj.get("geo") is not None else None,
            "homepage_url": obj.get("homepage_url"),
            "id": obj.get("id"),
            "ids": Ids.from_dict(obj.get("ids")) if obj.get("ids") is not None else None,
            "image_thumbnail_url": obj.get("image_thumbnail_url"),
            "image_url": obj.get("image_url"),
            "international": InternationalDisplayName.from_dict(obj.get("international")) if obj.get("international") is not None else None,
            "lineage": obj.get("lineage"),
            "repositories": obj.get("repositories"),
            "roles": obj.get("roles"),
            "ror": obj.get("ror"),
            "summary_stats": SummaryStats.from_dict(obj.get("summary_stats")) if obj.get("summary_stats") is not None else None,
            "type": obj.get("type"),
            "updated_date": obj.get("updated_date"),
            "works_api_url": obj.get("works_api_url"),
            "works_count": obj.get("works_count"),
            "x_concepts": obj.get("x_concepts")
        })
        return _obj


