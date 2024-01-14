# OpenAlex API

![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)

**OpenAlex** is a fully open catalog of the global research system.

It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).

## OpenAPI Specification

[Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)

This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).

The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.

**[Releases](https://github.com/Mearman/openalex-api-spec/releases)**

## Clients

[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)

[![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)

[![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python)
[![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python)
[![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)

---

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.4-3
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Mearman/openalex-python.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Mearman/openalex-python.git`)

Then import the package:

```python
import openalex_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import openalex_api
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openalex_api
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
    api_instance = openalex_api.AuthorsApi(api_client)
    id = 'id_example' # str |
    select = 'select_example' # str |  (optional)
    user_agent = None # object | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = None # object | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

    try:
        # Get Author
        api_response = api_instance.get_author(id, select=select, user_agent=user_agent, mailto=mailto)
        print("The response of AuthorsApi->get_author:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorsApi->get_author: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.openalex.org*

| Class             | Method                                                                                     | HTTP request                       | Description                |
| ----------------- | ------------------------------------------------------------------------------------------ | ---------------------------------- | -------------------------- |
| _AuthorsApi_      | [**get_author**](docs/AuthorsApi.md#get_author)                                            | **GET** /authors/{id}              | Get Author                 |
| _AuthorsApi_      | [**get_authors**](docs/AuthorsApi.md#get_authors)                                          | **GET** /authors                   | List Authors               |
| _AuthorsApi_      | [**get_autocomplete_authors**](docs/AuthorsApi.md#get_autocomplete_authors)                | **GET** /autocomplete/authors      | /autocomplete/authors      |
| _AuthorsApi_      | [**get_random_author**](docs/AuthorsApi.md#get_random_author)                              | **GET** /authors/random            | Get Random Author          |
| _AutocompleteApi_ | [**get_autocomplete**](docs/AutocompleteApi.md#get_autocomplete)                           | **GET** /autocomplete              | /autocomplete              |
| _AutocompleteApi_ | [**get_autocomplete_authors**](docs/AutocompleteApi.md#get_autocomplete_authors)           | **GET** /autocomplete/authors      | /autocomplete/authors      |
| _AutocompleteApi_ | [**get_autocomplete_concepts**](docs/AutocompleteApi.md#get_autocomplete_concepts)         | **GET** /autocomplete/concepts     | /autocomplete/concepts     |
| _AutocompleteApi_ | [**get_autocomplete_funders**](docs/AutocompleteApi.md#get_autocomplete_funders)           | **GET** /autocomplete/funders      | /autocomplete/funders      |
| _AutocompleteApi_ | [**get_autocomplete_institutions**](docs/AutocompleteApi.md#get_autocomplete_institutions) | **GET** /autocomplete/institutions | /autocomplete/institutions |
| _AutocompleteApi_ | [**get_autocomplete_publishers**](docs/AutocompleteApi.md#get_autocomplete_publishers)     | **GET** /autocomplete/publishers   | /autocomplete/publishers   |
| _AutocompleteApi_ | [**get_autocomplete_sources**](docs/AutocompleteApi.md#get_autocomplete_sources)           | **GET** /autocomplete/sources      | /autocomplete/sources      |
| _AutocompleteApi_ | [**get_autocomplete_works**](docs/AutocompleteApi.md#get_autocomplete_works)               | **GET** /autocomplete/works        | /autocomplete/works        |
| _ConceptsApi_     | [**get_autocomplete_concepts**](docs/ConceptsApi.md#get_autocomplete_concepts)             | **GET** /autocomplete/concepts     | /autocomplete/concepts     |
| _ConceptsApi_     | [**get_concept**](docs/ConceptsApi.md#get_concept)                                         | **GET** /concepts/{id}             | /concepts/{id}             |
| _ConceptsApi_     | [**get_concepts**](docs/ConceptsApi.md#get_concepts)                                       | **GET** /concepts                  | /concepts                  |
| _FundersApi_      | [**get_autocomplete_funders**](docs/FundersApi.md#get_autocomplete_funders)                | **GET** /autocomplete/funders      | /autocomplete/funders      |
| _FundersApi_      | [**get_funder**](docs/FundersApi.md#get_funder)                                            | **GET** /funders/{id}              | /funders/{id}              |
| _FundersApi_      | [**get_funders**](docs/FundersApi.md#get_funders)                                          | **GET** /funders                   | /funders                   |
| _InfoApi_         | [**get_root**](docs/InfoApi.md#get_root)                                                   | **GET** /                          | Root                       |
| _InstitutionsApi_ | [**get_autocomplete_institutions**](docs/InstitutionsApi.md#get_autocomplete_institutions) | **GET** /autocomplete/institutions | /autocomplete/institutions |
| _InstitutionsApi_ | [**get_institution**](docs/InstitutionsApi.md#get_institution)                             | **GET** /institutions/{id}         | /institutions/{id}         |
| _InstitutionsApi_ | [**get_institutions**](docs/InstitutionsApi.md#get_institutions)                           | **GET** /institutions              | /institutions              |
| _ListApi_         | [**get_works**](docs/ListApi.md#get_works)                                                 | **GET** /works                     | /works                     |
| _NgramsApi_       | [**get_work_ngrams**](docs/NgramsApi.md#get_work_ngrams)                                   | **GET** /works/{id}/ngrams         | /works/{id}/ngrams         |
| _PeopleApi_       | [**get_person**](docs/PeopleApi.md#get_person)                                             | **GET** /people/{id}               | /people/{id}               |
| _PublishersApi_   | [**get_autocomplete_publishers**](docs/PublishersApi.md#get_autocomplete_publishers)       | **GET** /autocomplete/publishers   | /autocomplete/publishers   |
| _PublishersApi_   | [**get_publisher**](docs/PublishersApi.md#get_publisher)                                   | **GET** /publishers/{id}           | /publishers/{id}           |
| _PublishersApi_   | [**get_publishers**](docs/PublishersApi.md#get_publishers)                                 | **GET** /publishers                | /publishers                |
| _SingleApi_       | [**get_work**](docs/SingleApi.md#get_work)                                                 | **GET** /works/{id}                | /works/{id}                |
| _SingleApi_       | [**get_work_ngrams**](docs/SingleApi.md#get_work_ngrams)                                   | **GET** /works/{id}/ngrams         | /works/{id}/ngrams         |
| _SourcesApi_      | [**get_autocomplete_sources**](docs/SourcesApi.md#get_autocomplete_sources)                | **GET** /autocomplete/sources      | /autocomplete/sources      |
| _SourcesApi_      | [**get_source**](docs/SourcesApi.md#get_source)                                            | **GET** /sources/{id}              | /sources/{id}              |
| _SourcesApi_      | [**get_sources**](docs/SourcesApi.md#get_sources)                                          | **GET** /sources                   | /sources                   |
| _WorksApi_        | [**get_autocomplete_works**](docs/WorksApi.md#get_autocomplete_works)                      | **GET** /autocomplete/works        | /autocomplete/works        |
| _WorksApi_        | [**get_work**](docs/WorksApi.md#get_work)                                                  | **GET** /works/{id}                | /works/{id}                |
| _WorksApi_        | [**get_work_ngrams**](docs/WorksApi.md#get_work_ngrams)                                    | **GET** /works/{id}/ngrams         | /works/{id}/ngrams         |
| _WorksApi_        | [**get_works**](docs/WorksApi.md#get_works)                                                | **GET** /works                     | /works                     |

## Documentation For Models

- [AffiliationsInner](docs/AffiliationsInner.md)
- [Apc](docs/Apc.md)
- [AssociatedInstitution](docs/AssociatedInstitution.md)
- [Author](docs/Author.md)
- [AuthorsResponseSchema](docs/AuthorsResponseSchema.md)
- [AutoCompleteResultItem](docs/AutoCompleteResultItem.md)
- [AutoCompleteResultSchema](docs/AutoCompleteResultSchema.md)
- [BaseSelectionAttributes](docs/BaseSelectionAttributes.md)
- [Concept](docs/Concept.md)
- [ConceptIds](docs/ConceptIds.md)
- [ConceptSchema](docs/ConceptSchema.md)
- [ConceptsResponseSchema](docs/ConceptsResponseSchema.md)
- [DehydratedConcept](docs/DehydratedConcept.md)
- [DehydratedInstitution](docs/DehydratedInstitution.md)
- [ErrorMessage](docs/ErrorMessage.md)
- [FunderSchema](docs/FunderSchema.md)
- [FundersArray](docs/FundersArray.md)
- [Geo](docs/Geo.md)
- [Ids](docs/Ids.md)
- [InstitutionSchema](docs/InstitutionSchema.md)
- [InstitutionsResponseSchema](docs/InstitutionsResponseSchema.md)
- [InternationalDescription](docs/InternationalDescription.md)
- [InternationalDisplayName](docs/InternationalDisplayName.md)
- [InternationalDisplayNameAndDescription](docs/InternationalDisplayNameAndDescription.md)
- [Internationalisation](docs/Internationalisation.md)
- [Location](docs/Location.md)
- [LocationSource](docs/LocationSource.md)
- [Meta](docs/Meta.md)
- [NgramMeta](docs/NgramMeta.md)
- [PersonResponseSchema](docs/PersonResponseSchema.md)
- [PublisherSchema](docs/PublisherSchema.md)
- [PublisherSchemaParentPublisher](docs/PublisherSchemaParentPublisher.md)
- [PublishersResponseSchema](docs/PublishersResponseSchema.md)
- [Role](docs/Role.md)
- [RootResponseSchema](docs/RootResponseSchema.md)
- [SourceSchema](docs/SourceSchema.md)
- [SourcesArray](docs/SourcesArray.md)
- [SummaryStats](docs/SummaryStats.md)
- [WorkAttributes](docs/WorkAttributes.md)
- [WorkNgramsSchema](docs/WorkNgramsSchema.md)
- [WorkSchema](docs/WorkSchema.md)
- [WorkSchemaBiblio](docs/WorkSchemaBiblio.md)
- [WorkSchemaCitedByPercentileYear](docs/WorkSchemaCitedByPercentileYear.md)
- [WorkSchemaOpenAccess](docs/WorkSchemaOpenAccess.md)
- [WorksResponseSchema](docs/WorksResponseSchema.md)

<a id="documentation-for-authorization"></a>

## Documentation For Authorization

Endpoints do not require authorization.

## Author
