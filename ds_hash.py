import dns.rdata

dnskey = dns.rdata.from_text('in', 'dnskey',
'257 3 13 mdsswUyr3DPW132mOi8V9xESWE8jTo0dxCjjnopKl+GqJxpVXckHAeF+ KkxLbxILfDLUT0rAK9iUzy1L53eKGQ==')

print(dnskey)
print(dns.dnssec.make_ds('torquegear.me.', dnskey, 2))




