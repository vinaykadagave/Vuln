# 2. Agent Logic (agents.py)
from typing import List, Dict
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI(model_name="gpt-4")

def prioritize_vulnerabilities(vulns: List[dict]) -> List[dict]:
    sorted_vulns = sorted(vulns, key=lambda x: x['cvss_score'], reverse=True)
    return sorted_vulns[:10]  # Top 10 risks

def suggest_remediations(vulns: List[dict]) -> List[Dict]:
    messages = [
        HumanMessage(content=f"Suggest remediation for: {v['cve_id']} - {v['description']}")
        for v in vulns
    ]
    results = [llm([msg]).content for msg in messages]
    return [
        {"cve_id": v['cve_id'], "remediation": r}
        for v, r in zip(vulns, results)
    ]
