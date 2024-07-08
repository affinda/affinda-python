<a id="_affinda_api"></a>

# \_affinda\_api

<a id="_affinda_api.AffindaAPI"></a>

## AffindaAPI Objects

```python
class AffindaAPI(AffindaAPIOperationsMixin)
```

Affinda API client for Python.

**Arguments**:

- `credential` (`~azure.core.credentials.TokenCredential`): Credential needed for the client to connect to Azure.
- `region` (`str or ~affinda.models.Region`): region - server parameter. Default value is "api".

<a id="operations._affinda_api_operations"></a>

# operations.\_affinda\_api\_operations

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin"></a>

## AffindaAPIOperationsMixin Objects

```python
class AffindaAPIOperationsMixin(object)
```

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_workspaces"></a>

#### get\_all\_workspaces

```python
def get_all_workspaces(organization, name=None, **kwargs)
```

Get list of all workspaces.

Returns your workspaces.

**Arguments**:

- `organization` (`str`): Filter by organization.
- `name` (`str`): Filter by name. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.Workspace]`: list of Workspace, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_workspace"></a>

#### create\_workspace

```python
def create_workspace(body, **kwargs)
```

Create a workspace.

Create a workspace.

**Arguments**:

- `body` (`~affinda.models.WorkspaceCreate`): Workspace to create.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Workspace`: Workspace, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_workspace"></a>

#### get\_workspace

```python
def get_workspace(identifier, **kwargs)
```

Get specific workspace.

Return a specific workspace.

**Arguments**:

- `identifier` (`str`): Workspace's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Workspace`: Workspace, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_workspace"></a>

#### update\_workspace

```python
def update_workspace(identifier, body, **kwargs)
```

Update a workspace.

Update a workspace.

**Arguments**:

- `identifier` (`str`): Workspace's identifier.
- `body` (`~affinda.models.WorkspaceUpdate`): Workspace data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Workspace`: Workspace, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_workspace"></a>

#### delete\_workspace

```python
def delete_workspace(identifier, **kwargs)
```

Delete a workspace.

Deletes the specified workspace from the database.

**Arguments**:

- `identifier` (`str`): Workspace's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_usage_by_workspace"></a>

#### get\_usage\_by\_workspace

```python
def get_usage_by_workspace(identifier, start=None, end=None, **kwargs)
```

Get usage by workspace.

Return monthly credits consumption of a workspace.

**Arguments**:

- `identifier` (`str`): Workspace's identifier.
- `start` (`str`): Start date of the period to retrieve. Format: YYYY-MM. Default value is None.
- `end` (`str`): End date of the period to retrieve. Format: YYYY-MM. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.UsageByWorkspace]`: list of UsageByWorkspace, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_workspace_memberships"></a>

#### get\_all\_workspace\_memberships

```python
def get_all_workspace_memberships(offset=None,
                                  limit=None,
                                  workspace=None,
                                  user=None,
                                  **kwargs)
```

Get list of all workspace memberships.

Returns the memberships of your workspaces.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `workspace` (`str`): Filter by workspace. Default value is None.
- `user` (`str`): Partial text match on user's email, case-insensitive. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsZ1JuagV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchema`: PathsZ1JuagV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchema, or the
result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_workspace_membership"></a>

#### create\_workspace\_membership

```python
def create_workspace_membership(body, **kwargs)
```

Create a workspace membership.

Create a workspace membership.

**Arguments**:

- `body` (`~affinda.models.WorkspaceMembershipCreate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.WorkspaceMembership`: WorkspaceMembership, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_workspace_membership"></a>

#### get\_workspace\_membership

```python
def get_workspace_membership(identifier, **kwargs)
```

Get specific workspace membership.

Return a specific workspace membership.

**Arguments**:

- `identifier` (`str`): Workspace membership's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.WorkspaceMembership`: WorkspaceMembership, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_workspace_membership"></a>

#### delete\_workspace\_membership

```python
def delete_workspace_membership(identifier, **kwargs)
```

Delete a workspace membership.

Remove an user from a workspace.

**Arguments**:

- `identifier` (`str`): Workspace membership's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_collections"></a>

#### get\_all\_collections

```python
def get_all_collections(workspace, **kwargs)
```

Get list of all collections.

Returns your collections.

**Arguments**:

- `workspace` (`str`): Filter by workspace.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.Collection]`: list of Collection, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_collection"></a>

#### create\_collection

```python
def create_collection(body, **kwargs)
```

Create a collection.

Create a collection.

**Arguments**:

- `body` (`~affinda.models.CollectionCreate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Collection`: Collection, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_collection"></a>

#### get\_collection

```python
def get_collection(identifier, **kwargs)
```

Get specific collection.

Return a specific collection.

**Arguments**:

- `identifier` (`str`): Collection's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Collection`: Collection, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_collection"></a>

#### update\_collection

```python
def update_collection(identifier, body, **kwargs)
```

Update a collection.

Update data of a collection.

**Arguments**:

- `identifier` (`str`): Collection's identifier.
- `body` (`~affinda.models.CollectionUpdate`): Collection data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Collection`: Collection, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_collection"></a>

#### delete\_collection

```python
def delete_collection(identifier, **kwargs)
```

Delete a collection.

Deletes the specified collection from the database.

**Arguments**:

- `identifier` (`str`): Collection's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_data_field_for_collection"></a>

#### create\_data\_field\_for\_collection

```python
def create_data_field_for_collection(identifier, body, **kwargs)
```

Create data field for a collection along with a new data point.

Create data field for a collection along with a new data point.

**Arguments**:

- `identifier` (`str`): Collection's identifier.
- `body` (`~affinda.models.DataFieldCreate`): The data field and data point to be created.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.DataField`: DataField, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_data_field_for_collection"></a>

#### get\_data\_field\_for\_collection

```python
def get_data_field_for_collection(identifier, datapoint_identifier, **kwargs)
```

Get data field for a collection assosciated with a data point.

Get a data field for a collection assosciated with a data point.

**Arguments**:

- `identifier` (`str`): Collection's identifier.
- `datapoint_identifier` (`str`): Datapoint's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.CollectionField`: CollectionField, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_data_field_for_collection"></a>

#### update\_data\_field\_for\_collection

```python
def update_data_field_for_collection(identifier, datapoint_identifier, body,
                                     **kwargs)
```

Update data field for a collection assosciated with a data point.

Update data field for a collection assosciated with a data point.

**Arguments**:

- `identifier` (`str`): Collection's identifier.
- `datapoint_identifier` (`str`): Datapoint's identifier.
- `body` (`~affinda.models.CollectionField`): Data field properties to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.CollectionField`: CollectionField, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_usage_by_collection"></a>

#### get\_usage\_by\_collection

```python
def get_usage_by_collection(identifier, start=None, end=None, **kwargs)
```

Get usage by collection.

Return monthly credits consumption of a collection.

**Arguments**:

- `identifier` (`str`): Collection's identifier.
- `start` (`str`): Start date of the period to retrieve. Format: YYYY-MM. Default value is None.
- `end` (`str`): End date of the period to retrieve. Format: YYYY-MM. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.UsageByCollection]`: list of UsageByCollection, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_documents"></a>

#### get\_all\_documents

```python
def get_all_documents(offset=None,
                      limit=None,
                      workspace=None,
                      collection=None,
                      state=None,
                      tags=None,
                      created_dt=None,
                      search=None,
                      ordering=None,
                      include_data=None,
                      exclude=None,
                      in_review=None,
                      failed=None,
                      ready=None,
                      validatable=None,
                      has_challenges=None,
                      custom_identifier=None,
                      compact=None,
                      count=None,
                      **kwargs)
```

Get list of all documents.

Returns all the document summaries for that user, limited to 300 per page.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `workspace` (`str`): Filter by workspace. Default value is None.
- `collection` (`str`): Filter by collection. Default value is None.
- `state` (`str or ~affinda.models.DocumentState`): Filter by the document's state. Default value is None.
- `tags` (`list[int]`): Filter by tag's IDs. Default value is None.
- `created_dt` (`str or ~affinda.models.DateRange`): Filter by created datetime. Default value is None.
- `search` (`str`): Partial, case-insensitive match with file name or tag name. Default value is
None.
- `ordering` (`list[str]`): Sort the result set. A "-" at the beginning denotes DESC sort, e.g.
-created_dt. Sort by multiple fields is supported. Supported values include: 'file_name',
'extractor', 'created_dt', 'validated_dt', 'archived_dt' and 'parsed__:code:`<dataPointSlug>`'.
Default value is None.
- `include_data` (`bool`): By default, this endpoint returns only the meta data of the documents. Set
this to ``true`` will return a summary of the data that was parsed. If you want to retrieve the
full set of data for a document, use the ``GET /documents/{identifier}`` endpoint. Default
value is None.
- `exclude` (`list[str]`): Exclude some documents from the result. Default value is None.
- `in_review` (`bool`): Exclude documents that are currently being reviewed. Default value is None.
- `failed` (`bool`): Filter by failed status. Default value is None.
- `ready` (`bool`): Filter by ready status. Default value is None.
- `validatable` (`bool`): Filter for validatable documents. Default value is None.
- `has_challenges` (`bool`): Filter for documents with challenges. Default value is None.
- `custom_identifier` (`str`): Filter for documents with this custom identifier. Default value is
None.
- `compact` (`bool`): If "true", the response is compacted to annotations' parsed data. Annotations'
meta data are excluded. Default is "false".
- `count` (`bool`): If "false", the documents count is not computed, thus saving time for large
collections. Default is "true".
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsOxm5M7V3DocumentsGetResponses200ContentApplicationJsonSchema`: PathsOxm5M7V3DocumentsGetResponses200ContentApplicationJsonSchema, or the result of
cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_document"></a>

#### create\_document

```python
def create_document(file=None,
                    url=None,
                    data=None,
                    collection=None,
                    workspace=None,
                    wait=True,
                    identifier=None,
                    custom_identifier=None,
                    file_name=None,
                    expiry_time=None,
                    language=None,
                    reject_duplicates=None,
                    region_bias=None,
                    low_priority=None,
                    compact=None,
                    delete_after_parse=None,
                    enable_validation_tool=None,
                    **kwargs)
```

Upload a document for parsing.

Uploads a document for parsing. When successful, returns an ``identifier`` in the response for
subsequent use with the `/documents/{identifier} <#get-/v3/documents/-identifier->`_ endpoint
to check processing status and retrieve results.:code:`<br/>`.

**Arguments**:

- `file` (`IO`): Default value is None.
- `url` (`str`): URL to download the document. Default value is None.
- `data` (`any`): Create resume or job description directly from data. Default value is None.
- `collection` (`str`): Default value is None.
- `workspace` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.
- `identifier` (`str`): Deprecated in favor of ``customIdentifier``. Default value is None.
- `custom_identifier` (`str`): Specify a custom identifier for the document if you need one, not
required to be unique. Default value is None.
- `file_name` (`str`): Default value is None.
- `expiry_time` (`~datetime.datetime`): Default value is None.
- `language` (`str`): Default value is None.
- `reject_duplicates` (`bool`): Default value is None.
- `region_bias` (`str`): A JSON representation of the RegionBias object. Default value is None.
- `low_priority` (`bool`): Explicitly mark this document as low priority. Default value is None.
- `compact` (`bool`): If true, the returned parse result (assuming ``wait`` is also true) will be a
compact version of the full result. Default value is None.
- `delete_after_parse` (`bool`): If true, no data will be stored after parsing. Only compatible with
requests where wait: True. Default value is None.
- `enable_validation_tool` (`bool`): If true, the document will be viewable in the Affinda Validation
Tool. Set to False to optimize parsing speed. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Document`: Document, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_document"></a>

#### get\_document

```python
def get_document(identifier, format=None, compact=None, **kwargs)
```

Get specific document.

Return a specific document.

**Arguments**:

- `identifier` (`str`): Document's identifier.
- `format` (`str or ~affinda.models.DocumentFormat`): Specify which format you want the response to be. Default is "json".
- `compact` (`bool`): If "true", the response is compacted to annotations' parsed data. Annotations'
meta data are excluded. Default is "false".
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Document`: Document, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_document"></a>

#### update\_document

```python
def update_document(identifier, body, **kwargs)
```

Update a document.

Update file name, expiry time, or move to another collection, etc.

**Arguments**:

- `identifier` (`str`): Document's identifier.
- `body` (`~affinda.models.DocumentUpdate`): Document data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Document`: Document, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_document"></a>

#### delete\_document

```python
def delete_document(identifier, **kwargs)
```

Delete a document.

Deletes the specified document from the database.

**Arguments**:

- `identifier` (`str`): Document's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_document_data"></a>

#### update\_document\_data

```python
def update_document_data(identifier, body, **kwargs)
```

Update a document's data.

Update data of a document.
Only applicable for resumes and job descriptions. For other document types, please use the
``PATCH /annotations/{id}`` endpoint or the ``POST /annotations/batch_update`` endpoint.

**Arguments**:

- `identifier` (`str`): Resume or Job Description identifier.
- `body` (`any`): Resume data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Document`: Document, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.batch_add_tag"></a>

#### batch\_add\_tag

```python
def batch_add_tag(body, **kwargs)
```

Add a tag to documents.

Add a tag to documents.
Tags are used to group documents together.
Tags can be used to filter documents.

**Arguments**:

- `body` (`~affinda.models.BatchAddTagRequest`): Specify the tag and the documents to tag.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.batch_remove_tag"></a>

#### batch\_remove\_tag

```python
def batch_remove_tag(body, **kwargs)
```

Remove a tag from documents.

Remove a tag from documents.

**Arguments**:

- `body` (`~affinda.models.BatchRemoveTagRequest`): Specify the tag and the documents to remove the tag from.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.edit_document_pages"></a>

#### edit\_document\_pages

```python
def edit_document_pages(identifier, body, **kwargs)
```

Edit pages of a document.

Split / merge / rotate / delete pages of a document.
Documents with multiple pages can be splitted into multiple documents, or merged into one
document.
Each page can also be rotated. Edit operations will trigger re-parsing of the documents
involved.

**Arguments**:

- `identifier` (`str`): Document's identifier.
- `body` (`~affinda.models.DocumentEditRequest`): Describe how the pages should be edited.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.Meta]`: list of Meta, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_validation_results"></a>

#### get\_all\_validation\_results

```python
def get_all_validation_results(document, offset=None, limit=None, **kwargs)
```

Get list of all validation results.

Returns the validation results of a document.

**Arguments**:

- `document` (`str`): Filter by document.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.ValidationResult]`: list of ValidationResult, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_validation_result"></a>

#### create\_validation\_result

```python
def create_validation_result(body, **kwargs)
```

Create a validation result.

Create a validation result.

**Arguments**:

- `body` (`~affinda.models.ValidationResultCreate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ValidationResult`: ValidationResult, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_validation_result"></a>

#### get\_validation\_result

```python
def get_validation_result(id, **kwargs)
```

Get specific validation result.

Return a specific validation result.

**Arguments**:

- `id` (`int`): Validation result's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ValidationResult`: ValidationResult, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_validation_result"></a>

#### update\_validation\_result

```python
def update_validation_result(id, body, **kwargs)
```

Update a validation result.

Update a validation result.

**Arguments**:

- `id` (`int`): Validation result's ID.
- `body` (`~affinda.models.ValidationResultUpdate`): Validation result data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ValidationResult`: ValidationResult, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_validation_result"></a>

#### delete\_validation\_result

```python
def delete_validation_result(id, **kwargs)
```

Delete a validation result.

Remove validation result.

**Arguments**:

- `id` (`int`): Validation result's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.batch_create_validation_results"></a>

#### batch\_create\_validation\_results

```python
def batch_create_validation_results(body, **kwargs)
```

Batch create validation results.

Batch create validation results.

**Arguments**:

- `body` (`list[~affinda.models.ValidationResultCreate]`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.ValidationResult]`: list of ValidationResult, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.batch_delete_validation_results"></a>

#### batch\_delete\_validation\_results

```python
def batch_delete_validation_results(body, **kwargs)
```

Batch delete validation results.

Batch delete validation results.

**Arguments**:

- `body` (`~affinda.models.BatchDeleteValidationResultsRequest`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_extractors"></a>

#### get\_all\_extractors

```python
def get_all_extractors(organization,
                       include_public_extractors=None,
                       name=None,
                       validatable=None,
                       **kwargs)
```

Get list of all extractors.

Returns your custom extractors as well as Affinda's off-the-shelf extractors.

**Arguments**:

- `organization` (`str`): Filter by organization.
- `include_public_extractors` (`bool`): Whether to include Affinda's off-the-shelf extractors.
Default value is None.
- `name` (`str`): Filter by name. Default value is None.
- `validatable` (`bool`): Filter by validatable. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.Extractor]`: list of Extractor, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_extractor"></a>

#### create\_extractor

```python
def create_extractor(body=None, **kwargs)
```

Create an extractor.

Create a custom extractor.

**Arguments**:

- `body` (`~affinda.models.ExtractorCreate`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Extractor`: Extractor, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_extractor"></a>

#### get\_extractor

```python
def get_extractor(identifier, **kwargs)
```

Get specific extractor.

Return a specific extractor.

**Arguments**:

- `identifier` (`str`): Extractor's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Extractor`: Extractor, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_extractor"></a>

#### update\_extractor

```python
def update_extractor(identifier, body, **kwargs)
```

Update an extractor.

Update data of an extractor.

**Arguments**:

- `identifier` (`str`): Extractor's identifier.
- `body` (`~affinda.models.ExtractorUpdate`): Extractor data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Extractor`: Extractor, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_extractor"></a>

#### delete\_extractor

```python
def delete_extractor(identifier, **kwargs)
```

Delete an extractor.

Deletes the specified extractor from the database.

**Arguments**:

- `identifier` (`str`): Extractor's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_data_points"></a>

#### get\_all\_data\_points

```python
def get_all_data_points(offset=None,
                        limit=None,
                        organization=None,
                        include_public=None,
                        extractor=None,
                        slug=None,
                        description=None,
                        annotation_content_type=None,
                        identifier=None,
                        **kwargs)
```

Get list of all data points.

Returns your custom data points as well as Affinda's off-the-shelf data points.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `organization` (`str`): Filter by organization. Default value is None.
- `include_public` (`bool`): Allows you to include public data points in the response when you're
filtering by organization. Default value is None.
- `extractor` (`str`): Filter by extractor. Default value is None.
- `slug` (`str`): Filter by slug. Default value is None.
- `description` (`str`): Filter by description. Default value is None.
- `annotation_content_type` (`str`): Filter by annotation content type, e.g. text, integer, float,
date, etc. Default value is None.
- `identifier` (`list[str]`): Filter by specific identifiers. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.DataPoint]`: list of DataPoint, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_data_point"></a>

#### create\_data\_point

```python
def create_data_point(body=None, **kwargs)
```

Create a data point.

Create a custom data point.

**Arguments**:

- `body` (`~affinda.models.DataPointCreate`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.DataPoint`: DataPoint, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_data_point"></a>

#### get\_data\_point

```python
def get_data_point(identifier, **kwargs)
```

Get specific data point.

Return a specific data point.

**Arguments**:

- `identifier` (`str`): Data point's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.DataPoint`: DataPoint, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_data_point"></a>

#### update\_data\_point

```python
def update_data_point(identifier, body, **kwargs)
```

Update a data point.

Update data of a data point.

**Arguments**:

- `identifier` (`str`): DataPoint's identifier.
- `body` (`~affinda.models.DataPointUpdate`): Data point to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.DataPoint`: DataPoint, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_data_point"></a>

#### delete\_data\_point

```python
def delete_data_point(identifier, **kwargs)
```

Delete a data point.

Deletes the specified data point from the database.

**Arguments**:

- `identifier` (`str`): DataPoint's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_data_point_choices"></a>

#### get\_data\_point\_choices

```python
def get_data_point_choices(data_point,
                           collection,
                           offset=None,
                           limit=None,
                           search=None,
                           **kwargs)
```

Get list of data point choices.

Returns available choices for a specific enum data point.

**Arguments**:

- `data_point` (`str`): The data point to get choices for.
- `collection` (`str`): The collection to get choices for.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `search` (`str`): Filter choices by searching for a substring. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsMnwxgV3DataPointChoicesGetResponses200ContentApplicationJsonSchema`: PathsMnwxgV3DataPointChoicesGetResponses200ContentApplicationJsonSchema, or the result
of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_data_point_choice"></a>

#### create\_data\_point\_choice

```python
def create_data_point_choice(body=None, **kwargs)
```

Create a data point choice.

Create a custom data point choice.

**Arguments**:

- `body` (`~affinda.models.DataPointChoiceCreate`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.DataPointChoice`: DataPointChoice, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_data_point_choice"></a>

#### get\_data\_point\_choice

```python
def get_data_point_choice(id, **kwargs)
```

Get specific data point choice.

Return a specific data point choice.

**Arguments**:

- `id` (`int`): Data point choice's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.DataPointChoice`: DataPointChoice, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_data_point_choice"></a>

#### update\_data\_point\_choice

```python
def update_data_point_choice(id, body, **kwargs)
```

Update a data point choice.

Update data of a data point choice.

**Arguments**:

- `id` (`int`): Data point choice's ID.
- `body` (`~affinda.models.DataPointChoiceUpdate`): Data point choice to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.DataPointChoice`: DataPointChoice, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_data_point_choice"></a>

#### delete\_data\_point\_choice

```python
def delete_data_point_choice(id, **kwargs)
```

Delete a data point choice.

Deletes the specified data point choice from the database.

**Arguments**:

- `id` (`int`): Data point choice's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.replace_data_point_choices"></a>

#### replace\_data\_point\_choices

```python
def replace_data_point_choices(body=None, **kwargs)
```

Replace choices of a data point.

Replace choices of a data point. Existing choices and incoming choices are matched base on
their ``value``. New ``value`` will be created, existing ``value`` will be updated, and
``value`` not in incoming choices will be deleted.

**Arguments**:

- `body` (`~affinda.models.DataPointChoiceReplaceRequest`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.DataPointChoiceReplaceResponse`: DataPointChoiceReplaceResponse, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_annotations"></a>

#### get\_all\_annotations

```python
def get_all_annotations(document, **kwargs)
```

Get list of all annotations.

Returns your annotations.

**Arguments**:

- `document` (`str`): Filter by document.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Paths1D5Zg6MV3AnnotationsGetResponses200ContentApplicationJsonSchema`: Paths1D5Zg6MV3AnnotationsGetResponses200ContentApplicationJsonSchema, or the result of
cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_annotation"></a>

#### create\_annotation

```python
def create_annotation(body, **kwargs)
```

Create a annotation.

Create a annotation.

**Arguments**:

- `body` (`~affinda.models.AnnotationCreate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.AnnotationWithValidationResults or None`: AnnotationWithValidationResults or None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_annotation"></a>

#### get\_annotation

```python
def get_annotation(id, **kwargs)
```

Get specific annotation.

Return a specific annotation.

**Arguments**:

- `id` (`int`): Annotation's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Annotation or None`: Annotation or None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_annotation"></a>

#### update\_annotation

```python
def update_annotation(id, body, **kwargs)
```

Update an annotation.

Update data of an annotation.

**Arguments**:

- `id` (`int`): Annotation's ID.
- `body` (`~affinda.models.AnnotationUpdate`): Annotation data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Annotation or None`: Annotation or None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_annotation"></a>

#### delete\_annotation

```python
def delete_annotation(id, **kwargs)
```

Delete an annotation.

Deletes the specified annotation from the database.

**Arguments**:

- `id` (`int`): Annotation's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.AnotationDelete`: AnotationDelete, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.batch_create_annotations"></a>

#### batch\_create\_annotations

```python
def batch_create_annotations(body, **kwargs)
```

Batch create annotations.

Batch create annotations.

**Arguments**:

- `body` (`list[~affinda.models.AnnotationCreate]`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.Annotation]`: list of Annotation, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.batch_update_annotations"></a>

#### batch\_update\_annotations

```python
def batch_update_annotations(body, **kwargs)
```

Batch update annotations.

Batch update annotations.

**Arguments**:

- `body` (`list[~affinda.models.AnnotationBatchUpdate]`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.Annotation]`: list of Annotation, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.batch_delete_annotations"></a>

#### batch\_delete\_annotations

```python
def batch_delete_annotations(body, **kwargs)
```

Batch delete annotations.

Batch delete annotations.

**Arguments**:

- `body` (`list[int]`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.BatchDeleteAnnotationsResponse`: BatchDeleteAnnotationsResponse, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_mapping_data_source"></a>

#### create\_mapping\_data\_source

```python
def create_mapping_data_source(body, **kwargs)
```

Create a mapping data source.

Create a custom mapping data source.

**Arguments**:

- `body` (`~affinda.models.MappingDataSourceCreate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.MappingDataSource`: MappingDataSource, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.list_mapping_data_sources"></a>

#### list\_mapping\_data\_sources

```python
def list_mapping_data_sources(offset=None,
                              limit=None,
                              name=None,
                              organization=None,
                              workspace=None,
                              identifier=None,
                              **kwargs)
```

List mapping data sources.

Returns the list of all custom mapping data sources.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `name` (`str`): Filter by name. Default value is None.
- `organization` (`str`): Filter by organization. Default value is None.
- `workspace` (`str`): Filter by workspace. Default value is None.
- `identifier` (`str`): Filter by identifier. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Paths11QdcofV3MappingDataSourcesGetResponses200ContentApplicationJsonSchema`: Paths11QdcofV3MappingDataSourcesGetResponses200ContentApplicationJsonSchema, or the
result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_mapping_data_source"></a>

#### get\_mapping\_data\_source

```python
def get_mapping_data_source(identifier, **kwargs)
```

Get specific mapping data source.

Return a specific mapping data source.

**Arguments**:

- `identifier` (`str`): Mapping data source's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.MappingDataSource`: MappingDataSource, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_mapping_data_source"></a>

#### delete\_mapping\_data\_source

```python
def delete_mapping_data_source(identifier, **kwargs)
```

Delete specific mapping data source.

Delete the specified mapping data source from the database.

**Arguments**:

- `identifier` (`str`): Mapping data source's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.list_mapping_data_source_values"></a>

#### list\_mapping\_data\_source\_values

```python
def list_mapping_data_source_values(identifier,
                                    limit=None,
                                    offset=None,
                                    search=None,
                                    annotation=None,
                                    **kwargs)
```

List values for a mapping data source.

Returns the list of all values in a mapping data source.

**Arguments**:

- `identifier` (`str`): Mapping data source's identifier.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `search` (`str`): Search for specific values. Default value is None.
- `annotation` (`int`): Filter based on annotation ID. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Paths1Qr7BnyV3MappingDataSourcesIdentifierValuesGetResponses200ContentApplicationJsonSchema`: Paths1Qr7BnyV3MappingDataSourcesIdentifierValuesGetResponses200ContentApplicationJsonSchema, or
the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.replace_mapping_data_source_values"></a>

#### replace\_mapping\_data\_source\_values

```python
def replace_mapping_data_source_values(identifier, body, **kwargs)
```

Replace values for a mapping data source.

Replaces the list of all values in a mapping data source.

**Arguments**:

- `identifier` (`str`): Mapping data source's identifier.
- `body` (`list[any]`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[any]`: list of any, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.add_mapping_data_source_value"></a>

#### add\_mapping\_data\_source\_value

```python
def add_mapping_data_source_value(identifier, body, **kwargs)
```

Add value for a mapping data source.

Adds a value to a mapping data source.

**Arguments**:

- `identifier` (`str`): Mapping data source's identifier.
- `body` (`any`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`any`: any, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_mapping_data_source_value"></a>

#### get\_mapping\_data\_source\_value

```python
def get_mapping_data_source_value(identifier, value, **kwargs)
```

Get specific mapping data source value.

Return a specific mapping dta source value.

**Arguments**:

- `identifier` (`str`): Mapping data source's identifier.
- `value` (`str`): Mapping Data Source Value's value.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`any`: any, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_mapping_data_source_value"></a>

#### delete\_mapping\_data\_source\_value

```python
def delete_mapping_data_source_value(identifier, value, **kwargs)
```

Delete specific mapping data source value.

Delete the specified mapping data source value from the database.

**Arguments**:

- `identifier` (`str`): Mapping data source's identifier.
- `value` (`str`): Mapping Data Source Value's value.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_mapping"></a>

#### create\_mapping

```python
def create_mapping(body, **kwargs)
```

Create a mapping.

Create a custom mapping.

**Arguments**:

- `body` (`~affinda.models.MappingCreate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Mapping`: Mapping, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.list_mappings"></a>

#### list\_mappings

```python
def list_mappings(mapping_data_source, offset=None, limit=None, **kwargs)
```

List mappings.

Returns the list of all custom data mappings.

**Arguments**:

- `mapping_data_source` (`str`): Mapping data source's identifier.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Paths1Dpvb2PV3MappingsGetResponses200ContentApplicationJsonSchema`: Paths1Dpvb2PV3MappingsGetResponses200ContentApplicationJsonSchema, or the result of
cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_mapping"></a>

#### get\_mapping

```python
def get_mapping(identifier, **kwargs)
```

Get specific mapping.

Return a specific mapping.

**Arguments**:

- `identifier` (`str`): Mapping's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Mapping`: Mapping, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_mapping"></a>

#### delete\_mapping

```python
def delete_mapping(identifier, **kwargs)
```

Delete specific mapping.

Delete the specified mapping from the database.

**Arguments**:

- `identifier` (`str`): Mapping's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_mapping"></a>

#### update\_mapping

```python
def update_mapping(identifier, body, **kwargs)
```

Update specific mapping.

Updates a specific mapping.

**Arguments**:

- `identifier` (`str`): Mapping's identifier.
- `body` (`~affinda.models.MappingUpdate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Mapping`: Mapping, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_tags"></a>

#### get\_all\_tags

```python
def get_all_tags(limit=None, offset=None, workspace=None, **kwargs)
```

Get list of all tags.

Returns your tags.

**Arguments**:

- `limit` (`int`): The numbers of results to return. Default value is None.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `workspace` (`str`): Filter by workspace. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.Tag]`: list of Tag, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_tag"></a>

#### create\_tag

```python
def create_tag(body, **kwargs)
```

Create a tag.

Create a tag.

**Arguments**:

- `body` (`~affinda.models.TagCreate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Tag`: Tag, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_tag"></a>

#### get\_tag

```python
def get_tag(id, **kwargs)
```

Get specific tag.

Return a specific tag.

**Arguments**:

- `id` (`int`): Tag's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Tag`: Tag, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_tag"></a>

#### update\_tag

```python
def update_tag(id, body, **kwargs)
```

Update a tag.

Update data of an tag.

**Arguments**:

- `id` (`int`): Tag's ID.
- `body` (`~affinda.models.TagUpdate`): Tag data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Tag`: Tag, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_tag"></a>

#### delete\_tag

```python
def delete_tag(id, **kwargs)
```

Delete an tag.

Deletes the specified tag from the database.

**Arguments**:

- `id` (`int`): Tag's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_organizations"></a>

#### get\_all\_organizations

```python
def get_all_organizations(**kwargs)
```

Get list of all organizations.

Returns all the organizations.

**Arguments**:

- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.Organization]`: list of Organization, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_organization"></a>

#### create\_organization

```python
def create_organization(name,
                        avatar=None,
                        resthook_signature_key=None,
                        **kwargs)
```

Create a new organization.

Create a new organization.

**Arguments**:

- `name` (`str`): 
- `avatar` (`IO`): Upload avatar for the organization. Default value is None.
- `resthook_signature_key` (`str`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Organization`: Organization, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_organization"></a>

#### get\_organization

```python
def get_organization(identifier, **kwargs)
```

Get detail of an organization.

Get detail of an organization.

**Arguments**:

- `identifier` (`str`): Organization identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Organization`: Organization, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_organization"></a>

#### update\_organization

```python
def update_organization(identifier,
                        name=None,
                        avatar=None,
                        resthook_signature_key=None,
                        validation_tool_config=None,
                        **kwargs)
```

Update an organization.

Update the detail of an organization.

**Arguments**:

- `identifier` (`str`): Organization identifier.
- `name` (`str`): Default value is None.
- `avatar` (`IO`): Default value is None.
- `resthook_signature_key` (`str`): Default value is None.
- `validation_tool_config` (`~affinda.models.ValidationToolConfig`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Organization`: Organization, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_organization"></a>

#### delete\_organization

```python
def delete_organization(identifier, **kwargs)
```

Delete an organization.

Delete the specified organization from the database.

**Arguments**:

- `identifier` (`str`): Organization identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_organization_memberships"></a>

#### get\_all\_organization\_memberships

```python
def get_all_organization_memberships(offset=None,
                                     limit=None,
                                     organization=None,
                                     role=None,
                                     **kwargs)
```

Get list of all organization memberships.

Returns all the organization memberships.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `organization` (`str`): Filter by organization. Default value is None.
- `role` (`str or ~affinda.models.OrganizationRole`): Filter by role. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsQ5Os5RV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchema`: PathsQ5Os5RV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchema, or
the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_organization_membership"></a>

#### get\_organization\_membership

```python
def get_organization_membership(identifier, **kwargs)
```

Get detail of an organization membership.

Get detail of an organization membership.

**Arguments**:

- `identifier` (`str`): Membership identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.OrganizationMembership`: OrganizationMembership, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_organization_membership"></a>

#### update\_organization\_membership

```python
def update_organization_membership(identifier, body, **kwargs)
```

Update an organization membership.

The admin users can use this endpoint to update the role of the members within their
organization.

**Arguments**:

- `identifier` (`str`): Membership identifier.
- `body` (`~affinda.models.OrganizationMembershipUpdate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.OrganizationMembership`: OrganizationMembership, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_organization_membership"></a>

#### delete\_organization\_membership

```python
def delete_organization_membership(identifier, **kwargs)
```

Delete an organization membership.

The admin users can use this endpoint to remove member from their organization. Other users can
also use this to leave their organization.

**Arguments**:

- `identifier` (`str`): Membership identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_invitations"></a>

#### get\_all\_invitations

```python
def get_all_invitations(offset=None,
                        limit=None,
                        organization=None,
                        status=None,
                        role=None,
                        **kwargs)
```

Get list of all invitations.

Get list of all invitations you created or sent to you.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `organization` (`str`): Filter by organization. Default value is None.
- `status` (`str or ~affinda.models.InvitationStatus`): Filter by status. Default value is None.
- `role` (`str or ~affinda.models.OrganizationRole`): Filter by role. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Paths18Wh2VcV3InvitationsGetResponses200ContentApplicationJsonSchema`: Paths18Wh2VcV3InvitationsGetResponses200ContentApplicationJsonSchema, or the result of
cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_invitation"></a>

#### create\_invitation

```python
def create_invitation(body, **kwargs)
```

Create a new invitation.

Create a new invitation.

**Arguments**:

- `body` (`~affinda.models.InvitationCreate`): Invitation to create.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Invitation`: Invitation, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_invitation"></a>

#### get\_invitation

```python
def get_invitation(identifier, **kwargs)
```

Get detail of an invitation.

Get detail of an invitation.

**Arguments**:

- `identifier` (`str`): Invitation identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Invitation`: Invitation, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_invitation"></a>

#### update\_invitation

```python
def update_invitation(identifier, body, **kwargs)
```

Update an invitation.

Update the detail of an invitation.

**Arguments**:

- `identifier` (`str`): Invitation identifier.
- `body` (`~affinda.models.InvitationUpdate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Invitation`: Invitation, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_invitation"></a>

#### delete\_invitation

```python
def delete_invitation(identifier, **kwargs)
```

Delete an invitation.

Delete the specified invitation from the database.

**Arguments**:

- `identifier` (`str`): Invitation identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_invitation_by_token"></a>

#### get\_invitation\_by\_token

```python
def get_invitation_by_token(token, **kwargs)
```

Get detail of an invitation by token.

Get detail of an invitation using a secret token. This allows users who have not
registered/logged in to view the invitation.

**Arguments**:

- `token` (`str`): Invitation token.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Invitation`: Invitation, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.respond_to_invitation"></a>

#### respond\_to\_invitation

```python
def respond_to_invitation(token, body, **kwargs)
```

Respond to an invitation.

Choose to accept or decline an invitation.

**Arguments**:

- `token` (`str`): Invitation token.
- `body` (`~affinda.models.InvitationResponse`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Invitation`: Invitation, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_api_users"></a>

#### get\_all\_api\_users

```python
def get_all_api_users(organization=None, **kwargs)
```

Get list of all API users.

Returns your API users.

**Arguments**:

- `organization` (`str`): Filter by organization. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Paths26Civ0V3ApiUsersGetResponses200ContentApplicationJsonSchema`: Paths26Civ0V3ApiUsersGetResponses200ContentApplicationJsonSchema, or the result of
cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_api_user"></a>

#### create\_api\_user

```python
def create_api_user(body, **kwargs)
```

Create an API user.

Create an API user.

**Arguments**:

- `body` (`~affinda.models.ApiUserCreate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ApiUserWithKey`: ApiUserWithKey, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_api_user"></a>

#### get\_api\_user

```python
def get_api_user(id, **kwargs)
```

Get specific API user.

Return a specific API user.

**Arguments**:

- `id` (`int`): API user's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ApiUserWithoutKey`: ApiUserWithoutKey, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_api_user"></a>

#### update\_api\_user

```python
def update_api_user(id, body, **kwargs)
```

Update an API user.

Update data of an API user.

**Arguments**:

- `id` (`int`): API user's ID.
- `body` (`~affinda.models.ApiUserUpdate`): API user to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ApiUserWithoutKey`: ApiUserWithoutKey, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_api_user"></a>

#### delete\_api\_user

```python
def delete_api_user(id, **kwargs)
```

Delete an API user.

Deletes the specified API user from the database.

**Arguments**:

- `id` (`int`): API user's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.regenerate_api_key_for_api_user"></a>

#### regenerate\_api\_key\_for\_api\_user

```python
def regenerate_api_key_for_api_user(id, **kwargs)
```

Regenerate API key for an API user.

Regenerate API key for an API user.

**Arguments**:

- `id` (`int`): API user's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ApiUserWithKey`: ApiUserWithKey, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_resthook_subscriptions"></a>

#### get\_all\_resthook\_subscriptions

```python
def get_all_resthook_subscriptions(offset=None, limit=None, **kwargs)
```

Get list of all resthook subscriptions.

Returns your resthook subscriptions.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsVz5Kj2V3ResthookSubscriptionsGetResponses200ContentApplicationJsonSchema`: PathsVz5Kj2V3ResthookSubscriptionsGetResponses200ContentApplicationJsonSchema, or the
result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resthook_subscription"></a>

#### create\_resthook\_subscription

```python
def create_resthook_subscription(body, **kwargs)
```

Create a resthook subscription.

After a subscription is successfully created, we'll send a POST request to your target URL with
a ``X-Hook-Secret`` header. :code:`<br />`
You need to response to this request with a 200 status code to confirm your subscribe
intention. :code:`<br />`
Then, you need to use the ``X-Hook-Secret`` to activate the subscription using the
`/resthook_subscriptions/activate <#post-/v3/resthook_subscriptions/activate>`_ endpoint.

**Arguments**:

- `body` (`~affinda.models.ResthookSubscriptionCreate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResthookSubscription`: ResthookSubscription, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resthook_subscription"></a>

#### get\_resthook\_subscription

```python
def get_resthook_subscription(id, **kwargs)
```

Get specific resthook subscription.

Return a specific resthook subscription.

**Arguments**:

- `id` (`int`): Resthook subscription's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResthookSubscription`: ResthookSubscription, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_resthook_subscription"></a>

#### update\_resthook\_subscription

```python
def update_resthook_subscription(id, body, **kwargs)
```

Update a resthook subscription.

Update data of a resthook subscription.

**Arguments**:

- `id` (`int`): ResthookSubscription's ID.
- `body` (`~affinda.models.ResthookSubscriptionUpdate`): ResthookSubscription data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResthookSubscription`: ResthookSubscription, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_resthook_subscription"></a>

#### delete\_resthook\_subscription

```python
def delete_resthook_subscription(id, **kwargs)
```

Delete a resthook subscription.

Deletes the specified resthook subscription from the database.

**Arguments**:

- `id` (`int`): ResthookSubscription's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.activate_resthook_subscription"></a>

#### activate\_resthook\_subscription

```python
def activate_resthook_subscription(x_hook_secret, **kwargs)
```

Activate a resthook subscription.

After creating a subscription, we'll send a POST request to your target URL with a
``X-Hook-Secret`` header. :code:`<br />`
You should response to this with a 200 status code, and use the value of the ``X-Hook-Secret``
header that you received to activate the subscription using this endpoint.

**Arguments**:

- `x_hook_secret` (`str`): The secret received when creating a subscription.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResthookSubscription`: ResthookSubscription, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.list_occupation_groups"></a>

#### list\_occupation\_groups

```python
def list_occupation_groups(**kwargs)
```

List occupation groups.

Returns the list of searchable occupation groups.

**Arguments**:

- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.OccupationGroup]`: list of OccupationGroup, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_job_description_search"></a>

#### create\_job\_description\_search

```python
def create_job_description_search(body, offset=None, limit=None, **kwargs)
```

Search through parsed job descriptions.

Searches through parsed job descriptions. You can search with custom criterias or a resume.

**Arguments**:

- `body` (`~affinda.models.JobDescriptionSearchParameters`): Search parameters.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.JobDescriptionSearch`: JobDescriptionSearch, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_job_description_search_detail"></a>

#### get\_job\_description\_search\_detail

```python
def get_job_description_search_detail(identifier, body, **kwargs)
```

Get search result of specific job description.

This contains more detailed information about the matching score of the search criteria, or
which search criteria is missing in this job description.
The ``identifier`` is the unique ID returned via the `/job_description_search
<#post-/job_description_search>`_ endpoint.

**Arguments**:

- `identifier` (`str`): Job Description identifier.
- `body` (`~affinda.models.JobDescriptionSearchParameters`): Search parameters.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.JobDescriptionSearchDetail`: JobDescriptionSearchDetail, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_job_description_search_config"></a>

#### get\_job\_description\_search\_config

```python
def get_job_description_search_config(**kwargs)
```

Get the config for the logged in user's embeddable job description search tool.

Return configurations such as which fields can be displayed in the logged in user's embeddable
job description search tool, what are their weights, what is the maximum number of results that
can be returned, etc.

**Arguments**:

- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.JobDescriptionSearchConfig`: JobDescriptionSearchConfig, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_job_description_search_config"></a>

#### update\_job\_description\_search\_config

```python
def update_job_description_search_config(body, **kwargs)
```

Update the config for the logged in user's embeddable job description search tool.

Update configurations such as which fields can be displayed in the logged in user's embeddable
job description search tool, what are their weights, what is the maximum number of results that
can be returned, etc.

**Arguments**:

- `body` (`~affinda.models.JobDescriptionSearchConfig`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.JobDescriptionSearchConfig`: JobDescriptionSearchConfig, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_job_description_search_embed_url"></a>

#### create\_job\_description\_search\_embed\_url

```python
def create_job_description_search_embed_url(body=None, **kwargs)
```

Create a signed URL for the embeddable job description search tool.

Create and return a signed URL of the job description search tool which then can be embedded on
a web page. An optional parameter ``config_override`` can be passed to override the user-level
configurations of the embeddable search tool.

**Arguments**:

- `body` (`~affinda.models.PathsM3DzbgV3JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.JobDescriptionSearchEmbed`: JobDescriptionSearchEmbed, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_indexes"></a>

#### get\_all\_indexes

```python
def get_all_indexes(offset=None,
                    limit=None,
                    document_type=None,
                    name=None,
                    **kwargs)
```

Get list of all indexes.

Returns all the indexes.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `document_type` (`str or ~affinda.models.Enum20`): Filter indices by a document type. Default value is None.
- `name` (`str`): Filter indices by name. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsDvrcp3V3IndexGetResponses200ContentApplicationJsonSchema`: PathsDvrcp3V3IndexGetResponses200ContentApplicationJsonSchema, or the result of
cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_index"></a>

#### create\_index

```python
def create_index(body, **kwargs)
```

Create a new index.

Create an index for the search tool.

**Arguments**:

- `body` (`~affinda.models.IndexCreate`): Index to create.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Index`: Index, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_index"></a>

#### update\_index

```python
def update_index(name, body, **kwargs)
```

Update an index.

Updates the specified index.

**Arguments**:

- `name` (`str`): Index name.
- `body` (`~affinda.models.IndexUpdate`): Index data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Index`: Index, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_index"></a>

#### delete\_index

```python
def delete_index(name, **kwargs)
```

Delete an index.

Deletes the specified index from the database.

**Arguments**:

- `name` (`str`): Index name.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_index_documents"></a>

#### get\_all\_index\_documents

```python
def get_all_index_documents(name, offset=None, limit=None, **kwargs)
```

Get indexed documents for a specific index.

Returns all the indexed documents for that index.

**Arguments**:

- `name` (`str`): Index name.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsO7SnenV3IndexNameDocumentsGetResponses200ContentApplicationJsonSchema`: PathsO7SnenV3IndexNameDocumentsGetResponses200ContentApplicationJsonSchema, or the
result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_index_document"></a>

#### create\_index\_document

```python
def create_index_document(name, body, **kwargs)
```

Index a new document.

Create an indexed document for the search tool.

**Arguments**:

- `name` (`str`): Index name.
- `body` (`~affinda.models.PathsCl024WV3IndexNameDocumentsPostRequestbodyContentApplicationJsonSchema`): Document to index.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsFte27NV3IndexNameDocumentsPostResponses201ContentApplicationJsonSchema`: PathsFte27NV3IndexNameDocumentsPostResponses201ContentApplicationJsonSchema, or the
result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_index_document"></a>

#### delete\_index\_document

```python
def delete_index_document(name, identifier, **kwargs)
```

Delete an indexed document.

Delete the specified indexed document from the database.

**Arguments**:

- `name` (`str`): Index name.
- `identifier` (`str`): Document identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.re_index_document"></a>

#### re\_index\_document

```python
def re_index_document(name, identifier, **kwargs)
```

Re-index a document.

Re-index a document.
This is relevant if you updated the document's data via the /annotations endpoint, and want to
refresh
the document's data in the search index.

**Arguments**:

- `name` (`str`): Index name.
- `identifier` (`str`): Document identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resume_search"></a>

#### create\_resume\_search

```python
def create_resume_search(body, offset=None, limit=None, **kwargs)
```

Search through parsed resumes.

Searches through parsed resumes. Users have 3 options to create a search::code:`<br
/>`:code:`<br />` 1.    Match to a job description - a parsed job description is used to find
candidates that suit it:code:`<br />` 2.  Match to a resume - a parsed resume is used to find
other candidates that have similar attributes:code:`<br />` 3.  Search using custom
criteria:code:`<br />`:code:`<br />` Users should only populate 1 of jobDescription, resume or
the custom criteria.

**Arguments**:

- `body` (`~affinda.models.ResumeSearchParameters`): Search parameters.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResumeSearch`: ResumeSearch, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume_search_detail"></a>

#### get\_resume\_search\_detail

```python
def get_resume_search_detail(identifier, body, **kwargs)
```

Get search result of specific resume.

This contains more detailed information about the matching score of the search criteria, or
which search criteria is missing in this resume.
The ``identifier`` is the unique ID returned via the `/resume_search <#post-/resume_search>`_
endpoint.

**Arguments**:

- `identifier` (`str`): Resume identifier.
- `body` (`~affinda.models.ResumeSearchParameters`): Search parameters.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResumeSearchDetail`: ResumeSearchDetail, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume_search_match"></a>

#### get\_resume\_search\_match

```python
def get_resume_search_match(resume,
                            job_description,
                            index=None,
                            search_expression=None,
                            job_titles_weight=None,
                            years_experience_weight=None,
                            locations_weight=None,
                            languages_weight=None,
                            skills_weight=None,
                            education_weight=None,
                            search_expression_weight=None,
                            soc_codes_weight=None,
                            management_level_weight=None,
                            **kwargs)
```

Match a single resume and job description.

Get the matching score between a resume and a job description. The score ranges between 0 and
1, with 0 being not a match at all, and 1 being perfect match.:code:`<br/>` Note, this score
will not directly match the score returned from POST `/resume_search/details/{identifier}
<#post-/resume_search/details/-identifier->`_.

**Arguments**:

- `resume` (`str`): Identify the resume to match.
- `job_description` (`str`): Identify the job description to match.
- `index` (`str`): Optionally, specify an index to search in. If not specified, will search in all
indexes. Default value is None.
- `search_expression` (`str`): Add keywords to the search criteria. Default value is None.
- `job_titles_weight` (`float`): How important is this criteria to the matching score, range from 0 to
1. Default value is None.
- `years_experience_weight` (`float`): How important is this criteria to the matching score, range
from 0 to 1. Default value is None.
- `locations_weight` (`float`): How important is this criteria to the matching score, range from 0 to
1. Default value is None.
- `languages_weight` (`float`): How important is this criteria to the matching score, range from 0 to
1. Default value is None.
- `skills_weight` (`float`): How important is this criteria to the matching score, range from 0 to 1.
Default value is None.
- `education_weight` (`float`): How important is this criteria to the matching score, range from 0 to
1. Default value is None.
- `search_expression_weight` (`float`): How important is this criteria to the matching score, range
from 0 to 1. Default value is None.
- `soc_codes_weight` (`float`): How important is this criteria to the matching score, range from 0 to
1. Default value is None.
- `management_level_weight` (`float`): How important is this criteria to the matching score, range
from 0 to 1. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResumeSearchMatch`: ResumeSearchMatch, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume_search_config"></a>

#### get\_resume\_search\_config

```python
def get_resume_search_config(**kwargs)
```

Get the config for the logged in user's embeddable resume search tool.

Return configurations such as which fields can be displayed in the logged in user's embeddable
resume search tool, what are their weights, what is the maximum number of results that can be
returned, etc.

**Arguments**:

- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResumeSearchConfig`: ResumeSearchConfig, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_resume_search_config"></a>

#### update\_resume\_search\_config

```python
def update_resume_search_config(body, **kwargs)
```

Update the config for the logged in user's embeddable resume search tool.

Update configurations such as which fields can be displayed in the logged in user's embeddable
resume search tool, what are their weights, what is the maximum number of results that can be
returned, etc.

**Arguments**:

- `body` (`~affinda.models.ResumeSearchConfig`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResumeSearchConfig`: ResumeSearchConfig, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resume_search_embed_url"></a>

#### create\_resume\_search\_embed\_url

```python
def create_resume_search_embed_url(body=None, **kwargs)
```

Create a signed URL for the embeddable resume search tool.

Create and return a signed URL of the resume search tool which then can be embedded on a web
page. An optional parameter ``config_override`` can be passed to override the user-level
configurations of the embeddable resume search tool.

**Arguments**:

- `body` (`~affinda.models.Paths1Czpnk1V3ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResumeSearchEmbed`: ResumeSearchEmbed, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume_search_suggestion_job_title"></a>

#### get\_resume\_search\_suggestion\_job\_title

```python
def get_resume_search_suggestion_job_title(job_titles, **kwargs)
```

Get job title suggestions based on provided job title(s).

Provided one or more job titles, get related suggestions for your search.

**Arguments**:

- `job_titles` (`list[str]`): Job title to query suggestions for.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[str]`: list of str, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume_search_suggestion_skill"></a>

#### get\_resume\_search\_suggestion\_skill

```python
def get_resume_search_suggestion_skill(skills, **kwargs)
```

Get skill suggestions based on provided skill(s).

Provided one or more skills, get related suggestions for your search.

**Arguments**:

- `skills` (`list[str]`): Skill to query suggestions for.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[str]`: list of str, or the result of cls(response)

