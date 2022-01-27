import numpy
import pytest
from RIAssigner.compute import Kovats

from tests.fixtures import (indexed_data, invalid_rt_data,
                                 non_indexed_data, queries, reference_alkanes)
from tests.fixtures.mocks import DataStub


def test_compute_ri_basic_case(non_indexed_data, indexed_data):
    method = Kovats()

    expected = [741.525424,  760.169492,  769.491525,  932.420091,  965.296804,
                986.757991, 1078.823529, 1157.142857]
    actual = method.compute(non_indexed_data, indexed_data)

    numpy.testing.assert_array_almost_equal(actual, expected)


def test_invalid_rt_has_none_ri(invalid_rt_data, indexed_data):
    method = Kovats()

    expected = [None, None, None, 741.5254237288136]
    actual = method.compute(invalid_rt_data, indexed_data)

    numpy.testing.assert_array_equal(actual, expected)


@pytest.mark.method('kovats')
def test_ref_queries(reference_alkanes, queries):
    method = Kovats()

    data, expected = queries
    actual = method.compute(data, reference_alkanes)
    numpy.testing.assert_array_almost_equal(actual, expected)


def test_missing_alkane():
    ref = DataStub([5.0, 7.0], [1000, 1200])
    query = DataStub([6.0], [None])
    expected = [1100]

    actual = Kovats().compute(query, ref)
    numpy.testing.assert_array_almost_equal(actual, expected)
