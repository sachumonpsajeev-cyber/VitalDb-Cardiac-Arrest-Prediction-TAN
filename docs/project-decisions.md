# Project Decisions Log

## Decision 1 - Label Definition
**Date:** 18 Feb 2026
**Decision:** Use in-hospital mortality as prediction label
**Reason:** No direct cardiac arrest label in VitalDB. 
Mortality is a reliable proxy and already available 
in clinical_information.csv
**Alternatives Considered:** Detecting cardiac arrest 
from vital signs patterns directly

## Decision 2 - Coding Environment
**Date:** 18 Feb 2026
**Decision:** Use Google Colab for development, 
then move to Jupyter/Anaconda for final code
**Reason:** No local setup needed, free GPU access

## Decision 3 - Note Taking
**Date:** 18 Feb 2026
**Decision:** Use GitHub /docs folder instead of Notion
**Reason:** Keeps everything in one place, 
looks professional on portfolio
