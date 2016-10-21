def print_result(func):
    def decorated_func(*args, **kwargs):
        print(func.__name__)
        res=func(*args, **kwargs)
        if type(res) is list:
            print("\n".join(map(str,res)))
        elif type(res) is dict:
            print('\n'.join([str(x)+"="+str(res[x]) for x in res]))
        else:
            print(res)
        return res
    return decorated_func
