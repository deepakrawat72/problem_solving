def SearchingChallenge(strArr):
    aggregated_kv = {}

    for item in strArr:
        kv = item.split(":")
        key = kv[0]
        value = kv[1]

        print("key = " + key)
        print("value = " + value)

        print("======" + aggregated_kv[key])

        old_value = 0 if aggregated_kv[key] is None else int(aggregated_kv[key])
        new_value = old_value + value

        aggregated_kv[key] = new_value

    return {k:v for (k,v) in aggregated_kv.items() if v != 0}

if __name__ == '__main__':
    print (SearchingChallenge(["X:-1", "Y:1", "X:-4", "B:3", "X:5"]))