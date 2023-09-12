from typing import Union, List

lines = []                      # list of binary numbers string
with open('./input') as f:
    for ln in f:
        lines.append(ln.strip())

def most_common_bit(bits: List[int]) -> int:
    if len(bits) == 2:
        assert bits[0] != bits[1]
        return 1

    c0, c1 = 0, 0
    for bit in bits:
        if bit == 0:
            c0 += 1
        elif bit == 1:
            c1 += 1
        else:
            assert False

    return 1 if c1 >= c0 else 0

def least_common_bit(bits: List[int]) -> int:
    return most_common_bit(bits) ^ 1

def bits_to_int(bits: Union[List[int], str]):
    exp = len(bits) - 1

    ret = 0
    for bit in bits:
        ret += 2 ** exp * int(bit)
        exp -= 1
    return ret

def bits_indexes(bits: List[int], a_bit: int):
    ret = []
    for idx, bit in enumerate(bits):
        if bit == a_bit:
            ret.append(idx)
    return ret

class Report:
    def __init__(self, rows: List[str]):
        self.rows = rows

    @property
    def row_count(self):
        return len(self.rows)

    @property
    def column_count(self):
        return len(self.rows[0])

    def column_at(self, index) -> List[int]:
        """Return a list of bit at column"""
        return [int(row[index]) for row in self.rows]

    def row_at(self, index) -> str:
        """Return a row at index"""
        return self.rows[index]

    def with_rows(self, row_indexes: List[int]):
        """Return a new Report with row indexes"""
        rows = []
        for idx, row in enumerate(self.rows):
            if idx in row_indexes:
                rows.append(row)
        return Report(rows)

# --------------------
r = Report(lines)

gamma_rate_bits = []
epsilon_rate_bits = []
for idx in range(r.column_count):
    mcb = most_common_bit(r.column_at(idx))
    gamma_rate_bits.append(mcb)
    epsilon_rate_bits.append(mcb ^ 1)

print(gamma_rate_bits, epsilon_rate_bits)
print(bits_to_int(gamma_rate_bits), bits_to_int(epsilon_rate_bits))
print(bits_to_int(gamma_rate_bits) * bits_to_int(epsilon_rate_bits))

# --------------------
r = Report(lines)

def calc(r: Report, f):
    col_idx = 0
    while 1:
        if r.row_count == 1:
            break

        col = r.column_at(col_idx)
        val = f(col)
        indexes = bits_indexes(col, val)
        r = r.with_rows(indexes)
        col_idx += 1

    return r.row_at(0)

oxy_rate, co2_rate = calc(r, most_common_bit), calc(r, least_common_bit)

print(oxy_rate, co2_rate)
print(bits_to_int(oxy_rate), bits_to_int(co2_rate))
print(bits_to_int(oxy_rate) * bits_to_int(co2_rate))
