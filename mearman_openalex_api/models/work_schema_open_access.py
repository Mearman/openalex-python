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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkSchemaOpenAccess(BaseModel):
    """
    WorkSchemaOpenAccess
    """ # noqa: E501
    any_repository_has_fulltext: Optional[Any]
    is_oa: Optional[Any]
    oa_status: Optional[Any]
    oa_url: Optional[Any]
    __properties: ClassVar[List[str]] = ["any_repository_has_fulltext", "is_oa", "oa_status", "oa_url"]

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
        """Create an instance of WorkSchemaOpenAccess from a JSON string"""
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
        # set to None if any_repository_has_fulltext (nullable) is None
        # and model_fields_set contains the field
        if self.any_repository_has_fulltext is None and "any_repository_has_fulltext" in self.model_fields_set:
            _dict['any_repository_has_fulltext'] = None

        # set to None if is_oa (nullable) is None
        # and model_fields_set contains the field
        if self.is_oa is None and "is_oa" in self.model_fields_set:
            _dict['is_oa'] = None

        # set to None if oa_status (nullable) is None
        # and model_fields_set contains the field
        if self.oa_status is None and "oa_status" in self.model_fields_set:
            _dict['oa_status'] = None

        # set to None if oa_url (nullable) is None
        # and model_fields_set contains the field
        if self.oa_url is None and "oa_url" in self.model_fields_set:
            _dict['oa_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WorkSchemaOpenAccess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "any_repository_has_fulltext": obj.get("any_repository_has_fulltext"),
            "is_oa": obj.get("is_oa"),
            "oa_status": obj.get("oa_status"),
            "oa_url": obj.get("oa_url")
        })
        return _obj


