import hashlib
s='netjamol'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
