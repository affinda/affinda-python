from ._models import Document as DocumentGenerated
from ._models import InvoiceData, JobDescriptionData, ResumeData


class Document(DocumentGenerated):
    def _validate_document_type(self, expected: str) -> bool:
        """
        Return `True` if the extractor is defined and has the identifier equal to `expected`
        """
        if self.meta.collection is None:
            return False
        if self.meta.collection.extractor is None:
            return False
        return self.meta.collection.extractor.identifier == expected

    def as_resume(self):
        """
        Convert the `data` of this document to an ~affinda.models.ResumeData

        :raises: ValueError if this document does not appear to be a resume
        :raises: ~msrest.exceptions.DeserializationError if something went wrong
        :raises: ~msrest.exceptions.SerializationError if something went wrong
        """
        if not self._validate_document_type("resume"):
            raise ValueError("Document does not appear to be a resume")
        if self.data:
            self.data = ResumeData.deserialize(self.data)

    def as_invoice(self):
        """
        Convert the `data` of this document to an ~affinda.models.InvoiceData

        :raises: ValueError if this document does not appear to be an invoice
        :raises: ~msrest.exceptions.DeserializationError if something went wrong
        :raises: ~msrest.exceptions.SerializationError if something went wrong
        """
        if not self._validate_document_type("invoice"):
            raise ValueError("Document does not appear to be an invoice")
        if self.data:
            self.data = InvoiceData.deserialize(self.data)

    def as_job_description(self):
        """
        Convert the `data` of this document to an ~affinda.models.JobDescriptionData

        :raises: ValueError if this document does not appear to be a job description
        :raises: ~msrest.exceptions.DeserializationError if something went wrong
        :raises: ~msrest.exceptions.SerializationError if something went wrong
        """
        if not self._validate_document_type("job-description"):
            raise ValueError("Document does not appear to be a job description")
        if self.data:
            self.data = JobDescriptionData.deserialize(self.data)


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """


__all__ = ["Document"]
