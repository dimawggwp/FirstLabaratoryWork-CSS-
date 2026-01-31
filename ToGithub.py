def analyze_text(text):
    res = []
    uniq = []
    respawn = []

    for i in text:
        if type(i) == int:
            continue

        elif type(i) == str:
            res.append(i)

            if len(i) == 5:
                uniq.append(i)

            if i not in respawn:
                respawn.append(i)

    return res, uniq, respawn


print(analyze_text(["qazaq", "same", 5, "apple", "torekhan", "islam"]))