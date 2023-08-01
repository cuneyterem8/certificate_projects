# Unit testing basics -----------------------------------------------------------------

# Import the pytest package
import pytest

# Import the function convert_to_int()
from preprocessing_helpers import convert_to_int

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
  # Complete the assert statement
  assert convert_to_int("2,081") == 2081

'''
!pytest test_convert_to_int.py


test_convert_to_int.py F                                                                                                                                                                                                                                                                                                                                                                                 [100%]

    def test_on_string_with_one_comma():
>     assert convert_to_int("2,081") == 2081
E     AssertionError: assert '2081' == 2081
E      +  where '2081' = convert_to_int('2,081')

test_convert_to_int.py:7: AssertionError

note: it expects to return integer but returns string instead
'''

# Intermediate unit testing -----------------------------------------------------------------

import pytest
from preprocessing_helpers import convert_to_int

def test_on_string_with_one_comma():
    test_argument = "2,081"
    expected = 2081
    actual = convert_to_int(test_argument)
    # Format the string with the actual return value
    message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)
    # Write the assert statement which prints message on failure
    assert actual is expected, message

'''
>       assert actual == expected, message
E       AssertionError: convert_to_int('2,081') should return the int 2081, but it actually returned None
E       assert None == 2081

test_convert_to_int.py:10: AssertionError
============================== 1 failed in 0.24s ===============================
'''


import numpy as np
import pytest
from as_numpy import get_data_as_numpy_array

def test_on_clean_file():
  expected = np.array([[2081.0, 314942.0],
                       [1059.0, 186606.0],
  					   [1148.0, 206186.0]
                       ]
                      )
  actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
  message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
  # Complete the assert statement
  assert actual == pytest.approx(expected), message

'''
compare floats with approx method
'''


def test_on_six_rows():
    example_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                 [1148.0, 206186.0], [1506.0, 248419.0],
                                 [1210.0, 214114.0], [1697.0, 277794.0]]
                                )
    # Fill in with training array's expected number of rows
    expected_training_array_num_rows = 4
    # Fill in with testing array's expected number of rows
    expected_testing_array_num_rows = 2
    actual = split_into_training_and_testing_sets(example_argument)
    # Write the assert statement checking training array's number of rows
    assert actual[0].shape[0] == expected_training_array_num_rows, "The actual number of rows in the training array is not {}".format(expected_training_array_num_rows)
    # Write the assert statement checking testing array's number of rows
    assert actual[1].shape[0] == expected_testing_array_num_rows, "The actual number of rows in the testing array is not {}".format(expected_testing_array_num_rows)

''''''

import pytest

with pytest.raises(ValueError) as exc_info:
    raise ValueError("Silence me!")
# Check if the raised ValueError contains the correct message
assert exc_info.match("Silence me!")


''''''


import numpy as np
import pytest
from train import split_into_training_and_testing_sets

def test_on_one_row():
    test_argument = np.array([[1382.0, 390167.0]])
    # Store information about raised ValueError in exc_info
    with pytest.raises(ValueError) as exc_info:
      split_into_training_and_testing_sets(test_argument)
    expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
    # Check if the raised ValueError contains the correct message
    assert exc_info.match(expected_error_msg)

''''''

def test_with_no_comma():
    actual = convert_to_int("756")
    # Complete the assert statement
    assert 756 == actual, "Expected: 756, Actual: {0}".format(actual)
    
def test_with_one_comma():
    actual = convert_to_int("2,081")
    # Complete the assert statement
    assert 2081 == actual, "Expected: 2081, Actual: {0}".format(actual)
    
def test_with_two_commas():
    actual = convert_to_int("1,034,891")
    # Complete the assert statement
    assert 1034891 == actual, "Expected: 1034891, Actual: {0}".format(actual)

''''''

# Test Organization and Execution -----------------------------------------------------------------

import pytest
import numpy as np

from models.train import split_into_training_and_testing_sets

# Declare the test class
class TestSplitIntoTrainingAndTestingSets(object):
    # Fill in with the correct mandatory argument
    def test_on_one_rows(self):
        test_argument = np.array([[1382.0, 390167.0]])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
        expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
        assert exc_info.match(expected_error_msg)

'''
!pytest tests/models/test_train.py::TestSplitIntoTrainingAndTestingSets

!pytest tests/models/test_train.py::TestSplitIntoTrainingAndTestingSets::test_on_six_rows
'''


# Mark the whole test class as "expected to fail"
@pytest.mark.xfail(reason="Using TDD, model_test() has not yet been implemented")
class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        message = "model_test({0}) should return {1}, but it actually returned {2}".format(test_input, expected, actual)
        assert actual == pytest.approx(expected), message
        
    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)

'''
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
>       actual = model_test(test_input, 2.0, 1.0)
E       NameError: name 'model_test' is not defined

models/test_train.py:9: NameError



    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
>           model_test(test_input, 1.0, 1.0)
E           NameError: name 'model_test' is not defined
'''


# Import the sys module
import sys

class TestGetDataAsNumpyArray(object):
    # Add a reason for skipping the test
    @pytest.mark.skipif(sys.version_info > (2, 7), reason="Works only on Python 2.7 or lower")
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
        actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
        assert actual == pytest.approx(expected), message

'''
features/test_as_numpy.py F                                              [100%]

=================================== FAILURES ===================================
__________________ TestGetDataAsNumpyArray.test_on_clean_file __________________

self = <features.test_as_numpy.TestGetDataAsNumpyArray object at 0x7f10e7b55fd0>

    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
>       actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)

features/test_as_numpy.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

clean_data_file_path = 'example_clean_data.txt', num_columns = 2

    def get_data_as_numpy_array(clean_data_file_path, num_columns):
        result = np.empty((0, num_columns))
        with open(clean_data_file_path, "r") as f:
            rows = f.readlines()
>           for row_num in xrange(len(rows)):
E           NameError: name 'xrange' is not defined

features/as_numpy.py:9: NameError
============================== 1 failed in 0.32s ===============================
'''


'''
!pytest -rx (failure)
!pytest -rs (skipped)
!pytest -rsx (both)


data/test_preprocessing_helpers.py .............                         [ 68%]
features/test_as_numpy.py s                                              [ 73%]
models/test_train.py ..xxx                                               [100%]

=========================== short test summary info ============================
XFAIL models/test_train.py::TestTrainModel::test_on_linear_data
  Using TDD, train_model() has not yet been implemented
XFAIL models/test_train.py::TestModelTest::test_on_linear_data
  Using TDD, model_test() has not yet been implemented
XFAIL models/test_train.py::TestModelTest::test_on_one_dimensional_array
  Using TDD, model_test() has not yet been implemented
=================== 15 passed, 1 skipped, 3 xfailed in 0.30s ===================

'''

# Testing Models, Plots and Much More -----------------------------------------------------------------

# Add a decorator to make this function a fixture
@pytest.fixture
def clean_data_file():
    file_path = "clean_data_file.txt"
    with open(file_path, "w") as f:
        f.write("201\t305671\n7892\t298140\n501\t738293\n")
    yield file_path
    os.remove(file_path)
    
# Pass the correct argument so that the test can use the fixture
def test_on_clean_file(clean_data_file):
    expected = np.array([[201.0, 305671.0], [7892.0, 298140.0], [501.0, 738293.0]])
    # Pass the clean data file path yielded by the fixture as the first argument
    actual = get_data_as_numpy_array(clean_data_file, 2)
    assert actual == pytest.approx(expected), "Expected: {0}, Actual: {1}".format(expected, actual) 

''''''

@pytest.fixture
def empty_file():
    # Assign the file path "empty.txt" to the variable
    file_path = "empty.txt"
    open(file_path, "w").close()
    # Yield the variable file_path
    yield file_path
    # Remove the file in the teardown
    os.remove(file_path)
    
def test_on_empty_file(self, empty_file):
    expected = np.empty((0, 2))
    actual = get_data_as_numpy_array(empty_file, 2)
    assert actual == pytest.approx(expected), "Expected: {0}, Actual: {1}".format(expected, actual)

''''''

# mocking: convert convert_to_int into bug_free version to avoid version dependency failure
# Define a function convert_to_int_bug_free
def convert_to_int_bug_free(comma_separated_integer_string):
    # Assign to the dictionary holding the correct return values
    return_values = {"1,801": 1801,
                     "201,411": 201411,
                     "2,002": 2002,
                     "333,209": 333209,
                     "1990": None,
                     "782,911": 782911,
                     "1,285": 1285,
                     "389129": None,
                     }
    # Return the correct result using the dictionary return_values
    return return_values[comma_separated_integer_string]


# Add the correct argument to use the mocking fixture in this test
def test_on_raw_data(self, raw_and_clean_data_file, mocker):
    raw_path, clean_path = raw_and_clean_data_file
    # Replace the dependency with the bug-free mock
    convert_to_int_mock = mocker.patch("data.preprocessing_helpers.convert_to_int",
                                       side_effect=convert_to_int_bug_free)
    preprocess(raw_path, clean_path)
    # Check if preprocess() called the dependency correctly
    assert convert_to_int_mock.call_args_list == [call("1,801"), call("201,411"), call("2,002"), call("333,209"), call("1990"), call("782,911"), call("1,285"), call("389129")]
    with open(clean_path, "r") as f:
        lines = f.readlines()
    first_line = lines[0]
    assert first_line == "1801\\t201411\\n"
    second_line = lines[1]
    assert second_line == "2002\\t333209\\n" 

'''
def test_with_one_comma(self):
        test_argument = "2,081"
        expected = 2081
        actual = convert_to_int(test_argument)
>       assert actual == expected, "Expected: 2081, Actual: {0}".format(actual)
E       AssertionError: Expected: 2081, Actual: None
E       assert None == 2081

data/test_preprocessing_helpers.py:48: AssertionError
____________________________________________________________________________________________________________________________________________________________________________________ TestConvertToInt.test_with_two_commas _____________________________________________________________________________________________________________________________________________________________________________________

self = <data.test_preprocessing_helpers.TestConvertToInt object at 0x7f2f59b53be0>

    def test_with_two_commas(self):
        test_argument = "1,034,891"
        expected = 1034891
        actual = convert_to_int(test_argument)
>       assert actual == expected, "Expected: 1034891, Actual: {0}".format(actual)
E       AssertionError: Expected: 1034891, Actual: None
E       assert None == 1034891
'''


import numpy as np
import pytest
from models.train import model_test

def test_on_perfect_fit():
    # Assign to a NumPy array containing a linear testing set
    test_argument = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
    # Fill in with the expected value of r^2 in the case of perfect fit
    expected = 1.0
    # Fill in with the slope and intercept of the model
    # 5.0 - 3.0 / 2.0 - 1.0 = 2, y = mx, then 3.0 = 2.0 x 1.0 + intercept = 1.0
    actual = model_test(test_argument, slope=2.0, intercept=1.0)
    # Complete the assert statement
    assert actual == pytest.approx(expected), "Expected: {0}, Actual: {1}".format(expected, actual)

''''''

def test_on_circular_data(self):
    theta = pi/4.0
    # Assign to a NumPy array holding the circular testing data
    test_argument = np.array([  [1.0, 0.0], [cos(theta), sin(theta)], 
                                [0.0, 1.0], [cos(3 * theta), sin(3 * theta)], 
                                [-1.0, 0.0], [cos(5 * theta), sin(5 * theta)], 
                                [0.0, -1.0], [cos(7 * theta), sin(7 * theta)]]
                             )
    # Fill in with the slope and intercept of the straight line
    actual = model_test(test_argument, slope=0.0, intercept=0.0)
    # Complete the assert statement
    assert actual == pytest.approx(0.0)

''''''

import pytest
import numpy as np

from visualization.plots import get_plot_for_best_fit_line


class TestGetPlotForBestFitLine(object):
    @pytest.mark.mpl_image_compare
    def test_plot_for_linear_data(self):
        slope = 2.0
        intercept = 1.0
        x_array = np.array([1.0, 2.0, 3.0])
        y_array = np.array([3.0, 5.0, 7.0])
        title = "Test plot for linear data"
        return get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title)

'''
pytest -k "TestGetPlotForBestFitLine" --mpl

To ensure plots are compared to the baseline, use --mpl
'''