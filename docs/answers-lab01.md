# Lab 01 – Câu hỏi thảo luận

Sinh viên: Vũ Văn Giang – MSSV 202416475

## Cấu hình `--global` nằm ở đâu, khác `--local` thế nào?

`git config --global` ghi vào tệp của tài khoản người dùng: `~/.gitconfig` trên
Linux/macOS, `C:\Users\<tên>\.gitconfig` trên Windows. Giá trị này áp dụng cho
mọi kho trên máy.

`git config --local` ghi vào `.git/config` của riêng kho đang đứng, nên chỉ có tác
dụng trong kho đó và ghi đè giá trị `--global` cùng tên. Thứ tự ưu tiên là
`--local` > `--global` > `--system`. Muốn biết một giá trị lấy từ đâu thì chạy
`git config --list --show-origin`.

## Vì sao dùng `git mv` mà không đổi tên bằng Explorer/`mv`?

Git không lưu sự kiện "đổi tên". Mỗi commit là một ảnh chụp toàn bộ cây thư mục, và
khi hiển thị lịch sử Git tự **phát hiện** đổi tên bằng cách so nội dung tệp bị xóa
với tệp mới xuất hiện.

`git mv cart.py aims/cart.py` làm ba việc trong một lệnh: đổi tên trên đĩa, stage
việc xóa tên cũ và stage tên mới. Nếu đổi bằng hệ điều hành thì phải tự
`git add`/`git rm` cả hai phía, và rất dễ quên phía xóa. Khi đó repo còn cả
`cart.py` lẫn `aims/cart.py`.

Vì Git dựa vào độ giống nội dung, commit đổi tên nên giữ nguyên nội dung tệp. Trong
PR #1 của tôi, tab *Files changed* hiện `renamed cart.py → aims/cart.py` và
`git log --follow -- aims/cart.py` vẫn lần được về commit tạo `cart.py` ở thư mục
gốc.

## `release/lab01` có phải baseline không?

Có, theo nghĩa đây là phiên bản đã được chốt để nộp. Nhánh tạo từ `master` ngay sau
khi PR #1 merge, mọi thay đổi trước đó đều qua PR, và người chấm lấy bản mới nhất
trên nhánh này.

Nhưng nhánh chỉ là con trỏ có thể dời đi. Ví dụ, nhánh này được cập nhật qua PR
cherry-pick để bổ sung README và tệp trả lời này. Định danh **bất biến** cho
baseline là annotated tag, ở Lab 04 sẽ gắn `v0.1.0` vào `origin/release/lab01`.
Nhánh release là dòng bảo trì, còn tag mới là "ảnh chụp không đổi".

## Vì sao không commit thẳng lên `master` dù làm một mình?

- `master` là cấu hình tích hợp, phải luôn chạy được. Trong repo của tôi, một thay đổi
  đi vào `master` mà không được kiểm tra kỹ đã khiến `main.py` crash
  (`Cart has no attribute 'print_cart'`). Đi qua PR có mô tả "Kiểm thử" buộc mình
  chạy chương trình trước khi merge.
- PR là **yêu cầu thay đổi** có ghi lại lý do, nội dung, người duyệt và thời điểm
  tích hợp. Commit thẳng thì mất hết dấu vết đó.
- Nếu một thay đổi sai, có thể bỏ nhánh hoặc revert cả PR mà không làm bẩn lịch sử
  chung.
- Từ Lab 02, `master` được bảo vệ ("Do not allow bypassing"): push thẳng bị từ chối
  với `GH006`. Làm một mình thì đặt Require approvals = 0 nhưng vẫn phải qua PR, nên
  quy trình giống hệt khi làm nhóm.
