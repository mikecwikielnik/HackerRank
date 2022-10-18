if __name__ == '__main__':
    records, scores  = [], []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)
    
    low_2nd = sorted(list(set(scores)))[1]
    names_low_2nd = sorted([record[0] for record in records if record[1] == low_2nd])
    
    for name in names_low_2nd:
        print(name)


