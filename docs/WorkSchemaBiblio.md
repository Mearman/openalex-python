# WorkSchemaBiblio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_page** | **object** |  | [optional] 
**issue** | **object** |  | [optional] 
**last_page** | **object** |  | [optional] 
**volume** | **object** |  | [optional] 

## Example

```python
from openalex_api.models.work_schema_biblio import WorkSchemaBiblio

# TODO update the JSON string below
json = "{}"
# create an instance of WorkSchemaBiblio from a JSON string
work_schema_biblio_instance = WorkSchemaBiblio.from_json(json)
# print the JSON string representation of the object
print WorkSchemaBiblio.to_json()

# convert the object into a dict
work_schema_biblio_dict = work_schema_biblio_instance.to_dict()
# create an instance of WorkSchemaBiblio from a dict
work_schema_biblio_form_dict = work_schema_biblio.from_dict(work_schema_biblio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


