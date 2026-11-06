# Changelog

Ghi lại các thay đổi đáng chú ý của AIMS-mini.

Định dạng theo [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
phiên bản theo [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-11-06

Bản phát hành Lab 05 (`release/lab05`).

### Added
- `Cart.sort_by_title()` và `Cart.sort_by_cost()` sắp xếp giỏ hàng
- `aims.search.search_by_category()` tìm đĩa theo thể loại
- CI bằng GitHub Actions: chạy test cho mọi PR vào `master` và `release/**`

### Fixed
- `search_by_title()` không phân biệt hoa thường (#28)

## [1.0.1] - 2026-11-06

Bản vá cho dòng 1.0.x (`release/lab04`).

### Fixed
- `search_by_title()` không phân biệt hoa thường: tìm "lion" ra "The Lion King" (#28)

## [1.0.0] - 2026-11-06

Phiên bản ổn định đầu tiên (Lab 04).

### Added
- `aims.__version__`; `main.py` in dòng `AIMS-mini v1.0.0` khi khởi động
- Tệp `CHANGELOG.md`

### Changed
- Coi API công khai là ổn định: `Cart`, `DigitalVideoDisc`, `search_by_title()`

## [0.3.0] - 2026-11-06

Bản nộp Lab 03 (`release/lab03`).

### Added
- `Cart.total_cost_with_discount(percent)` (#15)
- Thông báo giỏ hàng bằng tiếng Việt (#16)
- Test `tests/test_cart.py`, `tests/test_discount.py`

### Fixed
- Giỏ hàng nhận đĩa thứ 21 dù giới hạn là 20 (#19)
- `total_cost_with_discount()` trả về số tiền được giảm thay vì tổng sau giảm;
  kiểm tra `percent` trong khoảng 0–100 (#14)

### Removed
- Tiêu đề đĩa trong thông báo thêm đĩa (#17), đã revert ở #20

## [0.2.0] - 2026-11-06

Bản nộp Lab 02 (`release/lab02`).

### Added
- `Cart.print_cart()` in chi tiết giỏ hàng, giỏ trống thì in "The cart is empty" (#7)
- `aims.search.search_by_title()` (#4) và test (#11)
- Biểu đồ use case `docs/use-case.md` (#5)
- Pull request template (#2, #8)

### Fixed
- `main.py` crash `AttributeError: Cart has no attribute 'print_cart'` (#7)

## [0.1.0] - 2026-11-06

Bản nộp Lab 01 (`release/lab01`).

### Added
- `DigitalVideoDisc`, `Cart` và chương trình demo `main.py`

### Changed
- Chuyển mã nguồn vào package `aims/` (#1)

[Unreleased]: https://github.com/vuvangiang2006/it3180-202416475-aimss/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/vuvangiang2006/it3180-202416475-aimss/compare/v1.0.0...v1.1.0
[1.0.1]: https://github.com/vuvangiang2006/it3180-202416475-aimss/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/vuvangiang2006/it3180-202416475-aimss/compare/v0.3.0...v1.0.0
[0.3.0]: https://github.com/vuvangiang2006/it3180-202416475-aimss/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/vuvangiang2006/it3180-202416475-aimss/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/vuvangiang2006/it3180-202416475-aimss/releases/tag/v0.1.0
