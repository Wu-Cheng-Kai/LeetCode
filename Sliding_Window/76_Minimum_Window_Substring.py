# 1. count
# def minWindow(s: str, t: str) -> str:
#     t_num, s_num = len(t), len(s)
#     if t_num > s_num:
#         return ""
#     else:
#         t_all, t_set = {}, set()
#         current, min_s = "", ""
#         count, n = [], 0

#         for i in t:
#             if i in t_set:
#                 count[t_all[i]] -= 1
#             else:
#                 t_all[i] = n
#                 t_set.add(i)
#                 count.append(-1)
#                 n += 1
        
#         for i in s:
#             current += i
#             if i in t_set:
#                 count[t_all[i]] += 1
#             if min(count) >= 0:
#                 while min(count) >= 0:
#                     if len(min_s) == 0 or len(current) < len(min_s):
#                         min_s = current
#                     if current[0] in t_set:
#                         count[t_all[current[0]]] -= 1
#                     current = current[1:]

#             print(i, count, current, min_s)
#         return min_s

# 2. minimize the length of output
def minWindow(s: str, t: str) -> str:
    t_num, s_num = len(t), len(s)
    if t_num > s_num:
        return ""
    else:
        t_all, t_set = {}, set()
        min_s, min_len = "", s_num + 1
        count, n = [], 0
        start = 0
        find = False

        for i in t:
            if i in t_set:
                count[t_all[i]] -= 1
            else:
                t_all[i] = n
                t_set.add(i)
                count.append(-1)
                n += 1
        
        for i in range(s_num):
            if s[i] in t_set:
                count[t_all[s[i]]] += 1
                
            while i - start > min_len - 1:
                if s[start] in t_set:
                    count[t_all[s[start]]] -= 1
                start += 1

            while min(count) >= 0:
                find = True
                if s[start] in t_set:
                    count[t_all[s[start]]] -= 1
                start += 1
                
            if find:
                min_s = s[start-1:i+1]
                min_len = len(min_s)
                find = False

            print(i, count, s[start-1:i+1], min_s)
        return min_s


s = "cabwefgewcwaefgcf"
t = "cae"

answer = minWindow(s, t)
print(answer)
