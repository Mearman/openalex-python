# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  This OpenAPI specification is derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).

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

class ConceptIds(BaseModel):
    """
    ConceptIds
    """ # noqa: E501
    mag: Optional[Any] = None
    openalex: Optional[Any]
    umls_cui: Optional[Any] = None
    wikidata: Optional[Any] = None
    wikipedia: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["mag", "openalex", "umls_cui", "wikidata", "wikipedia"]

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
        """Create an instance of ConceptIds from a JSON string"""
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
        # set to None if mag (nullable) is None
        # and model_fields_set contains the field
        if self.mag is None and "mag" in self.model_fields_set:
            _dict['mag'] = None

        # set to None if openalex (nullable) is None
        # and model_fields_set contains the field
        if self.openalex is None and "openalex" in self.model_fields_set:
            _dict['openalex'] = None

        # set to None if umls_cui (nullable) is None
        # and model_fields_set contains the field
        if self.umls_cui is None and "umls_cui" in self.model_fields_set:
            _dict['umls_cui'] = None

        # set to None if wikidata (nullable) is None
        # and model_fields_set contains the field
        if self.wikidata is None and "wikidata" in self.model_fields_set:
            _dict['wikidata'] = None

        # set to None if wikipedia (nullable) is None
        # and model_fields_set contains the field
        if self.wikipedia is None and "wikipedia" in self.model_fields_set:
            _dict['wikipedia'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConceptIds from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mag": obj.get("mag"),
            "openalex": obj.get("openalex"),
            "umls_cui": obj.get("umls_cui"),
            "wikidata": obj.get("wikidata"),
            "wikipedia": obj.get("wikipedia")
        })
        return _obj


