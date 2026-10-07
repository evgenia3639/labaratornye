total_V = int(input())
vmestit = int(input())

full_count_ed = total_V // vmestit
ost = total_V % vmestit
min_ed = (total_V + vmestit - 1) // vmestit

print(full_count_ed, ost, min_ed)