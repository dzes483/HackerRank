# regex_pattern = r"^[C]?[M]{0,3}[DLV]?[XI]{0,3}[C]{0,3}[DLV]?[XI]{0,3}[DLV]?"

#999-3999
thousand = r"[C]?[M]{0,3}"
#99-999
hundred = r"[DX]?[C]{0,3}"
#9-98
ten = r"[ILD]?[X]{0,3}"
#1-8
one = r"[V]?[I]{0,3}[V]?"

regex_pattern = thousand + hundred + ten + one

import re
print(str(bool(re.fullmatch(regex_pattern, input()))))
