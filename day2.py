scores = [45, 67, 89, 90, 34]

print("total score:", len(scores))
print("first score:", scores[0])
print("last score:", scores[-1])

scores.append(99)
print("updated scores:",scores)


#slicing & removing items
# 1. slicing (extracting a portion )
top_three = scores[0:3]
print("top 3 scores:", top_three)

# 2. removing elements
scores.remove(34)
print("after removing 34:",scores)

last_item = scores.pop()
print("popped item:", last_item)
print("final list:", scores)


#---3. Looping through a list(sum and average)
total_scores = 0
for  s in scores:
    total_scores += s

average_score = total_scores / len(scores)
print("Total sum:", total_scores)
print("average score:",  average_score)

# --- 4. Tuples (Immutable Collections) ---
# Created with round brackets ()
dimensions = (1920, 1080)

print("Screen width:", dimensions[0])
print("Screen height:", dimensions[1])


# dimensions[0] = 1280  <-- This will cause a TypeError!