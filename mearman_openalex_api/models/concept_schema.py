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
from mearman_openalex_api.models.concept_ids import ConceptIds
from mearman_openalex_api.models.international_display_name_and_description import InternationalDisplayNameAndDescription
from mearman_openalex_api.models.summary_stats import SummaryStats
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConceptSchema(BaseModel):
    """
    ConceptSchema
    """ # noqa: E501
    ancestors: Optional[Any] = None
    cited_by_count: Optional[Any] = None
    counts_by_year: Optional[Any] = None
    created_date: Optional[Any] = None
    description: Optional[Any] = None
    display_name: Optional[Any]
    id: Optional[Any]
    ids: Optional[ConceptIds] = None
    image_thumbnail_url: Optional[Any] = None
    image_url: Optional[Any] = None
    international: Optional[InternationalDisplayNameAndDescription] = None
    level: Optional[Any] = None
    related_concepts: Optional[Any] = None
    summary_stats: Optional[SummaryStats] = None
    updated_date: Optional[Any] = None
    wikidata: Optional[Any] = None
    works_api_url: Optional[Any] = None
    works_count: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["ancestors", "cited_by_count", "counts_by_year", "created_date", "description", "display_name", "id", "ids", "image_thumbnail_url", "image_url", "international", "level", "related_concepts", "summary_stats", "updated_date", "wikidata", "works_api_url", "works_count"]

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
        """Create an instance of ConceptSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of international
        if self.international:
            _dict['international'] = self.international.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summary_stats
        if self.summary_stats:
            _dict['summary_stats'] = self.summary_stats.to_dict()
        # set to None if ancestors (nullable) is None
        # and model_fields_set contains the field
        if self.ancestors is None and "ancestors" in self.model_fields_set:
            _dict['ancestors'] = None

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

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if display_name (nullable) is None
        # and model_fields_set contains the field
        if self.display_name is None and "display_name" in self.model_fields_set:
            _dict['display_name'] = None

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

        # set to None if level (nullable) is None
        # and model_fields_set contains the field
        if self.level is None and "level" in self.model_fields_set:
            _dict['level'] = None

        # set to None if related_concepts (nullable) is None
        # and model_fields_set contains the field
        if self.related_concepts is None and "related_concepts" in self.model_fields_set:
            _dict['related_concepts'] = None

        # set to None if updated_date (nullable) is None
        # and model_fields_set contains the field
        if self.updated_date is None and "updated_date" in self.model_fields_set:
            _dict['updated_date'] = None

        # set to None if wikidata (nullable) is None
        # and model_fields_set contains the field
        if self.wikidata is None and "wikidata" in self.model_fields_set:
            _dict['wikidata'] = None

        # set to None if works_api_url (nullable) is None
        # and model_fields_set contains the field
        if self.works_api_url is None and "works_api_url" in self.model_fields_set:
            _dict['works_api_url'] = None

        # set to None if works_count (nullable) is None
        # and model_fields_set contains the field
        if self.works_count is None and "works_count" in self.model_fields_set:
            _dict['works_count'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConceptSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ancestors": obj.get("ancestors"),
            "cited_by_count": obj.get("cited_by_count"),
            "counts_by_year": obj.get("counts_by_year"),
            "created_date": obj.get("created_date"),
            "description": obj.get("description"),
            "display_name": obj.get("display_name"),
            "id": obj.get("id"),
            "ids": ConceptIds.from_dict(obj.get("ids")) if obj.get("ids") is not None else None,
            "image_thumbnail_url": obj.get("image_thumbnail_url"),
            "image_url": obj.get("image_url"),
            "international": InternationalDisplayNameAndDescription.from_dict(obj.get("international")) if obj.get("international") is not None else None,
            "level": obj.get("level"),
            "related_concepts": obj.get("related_concepts"),
            "summary_stats": SummaryStats.from_dict(obj.get("summary_stats")) if obj.get("summary_stats") is not None else None,
            "updated_date": obj.get("updated_date"),
            "wikidata": obj.get("wikidata"),
            "works_api_url": obj.get("works_api_url"),
            "works_count": obj.get("works_count")
        })
        return _obj

