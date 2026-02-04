"""
Explanation Templates.

Maps financial metrics to human-readable explanations.
"""


PE_TEMPLATES = {
    "low": "The stock appears undervalued based on its low P/E ratio.",
    "medium": "The stock is fairly valued based on its P/E ratio.",
    "high": "The stock may be overvalued based on its high P/E ratio.",
}

DE_TEMPLATES = {
    "low": "The company maintains a healthy debt position.",
    "medium": "The company has a moderate level of debt.",
    "high": "The company carries a high debt burden, increasing risk.",
}

PROFITABILITY_TEMPLATES = {
    "Strong": "The company demonstrates strong profitability.",
    "Moderate": "The company shows stable profitability.",
    "Weak": "The company has weak profitability metrics.",
}
