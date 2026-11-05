# Use case – AIMS-mini

Tác nhân: **Khách hàng** (người dùng chương trình dòng lệnh).

```mermaid
flowchart LR
    KH([Khách hàng])
    subgraph AIMS-mini
        UC1((Thêm DVD vào giỏ))
        UC2((Xóa DVD khỏi giỏ))
        UC3((Xem giỏ hàng))
        UC4((Tính tổng tiền))
        UC5((Tìm DVD theo tiêu đề))
    end
    KH --- UC1
    KH --- UC2
    KH --- UC3
    KH --- UC5
    UC3 -. include .-> UC4
    UC1 -. "extend: giỏ đầy (20 đĩa)" .-> UC1
```

| Use case | Mô tả | Lớp / hàm hiện thực |
|---|---|---|
| Thêm DVD vào giỏ | Thêm đĩa; từ chối khi giỏ đã đủ `MAX_NUMBERS_ORDERED` đĩa | `Cart.add_dvd` |
| Xóa DVD khỏi giỏ | Xóa đĩa nếu có trong giỏ | `Cart.remove_dvd` |
| Xem giỏ hàng | In danh sách đĩa; giỏ trống in "The cart is empty" | `Cart.print_cart` |
| Tính tổng tiền | Cộng giá của các đĩa trong giỏ | `Cart.total_cost` |
| Tìm DVD theo tiêu đề | Lọc danh sách đĩa theo từ khóa | `search_by_title` |