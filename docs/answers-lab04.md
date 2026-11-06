# Lab 04 – Câu hỏi thảo luận

Sinh viên: Vũ Văn Giang – MSSV 202416475

## 1. Vì sao chuẩn bị phát hành trên `master`, không sửa trên nhánh release?

Nhánh `release/lab04` phải là **bản sao chính xác của `master` tại thời điểm phát
hành**. Nếu tạo nhánh trước rồi mới nâng `__version__` và viết CHANGELOG trên nhánh
đó, `release/lab04` sẽ có những commit mà `master` không có.

Theo Release Flow, nhánh release không bao giờ được merge ngược về `master`. Các
commit đó sẽ kẹt lại trên dòng 1.0: `master` không có CHANGELOG 1.0.0, và lần chuẩn
bị 1.1.0 phải làm lại từ đầu.

Làm qua `topic/prepare-release-1.0.0` → PR → `master` thì:

- thay đổi chuẩn bị phát hành được review như mọi thay đổi khác;
- `release/lab04` tạo ra **trùng khớp** `master`, nên `git log master..release/lab04`
  rỗng;
- tag `v1.0.0` trỏ đúng vào commit đã được duyệt.

Trên nhánh release chỉ còn lại những sửa đổi bắt buộc *sau* khi phát hành (hotfix
ở Lab 05).

## 2. Vì sao `release/*` không merge vào `master`? So với GitFlow

Trong Release Flow, `master` là **nguồn sự thật duy nhất**. Mọi thay đổi vào `master`
trước, còn `release/*` chỉ **rẽ ra** từ đó. Một nhánh release chỉ chứa:

- những gì `master` đã có lúc rẽ nhánh, nên không cần merge lại;
- những thay đổi chỉ đúng cho dòng phiên bản đó, ví dụ commit nâng số `1.0.1`. Commit
  này không được về `master`, vì `master` đã sang `1.1.0`. Bản sửa lỗi được lan
  truyền có chọn lọc bằng `git cherry-pick -x`.

Nếu merge `release/lab04` vào `master`, số phiên bản và CHANGELOG của dòng cũ sẽ
xung đột với dòng mới, và lịch sử bị rối vì các đường merge chéo.

| | Release Flow (học phần) | GitFlow |
|---|---|---|
| Nhánh tích hợp | `master` | `develop` |
| Nhánh release tạo từ | `master` | `develop` |
| Sau khi phát hành | Giữ `release/*` làm dòng bảo trì, **không** merge về | Merge vào cả `main` và `develop`, rồi xóa |
| Hotfix | Từ `release/*`, lan truyền bằng cherry-pick | Từ `main`, merge vào `main` + `develop` |
| Phù hợp | Nhiều dòng phát hành chạy song song | Phát hành theo đợt, mỗi lúc một bản |

## 3. Vì sao lên `1.0.0` mà không phải `0.4.0`?

Theo SemVer, `0.y.z` là giai đoạn phát triển ban đầu: API có thể đổi bất cứ lúc nào
và chưa có cam kết tương thích. Các bản `v0.1.0`…`v0.3.0` của Lab 01–03 đúng như vậy.
Repo của tôi còn từng có bản `release/lab02` bị crash, phải sửa lại.

Lab 04 là bản **phát hành chính thức đầu tiên**, có CHANGELOG, GitHub Release, nhánh
release được bảo vệ và bắt đầu bảo trì. SemVer khuyên dùng `1.0.0` khi phần mềm đã
được dùng thật và có API công khai ổn định.

Từ `1.0.0`, số phiên bản là một cam kết: sửa lỗi tăng PATCH (`1.0.1`), thêm tính năng
tương thích tăng MINOR (`1.1.0`), phá vỡ tương thích tăng MAJOR (`2.0.0`). `0.4.0`
không mang cam kết đó.

## 4. Tag và nhánh release trong bài

- **Tag** `v1.0.0` (annotated, có người gắn, ngày, thông điệp) là định danh **bất
  biến**: không di chuyển, đã chia sẻ thì không xóa. `v0.1.0`–`v0.3.0` được gắn bù
  lên `origin/release/lab01`–`lab03`.
- **Nhánh** `release/lab04` là **dòng bảo trì** 1.0.x. Nó di chuyển khi có hotfix và
  được bảo vệ (bắt buộc PR, cấm force push, cấm xóa).
- Các lệnh ghi nhận và tái tạo:
  - `git log release/lab04..master` và `master..release/lab04`: so hai dòng;
  - `git describe --tags`: cho biết đang cách tag gần nhất bao nhiêu commit;
  - `git worktree add ../aims-v1.0.0 v1.0.0`: dựng lại đúng 1.0.0 để chạy test mà
    không đụng thư mục đang làm.
