
filename = 'a.bin' # bin : binary

data = 100
#with로 open하면 close불필요
# wb write binary
with open(filename, "wb") as f:
    # bytearray binary 배열로
    f.write(bytearray([data]))


