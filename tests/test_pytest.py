import pytest
import pytest_check as check


@pytest.mark.set1
def test_file1_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert x == y, "test failed"


@pytest.mark.set2
def testfile1_method2():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"


@pytest.mark.datatypes
def test_variable_ids():
    a = 5
    b = 5
    c = 6
    assert id(a) == id(b)
    assert id(a) != id(c)


@pytest.mark.sets
def test_variable_type_set():
    a = {7, 5.6, 'wow', ('new', 8)}
    for el in a:
        check.equal(str(type(el)), "<class 'int'>",
                        "el = {} and type of el is {}".format(el, type(el)))

    check.equal(str(type(a)), "<class 'set'>",
                "a = {} and type of a is {}".format(a, type(a)))

@pytest.mark.sets
def test_variable_type_set_tuple_to_dict():
    a = {7, 5.6, 'wow', ('new', 8)}
    for el in a:
        # check.not_equal(str(type(el)), "<class 'tuple'>", "it's tuple to dict: {}".format(str(dict(el))))
        d = None
        try:
            d = dict([el])
        except:
            print('{} is not a tuple'.format(el))
        check.not_equal(str(type(el)), "<class 'tuple'>", "it's tuple to dict: {}".format(d))

    check.equal(str(type(a)), "<class 'set'>",
                "a = {} and type of a is {}".format(a, type(a)))


@pytest.mark.datatypes
def test_variable_type_list():
    a = [7, 5.6, 'wow']
    print(a, type(a))
    for el in a:
        check.not_equal(str(type(el)), "<class 'int'>",
                        "el = {} and type of el is {}".format(el, type(el)))


@pytest.mark.datatypes
def test_variable_type_tuple():
    a = (7, 5.6, 'wow')
    print(a, type(a))
    for el in a:
        check.equal(str(type(el)), "<class 'int'>",
                    "el = {} and type of el is {}".format(el, type(el)))


@pytest.mark.datatypes
def test_variable_type_dict():
    a = {'first': 7, 'second': 5.6, 'third': 'wow'}
    print(a, type(a))
    for el in a.keys():
        print(a[el])
        check.equal(str(type(a[el])), "<class 'int'>",
                    "a[el] = {} and type of a[el] is {}".format(el, type(a[el])))


@pytest.mark.dict
def test_convert_to_dict():
    exp = {'a': 7}
    start = [('a', 7)]
    end = dict(start)
    check.not_equal(end, exp, 'end is: {}'.format(end))