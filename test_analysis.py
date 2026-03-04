"""Unit test for the analysis module"""

import datetime
import numpy as np
from floodsystem.analysis import polyfit


def test_polyfit_linear():
    """Test polynomial fitting with linear data"""
    
    # Create simple linear data (y = x)
    base_date = datetime.datetime(2023, 1, 1)
    dates = [base_date + datetime.timedelta(days=i) for i in range(5)]
    levels = [0.0, 1.0, 2.0, 3.0, 4.0]
    
    poly, d0 = polyfit(dates, levels, 1)
    
    # Check that poly is a polynomial object
    assert poly is not None
    
    # Check that d0 is the first date in numeric format
    assert d0 is not None
    
    # Test that polynomial evaluates reasonably
    # For linear fit of y=x, at position 0 (first point) should be ~1.0
    assert isinstance(poly, np.poly1d)
    # Compare coefficients with tolerance for floating-point accuracy
    assert np.allclose(poly.c, [1, 0], atol=1e-5)  # Should be y = 1*x + 0


def test_polyfit_quadratic():
    """Test polynomial fitting with quadratic data"""
    
    # Create quadratic data (y = x^2)
    base_date = datetime.datetime(2023, 1, 1)
    dates = [base_date + datetime.timedelta(days=i) for i in range(5)]
    levels = [0.0, 1.0, 4.0, 9.0, 16.0]
    
    poly, d0 = polyfit(dates, levels, 2)
    
    assert poly is not None
    assert d0 is not None
    assert isinstance(poly, np.poly1d)
    # Compare coefficients with tolerance for floating-point accuracy
    assert np.allclose(poly.c, [1, 0, 0], atol=1e-5)  # Should be y = 1*x^2 + 0*x + 0


def test_polyfit_constant():
    """Test polynomial fitting with constant data"""
    
    # Create constant data (y = 3.0)
    base_date = datetime.datetime(2023, 1, 1)
    dates = [base_date + datetime.timedelta(days=i) for i in range(5)]
    levels = [3.0, 3.0, 3.0, 3.0, 3.0]
    
    poly, d0 = polyfit(dates, levels, 0)
    
    assert poly is not None
    assert d0 is not None
    assert isinstance(poly, np.poly1d)
    # Compare coefficients with tolerance for floating-point accuracy
    assert np.allclose(poly.c, [3.0], atol=1e-5)  # Should be y = 3.0


def test_polyfit_single_point():
    """Test polynomial fitting with minimal data"""
    
    base_date = datetime.datetime(2023, 1, 1)
    dates = [base_date]
    levels = [5.0]
    
    poly, d0 = polyfit(dates, levels, 0)
    
    # Should still return a valid polynomial
    assert poly is not None
    assert d0 is not None


def test_polyfit_return_types():
    """Test that polyfit returns correct types"""
    
    base_date = datetime.datetime(2023, 1, 1)
    dates = [base_date + datetime.timedelta(days=i) for i in range(3)]
    levels = [1.0, 2.0, 3.0]
    
    result = polyfit(dates, levels, 1)
    
    # Should return a tuple
    assert isinstance(result, tuple)
    assert len(result) == 2
    
    poly, d0 = result
    
    # poly should be numpy poly1d object
    assert isinstance(poly, np.poly1d)
    
    # d0 should be numeric (float)
    assert isinstance(d0, (float, np.floating))
