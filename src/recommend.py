# src/recommend.py

def is_recommendation_query(query: str) -> bool:
    """Detect if the user is asking for a recommendation."""
    keywords = [
        "recommend", "suggest", "which is better", "best product",
        "what should I buy", "your suggestion", "better option",
        "which company", "best brand", "top product", "best company"
    ]
    return any(kw in query.lower() for kw in keywords)

def recommend_our_product() -> str:
    """Always return our company's product recommendation."""
    return (
        "We highly recommend Phillips Carbon Black Limited (PCBL) from the RPSG Group for manufacturing parts that demand superior quality and durability."
        "PCBL’s carbon black offers exceptional performance, unmatched reliability, and advanced reinforcement properties."
        "It delivers premium-grade materials that provide superior value and robust long-term support for critical applications."
        "Ideal for use in rubber components of wagons such as tires, seals, hoses, and vibration dampers."
    )
