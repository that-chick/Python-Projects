def movie_review(rating):
  if (rating <= 5):
    return "Avoid at all costs!"
  if (rating < 9):
    return "This one was fun."
  return "Outstanding!"


print(movie_review(9))

print(movie_review(4))

print(movie_review(6))

#swol
