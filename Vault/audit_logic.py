SUBSCRIPTION_PATTERNS = {
    'netflix.com': 'Netflix',
    'spotify.com': 'Spotify',
    'adobe.com': 'Adobe',
    'notion.so': 'Notion'
}

def analyze_transaction(transaction):
    for pattern, name in SUBSCRIPTION_PATTERNS.items():
        if pattern in transaction['description'].lower():
            return {
                'type': 'subscription',
                'name': name,
                'amount': transaction['amount'],
                'date': transaction['date']
            }
    return None