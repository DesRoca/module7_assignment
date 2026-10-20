import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import is_valid_url, create_directory, generate_qr_code

def test_is_valid_url_success():
    """Test that valid URLs return True."""
    assert is_valid_url("https://www.google.com") is True
    assert is_valid_url("https://www.njit.edu") is True

def test_is_valid_url_failure():
    """Test that invalid URLs return False."""
    assert is_valid_url("not_a_url") is False
    assert is_valid_url("htp:/invalid-url") is False

def test_create_directory(tmp_path):
    """Test that directories are created successfully using a temporary path."""
    test_dir = tmp_path / "test_qr_codes"
    create_directory(test_dir)
    assert test_dir.exists()
    assert test_dir.is_dir()

def test_generate_qr_code(tmp_path):
    """Test that the QR code image file is successfully generated and saved."""
    test_dir = tmp_path / "qr_output"
    test_dir.mkdir()
    file_path = test_dir / "test_qr.png"
    
    generate_qr_code("https://www.njit.edu", file_path, fill_color="red", back_color="white")
    
    assert file_path.exists()
    assert file_path.stat().st_size > 0