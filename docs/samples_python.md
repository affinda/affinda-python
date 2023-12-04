

Document API - Workspace
------------------------

### getAllWorkspaces - Get list of all workspaces

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
organization_identifier = "REPLACE_ORGANIZATION_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

workspaces = client.get_all_workspaces(organization_identifier)
for workspace in workspaces:
    print(workspace.as_dict())
```

### createWorkspace - Create a workspace

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import WorkspaceCreate, WorkspaceVisibility

token = "REPLACE_TOKEN"
organization_identifier = "REPLACE_ORGANIZATION_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = WorkspaceCreate(
    organization=organization_identifier,
    name="My Workspace",
    visibility=WorkspaceVisibility.ORGANIZATION,
    reject_invalid_documents=False,
)
response = client.create_workspace(body)

print(response.as_dict())
```

### getWorkspace - Get specific workspace

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

workspace = client.get_workspace(identifier)
print(workspace.as_dict())
```

### updateWorkspace - Update a workspace

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import WorkspaceUpdate, WorkspaceVisibility

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = WorkspaceUpdate(
    name="My New Workspace",
    visibility=WorkspaceVisibility.PRIVATE,
    reject_invalid_documents=True,
)
response = client.update_workspace(identifier, body)

print(response.as_dict())
```

### deleteWorkspace - Delete a workspace

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_workspace(identifier)
```

### getUsageByWorkspace - Get usage by workspace

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
workspace_identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

res = client.get_usage_by_workspace(workspace_identifier, start="2023-06", end="2023-07")
for usage in res:
    print(usage.as_dict())  # noqa: T201
```

### getAllWorkspaceMemberships - Get list of all workspace memberships

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
workspace_identifier = "REPLACE_WORKSPACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

memberships = client.get_all_workspace_memberships(workspace=workspace_identifier)
print(memberships.as_dict())
```

### createWorkspaceMembership - Create a workspace membership

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import WorkspaceMembershipCreate

token = "REPLACE_TOKEN"
organization_identifier = "REPLACE_ORGANIZATION_IDENTIFIER"
workspace_identifier = "REPLACE_WORKSPACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Get all members in organization
response = client.get_all_organization_memberships(organization=organization_identifier)
memberships = response.results

# Let's say we want to add the first member
membership = memberships[0]
body = WorkspaceMembershipCreate(
    workspace=workspace_identifier,
    user=membership.user.id,
)
response = client.create_workspace_membership(body)

print(response.as_dict())
```

### getWorkspaceMembership - Get specific workspace membership

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

workspace = client.get_workspace_membership(identifier)
print(workspace.as_dict())
```

### deleteWorkspaceMembership - Delete a workspace membership

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_workspace_membership(identifier)
```

Document API - Collection
-------------------------

### getAllCollections - Get list of all collections

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
workspace_identifier = "REPLACE_WORKSPACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

collections = client.get_all_collections(workspace_identifier)
for collection in collections:
    print(collection.as_dict())
```

### createCollection - Create a collection

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import CollectionCreate

token = "REPLACE_TOKEN"
workspace_identifier = "REPLACE_WORKSPACE_IDENTIFIER"
extractor_identifier = "REPLACE_EXTRACTOR_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = CollectionCreate(
    name="My Collection",
    workspace=workspace_identifier,
    extractor=extractor_identifier,
)
response = client.create_collection(body)

print(response.as_dict())
```

### getCollection - Get specific collection

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

collection = client.get_collection(identifier)
print(collection.as_dict())
```

### updateCollection - Update a collection

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import CollectionUpdate

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = CollectionUpdate(name="My New Collection")
response = client.update_collection(identifier, body)

print(response.as_dict())
```

### deleteCollection - Delete a collection

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_collection(identifier)
```

### createDataFieldForCollection - Create data field for a collection along with a new data point.

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import DataFieldCreate, DataFieldCreateDataPoint, DataFieldCreateField

token = "REPLACE_TOKEN"
collection_identifier = "REPLACE_COLLECTION_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

data_point = DataFieldCreateDataPoint(
    name="My Data Point",
    slug="myDataPoint",
    type="text",
)
field = DataFieldCreateField(
    label="My Field",
)

body = DataFieldCreate(
    data_point=data_point,
    field=field,
)

response = client.create_data_field_for_collection(collection_identifier, body)

print(response.as_dict())
```

### getUsageByCollection - Get usage by collection

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
collection_identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

res = client.get_usage_by_collection(collection_identifier, start="2023-06", end="2023-07")
for usage in res:
    print(usage.as_dict())  # noqa: T201
```

Document API - Document
-----------------------

### getAllDocuments - Get list of all documents

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
collection_identifier = "REPLACE_COLLECTION_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
documents = client.get_all_documents(collection=collection_identifier)

print(documents.as_dict())
```

### createDocument - Upload a document for parsing

```python
from pathlib import Path

from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
collection_identifier = "REPLACE_COLLECTION_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

file_pth = Path("path_to_file.pdf")
with open(file_pth, "rb") as f:
    document = client.create_document(file=f, collection=collection_identifier)

print(document.as_dict())
```

### getDocument - Get specific document

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Depend on whether the document you're getting is a resume/invoice/job description,
# the type of `document` will be either `ResumeDocument`, `InvoiceDocument` or `JobDescriptionDocument`
document = client.get_document(identifier)

# Example: print the candidate's raw name (in case `document` is a resume)
print(document.data.name.raw)
```

### updateDocument - Update a document

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import DocumentUpdate

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = DocumentUpdate(file_name="New-file-name.pdf")
response = client.update_document(identifier, body)

print(response.as_dict())
```

### deleteDocument - Delete a document

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_document(identifier)
```

### updateDocumentData - Update a document's data

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ResumeDataSkillsItem

token = "REPLACE_TOKEN"
identifier = "RESUME_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

resume = client.get_document(identifier)

# Update the data of the resume
updated_data = resume.data
updated_data.date_of_birth = "1980-08-15"  # Update some attributes

# For lists, you can update, create new, or delete objects
updated_data.skills[0].last_used = "2022-06-01"  # Update the first skill
updated_data.skills.pop(-1)  # Delete the last skill
updated_data.skills.append(ResumeDataSkillsItem(name="git", number_of_months=24))  # Create a new skill

updated_resume = client.update_document_data(identifier, updated_data)
print(updated_resume.as_dict())
```

### editDocumentPages - Edit pages of a document

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import DocumentEditRequest, DocumentSplit, DocumentSplitPage

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Get the page IDs of the document pages
document = client.get_document(identifier)
ids = []
for page in document.meta.pages:
    ids.append(page.id)

# Let's say the document has 5 pages, we want to split to 3 documents:
# - Document 1:
#   - Page 1
# - Document 2:
#   - Page 2 and 3
#   - Rotate page 3 by 90 degrees
# - Document 3:
#   - Page 4
#   - Delete page 5
split_1 = DocumentSplit(
    identifier=identifier,
    pages=[
        DocumentSplitPage(id=ids[0]),
    ],
)
split_2 = DocumentSplit(
    pages=[
        DocumentSplitPage(id=ids[1]),
        DocumentSplitPage(id=ids[2], rotation=90),
    ],
)
split_3 = DocumentSplit(
    pages=[
        DocumentSplitPage(id=ids[3]),
    ]
)

res = client.edit_document_pages(
    identifier,
    DocumentEditRequest(splits=[split_1, split_2, split_3]),
)
for document_meta in res:
    print(document_meta.as_dict())
```

Document API - Tag
------------------

### batchAddTag - Add a tag to documents

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import BatchAddTagRequest

token = "REPLACE_TOKEN"
document_1 = "REPLACE_DOCUMENT_IDENTIFIER_1"
document_2 = "REPLACE_DOCUMENT_IDENTIFIER_2"
tag_id = "REPLACE_TAG_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = BatchAddTagRequest(
    identifiers=[document_1, document_2],
    tag=tag_id,
)

client.batch_add_tag(body=body)
```

### batchRemoveTag - Remove a tag from documents

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import BatchRemoveTagRequest

token = "REPLACE_TOKEN"
document_1 = "REPLACE_DOCUMENT_IDENTIFIER_1"
document_2 = "REPLACE_DOCUMENT_IDENTIFIER_2"
tag_id = "REPLACE_TAG_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = BatchRemoveTagRequest(
    identifiers=[document_1, document_2],
    tag=tag_id,
)

client.batch_remove_tag(body=body)
```

### getAllTags - Get list of all tags

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
workspace_identifier = "REPLACE_WORKSPACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

tags = client.get_all_tags(workspace_identifier)
for tag in tags:
    print(tag.as_dict())
```

### createTag - Create a tag

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import TagCreate

token = "REPLACE_TOKEN"
workspace_identifier = "REPLACE_WORKSPACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = TagCreate(name="My Tag", workspace=workspace_identifier)
response = client.create_tag(body)

print(response.as_dict())
```

### getTag - Get specific tag

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
id = "REPLACE_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

tag = client.get_tag(id)
print(tag.as_dict())
```

### updateTag - Update a tag

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import TagUpdate

token = "REPLACE_TOKEN"
id = "REPLACE_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = TagUpdate(name="My New Tag")
response = client.update_tag(id, body)

print(response.as_dict())
```

### deleteTag - Delete an tag

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
id = "REPLACE_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_tag(id)
```

Document API - Extractor
------------------------

### getAllExtractors - Get list of all extractors

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
organization_identifier = "REPLACE_ORGANIZATION_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

extractors = client.get_all_extractors(organization_identifier, include_public_extractors=True)
for extractor in extractors:
    print(extractor.as_dict())
```

### createExtractor - Create an extractor

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ExtractorCreate

token = "REPLACE_TOKEN"
organization_identifier = "REPLACE_ORGANIZATION_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = ExtractorCreate(name="My Tailored Extractor", organization=organization_identifier)
response = client.create_extractor(body)

print(response.as_dict())
```

### updateExtractor - Update an extractor

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ExtractorUpdate

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = ExtractorUpdate(name="My New Extractor")
response = client.update_extractor(identifier, body)

print(response.as_dict())
```

### deleteExtractor - Delete an extractor

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_extractor(identifier)
```

Document API - Data Point
-------------------------

### getAllDataPoints - Get list of all data points

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
extractor_identifier = "REPLACE_EXTRACTOR_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

data_points = client.get_all_data_points(extractor=extractor_identifier)
for data_point in data_points:
    print(data_point.as_dict())
```

### createDataPoint - Create a data point

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import DataPointCreate

token = "REPLACE_TOKEN"
organization_identifier = "REPLACE_ORGANIZATION_IDENTIFIER"
extractor_identifier = "REPLACE_EXTRACTOR_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = DataPointCreate(
    slug="myDataPoint",
    annotation_content_type="text",
    organization=organization_identifier,
    extractor=extractor_identifier,
)
response = client.create_data_point(body)

print(response.as_dict())
```

### getDataPoint - Get specific data point

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

data_point = client.get_data_point(identifier)
print(data_point.as_dict())
```

### updateDataPoint - Update a data point

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import DataPointUpdate

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = DataPointUpdate(
    slug="myNewDataPoint",
    name="My New Data Point",
)
response = client.update_data_point(identifier, body)

print(response.as_dict())
```

### deleteDataPoint - Delete a data point

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_data_point(identifier)
```

### getDataPointChoices - Get list of data point choices

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
data_point_identifier = "REPLACE_DATA_POINT_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

data_point_choices = client.get_data_point_choices(data_point_identifier)
print(data_point_choices.as_dict())
```

### createDataPointChoice - Create a data point choice

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import DataPointChoiceCreate

token = "REPLACE_TOKEN"
data_point_identifier = "REPLACE_DATA_POINT_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = DataPointChoiceCreate(
    data_point=data_point_identifier,
    label="My Company Ltd",
    value="COMPANY_CODE",
    synonyms=["COMPANY_CODE"],
    description="My Company",
)
response = client.create_data_point_choice(body)

print(response.as_dict())
```

### getDataPointChoice - Get specific data point choice

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
id = "REPLACE_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

data_point = client.get_data_point_choice(id)
print(data_point.as_dict())
```

### updateDataPointChoice - Update a data point choice

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import DataPointChoiceUpdate

token = "REPLACE_TOKEN"
id = "REPLACE_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = DataPointChoiceUpdate(value="NEW_COMPANY_CODE")
response = client.update_data_point_choice(id, body)

print(response.as_dict())
```

### deleteDataPointChoice - Delete a data point choice

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
id = "REPLACE_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_data_point_choice(id)
```

### replaceDataPointChoices - Replace choices of a data point

```python
# ruff: noqa: T201

from affinda import AffindaAPI, TokenCredential
from affinda.models import DataPointChoiceForReplace, DataPointChoiceReplaceRequest

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

choices = [
    DataPointChoiceForReplace(value="cj", label="CJ"),
    DataPointChoiceForReplace(value="sweet", label="Sweet"),
    DataPointChoiceForReplace(value="big_smoke", label="Big Smoke"),
]

body = DataPointChoiceReplaceRequest(
    data_point="REPLACE_DATA_POINT_IDENTIFIER",
    collection="REPLACE_COLLECTION_IDENTIFIER",  # Either `collection` or `organization` is required
    choices=choices,
)

response = client.replace_data_point_choices(body=body)
print(response.as_dict())
```

Document API - Annotation
-------------------------

### getAllAnnotations - Get list of all annotations

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
document_identifier = "REPLACE_DOCUMENT_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

response = client.get_all_annotations(document_identifier)
print(response.as_dict())
```

### createAnnotation - Create a annotation

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import AnnotationCreate

token = "REPLACE_TOKEN"
document_identifier = "REPLACE_DOCUMENT_IDENTIFIER"
data_point_identifier = "REPLACE_DATA_POINT_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = AnnotationCreate(
    document=document_identifier,
    page_index=0,
    parsed="Affinda",
    data_point=data_point_identifier,
)
response = client.create_annotation(body)

print(response.as_dict())
```

### getAnnotation - Get specific annotation

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

annotation = client.get_annotation(identifier)
print(annotation.as_dict())
```

### updateAnnotation - Update an annotation

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import AnnotationUpdate

token = "REPLACE_TOKEN"
id = "REPLACE_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = AnnotationUpdate(parsed="New Value")
response = client.update_annotation(id, body)

print(response.as_dict())
```

### deleteAnnotation - Delete an annotation

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
id = "REPLACE_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_annotation(id)
```

### batchCreateAnnotations - Batch create annotations

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import AnnotationCreate

token = "REPLACE_TOKEN"
document_identifier = "REPLACE_DOCUMENT_IDENTIFIER"
data_point_identifier = "REPLACE_DATA_POINT_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = [
    AnnotationCreate(
        document=document_identifier,
        page_index=0,
        data_point=data_point_identifier,
        parsed="hello",
    ),
    AnnotationCreate(
        document=document_identifier,
        page_index=0,
        data_point=data_point_identifier,
        parsed="world",
    ),
]

annotations = client.batch_create_annotations(body)
for annotation in annotations:
    print(annotation.as_dict())
```

### batchUpdateAnnotations - Batch update annotations

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import AnnotationBatchUpdate

token = "REPLACE_TOKEN"
annotation_id = "REPLACE_ANNOTATION_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = [
    AnnotationBatchUpdate(id=annotation_id, parsed="new value 1"),
    AnnotationBatchUpdate(id=annotation_id, parsed="new value 2"),
]

annotations = client.batch_update_annotations(body)
for annotation in annotations:
    print(annotation.as_dict())
```

### batchDeleteAnnotations - Batch delete annotations

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = [1, 2, 3]  # List of annotation IDs
client.batch_delete_annotations(body)
```

Document API - Mapping Data Sources
-----------------------------------

Organization API - Organization
-------------------------------

### getAllOrganizations - Get list of all organizations

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

organizations = client.get_all_organizations()
for organization in organizations:
    print(organization.as_dict())
```

### createOrganization - Create a new organization

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

response = client.create_organization(name="Grove Street King")

print(response.as_dict())
```

### getOrganization - Get detail of an organization

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

organization = client.get_organization(identifier)
print(organization.as_dict())
```

### updateOrganization - Update an organization

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
response = client.update_organization(identifier, name="My New Organization")

print(response.as_dict())
```

### deleteOrganization - Delete an organization

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_organization(identifier)
```

Organization API - Membership
-----------------------------

### getAllOrganizationMemberships - Get list of all organization memberships

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

memberships = client.get_all_organization_memberships()
print(memberships.as_dict())
```

### getOrganizationMembership - Get detail of an organization membership

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

organization = client.get_organization_membership(identifier)
print(organization.as_dict())
```

### updateOrganizationMembership - Update an organization membership

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import OrganizationMembershipUpdate, OrganizationRole

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = OrganizationMembershipUpdate(role=OrganizationRole.ADMIN)
response = client.update_organization_membership(identifier, body)

print(response.as_dict())
```

### deleteOrganizationMembership - Delete an organization membership

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_organization_membership(identifier)
```

Organization API - Invitation
-----------------------------

### getAllInvitations - Get list of all invitations

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

invitations = client.get_all_invitations()
print(invitations.as_dict())
```

### createInvitation - Create a new invitation

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import InvitationCreate, OrganizationRole

token = "REPLACE_TOKEN"
organization_identifier = "REPLACE_ORGANIZATION_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = InvitationCreate(
    organization=organization_identifier,
    email="carljohnson@grove.street",
    role=OrganizationRole.MEMBER,
)
response = client.create_invitation(body)

print(response.as_dict())
```

### getInvitation - Get detail of an invitation

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

invitation = client.get_invitation(identifier)
print(invitation.as_dict())
```

### updateInvitation - Update an invitation

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import InvitationUpdate, OrganizationRole

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = InvitationUpdate(role=OrganizationRole.ADMIN)
response = client.update_invitation(identifier, body)

print(response.as_dict())
```

### deleteInvitation - Delete an invitation

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_invitation(identifier)
```

### getInvitationByToken - Get detail of an invitation by token

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
invitation_token = "REPLACE_INVITATION_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

invitation = client.get_invitation_by_token(token=invitation_token)
print(invitation.as_dict())
```

### respondToInvitation - Respond to an invitation

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import InvitationResponse, InvitationResponseStatus

token = "REPLACE_TOKEN"
invitation_token = "REPLACE_INVITATION_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = InvitationResponse(status=InvitationResponseStatus.ACCEPTED)
response = client.respond_to_invitation(invitation_token, body)

print(response.as_dict())
```

Organization API - Users
------------------------

### getAllApiUsers - Get list of all API users

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
organization = "REPLACE_ORGANIZATION_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

res = client.get_all_api_users(organization=organization)
for user in res.results:
    print(user.as_dict())
```

### createApiUser - Create an API user

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ApiUserCreate

token = "REPLACE_TOKEN"
organization = "REPLACE_ORGANIZATION_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = ApiUserCreate(
    organization=organization,
    name="My API User",
    email="my.user@my.company",
)

res = client.create_api_user(body)
print(res.as_dict())

# Keep this key safe, it is not possible to retrieve it again.
print(res.api_key)
```

### getApiUser - Get specific API user

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
api_user_id = "REPLACE_API_USER_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

res = client.get_api_user(api_user_id)
print(res.as_dict())
```

### updateApiUser - Update an API user

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ApiUserUpdate

token = "REPLACE_TOKEN"
api_user_id = "REPLACE_API_USER_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = ApiUserUpdate(name="My New API User Name", email="new.email@my.company")

res = client.update_api_user(api_user_id, body)
print(res.as_dict())
```

### deleteApiUser - Delete an API user

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
api_user_id = "REPLACE_API_USER_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_api_user(api_user_id)
```

### regenerateApiKeyForApiUser - Regenerate API key for an API user

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
api_user_id = "REPLACE_API_USER_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

res = client.regenerate_api_key_for_api_user(api_user_id)
print(res.as_dict())

# Keep this key safe, it is not possible to retrieve it again.
print(res.api_key)
```

Webhook API
-----------

### getAllResthookSubscriptions - Get list of all resthook subscriptions

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

response = client.get_all_resthook_subscriptions()
print(response.as_dict())
```

### createResthookSubscription - Create a resthook subscription

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ResthookSubscriptionCreate

token = "REPLACE_TOKEN"
organization_identifier = "REPLACE_ORGANIZATION_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = ResthookSubscriptionCreate(
    target_url="https://my-site.com/receive",
    event="document.parse.succeeded",
    organization=organization_identifier,
)
response = client.create_resthook_subscription(body)

print(response.as_dict())
```

### getResthookSubscription - Get specific resthook subscription

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
id = "REPLACE_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

response = client.get_resthook_subscription(id=id)
print(response.as_dict())
```

### updateResthookSubscription - Update a resthook subscription

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ResthookSubscriptionUpdate

token = "REPLACE_TOKEN"
id = "REPLACE_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

body = ResthookSubscriptionUpdate(event="document.parse.completed")
response = client.update_resthook_subscription(id, body)

print(response.as_dict())
```

### deleteResthookSubscription - Delete a resthook subscription

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
id = "REPLACE_ID"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_resthook_subscription(id=id)
```

### activateResthookSubscription - Activate a resthook subscription

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
x_hook_secret = "REPLACE_X_HOOK_SECRET"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

res = client.activate_resthook_subscription(x_hook_secret)
print(res.as_dict())
```

Search & Match API - Searching
------------------------------

### createJobDescriptionSearch - Search through parsed job descriptions

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import JobDescriptionSearchParameters

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Search with custom criterias
parameters = JobDescriptionSearchParameters(
    indices=["Job-Description-Search-Demo"],
    job_titles=["Senior Java Software Developer"],
    skills=[
        {"name": "Java Programming", "required": True},
        {"name": "Python Programming", "required": False},
    ],
    # Many more criterias are available, refer to JobDescriptionSearchParameters
)
resp = client.create_job_description_search(parameters)
print(resp.as_dict())

# Search with a resume
resume_identifier = "REPLACE_RESUME_IDENTIFIER"
parameters = JobDescriptionSearchParameters(
    indices=["Job-Description-Search-Demo"],
    resume=resume_identifier,
)
resp = client.create_job_description_search(parameters)
print(resp.as_dict())
```

### getJobDescriptionSearchDetail - Get search result of specific job description

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import JobDescriptionSearchParameters

token = "REPLACE_TOKEN"
job_description_identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Search with custom criterias
parameters = JobDescriptionSearchParameters(
    indices=["Job-Description-Search-Demo"],
    job_titles=["Senior Java Software Developer"],
    degrees=["Bachelors"],
    # Many more criterias are available, refer to JobDescriptionSearchParameters
)
resp = client.get_job_description_search_detail(body=parameters, identifier=job_description_identifier)
print(resp.as_dict())
```

### createResumeSearch - Search through parsed resumes

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ResumeSearchParameters

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Search with custom criterias
parameters = ResumeSearchParameters(
    indices=["Resume-Search-Demo"],
    job_titles=["Senior Java Software Developer"],
    institutions=["Boston University"],
    # Many more criterias are available, refer to ResumeSearchParameters
)
resp = client.create_resume_search(parameters)
print(resp.as_dict())

# Search with a job description
job_description_identifier = "REPLACE_JOB_DESCRIPTION_IDENTIFIER"
parameters = ResumeSearchParameters(
    indices=["Resume-Search-Demo"],
    job_description=job_description_identifier,
)
resp = client.create_resume_search(parameters)
print(resp.as_dict())

# Search with a resume
resume_identifier = "REPLACE_RESUME_IDENTIFIER"
parameters = ResumeSearchParameters(
    indices=["Resume-Search-Demo"],
    resume=resume_identifier,
)
resp = client.create_resume_search(parameters)
print(resp.as_dict())
```

### getResumeSearchDetail - Get search result of specific resume

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ResumeSearchParameters

token = "REPLACE_TOKEN"
resume_identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Search with custom criterias
parameters = ResumeSearchParameters(
    indices=["Resume-Search-Demo"],
    job_titles=["Senior Java Software Developer"],
    institutions=["Boston University"],
    # Many more criterias are available, refer to ResumeSearchParameters
)
resp = client.get_resume_search_detail(body=parameters, identifier=resume_identifier)
print(resp.as_dict())
```

### getResumeSearchMatch - Match a single resume and job description

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

resume = "REPLACE_RESUME_IDENTIFIER"
job_description = "REPLACE_JOB_DESCRIPTION_IDENTIFIER"
index = "REPLACE_INDEX_NAME"  # Optional

result = client.get_resume_search_match(resume, job_description, index=index)
print(result.score)
```

### getResumeSearchSuggestionJobTitle - Get job title suggestions based on provided job title(s)

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

suggested_job_titles = client.get_resume_search_suggestion_job_title(["Software Developer", "Team Lead"])
print(suggested_job_titles)
```

### getResumeSearchSuggestionSkill - Get skill suggestions based on provided skill(s)

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

suggested_skills = client.get_resume_search_suggestion_skill(["Javascript", "Python"])
print(suggested_skills)
```

Search & Match API - Embedding
------------------------------

### getResumeSearchConfig - Get the config for the logged in user's embeddable resume search tool

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

result = client.get_resume_search_config()
print(result.as_dict())
```

### updateResumeSearchConfig - Update the config for the logged in user's embeddable resume search tool

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ResumeSearchConfig

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

config = ResumeSearchConfig(
    indices=["my-index"],
    max_results=10,
    display_job_title=False,
    weight_location=0.8,
    # etc.
)

result = client.update_resume_search_config(config)
print(result.as_dict())
```

### createResumeSearchEmbedUrl - Create a signed URL for the embeddable resume search tool

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ResumeSearchConfig

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Config override is optional
request_body = {
    "config_override": ResumeSearchConfig(
        indices=["my-index"],
        max_results=10,
        display_job_title=False,
        weight_location=0.8,
        # etc.
    )
}

result = client.create_resume_search_embed_url(body=request_body)
print(result.url)
```

Search & Match API - Indexing
-----------------------------

### getAllIndexes - Get list of all indexes

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

all_indexes = client.get_all_indexes()

print(all_indexes.as_dict())
```

### createIndex - Create a new index

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
index_name = "REPLACE_INDEX_NAME"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

response = client.create_index(name=index_name)

print(response.as_dict())
```

### updateIndex - Update an index

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
old_index = "REPLACE_INDEX_NAME"
new_index = "REPLACE_NEW_INDEX_NAME"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

request_body = {
    "name": new_index,
}

resp = client.update_index(name=old_index, body=request_body)

print(resp.as_dict())
```

### deleteIndex - Delete an index

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
index_name = "REPLACE_INDEX_NAME"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_index(name=index_name)
```

### createIndexDocument - Index a new document

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
index_name = "REPLACE_INDEX_NAME"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

request_body = {
    "document": identifier,
}

resp = client.create_index_document(name=index_name, body=request_body)

print(resp.as_dict())
```

### deleteIndexDocument - Delete an indexed document

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
index_name = "REPLACE_INDEX_NAME"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_index_document(name=index_name, identifier=identifier)
```