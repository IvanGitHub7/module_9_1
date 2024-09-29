def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        res = function(int_list)
        new_value = {function.__name__ : res}
        results.update(new_value)
    return results
        
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))