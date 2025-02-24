import re


GATES = {
    'AND': lambda x,y : x & y,
    'OR': lambda x,y : x | y,
    'XOR': lambda x,y : x ^ y,
    'CONST': lambda x,_ : x
}


with open('day24.txt', 'r') as f:
    calculated_values = {}
    while l := f.readline().strip():
        name, value = re.findall(r'(\w+): (\d)', l)[0]
        calculated_values[name] = int(value)

    gates = {}
    for l in f.readlines():
        in1, op, in2, _, out = l.strip().split(' ')
        gates[out] = (in1, op, in2)

while gates:
    items = list(gates.items())
    for out, gate in items:
        in1, op, in2 = gate
        if in1 in calculated_values and in2 in calculated_values:
            calculated_values[out] = GATES[op](calculated_values[in1], calculated_values[in2])
            del gates[out]

z_gates = {k:v for k,v in calculated_values.items() if k.startswith('z')}
bin_out = ''.join(str(v) for _,v in sorted(list(z_gates.items()), key=lambda it: it[0], reverse=True))
print(int(bin_out, 2))
