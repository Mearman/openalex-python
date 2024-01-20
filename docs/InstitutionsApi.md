# openalex_api.InstitutionsApi

All URIs are relative to *https://api.openalex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_autocomplete_institutions**](InstitutionsApi.md#get_autocomplete_institutions) | **GET** /autocomplete/institutions | /autocomplete/institutions
[**get_institution**](InstitutionsApi.md#get_institution) | **GET** /institutions/{id} | /institutions/{id}
[**get_institutions**](InstitutionsApi.md#get_institutions) | **GET** /institutions | /institutions


# **get_autocomplete_institutions**
> AutoCompleteResultSchema get_autocomplete_institutions(q=q, user_agent=user_agent, mailto=mailto)

/autocomplete/institutions



### Example


```python
import time
import os
import openalex_api
from openalex_api.models.auto_complete_result_schema import AutoCompleteResultSchema
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
    api_instance = openalex_api.InstitutionsApi(api_client)
    q = 'q_example' # str |  (optional)
    user_agent = None # object | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = None # object | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

    try:
        # /autocomplete/institutions
        api_response = api_instance.get_autocomplete_institutions(q=q, user_agent=user_agent, mailto=mailto)
        print("The response of InstitutionsApi->get_autocomplete_institutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->get_autocomplete_institutions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **user_agent** | [**object**](.md)| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | [**object**](.md)| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

### Return type

[**AutoCompleteResultSchema**](AutoCompleteResultSchema.md)

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

# **get_institution**
> InstitutionSchema get_institution(id, select=select, user_agent=user_agent, mailto=mailto)

/institutions/{id}



### Example


```python
import time
import os
import openalex_api
from openalex_api.models.institution_schema import InstitutionSchema
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
    api_instance = openalex_api.InstitutionsApi(api_client)
    id = 'id_example' # str | 
    select = 'select_example' # str |  (optional)
    user_agent = None # object | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = None # object | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

    try:
        # /institutions/{id}
        api_response = api_instance.get_institution(id, select=select, user_agent=user_agent, mailto=mailto)
        print("The response of InstitutionsApi->get_institution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->get_institution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **select** | **str**|  | [optional] 
 **user_agent** | [**object**](.md)| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | [**object**](.md)| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

### Return type

[**InstitutionSchema**](InstitutionSchema.md)

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

# **get_institutions**
> InstitutionsResponseSchema get_institutions(api_key=api_key, cursor=cursor, filter=filter, group_by=group_by, page=page, per_page=per_page, sample=sample, search=search, select=select, sort=sort, user_agent=user_agent, mailto=mailto)

/institutions



### Example


```python
import time
import os
import openalex_api
from openalex_api.models.institutions_response_schema import InstitutionsResponseSchema
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
    api_instance = openalex_api.InstitutionsApi(api_client)
    api_key = 'api_key_example' # str |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    filter = 'filter_example' # str |  (optional)
    group_by = 'group_by_example' # str |  (optional)
    page = 1 # int |  (optional)
    per_page = 3 # int |  (optional)
    sample = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    select = 'select_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    user_agent = None # object | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = None # object | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

    try:
        # /institutions
        api_response = api_instance.get_institutions(api_key=api_key, cursor=cursor, filter=filter, group_by=group_by, page=page, per_page=per_page, sample=sample, search=search, select=select, sort=sort, user_agent=user_agent, mailto=mailto)
        print("The response of InstitutionsApi->get_institutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->get_institutions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **group_by** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **sample** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **select** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **user_agent** | [**object**](.md)| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | [**object**](.md)| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

### Return type

[**InstitutionsResponseSchema**](InstitutionsResponseSchema.md)

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

