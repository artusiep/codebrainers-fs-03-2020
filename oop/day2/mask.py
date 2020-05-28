# filter

germs = ["bacteria", "viruses", "fungus"]

no_viruses = [x for x in germs if x != "viruses"]

print(no_viruses)


# def is_virus(elem):
#     if elem == "viruses":
#         return True
#     else:
#         return False

def is_virus(elem):
    return elem != "viruses"

no_viruses_with_filter = filter(is_virus, germs)

print(list(no_viruses_with_filter))


no_viruses_with_filter_with_lambda = filter(lambda elem: elem != "viruses", germs)

print(tuple(no_viruses_with_filter_with_lambda))