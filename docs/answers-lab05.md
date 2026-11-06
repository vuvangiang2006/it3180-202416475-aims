# Lab 05 – Câu hỏi thảo luận

Sinh viên: Vũ Văn Giang – MSSV 202416475

## 1. Vì sao không merge cả nhánh hotfix vào `master`?

Nhánh `hotfix/search-case-insensitive` rẽ từ `release/lab04` (dòng 1.0.x) và có đúng
hai commit với vai trò khác nhau:

1. **Commit sửa lỗi** (`search.py` + test). Mọi dòng phiên bản bị ảnh hưởng đều cần
   commit này.
2. **Commit nâng phiên bản** (`__version__ = "1.0.1"` + mục `[1.0.1]` của
   CHANGELOG). Commit này chỉ đúng cho dòng 1.0.x.

`master` lúc đó đã là `1.1.0`. Merge cả nhánh sẽ mang commit 2 vào, khiến
`__init__.py` xung đột (GitHub báo *Can't automatically merge*). Kể cả khi sửa tay
được thì `master` cũng bị kéo theo lịch sử riêng của dòng cũ. Vì vậy ta chỉ lấy
đúng commit 1 bằng `git cherry-pick -x <FIX_SHA>`. Tùy chọn `-x` thêm dòng
`(cherry picked from commit …)` để truy vết ngược về bản sửa gốc.

Đó cũng là lý do commit sửa lỗi phải **tách riêng** khỏi commit nâng số phiên bản.

## 2. Vì sao ở Phần A chưa gắn tag `v1.1.0`?

Tag đã đẩy lên là **bất biến**: không di chuyển, không xóa. Ở Phần A, `release/lab05`
mới tạo và chưa giao cho ai. Lỗi phát hiện ở Phần B ảnh hưởng cả dòng 1.1, nên ta
cherry-pick bản sửa vào `release/lab05` trước, rồi mới gắn `v1.1.0`. Nhờ vậy 1.1.0
phát hành ra đã có bản sửa.

Nếu đã lỡ gắn và push `v1.1.0` thì không được dời tag. Bản sửa khi đó phải ra
**`v1.1.1`** (tăng PATCH), giống cách `v1.0.0` → `v1.0.1`.

## 3. *Upstream first* so với *release first*

| | Upstream first (Release Flow của Microsoft) | Release first (cách làm trong bài) |
|---|---|---|
| Thứ tự | Sửa trên `master` trước qua PR, rồi cherry-pick xuống `release/*` | Sửa trên `release/*` đã phát hành trước, rồi cherry-pick lên `master` và các dòng khác |
| Ưu điểm | Không bao giờ quên sửa ở `master`, nên lỗi không quay lại ở bản sau; bản sửa được kiểm thử trên dòng phát triển chính | Sửa và test đúng trên mã người dùng đang chạy; ra bản vá nhanh khi khẩn cấp; hợp khi release đã khác xa `master` |
| Nhược điểm | Bản vá cho người dùng phải chờ PR vào `master`; nếu `master` đã đổi nhiều thì cherry-pick xuống dễ xung đột | Dễ quên lan truyền lên `master` hoặc sang dòng khác, gây regression; phải kiểm toán đa phiên bản (Phần F) |

## 4. Nếu quên đưa bản sửa sang `release/lab05`, lệnh nào ở Phần F phát hiện?

- `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"` chỉ trả về
  **1** bản cherry-pick (trên `master`) thay vì 2.
- `git cherry -v origin/release/lab05 origin/release/lab04` hiện commit sửa lỗi với
  dấu **`+`**, nghĩa là `release/lab05` chưa có bản tương đương. Trên `master`, dòng
  này mang dấu `-`.
- Vòng lặp kiểm tra hành vi sẽ in `0` cho `v1.1.0` (tìm "lion" không ra *The Lion
  King*), còn `v1.0.1` và `master` in `1`.

`git tag --contains <FIX_SHA>` thì **không đủ**. Cherry-pick tạo commit mới với SHA
khác, nên lệnh này chỉ thấy `v1.0.1`, chứa chính commit gốc, dù các dòng khác đã
có bản sửa hay chưa.
