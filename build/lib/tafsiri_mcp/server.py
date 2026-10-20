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

@mcp.tool(name="swahili_english_glossary", description="Translate civic and government terms between Swahili and English from a small glossary, or list the whole glossary. Use when someone needs the Swahili or English word for an official term. term is looked up in both directions; a term not in the glossary returns null for both directions with a note, not a guess. Returns the source label, the term, swahili_to_english, english_to_swahili and a note, or the glossary and its size when no term is given. A short civic glossary labelled DEMO, not a translation service: use a professional translator for important documents. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def swahili_english_glossary(term: str | None = Field(None, description="Swahili or English term to look up e.g. 'kaunti', 'serikali', 'maji', 'shule'. Leave empty for full civic glossary.")) -> dict:
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

@mcp.tool(name="kikuyu_language_guide", description="Basic Kikuyu (Gikuyu) phrases and facts: how many people belong to the community, the script and learning resources. Use when someone wants an introduction to Kikuyu or a basic phrase. term filters the phrase list; an unmatched term returns empty matches. Returns the source label, the matching phrases or the basics, an ethnic-group population (about 8.1 million, 2019 census, which is not a count of speakers), the script, resources and a note. A small reference labelled DEMO: not a dictionary. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def kikuyu_language_guide(term: str | None = Field(None, description="Optional filter for term. Pass None to return all results.")) -> dict:
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

@mcp.tool(name="luo_language_guide", description="Basic Dholuo (Luo) phrases and facts: community size, script and resources. Use when someone wants an introduction to Dholuo or a basic phrase. term filters the phrase list; an unmatched term returns empty matches. Returns the source label, the matching phrases or the basics, an ethnic-group population (about 5.07 million, fourth largest in the 2019 census, which is not a count of speakers), the script, resources and a note. A small reference labelled DEMO: not a dictionary. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def luo_language_guide(term: str | None = Field(None, description="Optional filter for term. Pass None to return all results.")) -> dict:
    """Return linguistic information and key phrases for the Luo language."""
    if term:
        t = term.lower()
        matched = {k: v for k, v in LUO_BASICS.items() if t in k or t in v}
        return {"source": "DEMO — Luo language reference", "term": term, "matches": matched}
    return {"source": "DEMO", "basics": LUO_BASICS,
            "speakers": "~5.07 million people in the Luo community (fourth largest ethnic group, 2019 census; not a count of speakers)",
            "script": "Latin alphabet. Nilotic language family.",
            "resources": ["Dholuo resources at KICD", "Lake Victoria basin oral traditions project"],
            "note": "Dholuo (Luo) is spoken primarily in Nyanza and parts of Rift Valley."}

@mcp.tool(name="official_document_glossary", description="Explain Kenyan official documents (such as ID, birth certificate, KRA PIN) with the issuing office and where to apply. Use when someone asks what a document is called or where to get it. document_type is matched by name (spaces become underscores); an unmatched type returns a note pointing to ecitizen.go.ke instead of a guess. Returns the source label, the document and the matching information, or all documents and the portal when none is given. A sample labelled DEMO: confirm with the issuing office. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def official_document_glossary(document_type: str | None = Field(None, description="Optional filter for document type. Pass None to return all results.")) -> dict:
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

@mcp.tool(name="language_detection_guide", description="Help identify which Kenyan language a text is in and where to find language tools: the languages with speaker numbers, type, markers, and translation and NLP resources. Use when someone is unsure which language a text sample is. This tool does NOT detect the language itself: text_sample is accepted but the same guide is returned. Returns the languages with their common marker words and tool pointers such as Google Translate and Masakhane. Speaker figures are rough and labelled DEMO. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def language_detection_guide(text_sample: str | None = Field(None, description="Optional filter for text sample. Pass None to return all results.")) -> dict:
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

@mcp.tool(name="civic_terminology_swahili", description="Swahili and English terms for common Kenyan civic processes (voter registration, getting an ID and others), with how to do each. Use when someone needs the Swahili wording or steps for a civic process. process matches by name or by text in the entries; if none match, ALL processes are returned. Returns the source label, the process and the guidance, or all processes and the portal. A short list labelled DEMO: check the issuing office. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def civic_terminology_swahili(process: str | None = Field(None, description="Optional filter for process. Pass None to return all results.")) -> dict:
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

def main() -> None:
    """Console entry point."""
    mcp.run()
