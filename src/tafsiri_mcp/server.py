"""TafsiriMCP — Kenya Translation Infrastructure (6 tools). All data DEMO."""
from __future__ import annotations
from typing import Annotated, Optional
from fastmcp import FastMCP
from pydantic import Field
mcp = FastMCP(name="tafsiri-mcp", instructions="Kenya translation infrastructure — Swahili, Kikuyu, Luo. DEMO.")

SWAHILI_CIVIC = {
    "serikali": "government", "kaunti": "county", "uchaguzi": "election",
    "kura": "vote", "mkataba": "contract", "leseni": "licence", "faini": "fine",
    "haki": "right/justice", "sheria": "law", "mshtaki": "plaintiff",
    "mahakama": "court", "hakimu": "magistrate", "jaji": "judge",
    "bunge": "parliament", "seneti": "senate", "gavana": "governor",
    "mkurugenzi": "director", "msajili": "registrar", "fomu": "form",
    "cheti": "certificate", "stakabadhi": "receipt", "ankara": "invoice",
    "mpango": "plan/policy", "bajeti": "budget", "ushuru": "tax",
}
KIKUYU_BASICS = {
    "mũtũngati": "government official", "ũhoro": "matter/issue",
    "mũtũ": "person", "ngũgũ": "law/rule", "thakame": "blood (medicine)",
    "mũrĩmi": "farmer", "mũrutani": "teacher", "mũndũ": "person",
    "gĩthomo": "school", "ũgĩmĩ": "health", "mbarĩ": "family/clan",
    "mucii": "home", "itura": "village", "mbũrũ": "land",
}
LUO_BASICS = {
    "loch": "government/authority", "piny": "land/area",
    "oganda": "clan/community", "somo": "learning", "yiero": "health",
    "jajuok": "elder", "milambo": "rights", "chak": "beginning",
    "ber": "good/benefit", "rach": "problem/difficulty",
    "luo": "Luo people", "nam": "lake", "nam lolwe": "Lake Victoria",
}

@mcp.tool(name="swahili_english_glossary", description="Swahili-English civic and government glossary. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def swahili_english_glossary(term: Optional[str] = Field(None, description="Swahili or English term to look up e.g. 'kaunti', 'serikali', 'maji', 'shule'. Leave empty for full civic glossary.")) -> dict:
    """Translate civic and government terminology between Swahili and English."""
    if term:
        t = term.lower()
        en = SWAHILI_CIVIC.get(t)
        sw = {v: k for k, v in SWAHILI_CIVIC.items()}.get(t)
        return {"source": "DEMO — Kenya government terminology", "term": term,
                "swahili_to_english": en, "english_to_swahili": sw,
                "note": "For full translation use a professional service or translator."}
    return {"source": "DEMO", "glossary": SWAHILI_CIVIC,
            "size": len(SWAHILI_CIVIC), "domain": "Kenya civic and government"}

@mcp.tool(name="kikuyu_language_guide", description="Kikuyu language basics and resources for Kenya. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def kikuyu_language_guide(term: Optional[str] = Field(None, description="Optional filter for term. Pass None to return all results.")) -> dict:
    """Return linguistic information and key phrases for the Kikuyu language."""
    if term:
        t = term.lower()
        matched = {k: v for k, v in KIKUYU_BASICS.items() if t in k or t in v}
        return {"source": "DEMO — Kikuyu language reference", "term": term, "matches": matched}
    return {"source": "DEMO", "basics": KIKUYU_BASICS,
            "speakers": "~8.1 million (largest ethnic group in Kenya)",
            "script": "Latin alphabet. Tonal language.",
            "resources": ["kiukuyu.com", "Kenya Institute of Curriculum Development (KICD)",
                         "Gĩkũyũ Cultural and Online Museum"],
            "note": "Kikuyu (Gĩkũyũ) is the first language of approximately 17% of Kenya's population."}

@mcp.tool(name="luo_language_guide", description="Luo language basics and resources for Kenya. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def luo_language_guide(term: Optional[str] = Field(None, description="Optional filter for term. Pass None to return all results.")) -> dict:
    """Return linguistic information and key phrases for the Luo language."""
    if term:
        t = term.lower()
        matched = {k: v for k, v in LUO_BASICS.items() if t in k or t in v}
        return {"source": "DEMO — Luo language reference", "term": term, "matches": matched}
    return {"source": "DEMO", "basics": LUO_BASICS,
            "speakers": "~4.2 million (third largest ethnic group in Kenya)",
            "script": "Latin alphabet. Nilotic language family.",
            "resources": ["Dholuo resources at KICD", "Lake Victoria basin oral traditions project"],
            "note": "Dholuo (Luo) is spoken primarily in Nyanza and parts of Rift Valley."}

@mcp.tool(name="official_document_glossary", description="Kenya official document terminology guide — forms, certificates, legal terms. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def official_document_glossary(document_type: Optional[str] = Field(None, description="Optional filter for document type. Pass None to return all results.")) -> dict:
    """Return standard terminology for Kenya official documents and certificates."""
    DOCS = {
        "id_card": {"swahili": "Kitambulisho", "common_name": "ID", "issued_by": "NIIMS/NDRS", "cost_kes": 300},
        "birth_certificate": {"swahili": "Cheti cha Kuzaliwa", "issued_by": "Civil Registration Service", "cost_kes": 150},
        "land_title": {"swahili": "Hati ya Ardhi", "issued_by": "Lands Registry", "cost_kes": "varies"},
        "business_permit": {"swahili": "Leseni ya Biashara", "issued_by": "County Government", "cost_kes": "varies by business"},
        "driving_licence": {"swahili": "Leseni ya Udereva", "issued_by": "NTSA", "cost_kes": 3050},
        "passport": {"swahili": "Pasi/Hati ya Kusafiria", "issued_by": "Department of Immigration", "cost_kes": 4550},
        "kra_pin": {"swahili": "Nambari ya PIN ya KRA", "issued_by": "Kenya Revenue Authority", "cost_kes": 0},
        "nhif_card": {"swahili": "Kadi ya NHIF/SHA", "issued_by": "Social Health Authority", "cost_kes": 0},
        "nssf_card": {"swahili": "Kadi ya NSSF", "issued_by": "National Social Security Fund", "cost_kes": 0},
        "marriage_cert": {"swahili": "Cheti cha Ndoa", "issued_by": "Attorney General's office", "cost_kes": 1000},
    }
    if document_type:
        d = document_type.lower().replace(" ","_")
        matched = {k: v for k, v in DOCS.items() if d in k}
        return {"source": "DEMO — Kenya government services", "document": document_type, "info": matched or {"note": "Document not in sample dataset. Visit ecitizen.go.ke for full list."}}
    return {"source": "DEMO — Kenya government documents", "documents": DOCS, "portal": "ecitizen.go.ke"}

@mcp.tool(name="language_detection_guide", description="Guide to language detection and translation resources for Kenya. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def language_detection_guide(text_sample: Optional[str] = Field(None, description="Optional filter for text sample. Pass None to return all results.")) -> dict:
    """Identify which Kenyan language a text sample is written in."""
    KENYA_LANGUAGES = {
        "Swahili (Kiswahili)": {"code": "sw", "speakers_m": 47, "type": "Bantu", "official": True, "markers": ["na", "ya", "wa", "ni", "kwa", "au"]},
        "Kikuyu (Gĩkũyũ)": {"code": "ki", "speakers_m": 8.1, "type": "Bantu", "official": False, "markers": ["na", "nĩ", "mũ", "gĩ", "ũ"]},
        "Luo (Dholuo)": {"code": "luo", "speakers_m": 4.2, "type": "Nilotic", "official": False, "markers": ["e", "gi", "ne", "ni"]},
        "Kalenjin": {"code": "kln", "speakers_m": 4.9, "type": "Nilotic", "official": False, "markers": []},
        "Kamba (Kikamba)": {"code": "kam", "speakers_m": 3.9, "type": "Bantu", "official": False, "markers": []},
        "English": {"code": "en", "speakers_m": 47, "type": "Indo-European", "official": True, "markers": ["the", "and", "is", "of"]},
    }
    detect = None
    if text_sample:
        for lang, info in KENYA_LANGUAGES.items():
            if any(f" {m} " in f" {text_sample.lower()} " for m in info["markers"] if m):
                detect = lang; break
    return {"source": "DEMO", "kenya_languages": KENYA_LANGUAGES,
            "detected_language": detect, "text_sample": text_sample,
            "translation_tools": {
                "google_translate": "translate.google.com (supports Swahili, limited Kikuyu)",
                "microsoft_translator": "translator.microsoft.com",
                "kiswahili": "kiswahili.co.ke (Swahili dictionary)",
                "masakhane": "masakhane.ai (African NLP research)"
            }}

@mcp.tool(name="civic_terminology_swahili", description="Swahili translations of Kenya civic and legal processes. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def civic_terminology_swahili(process: Optional[str] = Field(None, description="Optional filter for process. Pass None to return all results.")) -> dict:
    """Return Swahili terminology for Kenya government processes and civic interactions."""
    PROCESSES = {
        "voter_registration": {"en": "Voter Registration", "sw": "Usajili wa Mpigakura", "how": "Register at IEBC offices or online at iebc.or.ke", "docs_needed": "National ID"},
        "land_transfer": {"en": "Land Transfer", "sw": "Uhamisho wa Ardhi", "how": "Apply at Lands Registry with consent, stamp duty payment, and title deed", "docs_needed": "Title deed, IDs, consent"},
        "business_registration": {"en": "Business Registration", "sw": "Usajili wa Biashara", "how": "Register at eCitizen, Business Registration Service, or county", "docs_needed": "ID, KRA PIN, address"},
        "birth_registration": {"en": "Birth Registration", "sw": "Usajili wa Kuzaliwa", "how": "Register within 6 months at Civil Registration Service. Free if within 6 months.", "docs_needed": "Parents' IDs, hospital notification"},
        "court_filing": {"en": "Court Filing", "sw": "Kuwasilisha Mahakamani", "how": "Visit court registry with correctly filled forms, pay filing fee", "docs_needed": "Statement of claim/petition, ID"},
        "succession_petition": {"en": "Succession Petition", "sw": "Ombi la Urithi", "how": "File at High Court probate registry. KES 3,000 filing fee.", "docs_needed": "Death certificate, list of assets, names of heirs"},
    }
    if process:
        p = process.lower().replace(" ","_")
        matched = {k: v for k, v in PROCESSES.items() if p in k or any(p in str(v[f]) for f in ["en","sw","how"])}
        return {"source": "DEMO — Kenya government processes", "process": process, "guidance": matched or PROCESSES}
    return {"source": "DEMO", "processes": PROCESSES, "portal": "ecitizen.go.ke"}
