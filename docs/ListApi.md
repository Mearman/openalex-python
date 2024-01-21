# openalex_api.ListApi

All URIs are relative to *https://api.openalex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_works**](ListApi.md#get_works) | **GET** /works | /works


# **get_works**
> WorksResponseSchema get_works(api_key=api_key, cursor=cursor, group_by=group_by, page=page, per_page=per_page, sample=sample, search=search, seed=seed, select=select, sort=sort, filter=filter, user_agent=user_agent, mailto=mailto)

/works



### Example


```python
import time
import os
import openalex_api
from openalex_api.models.works_response_schema import WorksResponseSchema
from openalex_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.openalex.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openalex_api.Configuration(
    host = "https://api.openalex.org"
)


# Enter a context with an instance of the API client
with openalex_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openalex_api.ListApi(api_client)
    api_key = 'api_key_example' # str |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    group_by = 'group_by_example' # str |  (optional)
    page = 1 # int |  (optional)
    per_page = 3 # int |  (optional)
    sample = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    seed = None # object |  (optional)
    select = 'select_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    filter = abstract.search: # object | Filter works by a specific field. See the [filter works](https://docs.openalex.org/api-entities/works/filter-works) documentation for more information. Valid filters are:   - `abstract.search` - `apc_list.currency` - `apc_list.provenance` - `apc_list.value` - `apc_list.value_usd` - `apc_paid.currency` - `apc_paid.provenance` - `apc_paid.value` - `apc_paid.value_usd` - `author.id` - `author.orcid` - `authors_count` - `authorships.author.id` - `authorships.author.orcid` - `authorships.countries` - `authorships.institutions.continent` - `authorships.institutions.country_code` - `authorships.institutions.id` - `authorships.institutions.is_global_south` - `authorships.institutions.lineage` - `authorships.institutions.ror` - `authorships.institutions.type` - `authorships.is_corresponding` - `best_oa_location.is_accepted` - `best_oa_location.is_oa` - `best_oa_location.is_published` - `best_oa_location.landing_page_url` - `best_oa_location.license` - `best_oa_location.source.host_organization` - `best_oa_location.source.host_organization_lineage` - `best_oa_location.source.id` - `best_oa_location.source.is_in_doaj` - `best_oa_location.source.is_oa` - `best_oa_location.source.issn` - `best_oa_location.source.type` - `best_oa_location.version` - `best_open_version` - `cited_by` - `cited_by_count` - `cited_by_percentile_year.max` - `cited_by_percentile_year.min` - `cites` - `concept.id` - `concepts.id` - `concepts.wikidata` - `concepts_count` - `corresponding_author_ids` - `corresponding_institution_ids` - `countries_distinct_count` - `default.search` - `display_name` - `display_name.search` - `doi` - `doi_starts_with` - `from_created_date` - `from_publication_date` - `fulltext.search` - `fulltext_origin` - `grants.award_id` - `grants.funder` - `has_abstract` - `has_doi` - `has_fulltext` - `has_ngrams` - `has_oa_accepted_or_published_version` - `has_oa_submitted_version` - `has_old_authors` - `has_orcid` - `has_pdf_url` - `has_pmcid` - `has_pmid` - `has_raw_affiliation_string` - `has_references` - `host_venue.id` - `ids.mag` - `ids.openalex` - `ids.pmcid` - `ids.pmid` - `institution.id` - `institutions.continent` - `institutions.country_code` - `institutions.id` - `institutions.is_global_south` - `institutions.ror` - `institutions.type` - `institutions_distinct_count` - `is_corresponding` - `is_oa` - `is_paratext` - `is_retracted` - `journal` - `keyword.search` - `keywords.keyword` - `language` - `locations.is_accepted` - `locations.is_oa` - `locations.is_published` - `locations.landing_page_url` - `locations.license` - `locations.source.has_issn` - `locations.source.host_institution_lineage` - `locations.source.host_organization` - `locations.source.host_organization_lineage` - `locations.source.id` - `locations.source.is_in_doaj` - `locations.source.is_oa` - `locations.source.issn` - `locations.source.publisher_lineage` - `locations.source.type` - `locations.version` - `locations_count` - `mag` - `oa_status` - `open_access.any_repository_has_fulltext` - `open_access.is_oa` - `open_access.oa_status` - `openalex` - `openalex_id` - `pmcid` - `pmid` - `primary_location.is_accepted` - `primary_location.is_oa` - `primary_location.is_published` - `primary_location.landing_page_url` - `primary_location.license` - `primary_location.source.has_issn` - `primary_location.source.host_institution_lineage` - `primary_location.source.host_organization` - `primary_location.source.host_organization_lineage` - `primary_location.source.id` - `primary_location.source.is_in_doaj` - `primary_location.source.is_oa` - `primary_location.source.issn` - `primary_location.source.publisher_lineage` - `primary_location.source.type` - `primary_location.version` - `publication_date` - `publication_year` - `raw_affiliation_string.search` - `referenced_works` - `referenced_works_count` - `related_to` - `repository` - `sustainable_development_goals.id` - `sustainable_development_goals.score` - `title.search` - `title_and_abstract.search` - `to_publication_date` - `to_updated_date` - `type` - `type_crossref` - `version` (optional)
    user_agent = None # object | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = None # object | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

    try:
        # /works
        api_response = api_instance.get_works(api_key=api_key, cursor=cursor, group_by=group_by, page=page, per_page=per_page, sample=sample, search=search, seed=seed, select=select, sort=sort, filter=filter, user_agent=user_agent, mailto=mailto)
        print("The response of ListApi->get_works:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->get_works: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **group_by** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **sample** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **seed** | [**object**](.md)|  | [optional] 
 **select** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **filter** | [**object**](.md)| Filter works by a specific field. See the [filter works](https://docs.openalex.org/api-entities/works/filter-works) documentation for more information. Valid filters are:   - &#x60;abstract.search&#x60; - &#x60;apc_list.currency&#x60; - &#x60;apc_list.provenance&#x60; - &#x60;apc_list.value&#x60; - &#x60;apc_list.value_usd&#x60; - &#x60;apc_paid.currency&#x60; - &#x60;apc_paid.provenance&#x60; - &#x60;apc_paid.value&#x60; - &#x60;apc_paid.value_usd&#x60; - &#x60;author.id&#x60; - &#x60;author.orcid&#x60; - &#x60;authors_count&#x60; - &#x60;authorships.author.id&#x60; - &#x60;authorships.author.orcid&#x60; - &#x60;authorships.countries&#x60; - &#x60;authorships.institutions.continent&#x60; - &#x60;authorships.institutions.country_code&#x60; - &#x60;authorships.institutions.id&#x60; - &#x60;authorships.institutions.is_global_south&#x60; - &#x60;authorships.institutions.lineage&#x60; - &#x60;authorships.institutions.ror&#x60; - &#x60;authorships.institutions.type&#x60; - &#x60;authorships.is_corresponding&#x60; - &#x60;best_oa_location.is_accepted&#x60; - &#x60;best_oa_location.is_oa&#x60; - &#x60;best_oa_location.is_published&#x60; - &#x60;best_oa_location.landing_page_url&#x60; - &#x60;best_oa_location.license&#x60; - &#x60;best_oa_location.source.host_organization&#x60; - &#x60;best_oa_location.source.host_organization_lineage&#x60; - &#x60;best_oa_location.source.id&#x60; - &#x60;best_oa_location.source.is_in_doaj&#x60; - &#x60;best_oa_location.source.is_oa&#x60; - &#x60;best_oa_location.source.issn&#x60; - &#x60;best_oa_location.source.type&#x60; - &#x60;best_oa_location.version&#x60; - &#x60;best_open_version&#x60; - &#x60;cited_by&#x60; - &#x60;cited_by_count&#x60; - &#x60;cited_by_percentile_year.max&#x60; - &#x60;cited_by_percentile_year.min&#x60; - &#x60;cites&#x60; - &#x60;concept.id&#x60; - &#x60;concepts.id&#x60; - &#x60;concepts.wikidata&#x60; - &#x60;concepts_count&#x60; - &#x60;corresponding_author_ids&#x60; - &#x60;corresponding_institution_ids&#x60; - &#x60;countries_distinct_count&#x60; - &#x60;default.search&#x60; - &#x60;display_name&#x60; - &#x60;display_name.search&#x60; - &#x60;doi&#x60; - &#x60;doi_starts_with&#x60; - &#x60;from_created_date&#x60; - &#x60;from_publication_date&#x60; - &#x60;fulltext.search&#x60; - &#x60;fulltext_origin&#x60; - &#x60;grants.award_id&#x60; - &#x60;grants.funder&#x60; - &#x60;has_abstract&#x60; - &#x60;has_doi&#x60; - &#x60;has_fulltext&#x60; - &#x60;has_ngrams&#x60; - &#x60;has_oa_accepted_or_published_version&#x60; - &#x60;has_oa_submitted_version&#x60; - &#x60;has_old_authors&#x60; - &#x60;has_orcid&#x60; - &#x60;has_pdf_url&#x60; - &#x60;has_pmcid&#x60; - &#x60;has_pmid&#x60; - &#x60;has_raw_affiliation_string&#x60; - &#x60;has_references&#x60; - &#x60;host_venue.id&#x60; - &#x60;ids.mag&#x60; - &#x60;ids.openalex&#x60; - &#x60;ids.pmcid&#x60; - &#x60;ids.pmid&#x60; - &#x60;institution.id&#x60; - &#x60;institutions.continent&#x60; - &#x60;institutions.country_code&#x60; - &#x60;institutions.id&#x60; - &#x60;institutions.is_global_south&#x60; - &#x60;institutions.ror&#x60; - &#x60;institutions.type&#x60; - &#x60;institutions_distinct_count&#x60; - &#x60;is_corresponding&#x60; - &#x60;is_oa&#x60; - &#x60;is_paratext&#x60; - &#x60;is_retracted&#x60; - &#x60;journal&#x60; - &#x60;keyword.search&#x60; - &#x60;keywords.keyword&#x60; - &#x60;language&#x60; - &#x60;locations.is_accepted&#x60; - &#x60;locations.is_oa&#x60; - &#x60;locations.is_published&#x60; - &#x60;locations.landing_page_url&#x60; - &#x60;locations.license&#x60; - &#x60;locations.source.has_issn&#x60; - &#x60;locations.source.host_institution_lineage&#x60; - &#x60;locations.source.host_organization&#x60; - &#x60;locations.source.host_organization_lineage&#x60; - &#x60;locations.source.id&#x60; - &#x60;locations.source.is_in_doaj&#x60; - &#x60;locations.source.is_oa&#x60; - &#x60;locations.source.issn&#x60; - &#x60;locations.source.publisher_lineage&#x60; - &#x60;locations.source.type&#x60; - &#x60;locations.version&#x60; - &#x60;locations_count&#x60; - &#x60;mag&#x60; - &#x60;oa_status&#x60; - &#x60;open_access.any_repository_has_fulltext&#x60; - &#x60;open_access.is_oa&#x60; - &#x60;open_access.oa_status&#x60; - &#x60;openalex&#x60; - &#x60;openalex_id&#x60; - &#x60;pmcid&#x60; - &#x60;pmid&#x60; - &#x60;primary_location.is_accepted&#x60; - &#x60;primary_location.is_oa&#x60; - &#x60;primary_location.is_published&#x60; - &#x60;primary_location.landing_page_url&#x60; - &#x60;primary_location.license&#x60; - &#x60;primary_location.source.has_issn&#x60; - &#x60;primary_location.source.host_institution_lineage&#x60; - &#x60;primary_location.source.host_organization&#x60; - &#x60;primary_location.source.host_organization_lineage&#x60; - &#x60;primary_location.source.id&#x60; - &#x60;primary_location.source.is_in_doaj&#x60; - &#x60;primary_location.source.is_oa&#x60; - &#x60;primary_location.source.issn&#x60; - &#x60;primary_location.source.publisher_lineage&#x60; - &#x60;primary_location.source.type&#x60; - &#x60;primary_location.version&#x60; - &#x60;publication_date&#x60; - &#x60;publication_year&#x60; - &#x60;raw_affiliation_string.search&#x60; - &#x60;referenced_works&#x60; - &#x60;referenced_works_count&#x60; - &#x60;related_to&#x60; - &#x60;repository&#x60; - &#x60;sustainable_development_goals.id&#x60; - &#x60;sustainable_development_goals.score&#x60; - &#x60;title.search&#x60; - &#x60;title_and_abstract.search&#x60; - &#x60;to_publication_date&#x60; - &#x60;to_updated_date&#x60; - &#x60;type&#x60; - &#x60;type_crossref&#x60; - &#x60;version&#x60; | [optional] 
 **user_agent** | [**object**](.md)| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | [**object**](.md)| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

### Return type

[**WorksResponseSchema**](WorksResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

