import faiss
from sentence_transformers import SentenceTransformer
import glob
import numpy as np

index = faiss.read_index("faiss_index.bin")
print("FAISS index loaded!")

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

user_query = """
 2019KERDNT

IN THE HIGH COURT OF KERALA AT ERNAKULAM
PRESENT:
‘THE HONOURABLE MR. JUSTICE P.UBAID

TUESDAY, THE 6TH DAY OF JANUARY 2015/167H POUSHA, 19361

cel.Mc.to. 10 of 2015

IN CC 276/2014 OF THE JUDICIAL FIRST CLASS MAGISTRATE COURT,
‘MALAPPURAM,

(CRIME NO. 2/2013 OF VENGARA POLICE STATION , MALAPPURAM

-ETITIONERS/ACCUSED :

1. ABU TARIR, AGED 27 YEARS,
8/0. KONJALIKUTTY, PANDIKADAVATH HOUSE, KARATHODU,
‘URAKOM, VENGARA, 'MALAPPURAM DISTRICT

KABEER, AGED 23 YEARS,
5/0.MOHAMMED, CHAKKINGALTHODI HOUSE, URAKOM
MELMURI, MALAPPURAM DISTRICT

BHARATHAN, AGED 29 YEARS,
5/0. BHASKARAN, ALAMBATTA HOUSE, URAKOM,
MELMURI P.O., KARATHODU, MALAPPURAM DISTRICT.

4. SADIKALE, AGED 21 YEARS,
'8/0.ALAVE, NARAYANKUNNEN HOUSE, URAKOM,
MELMURI P.O., KARATHODU, MALAPPURAM DISTRICT.

BY ADV. SRI.P.SAMSUDIN

[RESPONDENTS/STATE AND DE-FACTO COMPLAINANT:

1. STATE OF KERALA
[REPRESENTED BY THE PUBLIC PROSECUTOR,
RIGH COURT OF KERALA
[BRNAKULAM ~682 031. (CRIME NO.2/2013 OF VENGARA
POLICE STATION IN MALAPPURAM DISTRICT) .

2. SUHALT, AGED 27 YEARS,
$/0.MOHAMMEDKUTTY HAJI, THOTTASSERI HOUSE,
‘OORAKAM KEEZHMORI, OK MURI P.O - 679 324
‘THIRURANGADI TALUK, MALAPPURAM DISTRICT

R2_BY ADV. SRI.K.C.ANTONY MATHER
RI BY PUBLIC PROSECUTOR S¥T.S.HYHA

THIS CRIMINAL MISC. CASE HAVING COME UP FOR ADMISSION
(ON 06-01-2015, THE COURT ON THE SAME DAY PASSED THE FOLLOWING:
 2019KERDNT
ceL.MC.No. 10 of 2015

APPENDIX

PETITIONERS’ ANWEXURES:

ANMEXURE-AL: COPY OF THE FINAL REPORT IN CRIME NO.2/2013 OF
VENGARA POLICE STATION.

ANNEXURE-A2: COPY OF THE AFFIDAVIT DATED 22.12.2014 SWORN IN BY
‘THE 2ND RESPONDENT.

RESPONDENTS’

wr

//7808 COPY//

P.A To JUDGE
 2019KERDNT

P.UBAID, J.

Crl.M.C No.10 of 2015

Dated this the 6" day of January, 2015

ORDER

The petitioners herein are the four accused in
C.C No.278/2014 of the Judicial First Class Magistrate Court,
Malappuram. Crime in the said case was registered under
Sections 341, 323 and 324 r/w 34 of the Indian Penal Code, on
the complaint of one Suhail. The petitioners now seek orders
quashing the prosecution as against them on the ground that
they and the defacto complainant have amicably settled the
dispute out of court. The defacto complainant Suhail is the
second respondent in this proceeding. He has filed affidavit to
the effect that he has settled the whole dispute with the accused,
and he has no complaint or grievance now. I am well satisfied
that there is a real and genuine settlement between the parties,
and I find that continuance of prosecution in such a situation will
not serve any purpose, other than wasting the precious time of
the court. Nobody will support the prosecution if the case

against the petitioners goes to trial.
 2019KERDNT

CALM No.10 0f 2015 2

In the result, this Criminal Miscellaneous Case is
allowed. The prosecution against the petitioners herein in C.C
'No.278/2014 before the Judicial First Class Magistrate Court,
Malappuram, will stand quashed under Section 482 of the Code
of Criminal Procedure. Accordingly, the petitioners will stand
released from prosecution, and the bail bond, if any, executed by

them will stand discharged.

P.UBAID
JUDGE

ab

 
"""

query_embedding = model.encode([user_query]).astype("float32")

query_embedding /= np.linalg.norm(query_embedding, axis=1, keepdims=True)

k = 5

distances, indices = index.search(query_embedding, k)

print("Most similar document indices:", indices)
print("Distances:", distances)