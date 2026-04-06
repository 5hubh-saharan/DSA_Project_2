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
            raise ValueError(f"Book '{title}' already exists within this library!")

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



def terminal_interface():
    library = BST()
    print("Welcome to the BST Library!")

    library.insert("Meatball", "Shubkarman", 2025)
    library.insert("Moby Dick", "Herman Melville", 1851)  # Root
    library.insert("Fahrenheit 451", "Ray Bradbury", 1953)  # Left child
    library.insert("Ling ling ling", "ling ling ling", 2027)
    library.insert("The Great Gatsby", "F. Scott Fitzgerald", 1925)  # Right child
    library.insert("The Second Coming of Brian", "Brian Wu", 2026)  # Right-Right
    library.insert("A Tale of Two Cities", "Charles Dickens", 1859)  # Left-Left
    library.insert("Jane Eyre", "Charlotte Bronte", 1847)  # Left-Right
    library.insert("Pride and Prejudice", "Jane Austen", 1813)  # Right-Left
    library.insert("Zuleika Dobson", "Max Beerbohm", 1911)  # Right-Right
    library.insert("Retail Trading with Brian", "Brian Wu", 2026)  # Right-Right

    while True:
        print("\nMain Menu:")
        print("1. Add a new book")
        print("2. Search for a book")
        print("3 View all books (Alphabetically)")
        print("4 View all books (pre-order)")
        print("5 View all books (post-order)")
        print("6 Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            print("\nAdd a Book")
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()

            # Use a tiny loop to make sure they type a real number for the year
            while True:
                year_input = input("Enter publication year: ").strip()
                if year_input.isdigit():
                    year = int(year_input)
                    break
                else:
                    print("Invalid input. Please enter a valid number for the year.")

            try:
                library.insert(title, author, year)
                print(f"Successfully added '{title}' to the library!")
            except ValueError as e:
                # This catches the duplicate book error you wrote in your insert logic!
                print(f"Error: {e}")

        elif choice == '2':
            print("\nSearch")
            target = input("Enter the exact title to search for: ").strip()
            found_book = library.search(target)

            if found_book:
                print(f"\nFound Match:")
                print(f"Title:  {found_book.title}")
                print(f"Author: {found_book.author}")
                print(f"Year:   {found_book.date}")
            else:
                print(f"\n'{target}' was not found in the library.")

        elif choice == '3':
            print("\nAlphabetical Catalog")
            # We use your in-order traversal here because it sorts alphabetically!
            all_nodes = library.in_order_traversal(library.root)

            if not all_nodes:
                print("The library is currently empty.")
            else:
                for i, book in enumerate(all_nodes, 1):
                    print(f"{i}. {book.title} ({book.date}) by {book.author}")

        elif choice == '4':
            print("\nPre-order Catalog")
            # We use your pre-order traversal here because it sorts alphabetically!
            all_nodes = library.pre_order_traversal(library.root)

            if not all_nodes:
                print("The library is currently empty.")
            else:
                for i, book in enumerate(all_nodes, 1):
                    print(f"{i}. {book.title} ({book.date}) by {book.author}")

        elif choice == '5':
            print("\nPost-order Catalog")
            # We use your post-order traversal here because it sorts alphabetically!
            all_nodes = library.post_order_traversal(library.root)

            if not all_nodes:
                print("The library is currently empty.")
            else:
                for i, book in enumerate(all_nodes, 1):
                    print(f"{i}. {book.title} ({book.date}) by {book.author}")

        elif choice == '6':
            print("\nClosing library.")
            break  # This breaks the while loop and ends the program

        else:
            print("\nInvalid choice. Please type 1, 2, 3, 4, 5 or 6.")


if __name__ == "__main__":
    terminal_interface()

    # library = BST()
    #
    # library.insert("Meatball", "Shubkarman", 2025)
    # library.insert("Moby Dick", "Herman Melville", 1851)  # Root
    # library.insert("Fahrenheit 451", "Ray Bradbury", 1953)  # Left child
    # library.insert("The Great Gatsby", "F. Scott Fitzgerald", 1925)  # Right child
    # library.insert("The Second Coming of Brian", "Brian Wu", 2026)  # Right-Right
    # library.insert("A Tale of Two Cities", "Charles Dickens", 1859)  # Left-Left
    # library.insert("Jane Eyre", "Charlotte Bronte", 1847)  # Left-Right
    # library.insert("Pride and Prejudice", "Jane Austen", 1813)  # Right-Left
    # library.insert("Zuleika Dobson", "Max Beerbohm", 1911)  # Right-Right
    # library.insert("Retail Trading with Brian", "Brian Wu", 2026)  # Right-Right
    #
    # print("=" * 25)
    # print("Library BST initialized")
    # print("=" * 25, "\n")
    #
    # # Test the search method
    # target = "Jane Eyre"
    # print(f"Searching: {target}")
    # print("-" * 20)
    # found_book = library.search(target)
    #
    # if found_book:
    #     print(f"Found!: '{found_book.title}' by {found_book.author} ({found_book.date})\n")
    # else:
    #     print(f"'{target}' not found in the library.\n")
    #
    # # Test the Traversals
    # print("Testing traversals (in order, pre-order, post-order.)")
    # print("-" * 20)
    #
    # # In-Order: Should be perfectly alphabetical!
    # in_order_nodes = library.in_order_traversal(library.root)
    # in_order_titles = [book.title for book in in_order_nodes]
    # print("1. in-order (Alphabetical):")
    # print(" -> ".join(in_order_titles) + "\n")
    #
    # # Pre-Order: Good for seeing how the tree was built (Root -> Left -> Right)
    # pre_order_nodes = library.pre_order_traversal(library.root)
    # pre_order_titles = [book.title for book in pre_order_nodes]
    # print("2. pre-order (Root First):")
    # print(" -> ".join(pre_order_titles) + "\n")
    #
    # # Post-Order: Good for safely deleting a tree (Leaves -> Root)
    # post_order_nodes = library.post_order_traversal(library.root)
    # post_order_titles = [book.title for book in post_order_nodes]
    # print("3. post-order (Leaves First):")
    # print(" -> ".join(post_order_titles) + "\n")







    """
    Question 3:
    In order traversal is primarily used for sorting. Since the BST is organized by book titles, in-order traversal visits the nodes in 
    ascending alphabetical order. This would generate an alphabetically sorted catalog.
    
    Pre-order traversal can be used for cloning or exporting the tree structure. For example if you need to save the library database to a file
    such as json and want to rebuilt it later, pre-order is best. By recording the root first, you ensure that when the data is re-inserted, the tree
    maintains its original shape and balance.
    
    Post-order traversal is used for deletion or memory cleanup. For languages such as C++ where memory is managed by the programmer, the root must be deleted last
    or else there will be a dangling pointers and memory leaks. Thus the best way to delete is the left then right then root. Post-order ensures you don't lose the pointers
    to the sub-branches before they are processed which makes it the safest way to deallocate memory. (Though for python's garbage collector, we don't need to worry about that)
    
    Question 4:
    Insertion
    Best/Average case O(log n): Insertion for a relatively balanced tree traverses down one specific path which effectively cuts the number of remaining nodes to check in half
    (similar to binary search) at each step
    Worse case O(n): The tree is "skewed" and is 1 long chain effectively a linked list. This can occur if the tree is constructed/inserted with alphabetically sorted titles.
    This results in a 1 long branch. Because  you have to traverse that entire chain (to insert for example Z), every node has to be visited. 
    
    Search
    Best/average case O(log n): For a balanced tree the search time is logarithmic because you eliminate half of the remaining books with every step. Thus: O(log n) 
    Worse case O(n): If the books are added in perfect alphabetical order, the tree becomes "skewed" essentially having 1-2 very long chained subtree. This is 
    essentially a linked list and thus would require you to check every single book to find the one you want. 
    
    Traversal (in, pre, post)
    All cases: O(n). All nodes have to be visited once, since there are n nodes in the library they all have to visited thus O(n).
    """