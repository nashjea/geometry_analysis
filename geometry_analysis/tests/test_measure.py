"""
Tests
"""

# Import package, test suite, and other packages as needed
import geometry_analysis
import pytest
import sys

import numpy as np

def test_calculate_distance():
    
    expected_distance = np.sqrt(2.)

    r1 = np.array([0,0,-1])
    r2 = np.array([0, 1, 0 ])

    measured_distance = geometry_analysis.calculate_distance(r1, r2)

    assert measured_distance == expected_distance

def test_calculate_angle():
    r1 = np.array([1,0,0])
    r2 = np.array([0,0,0])
    r3 = np.array([0,1,0])

    expected_value = 90
    calculated_value = geometry_analysis.calculate_angle(r1, r2, r3, degrees=True)

    assert expected_value == calculated_value
