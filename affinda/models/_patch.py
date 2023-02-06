from msrest.serialization import UTC

from ._models import Document as DocumentGenerated
from ._models import Invoice, JobDescription, Resume


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

    def as_invoice(self) -> Invoice:
        """
        Convert this document to an ~affinda.models.Invoice

        :raises: ValueError if this document does not appear to be an invoice
        :raises: ~msrest.exceptions.DeserializationError if something went wrong
        :raises: ~msrest.exceptions.SerializationError if something went wrong
        """
        if not self._validate_document_type("invoice"):
            raise ValueError("Document does not appear to be an invoice")
        invoice = Invoice.deserialize(self.serialize(keep_readonly=True))
        invoice.meta.is_verified = self.meta.is_confirmed
        if self.meta.confirmed_dt is not None:
            invoice.client_verified_dt = self.meta.confirmed_dt.astimezone(tz=UTC()).isoformat()
        return invoice

    def as_job_description(self) -> JobDescription:
        """
        Convert this document to a ~affinda.models.JobDescription

        :raises: ValueError if this document does not appear to be a job description
        :raises: ~msrest.exceptions.DeserializationError if something went wrong
        :raises: ~msrest.exceptions.SerializationError if something went wrong
        """
        if not self._validate_document_type("job-description"):
            raise ValueError("Document does not appear to be a job description")
        job_description = JobDescription.deserialize(self.serialize(keep_readonly=True))
        job_description.meta.is_verified = self.meta.is_confirmed
        return job_description

    def as_resume(self) -> Resume:
        """
        Convert this document to a ~affinda.models.Resume

        :raises: ValueError if this document does not appear to be a resume
        :raises: ~msrest.exceptions.DeserializationError if something went wrong
        :raises: ~msrest.exceptions.SerializationError if something went wrong
        """
        if not self._validate_document_type("resume"):
            raise ValueError("Document does not appear to be a resume")
        resume = Resume.deserialize(self.serialize(keep_readonly=True))
        resume.meta.is_verified = self.meta.is_confirmed
        return resume


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """


__all__ = ["Document"]
