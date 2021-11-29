def get_res(txt):
    try:
        return sum([1 for x in txt.lower() if x in 'aeiouy'])
    except AttributeError as ae:
        print(f'An Error occured : {ae} ')




