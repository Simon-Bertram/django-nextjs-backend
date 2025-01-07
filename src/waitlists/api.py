from typing import List
from ninja import Router

from .models import WaitlistEntry
from .schemas import WaitlistEntryListSchema

router = Router()

@router.get("", response=List[WaitlistEntryListSchema])
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.all()
    return qs

@router.get("{entry_id}", response=WaitlistEntryListSchema)
def list_waitlist_entries(request, entry_id:int):
    qs = WaitlistEntry.objects.all()
    return qs