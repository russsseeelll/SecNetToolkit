from django import forms

ACTION_CHOICES = [
    ('nmap_common', 'Nmap: Common Ports'),
    ('nmap_full', 'Nmap: Full Scan (All 65535 Ports)'),
    ('nslookup', 'NSLookup'),
    ('whois', 'WHOIS Lookup'),
    ('dig', 'Dig (DNS Lookup)'),
    ('traceroute', 'Traceroute'),
    ('sslscan', 'SSLScan'),
    ('curl_headers', 'HTTP Headers (curl -I)'),
]

class ScanForm(forms.Form):
    target = forms.CharField(
        label='Target (URL or IP)',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. example.com or 8.8.8.8',
        })
    )
    action = forms.MultipleChoiceField(
        label='Actions',
        choices=ACTION_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input',
        }),
        required=True,
    )
