# Currency Support Analysis - Affinda Python SDK

## Summary
After analyzing the codebase, I found this is the **Affinda Python SDK** - a client library for document parsing APIs, not a web application with billing functionality.

## What This Codebase Contains
- Python API client for Affinda's document parsing service
- Models for parsing structured data from documents (resumes, invoices, etc.)
- `CurrencyCodeAnnotation` class for extracting currency codes from parsed documents
- Support for parsing currency information from invoice documents

## What This Codebase Does NOT Contain
- No billing pages or payment interfaces
- No web application UI components  
- No currency selection dropdowns or forms
- No payment processing functionality

## Currency-Related Components Found
1. **CurrencyCodeAnnotation** class in `affinda/models/_models_py3.py`
   - Used for parsing currency codes from documents
   - Part of the document annotation system
   - Handles extracted currency data from invoices/receipts

2. **Invoice Data Models** with currency fields
   - Various models include `currency` and `currency_code` fields
   - Used for structured data extraction from parsed documents

## Clarification Needed
The request to "update our billing page to include AUD currency as an option" doesn't match this codebase because:

1. **This is an SDK/API client**, not a web application
2. **No billing pages exist** in this codebase
3. **Currency handling** here is for document parsing, not payment processing

## Possible Scenarios
1. **Wrong Repository**: You may be looking for a different repository that contains your billing application
2. **Separate Application**: Your billing page exists in a different codebase that uses this SDK
3. **Document Parsing Enhancement**: You might want to improve currency parsing capabilities to support AUD

## Next Steps
To properly implement AUD currency support in a billing page, you would need:

1. **Identify the correct repository** containing your billing application
2. **Locate the billing page components** (likely React, Vue, Angular, or server-side templates)
3. **Find the currency options configuration** (dropdown lists, constants, enums)
4. **Add AUD to the supported currencies list**
5. **Update any related payment processing logic**

## If You Want to Enhance Document Parsing
If the goal is to improve how this SDK handles AUD currency in parsed documents, the current implementation should already support it since `CurrencyCodeAnnotation` handles currency extraction generically.

---
*Analysis completed on codebase: affinda-python SDK*