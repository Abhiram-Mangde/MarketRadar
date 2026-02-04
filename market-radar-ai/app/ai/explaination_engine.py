"""
AI Explanation Engine.

Generates human-readable investment insights
from fundamental analysis data.
"""

from typing import Dict

from app.ai.explanation_templates import (
    PE_TEMPLATES,
    DE_TEMPLATES,
    PROFITABILITY_TEMPLATES,
)


def explain_fundamentals(fundamental_data: Dict) -> str:
    """
    Generate AI-style explanation for fundamental analysis.

    Args:
        fundamental_data (Dict): Output from analyze_fundamentals()

    Returns:
        str: Human-readable explanation
    """
    ratios = fundamental_data["ratios"]
    assessment = fundamental_data["assessment"]

    pe = ratios["pe_ratio"]
    de = ratios["de_ratio"]
    profitability = assessment["profitability"]

    # PE interpretation
    if pe < 12:
        pe_text = PE_TEMPLATES["low"]
    elif pe < 20:
        pe_text = PE_TEMPLATES["medium"]
    else:
        pe_text = PE_TEMPLATES["high"]

    # Debt interpretation
    if de < 0.5:
        de_text = DE_TEMPLATES["low"]
    elif de < 1:
        de_text = DE_TEMPLATES["medium"]
    else:
        de_text = DE_TEMPLATES["high"]

    profit_text = PROFITABILITY_TEMPLATES.get(
        profitability, "Profitability data is inconclusive."
    )

    explanation = (
        f"{fundamental_data['symbol']} Fundamental Analysis:\n"
        f"- {pe_text}\n"
        f"- {profit_text}\n"
        f"- {de_text}\n"
        f"Overall Assessment: {assessment['valuation']} with {assessment['risk']} risk."
    )

    return explanation
