"""
Unit and regression test for the geometry_analysis package.
"""

# Import package, test suite, and other packages as needed
import geometry_analysis
import pytest
import sys

import numpy as np
import qcportal as ptl

@pytest.fixture
def water_molecule():
    name = "water"
    symbols = ["H", "O", "H"]
    coordinates = np.array([[2, 0, 0], [0,0,0], [-2, 0, 0]])

    water = geometry_analysis.Molecule(name, symbols, coordinates)

    return water

@pytest.fixture
def butane_molecule():
    client = ptl.FractalClient()
    butane_molecules = client.query_molecules(id=['61139', '70659'])

    yield butane_molecules

def test_geometry_analysis_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "geometry_analysis" in sys.modules

def test_create_molecule(water_molecule):

    name = "water"
    symbols = ["H", "O", "H"]
    coordinates = np.array([[2, 0, 0], [0,0,0], [-2, 0, 0]])

    assert water_molecule.name == name
    assert water_molecule.symbols == symbols
    assert np.array_equal(coordinates, water_molecule.coordinates)

def test_create_failure():

    name = 25
    symbols = ["H", "O", "H"]
    coordinates = np.array([[1.43, 0, 0.83], [0,0,0], [-1.43, 0, 0.83]])

    with pytest.raises(TypeError):
        water_molecule = geometry_analysis.Molecule(name, symbols, coordinates)

def test_molecule_set_coordinates(water_molecule):
    """Test that our setter for coordinates works."""

    num_bonds = len(water_molecule.bonds)
    assert(len(water_molecule.bonds.keys()) == 2)
    
    new_coordinates = np.array([[5, 0, 0], [0,0,0], [0, 1, 0]])
    water_molecule.coordinates = new_coordinates
    assert(len(water_molecule.bonds.keys()) == 1)

    assert np.array_equal(new_coordinates, water_molecule.coordinates)

def test_butane_bonds(butane_molecule):

    my_molecule = geometry_analysis.Molecule("butane", butane_molecule[0].symbols, butane_molecule[0].geometry )

    known_bonds = butane_molecule[0].connectivity

    calculated_bonds = my_molecule.bonds
    calculated_keys = list(my_molecule.bonds.keys())

    assert len(known_bonds) == len(calculated_bonds)

    for i in range(len(known_bonds)):
        assert known_bonds[i][:2] == calculated_keys[i]

def test_butane_distance(butane_molecule):

    coordinates = butane_molecule[0].geometry

    calculated_distance = geometry_analysis.calculate_distance(coordinates[0], coordinates[1])

    expected_distance = butane_molecule[0].measure([0, 1])


