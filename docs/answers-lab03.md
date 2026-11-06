# Lab 03 – Câu hỏi thảo luận

Sinh viên: Vũ Văn Giang – MSSV 202416475

## 1. Merge base là gì?

Merge base của hai nhánh là **commit tổ tiên chung gần nhất**, tức điểm cuối cùng
mà cả hai nhánh còn giống nhau trước khi rẽ đôi. Xem bằng `git merge-base A B`.

Trong bài, Dev 1 (`feature/vietnamese-messages`) và Dev 2
(`feature/show-added-title`) cùng tách từ `master` tại `7fa29be` (merge của PR #10):

```
$ git merge-base origin/feature/vietnamese-messages origin/feature/show-added-title
7fa29be...
```

Git merge theo kiểu **three-way merge**, so 3 phiên bản: base, nhánh đích (ours) và
nhánh đem vào (theirs). Với mỗi đoạn mã:

- chỉ một bên thay đổi so với base → Git tự lấy thay đổi đó;
- cả hai bên đổi **cùng một đoạn** theo hai cách khác nhau → **xung đột**, người
  làm phải tự quyết.

Tại base, dòng in là `print("The disc has been added")`. Dev 1 đổi thành câu tiếng
Việt, Dev 2 đổi thành f-string có tiêu đề đĩa. Vì vậy PR thứ hai báo *This branch
has conflicts*. Cách giải quyết là kết hợp ý đồ của cả hai:
`print(f"Đã thêm đĩa '{dvd.title}' vào giỏ hàng")`, rồi chạy lại test trước khi
commit merge.

Merge base cũng là lý do PR bugfix ở Phần B phải chọn base `feature/discount`. Nếu
để base `master`, PR sẽ hiện cả commit của nhánh tính năng, vì các commit đó chưa có
từ merge base trở đi trên `master`.

## 2. Vì sao `master`/`release/*` phải dùng `revert` mà không dùng `reset`?

| | `reset` | `revert` |
|---|---|---|
| Cơ chế | Dời con trỏ nhánh về commit cũ | Tạo commit mới đảo ngược thay đổi |
| Viết lại lịch sử | Có, các commit phía sau biến mất khỏi nhánh | Không, lịch sử cũ giữ nguyên |
| Đưa lên remote | Phải `push --force` | Push bình thường, qua PR |

`master` và `release/*` là lịch sử **đã chia sẻ**: người khác đã pull, nhánh khác đã
tách ra, và tag/baseline trỏ vào đó. Nếu reset rồi force push:

- clone của người khác lệch với remote, và lần pull sau sẽ kéo commit "đã xóa" quay
  lại;
- mất dấu vết kiểm toán, không còn biết thay đổi đã từng vào rồi bị gỡ ra vì sao;
- với `release/*`, baseline đã giao bị đổi ngầm, trái nguyên tắc quản lý cấu hình.

Hơn nữa, cả hai loại nhánh đều được bảo vệ, không cho force push, nên chỉ có thể sửa
bằng PR. Hoàn tác đúng cách là tạo nhánh `bugfix/revert-show-added-title` rồi chạy
`git revert -m 1 <sha-merge-commit>`. Tham số `-m 1` chọn parent 1 (phía `master`)
làm mainline, nghĩa là giữ `master` và gỡ phần do nhánh tính năng mang vào. Sau đó
mở PR, nên chính việc hoàn tác cũng được review.

`reset`, `commit --amend` và `rebase` chỉ dùng cho commit **chưa push**, như khi tôi
luyện tập trên nhánh nháp `topic/undo-practice`. Commit "mất" sau `reset --hard`
vẫn tìm lại được bằng `git reflog`.
