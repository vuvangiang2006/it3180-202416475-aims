"""Các hàm tìm kiếm đĩa DVD trong danh sách."""


def search_by_title(items, keyword):
    """Trả về các đĩa có tiêu đề chứa keyword."""
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
