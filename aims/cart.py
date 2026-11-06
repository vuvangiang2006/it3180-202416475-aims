MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("Đã thêm đĩa vào giỏ hàng")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("Đã xóa đĩa khỏi giỏ hàng")
            return True
        print("Đĩa không có trong giỏ hàng")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        print("*********************** CART ***********************")
        print("Ordered Items:")
        for index, dvd in enumerate(self.items, start=1):
            print(f"{index}. {dvd}")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("****************************************************")

    def total_cost_with_discount(self, percent):
        """Tổng tiền sau khi giảm giá percent phần trăm (0–100)."""
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        return self.total_cost() * (100 - percent) / 100

    def sort_by_title(self):
        """Sắp xếp giỏ theo tiêu đề A→Z; cùng tiêu đề thì đĩa đắt hơn đứng trước."""
        self.items.sort(key=lambda dvd: (dvd.title, -dvd.cost))

    def sort_by_cost(self):
        """Sắp xếp giỏ theo giá giảm dần; cùng giá thì theo tiêu đề A→Z."""
        self.items.sort(key=lambda dvd: (-dvd.cost, dvd.title))
