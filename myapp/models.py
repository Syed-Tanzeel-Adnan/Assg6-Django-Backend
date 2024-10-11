from django.db import models
import uuid

class SYS_State(models.Model):
    Stt_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Stt_Name = models.CharField(max_length=100)
    Stt_Code = models.CharField(max_length=10)

class OPT_Party(models.Model):
    PTY_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    PTY_FirstName = models.CharField(max_length=100)
    PTY_LastName = models.CharField(max_length=100)
    PTY_Phone = models.CharField(max_length=15, null=True, blank=True)
    PTY_SSN = models.CharField(max_length=11, null=True, blank=True)

class OPT_Address(models.Model):
    Add_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Add_Line1 = models.CharField(max_length=255)
    Add_Line2 = models.CharField(max_length=255, null=True, blank=True)
    Add_City = models.CharField(max_length=100)
    Add_State = models.ForeignKey(SYS_State, on_delete=models.CASCADE)
    Add_Zip = models.CharField(max_length=10)
    Add_PartyID = models.ForeignKey(OPT_Party, on_delete=models.CASCADE)
