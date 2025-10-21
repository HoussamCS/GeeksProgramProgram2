import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        # Handle default value
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0  # page index (0-based)
        # Total number of pages
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 0

    # Step 3: Visible items on current page
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # Step 4: Navigation methods
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Page number out of range!")
        self.current_idx = page_num - 1
        return self

    def first_page(self):
        self.current_idx = 0
        return self  # allow chaining

    def last_page(self):
        if self.total_pages > 0:
            self.current_idx = self.total_pages - 1
        return self  # allow chaining

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self  # allow chaining

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self  # allow chaining

    # Step 5: String representation
    def __str__(self):
        return "\n".join(self.get_visible_items())


# ✅ Step 6: Test Cases
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print(p.get_visible_items())
    # ['a', 'b', 'c', 'd']

    p.next_page()
    print(p.get_visible_items())
    # ['e', 'f', 'g', 'h']

    p.last_page()
    print(p.get_visible_items())
    # ['y', 'z']

    # Test invalid pages
    try:
        p.go_to_page(10)
    except ValueError as e:
        print("Error:", e)

    try:
        p.go_to_page(0)
    except ValueError as e:
        print("Error:", e)

    # Bonus: print current page nicely
    p.first_page()
    print(str(p))
