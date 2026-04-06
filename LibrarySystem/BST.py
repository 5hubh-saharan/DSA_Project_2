"""
Author: Brian Wu (182531236)
Group: 12
Date: 2026-04-04
"""


class Book_Node:
    def __init__(self, title, author, year, left=None, right=None):
        self.title = title
        self.author = author
        self.date = year
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, title, author, year):
        """
        Adds the new info as Book_Node to the BST.
        Performance is O(log n) for a balanced BST, if the tree becomes skewed
        then performance degrades to O(n)
        """
        if self.root is None:
            self.root = Book_Node(title, author, year)
        else:
            self._insert(self.root, title, author, year)

    def _insert(self, node, title, author, year):
        """
        Recursively traverses and adds the new node
        """
        if title < node.title:
            if node.left is None:  # if there is no left node, create one and place the new info there
                node.left = Book_Node(title, author, year)
            else:  # if there is then continue the traversal
                self._insert(node.left, title, author, year)
        elif title > node.title:
            if node.right is None:  # if there is no right node, create one and place the new info there
                node.right = Book_Node(title, author, year)
            else:  # if there is then continue the traversal
                self._insert(node.right, title, author, year)
        else:
            # there is a duplicate book since title == node.title
            raise ValueError(f"Book '{title} already exists within this library!")

    def search(self, title):
        if self.root is None:
            return None
        return self._search(self.root, title)

    def _search(self, node, title):
        """
        Recursively traverses and searches for the node
        """
        if node is None:  # base case when there are no nodes containing title
            return None

        if node.title == title:  # base case that the node is found
            return node
        if title < node.title:
            # if title is smaller than node title, traverse left
            return self._search(node.left, title)
        else:
            # if title is larger than node title, traverse right
            return self._search(node.right, title)

    def in_order_traversal(self, node, result=None):
        # basic dfs (left -> root -> right), returns a list of nodes in "in order"
        if result is None:
            result = []

        if node:
            self.in_order_traversal(node.left, result)  # left node
            result.append(node)  # root
            self.in_order_traversal(node.right, result)  # right node

        return result

    def pre_order_traversal(self, node, result=None):
        # dfs but (root -> left -> right)
        if result is None:
            result = []

        if node:
            result.append(node)  # root
            self.pre_order_traversal(node.left, result)  # left
            self.pre_order_traversal(node.right, result)  # right
        return result

    def post_order_traversal(self, node, result=None):
        # dfs but (left -> right -> root)
        if result is None:
            result = []

        if node:
            self.post_order_traversal(node.left, result)  # left
            self.post_order_traversal(node.right, result)  # right
            result.append(node)  # root
        return result


if __name__ == "__main__":
    library = BST()

    library.insert("Meatball", "Shubkarman", 2025)
    library.insert("Moby Dick", "Herman Melville", 1851)  # Root
    library.insert("Fahrenheit 451", "Ray Bradbury", 1953)  # Left child
    library.insert("The Great Gatsby", "F. Scott Fitzgerald", 1925)  # Right child
    library.insert("The Second Coming of Brian", "Brian Wu", 2026)  # Right-Right
    library.insert("A Tale of Two Cities", "Charles Dickens", 1859)  # Left-Left
    library.insert("Jane Eyre", "Charlotte Bronte", 1847)  # Left-Right
    library.insert("Pride and Prejudice", "Jane Austen", 1813)  # Right-Left
    library.insert("Zuleika Dobson", "Max Beerbohm", 1911)  # Right-Right
    library.insert("Retail Trading with Brian", "Brian Wu", 2026)  # Right-Right

    print("=" * 25)
    print("Library BST initialized")
    print("=" * 25, "\n")

    # Test the search method
    target = "Jane Eyre"
    print(f"Searching: {target}")
    print("-" * 20)
    found_book = library.search(target)

    if found_book:
        print(f"Found!: '{found_book.title}' by {found_book.author} ({found_book.date})\n")
    else:
        print(f"'{target}' not found in the library.\n")

    # Test the Traversals
    print("Testing traversals (in order, pre-order, post-order.)")
    print("-" * 20)

    # In-Order: Should be perfectly alphabetical!
    in_order_nodes = library.in_order_traversal(library.root)
    in_order_titles = [book.title for book in in_order_nodes]
    print("1. in-order (Alphabetical):")
    print(" -> ".join(in_order_titles) + "\n")

    # Pre-Order: Good for seeing how the tree was built (Root -> Left -> Right)
    pre_order_nodes = library.pre_order_traversal(library.root)
    pre_order_titles = [book.title for book in pre_order_nodes]
    print("2. pre-order (Root First):")
    print(" -> ".join(pre_order_titles) + "\n")

    # Post-Order: Good for safely deleting a tree (Leaves -> Root)
    post_order_nodes = library.post_order_traversal(library.root)
    post_order_titles = [book.title for book in post_order_nodes]
    print("3. post-order (Leaves First):")
    print(" -> ".join(post_order_titles) + "\n")

