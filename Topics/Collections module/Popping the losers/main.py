# the following line reads a dict from the input and converts it into an OrderedDict, do not modify it, please
firms = OrderedDict(json.loads(input()))

firms.popitem(last=True)
firms.popitem(last=True)

print(firms)
