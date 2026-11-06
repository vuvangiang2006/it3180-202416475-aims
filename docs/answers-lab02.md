# Lab 02 – Câu hỏi thảo luận

Sinh viên: Vũ Văn Giang – MSSV 202416475

## 1. Vì sao phải đồng bộ `master` vào nhánh trước khi gửi PR?

Nhánh `topic/search-tests` của Dev 2 được tạo khi `master` vẫn còn lỗi `print_cart`.
Trong lúc Dev 2 viết test, PR #7 (sửa `print_cart`) đã được merge, nên
`origin/master` đã đi trước nhánh của Dev 2.

Nếu gửi PR ngay, thứ được review là "mã của Dev 2 trên nền `master` cũ". Còn thứ
thực sự vào `master` là "mã của Dev 2 + bản sửa của PR #7", và tổ hợp này chưa ai
chạy thử. Chạy `git fetch` rồi `git merge origin/master` trên nhánh của mình mang lại
ba lợi ích:

- xung đột (nếu có) được giải quyết ở nhánh riêng, `master` không bị ảnh hưởng;
- có thể chạy lại `python main.py` và bộ test trên đúng kết quả tích hợp, nên thứ
  được duyệt chính là thứ được tích hợp;
- tab *Files changed* của PR chỉ còn phần thay đổi thật so với `master` mới.

Bài học thực tế trong repo này: lần làm trước, các PR được merge mà không chạy lại
chương trình sau khi tích hợp, nên `master` và `release/lab02` bị crash.

## 2. Khi nào **không** được rebase?

`rebase` tạo lại từng commit với mã SHA mới, tức là viết lại lịch sử. Vì vậy:

- không rebase những commit **đã chia sẻ** mà người khác đã pull hoặc đã tách nhánh
  từ đó. Bản clone của họ sẽ lệch với remote, và commit cũ có thể quay lại hoặc bị
  mất;
- tuyệt đối không rebase `master` và `release/*`. Đây là lịch sử chung và baseline,
  được bảo vệ, cấm force push;
- không rebase khi muốn giữ dấu vết merge để sau này revert cả tính năng bằng
  `git revert -m 1`.

Chỉ rebase nhánh **cá nhân** chưa ai dùng. Nếu nhánh đó đã push thì đẩy lại bằng
`git push --force-with-lease`, không dùng `--force`, để không đè mất commit của
người khác.

## 3. `feature/*` khác `topic/*` ra sao?

| | `feature/*` | `topic/*` |
|---|---|---|
| Dùng cho | Tính năng mới, làm thay đổi hành vi chương trình | Việc không phải tính năng: tài liệu, cấu hình, quy trình, test, công cụ |
| Ví dụ trong repo | `feature/cart-print`, `feature/search-by-title` | `topic/pr-template`, `topic/pr-template-format`, `topic/search-tests`, `topic/answers-lab02` |
| Loại commit thường gặp | `feat:` | `docs:`, `test:`, `chore:`, `ci:` |
| Ảnh hưởng phiên bản (SemVer) | Thường tăng MINOR | Thường không đổi phiên bản |

Hai loại đều tạo từ `master`, merge lại vào `master` qua PR và xóa sau khi merge.
Lỗi thì dùng `bugfix/*`, như `bugfix/print-cart-missing`. Tên nhánh cho người
review biết ngay mục đích của nhánh.

## 4. So sánh 3 kiểu merge trên lịch sử repo

| | Merge commit – PR #7 `bugfix/print-cart-missing` | Squash – PR #11 `topic/search-tests` | Rebase – PR #8 `topic/pr-template-format` |
|---|---|---|---|
| Giữ commit chi tiết | Có (các commit gốc + 1 merge commit) | Không, gộp thành 1 commit `(#11)` | Có, nhưng SHA mới |
| Lịch sử tuyến tính | Không | Có | Có |
| Revert cả thay đổi | 1 lệnh `git revert -m 1 <merge>` | 1 lệnh `git revert <sha>` | Phải revert từng commit |
| `git branch -d` sau khi merge | Được | Báo *not fully merged*, cần `-D` sau khi xác nhận PR đã merge | Như squash |

PR #7 cũng là PR đi đủ vòng review: comment trên dòng `def print_cart` ("giỏ trống
thì in 'The cart is empty'"), sửa trên cùng nhánh, Resolve conversation rồi mới
merge.
