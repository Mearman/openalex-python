# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript) [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch) [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)   ### Python  [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![CodeSpaces](https://img.shields.io/badge/CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Colab](https://img.shields.io/badge/Colab-gray?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ### Many more coming soon  ---

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
from openalex_api.models.affiliations_inner import AffiliationsInner
from openalex_api.models.dehydrated_institution import DehydratedInstitution
from openalex_api.models.ids import Ids
from openalex_api.models.summary_stats import SummaryStats
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Author(BaseModel):
    """
    Author
    """ # noqa: E501
    affiliations: Optional[List[AffiliationsInner]] = None
    cited_by_count: Optional[Any] = None
    counts_by_year: Optional[Any] = None
    created_date: Optional[Any] = None
    display_name: Optional[Any]
    display_name_alternatives: Optional[Any] = None
    id: Optional[Any]
    ids: Optional[Ids] = None
    last_known_institution: Optional[DehydratedInstitution] = None
    last_known_institutions: Optional[Any] = None
    orcid: Optional[Any] = None
    summary_stats: Optional[SummaryStats] = None
    updated_date: Optional[Any] = None
    works_api_url: Optional[Any] = None
    works_count: Optional[Any] = None
    x_concepts: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["affiliations", "cited_by_count", "counts_by_year", "created_date", "display_name", "display_name_alternatives", "id", "ids", "last_known_institution", "last_known_institutions", "orcid", "summary_stats", "updated_date", "works_api_url", "works_count", "x_concepts"]

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
        """Create an instance of Author from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in affiliations (list)
        _items = []
        if self.affiliations:
            for _item in self.affiliations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['affiliations'] = _items
        # override the default output from pydantic by calling `to_dict()` of ids
        if self.ids:
            _dict['ids'] = self.ids.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_known_institution
        if self.last_known_institution:
            _dict['last_known_institution'] = self.last_known_institution.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summary_stats
        if self.summary_stats:
            _dict['summary_stats'] = self.summary_stats.to_dict()
        # set to None if cited_by_count (nullable) is None
        # and model_fields_set contains the field
        if self.cited_by_count is None and "cited_by_count" in self.model_fields_set:
            _dict['cited_by_count'] = None

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

        # set to None if display_name_alternatives (nullable) is None
        # and model_fields_set contains the field
        if self.display_name_alternatives is None and "display_name_alternatives" in self.model_fields_set:
            _dict['display_name_alternatives'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if last_known_institutions (nullable) is None
        # and model_fields_set contains the field
        if self.last_known_institutions is None and "last_known_institutions" in self.model_fields_set:
            _dict['last_known_institutions'] = None

        # set to None if orcid (nullable) is None
        # and model_fields_set contains the field
        if self.orcid is None and "orcid" in self.model_fields_set:
            _dict['orcid'] = None

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
        """Create an instance of Author from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "affiliations": [AffiliationsInner.from_dict(_item) for _item in obj.get("affiliations")] if obj.get("affiliations") is not None else None,
            "cited_by_count": obj.get("cited_by_count"),
            "counts_by_year": obj.get("counts_by_year"),
            "created_date": obj.get("created_date"),
            "display_name": obj.get("display_name"),
            "display_name_alternatives": obj.get("display_name_alternatives"),
            "id": obj.get("id"),
            "ids": Ids.from_dict(obj.get("ids")) if obj.get("ids") is not None else None,
            "last_known_institution": DehydratedInstitution.from_dict(obj.get("last_known_institution")) if obj.get("last_known_institution") is not None else None,
            "last_known_institutions": obj.get("last_known_institutions"),
            "orcid": obj.get("orcid"),
            "summary_stats": SummaryStats.from_dict(obj.get("summary_stats")) if obj.get("summary_stats") is not None else None,
            "updated_date": obj.get("updated_date"),
            "works_api_url": obj.get("works_api_url"),
            "works_count": obj.get("works_count"),
            "x_concepts": obj.get("x_concepts")
        })
        return _obj


