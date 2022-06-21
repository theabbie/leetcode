import base64

MESSAGE = '''
OkUbHBALABhEQEcNYUUPGxYJEUwbR0BULg4EDBIPEA4QR10XZgcbHRYNCA5TQEsXZgcODxwaERgQ R10XZgsGCgENAQJVCwIQbUJPCBAADA5BAgpSLxZPSUlIQh5ZCwhUKgcMTl9IQhlWBQVeNRFPSUlI QhhWAQIQbUJPDxwHQksNR0BAKAxJTg4=
'''

KEY = 'abhishek7gg7'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))
