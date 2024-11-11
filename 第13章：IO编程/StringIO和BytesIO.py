'''
# StringIO
# 把 str  写入 StringIO

from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('世界')
print(f.getvalue())
'''

# BytesIO
from io import BytesIO
f = BytesIO()
f.write('Hello, 世界'.encode('utf-8'))
print(f.getvalue())
