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
from mearman_openalex_api.models.location_source import LocationSource
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Location(BaseModel):
    """
    Location
    """ # noqa: E501
    is_accepted: Optional[Any]
    is_oa: Optional[Any]
    is_published: Optional[Any]
    landing_page_url: Optional[Any]
    license: Optional[Any] = None
    pdf_url: Optional[Any] = None
    source: LocationSource
    version: Optional[Any]
    __properties: ClassVar[List[str]] = ["is_accepted", "is_oa", "is_published", "landing_page_url", "license", "pdf_url", "source", "version"]

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
        """Create an instance of Location from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # set to None if is_accepted (nullable) is None
        # and model_fields_set contains the field
        if self.is_accepted is None and "is_accepted" in self.model_fields_set:
            _dict['is_accepted'] = None

        # set to None if is_oa (nullable) is None
        # and model_fields_set contains the field
        if self.is_oa is None and "is_oa" in self.model_fields_set:
            _dict['is_oa'] = None

        # set to None if is_published (nullable) is None
        # and model_fields_set contains the field
        if self.is_published is None and "is_published" in self.model_fields_set:
            _dict['is_published'] = None

        # set to None if landing_page_url (nullable) is None
        # and model_fields_set contains the field
        if self.landing_page_url is None and "landing_page_url" in self.model_fields_set:
            _dict['landing_page_url'] = None

        # set to None if license (nullable) is None
        # and model_fields_set contains the field
        if self.license is None and "license" in self.model_fields_set:
            _dict['license'] = None

        # set to None if pdf_url (nullable) is None
        # and model_fields_set contains the field
        if self.pdf_url is None and "pdf_url" in self.model_fields_set:
            _dict['pdf_url'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Location from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "is_accepted": obj.get("is_accepted"),
            "is_oa": obj.get("is_oa"),
            "is_published": obj.get("is_published"),
            "landing_page_url": obj.get("landing_page_url"),
            "license": obj.get("license"),
            "pdf_url": obj.get("pdf_url"),
            "source": LocationSource.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "version": obj.get("version")
        })
        return _obj


