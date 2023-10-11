def add_to_str(text):
    assert text is my_str
    text += "a"
    assert text is not my_str


def add_to_list(lst):
    assert lst is my_lst
    lst += ["a"]
    assert lst is my_lst


def add_to_str_modify_str(text):
    assert text is my_str
    text += "a"
    assert text is not my_str
    return text


my_str = "test"
add_to_str(my_str)
print(my_str)

my_lst = ["b"]
add_to_list(my_lst)
print(my_lst)

my_str = "test"
my_str = add_to_str_modify_str(my_str)
print(my_str)
