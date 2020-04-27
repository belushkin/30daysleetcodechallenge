import heapq


class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"


def merge_k_linked_lists(linked_lists):
    """
    >>> print(merge_k_linked_lists([Link(1, Link(2)),Link(3, Link(4))]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_k_linked_lists([Link(1, Link(2)),Link(2, Link(4)),Link(3, Link(3))]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    """
    links = []
    for link in linked_lists:
        while link:
            heapq.heappush(links, link.val)
            link = link.next

    res = Link(heapq.heappop(links))
    v = res
    while links:
        v.next = Link(heapq.heappop(links))
        v = v.next

    return res
