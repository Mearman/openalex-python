# PublisherSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_titles** | **object** |  | [optional] 
**cited_by_count** | **object** |  | [optional] 
**country_codes** | **object** |  | [optional] 
**counts_by_year** | **object** |  | [optional] 
**created_date** | **object** |  | [optional] 
**display_name** | **object** |  | 
**hierarchy_level** | **object** |  | [optional] 
**homepage_url** | **object** |  | [optional] 
**id** | **object** |  | 
**ids** | [**Ids**](Ids.md) |  | [optional] 
**image_thumbnail_url** | **object** |  | [optional] 
**image_url** | **object** |  | [optional] 
**lineage** | **object** |  | [optional] 
**parent_publisher** | [**PublisherSchemaParentPublisher**](PublisherSchemaParentPublisher.md) |  | [optional] 
**roles** | **object** |  | [optional] 
**sources_api_url** | **object** |  | [optional] 
**summary_stats** | [**SummaryStats**](SummaryStats.md) |  | [optional] 
**updated_date** | **object** |  | [optional] 
**works_count** | **object** |  | [optional] 

## Example

```python
from mearman_openalex_api.models.publisher_schema import PublisherSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PublisherSchema from a JSON string
publisher_schema_instance = PublisherSchema.from_json(json)
# print the JSON string representation of the object
print PublisherSchema.to_json()

# convert the object into a dict
publisher_schema_dict = publisher_schema_instance.to_dict()
# create an instance of PublisherSchema from a dict
publisher_schema_form_dict = publisher_schema.from_dict(publisher_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


